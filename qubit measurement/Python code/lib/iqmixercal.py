#%% library
import pynput as pk
import sys


#%% define class and functions
def loop_i(i, n):
    return (i + 1) % n


class CalState:
    def __init__(self, bq, mixer, amp, con):
        self.state_list = ['i_offset', 'q_offset', 'i_amp', 'q_amp', 'q_phase']
        self.voltage_list = [0.1, 0.01, 0.001]
        self.phase_list = [10, 1, 0.1, 0.01]
        self.state_i = 0
        self.vstep_i = 0
        self.pstep_i = 0
        self.v_step = 0.01
        self.phase_step = 1
        self.bq = bq
        self.mixer_name = ''
        self.setpulse = None
        self.iqcal = None
        self.i_ch = 0
        self.q_ch = 0
        self.change_mixer(mixer)
        self.iqcal.i_amp = amp
        self.iqcal.q_amp = amp * self.iqcal.q_ratio
        self.con = con

    def change_mixer(self, mixer):
        self.mixer_name = mixer
        if self.mixer_name == 'qubit':
            self.setpulse = self.bq.load_drive
            self.iqcal = self.bq.msys.qubit_mixer
            self.i_ch = 1
            self.q_ch = 2
        elif self.mixer_name == 'readout':
            self.setpulse = self.bq.load_readout
            self.iqcal = self.bq.msys.cavity_mixer
            self.i_ch = 3
            self.q_ch = 4
        else:
            print('no mixer name matched!')

    def setup_wave(self):
        if not self.con:
            self.bq.pause()
            self.bq.stop_hvi()
            self.setpulse(100, 10000, self.iqcal.i_amp, 1)
            self.bq.setup_hvi()
            self.bq.test_awg()
        else:
            self.bq.km.load_sin(self.bq.msys.awg, self.i_ch, self.iqcal.i_amp, 0, 0, self.bq.msys.pulse_fre)
            self.bq.km.load_sin(self.bq.msys.awg, self.q_ch, self.iqcal.q_amp, 0, 0, self.bq.msys.pulse_fre)
            self.bq.msys.awg.channelOffset(self.i_ch, self.iqcal.i_offset)
            self.bq.msys.awg.channelOffset(self.q_ch, self.iqcal.q_offset)
            self.bq.msys.awg.channelAmplitude(self.i_ch, self.iqcal.i_amp)
            self.bq.msys.awg.channelAmplitude(self.q_ch, self.iqcal.q_amp)
            self.bq.msys.awg.channelPhaseResetMultiple(15)  # reset phase for all function gen channels.
            self.bq.msys.awg.channelPhase(self.q_ch, self.iqcal.phase)

    def inc_state(self):
        self.state_i = loop_i(self.state_i, len(self.state_list))
        print('Adjusting ' + self.state_list[self.state_i])

    def inc_vstep(self):
        self.vstep_i = loop_i(self.vstep_i, len(self.voltage_list))
        self.v_step = self.voltage_list[self.vstep_i]
        print('voltage step is ' + str(self.v_step))

    def inc_pstep(self):
        self.pstep_i = loop_i(self.pstep_i, len(self.phase_list))
        self.phase_step = self.phase_list[self.pstep_i]
        print('phase step is ' + str(self.phase_step))

    def update(self, d):
        if not self.con:
            self.bq.pause()
            self.bq.stop_hvi()
        if self.state_i == 0:  # i_offset
            self.iqcal.i_offset += d * self.v_step
            if not self.con:
                self.setpulse(100, 10000, self.iqcal.i_amp, 1)
            else:
                self.bq.msys.awg.channelOffset(self.i_ch, self.iqcal.i_offset)
            print('set ' + self.state_list[self.state_i] + ' to ' + str(self.iqcal.i_offset))
        elif self.state_i == 1:  # q_offset
            self.iqcal.q_offset += d * self.v_step
            if not self.con:
                self.setpulse(100, 10000, self.iqcal.i_amp, 1)
            else:
                self.bq.msys.awg.channelOffset(self.q_ch, self.iqcal.q_offset)
            print('set ' + self.state_list[self.state_i] + ' to ' + str(self.iqcal.q_offset))
        elif self.state_i == 2:  # i_amp
            self.iqcal.i_amp += d * self.v_step
            self.iqcal.cal_q_ratio()
            if not self.con:
                self.setpulse(100, 10000, self.iqcal.i_amp, 1)
            else:
                self.bq.msys.awg.channelAmplitude(self.i_ch, self.iqcal.i_amp)
            print('set ' + self.state_list[self.state_i] + ' to ' + str(self.iqcal.i_amp))
        elif self.state_i == 3:  # q_amp
            self.iqcal.q_amp += d * self.v_step
            self.iqcal.cal_q_ratio()
            if not self.con:
                self.setpulse(100, 10000, self.iqcal.i_amp, 1)
            else:
                self.bq.msys.awg.channelAmplitude(self.q_ch, self.iqcal.q_amp)
            print('set ' + self.state_list[self.state_i] + ' to ' + str(self.iqcal.q_amp))
        elif self.state_i == 4:  # q_phase
            self.iqcal.phase += d * self.phase_step
            if not self.con:
                self.setpulse(100, 10000, self.iqcal.i_amp, 1)
            else:
                self.bq.msys.awg.channelPhaseResetMultiple(15)
                self.bq.msys.awg.channelPhase(self.q_ch, self.iqcal.phase)
            print('set ' + self.state_list[self.state_i] + ' to ' + str(self.iqcal.phase))
        if not self.con:
            self.bq.setup_hvi()
            self.bq.test_awg()

    # keyboard event handling
    def release(self, key):
        if key == pk.keyboard.KeyCode.from_char('a'):
            self.inc_state()
        if key == pk.keyboard.KeyCode.from_char('d'):
            self.inc_vstep()
        if key == pk.keyboard.KeyCode.from_char('f'):
            self.inc_pstep()
        if key == pk.keyboard.KeyCode.from_char('w'):
            self.update(1.0)
        if key == pk.keyboard.KeyCode.from_char('s'):
            self.update(-1.0)
        if key == pk.keyboard.Key.space:
            return False

    def run(self):
        self.setup_wave()
        with pk.keyboard.Listener(on_release=self.release) as listener:
            listener.join()

