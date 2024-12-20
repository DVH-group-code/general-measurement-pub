# -*- coding: utf-8 -*-
"""
Created on 04/25/2022

@author: Guang Yue
This program sends out RF pulse then readout the cavity status to find qubit resonance
"""

import sys
import time
import keysight_hvi as kthvi
import libwaveform as lq
import matplotlib.pyplot as plt
import numpy as np
import keysightmeasure as km

sys.path.append(r'C:\Program Files\Keysight\SD1\Libraries\Python')

# parameters for the measurement
# choose awg ch1 and ch2 for IQ of qubit pulse, ch3 and ch4 for IQ of cavity readout pulse
Chassis = 1  # Chassis number of AWG1
AWG1_Slot = 3  # PXI slot number of AWG1
DIN_Slot = 5  # PXI slot for DIN
qp_length = 50000  # length of the qubit dc pulse in ns including delay
cp_length = 52000  # length of the cavity dc pulse including delay
cp_delay = 50000  # delay of cavity pulse
pulse_fre = 50  # pulse frequency in MHz
delay_digitizer = 45000  # delay of digitizer reading, need to end in 10ns
finish_delay = 70000  # delay after each HVI cycle
DIN_ch = 1  # channel of DIN for cavity readout
DIN_scale = 2  # DIN full scale
DIN_points = 10000  # data points read from DIN
DIN_cycles = 3  # cycles read from DIN
# prepare awg waveform
wfqI = lq.dc_waveform(0, qp_length, pulse_fre, 0)
wfqQ = lq.dc_waveform(0, qp_length, pulse_fre, np.pi / 2)
wfcI = lq.dc_waveform(cp_delay, cp_length, pulse_fre, 0)
wfcQ = lq.dc_waveform(cp_delay, cp_length, pulse_fre, np.pi / 2)
# open awg
awg1 = km.open_awg(Chassis, AWG1_Slot)
# load waveform to awg
# 0,1 is the qubit pulse I and Q, 2,3 is the cavity pulse IQ
awg1.waveformFlush()
km.load_wave_awg(awg1, wfqI, 0)
km.load_wave_awg(awg1, wfqQ, 1)
km.load_wave_awg(awg1, wfcI, 2)
km.load_wave_awg(awg1, wfcQ, 3)
# prepare four channels of AWG for HVI
km.stop_flush_all_ch(awg1)
km.queue_dc_pulse(awg1, 1, 1, 0)
km.queue_dc_pulse(awg1, 2, 1, 1)
km.queue_dc_pulse(awg1, 3, 1, 2)
km.queue_dc_pulse(awg1, 4, 1, 3)
# prepare DIN
din = km.open_din(Chassis, DIN_Slot)
km.din_setup(din, DIN_ch, DIN_scale, DIN_points, DIN_cycles)
# define HVI system and code
hvicode = km.hvi_spectroscopy_code(Chassis, awg1, din)
# run HVI
hvicode.hvi.load_to_hw()
hvicode.hvi.run(hvicode.hvi.no_wait)
hvicode.hvi.sync_sequence.scopes['awg1Engine'].registers['max_cycle'].write(DIN_cycles)
hvicode.hvi.sync_sequence.scopes['awg1Engine'].registers['finish_delay'].write(round(finish_delay/10))
hvicode.hvi.sync_sequence.scopes['din'].registers['din_delay'].write(round(delay_digitizer/10))
hvicode.hvi.sync_sequence.scopes['awg1Engine'].registers['hvi_status'].write(1)  # start measurement
# get data
dataset = []
for x in range(DIN_cycles):
    data = din.DAQread(DIN_ch, DIN_points, 1000)
    dataset.append(data)
print('data saved in datas[]')
input('press any key to stop program')
hvicode.hvi.sync_sequence.scopes['awg1Engine'].registers['hvi_status'].write(2)  # stop HVI program
hvicode.hvi.release_hw()
# print HVI program graph
"""
file = open("HVI_spectroscopy.txt", "w")
file.write(hvicode.hvi_text)
file.close()
"""
# Stop all awg and din, close connection
"""
km.awg_stop_all(awg1)
km.din_stop_all(din)
awg1.close()
din.close()
"""