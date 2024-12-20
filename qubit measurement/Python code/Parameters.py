# Libraries
import sys

sys.path.append(r'C:\Program Files\Keysight\SD1\Libraries\Python')


# IQ mixer calibration
class IQcal:
    def __init__(self):
        self.phase = 0
        self.i_offset = 0
        self.q_offset = 0
        self.i_amp = 0.6
        self.q_amp = 0.6
        self.q_ratio = 1.0

    def cal_q_ratio(self):  # i*ratio =q
        self.q_ratio = self.q_amp/self.i_amp

    def print(self):
        self.cal_q_ratio()
        print('iq mixer parameters: ' + '\n offset: i ' + str(self.i_offset) + ' q ' + str(self.q_offset)
              + '\n amp: i ' + str(self.i_amp) + ' q ' + str(self.q_amp) + ' ratio ' + str(self.q_ratio) +
              '\n phase: ' + str(self.phase), end='')

    def to_dict(self):
        cal = {'phase': self.phase,
               'i_offset': self.i_offset,
               'q_offset': self.q_offset,
               'i_amp': self.i_amp,
               'q_amp': self.q_amp}
        return cal

    def read_dict(self, cal):
        self.phase = cal['phase']
        self.i_offset = cal['i_offset']
        self.q_offset = cal['q_offset']
        self.i_amp = cal['i_amp']
        self.q_amp = cal['q_amp']
        self.cal_q_ratio()


# class to record measurement system status
class MSys:
    def __init__(self):
        # parameters for general and spectroscopy measurement
        self.chassis = 1  # Chassis number of AWG1
        self.awg_slot = 3  # PXI slot number of AWG1
        self.awg = 0  # awg object
        self.awg_eng = 'awg1Engine'
        self.awg_crange = 1.5  # AWG cavity channel max output Vpp/2
        self.awg_qrange = 1.5  # AWG drive channel max output
        self.awg_next_id = 0
        self.qp_length = 2000  # length of the qubit dc pulse in ns including delay
        self.cp_length = 5000  # length of the cavity dc pulse including delay
        self.cp_delay = 2000  # delay of cavity pulse
        self.pulse_fre = 50  # pulse frequency in MHz
        self.finish_delay = 500000  # delay after each HVI cycle
        self.drive_i = None  # waveforms for drive I etc
        self.drive_q = None
        self.readout_i = None
        self.readout_q = None

        self.din_slot = 5  # PXI slot for DIN
        self.din = 0  # din object
        self.din_eng = 'din'
        self.dataset = 0  # data read from DIN
        self.delay_digitizer = 88000  # delay of digitizer reading, need to end in 10ns
        self.din_ch = 1  # channel of DIN for cavity readout
        self.din_scale = 0.0625  # DIN full scale Vpp/2
        self.din_factor = self.din_scale / (2 ** 15 - 1.0)  # reading x factor = voltage
        self.din_points = 4000  # data points read from DIN
        self.istart = 750  # start index of the din data for S21 calculation
        self.iend = 1150  # end index of the din data for S21 calculation
        self.din_cycles = 1000  # cycles read from DIN
        self.din_rate = 500  # data reading rate MSa/s
        self.hvi = 0  # hvi object after compile
        self.hvi_text = ''  # hvi code into text

        # IQ mixer calibration
        self.qubit_mixer = IQcal()
        self.cavity_mixer = IQcal()

    def cal_din_scale(self):
        self.din_factor = self.din_scale / (2 ** 15 - 1.0)  # reading x factor = voltage

    def reset_if(self):
        self.drive_q.fre = self.pulse_fre
        self.drive_i.fre = self.pulse_fre
        self.readout_i.fre = self.pulse_fre
        self.readout_q.fre = self.pulse_fre

    def print_hvi(self):
        # print HVI program graph
        file = open("HVI_spectroscopy.txt", "w")
        file.write(self.hvi_text)
        file.close()




