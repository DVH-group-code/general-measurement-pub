# -*- coding: utf-8 -*-
"""
Created on 04/25/2022

@author: Guang Yue
This program sends out RF pulse using four channels of AWG to simulate the IQ of drive pulse and readout pulse.
Then use DIN to read out the pulse. all timing is controlled by HVI.
This program is useful to test the RF setup with mixers circuit connected without real qubit.
"""

# lib import
# parameters for the measurement
# choose awg ch1 and ch2 for IQ of qubit pulse, ch3 and ch4 for IQ of cavity readout pulse
# Parameters.py for the above
import Parameters
import numpy as np
import keysightmeasure as km
import libwaveform as lq
import keyboard

msys = Parameters.MSys()


# prepare awg waveform
def setup_io():
    wfqi = lq.dc_waveform(0, msys.qp_length, msys.pulse_fre, 0, msys.qi_offset / msys.qi_amp)
    wfqq = lq.dc_waveform(0, msys.qp_length, msys.pulse_fre,
                          np.pi / 2 * msys.phaseq_90 / 90.0, msys.qq_offset / msys.qq_amp)
    wfci = lq.dc_waveform(msys.cp_delay, msys.cp_length, msys.pulse_fre, 0, msys.ci_offset / msys.ci_amp)
    wfcq = lq.dc_waveform(msys.cp_delay, msys.cp_length, msys.pulse_fre,
                          np.pi / 2 * msys.phasec_90 / 90.0, msys.cq_offset / msys.cq_amp)

    # open awg
    awg1 = km.open_awg(msys.chassis, msys.awg_slot)
    # load waveform to awg
    # 0,1 is the qubit pulse I and Q, 2,3 is the cavity pulse IQ
    awg1.waveformFlush()
    km.load_wave_awg(awg1, wfqi, 0)
    km.load_wave_awg(awg1, wfqq, 1)
    km.load_wave_awg(awg1, wfci, 2)
    km.load_wave_awg(awg1, wfcq, 3)
    # prepare four channels of AWG for HVI
    km.stop_flush_all_ch(awg1)
    km.queue_dc_pulse(awg1, 1, msys.qi_amp, 0)
    km.queue_dc_pulse(awg1, 2, msys.qq_amp, 1)
    km.queue_dc_pulse(awg1, 3, msys.ci_amp, 2)
    km.queue_dc_pulse(awg1, 4, msys.cq_amp, 3)

    # prepare DIN
    din = km.open_din(msys.chassis, msys.din_slot)
    km.din_setup(din, msys.din_ch, msys.din_scale, msys.din_points, msys.din_cycles)
    msys.din = din
    msys.awg = awg1


# define HVI system and code
# setup HVI
def setup_hvi():
    global msys
    msys = km.hvi_spectroscopy_code(msys)
    # run HVI
    msys.hvi.load_to_hw()
    msys.hvi.run(msys.hvi.no_wait)
    msys.hvi.sync_sequence.scopes[msys.awg_eng].registers['max_cycle'].write(msys.din_cycles)
    msys.hvi.sync_sequence.scopes[msys.awg_eng].registers['finish_delay'].write(round(msys.finish_delay/10))
    msys.hvi.sync_sequence.scopes[msys.din_eng].registers['din_delay'].write(round(msys.delay_digitizer/10))
    print('Done load hvi code')


# run hvi process once and get the data
def one_run():
    msys.din.DAQstart(msys.din_ch)
    msys.hvi.sync_sequence.scopes[msys.awg_eng].registers['hvi_status'].write(1)  # start measurement
    # get data
    dataset = []
    for x in range(msys.din_cycles):
        data = msys.din.DAQread(msys.din_ch, msys.din_points, 1000)
        dataset.append(data)
    # print('data saved')
    msys.dataset = dataset


# stop hvi program and release hw
def hvi_stop():
    # input('press any key to stop program')
    msys.hvi.sync_sequence.scopes[msys.awg_eng].registers['hvi_status'].write(2)  # stop HVI program
    msys.hvi.release_hw()


# Stop all awg and din, close connection
def stop_measurement():
    km.awg_stop_all(msys.awg)
    km.din_stop_all(msys.din)
    msys.awg.close()
    msys.din.close()


def test_pulses():
    while True:
        a = msys.hvi.sync_sequence.scopes['awg1Engine'].registers['hvi_status'].read()
        if a == 0:
            msys.hvi.sync_sequence.scopes['awg1Engine'].registers['hvi_status'].write(1)  # start measurement
        if keyboard.is_pressed("q"):
            break


"""
if __name__ == "__main__":
    setup_io()
    setup_hvi()
    one_run()
    hvi_stop()
    stop_measurement()
"""
