# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:50:47 2022

@author: Guang Yue
This program is to test keysight AWG, DIN and HVI. It will generate gaussian
wave packet using ch1 2, DIN can be triggered by press key and capture data in ch1
"""

import sys
import time
import keysight_hvi as kthvi
import keysightSD1 as SD1
import libwaveform as lq
import matplotlib.pyplot as plt
sys.path.append(r'C:\Program Files\Keysight\SD1\Libraries\Python')
# prepare awg waveform
wf1 = lq.gwaveform(250, 500, 50, 50, 0)
wf2 = lq.gwaveform(200, 400, 25, 23, 1)

AWG1_Slot = 3
awg1 = SD1.SD_AOU()
awg1id = awg1.openWithSlot("", 1, AWG1_Slot)
if awg1id < 0:
    print("awg1 open error:", awg1id)
else:
    print("AWG1 Module opened:", awg1id)
    print("Module name:", awg1.getProductName())
    print("slot:", awg1.getSlot())
    print("Chassis:", awg1.getChassis())
    print()
# load waveform to awg
awg1.waveformFlush()
wave = SD1.SD_Wave()
wave.newFromArrayDouble(0, wf1)
awg1.waveformLoad(wave, 0)
wave.newFromArrayDouble(0, wf2)
awg1.waveformLoad(wave, 1)
awg1.AWGstop(1)
awg1.AWGflush(1)
# queue waveforms for ch1
awg1.channelWaveShape(1, SD1.SD_Waveshapes.AOU_AWG)
awg1.channelAmplitude(1, 0.2)
awg1.AWGqueueWaveform(1, 0, 1, 0, 2, 0)  # repeat wf1 twice, HVI trigger
awg1.AWGqueueConfig(1, 1)  # queue repeat in cyclic mode
awg1.AWGqueueSyncMode(1, 0)  # sync to CLKSYS
awg1.AWGstart(1)
# queue waveforms for ch2
awg1.channelWaveShape(2, SD1.SD_Waveshapes.AOU_AWG)
awg1.channelAmplitude(2, 0.2)
awg1.AWGqueueWaveform(2, 1, 1, 0, 3, 0)  # repeat wf2 three times, HVI trigger
awg1.AWGqueueConfig(2, 1)  # queue repeat in cyclic mode
awg1.AWGqueueSyncMode(2, 0)  # sync to CLKSYS
awg1.AWGstart(2)
# prepare DIN
din_slot = 5
din = SD1.SD_AIN()
dinid = din.openWithSlot("", 1, 5)
if dinid < 0:
    print("Module open error:", dinid)
else:
    print("Module opened:", dinid)
    print("Module name:", din.getProductName())
    print("slot:", din.getSlot())
    print("Chassis:", din.getChassis())
    print()
points_cycle = 750
cycles = 2
din.DAQflush(1)
din.channelInputConfig(1, 2, SD1.AIN_Impedance.AIN_IMPEDANCE_50, SD1.AIN_Coupling.AIN_COUPLING_DC)
din.DAQconfig(1, points_cycle, cycles, 0, 1)  # get 750 points on ch1, trigger by HVI for two cycles
din.DAQstart(1)

# define HVI system
my_system = kthvi.SystemDefinition("mysystem")
my_system.chassis.add(1)
my_system.sync_resources = [
    kthvi.TriggerResourceId.PXI_TRIGGER0,
    kthvi.TriggerResourceId.PXI_TRIGGER1,
    kthvi.TriggerResourceId.PXI_TRIGGER2,
    kthvi.TriggerResourceId.PXI_TRIGGER3,
    kthvi.TriggerResourceId.PXI_TRIGGER4,
    kthvi.TriggerResourceId.PXI_TRIGGER5,
    kthvi.TriggerResourceId.PXI_TRIGGER6,
    kthvi.TriggerResourceId.PXI_TRIGGER7]
my_system.non_hvi_core_clocks = [10e6]
my_system.engines.add(awg1.hvi.engines.main_engine, 'awg1Engine')
my_system.engines.add(din.hvi.engines.main_engine, 'din')
# define HVI actions
action_id = getattr(awg1.hvi.actions, "awg1_trigger")
my_system.engines['awg1Engine'].actions.add(action_id, 'tr_awg_ch1')
action_id = getattr(awg1.hvi.actions, "awg2_trigger")
my_system.engines['awg1Engine'].actions.add(action_id, 'tr_awg_ch2')
action_id = getattr(din.hvi.actions, "daq1_trigger")
my_system.engines['din'].actions.add(action_id, 'tr_din')
# define sequencer
sequencer = kthvi.Sequencer("mySequencer", my_system)
# define HVI stop register
hvi_stop = sequencer.sync_sequence.scopes['awg1Engine'].registers.add('hvi_stop', kthvi.RegisterSize.SHORT)
hvi_stop.initial_value = 0
# define main while
sync_while_condition = kthvi.Condition.register_comparison(hvi_stop, kthvi.ComparisonOperator.EQUAL_TO, 0)
sync_while = sequencer.sync_sequence.add_sync_while("main while", 90, sync_while_condition)
statement1 = sync_while.sync_sequence.add_sync_multi_sequence_block("loop body", 260)
# AWG HVI
awg_seq = statement1.sequences['awg1Engine']
instruction = awg_seq.add_instruction("trigger awg1 ch1", 10, awg_seq.instruction_set.action_execute.id)
instruction.set_parameter(awg_seq.instruction_set.action_execute.action.id, awg_seq.engine.actions['tr_awg_ch1'])
instruction = awg_seq.add_instruction("trigger awg1 ch2", 1000, awg_seq.instruction_set.action_execute.id)
instruction.set_parameter(awg_seq.instruction_set.action_execute.action.id, awg_seq.engine.actions['tr_awg_ch2'])
instruction = awg_seq.add_delay("1us delay", kthvi.time.Duration(3000))
# DIN HVI
din_seq = statement1.sequences['din']
instruction = din_seq.add_instruction("trigger DIN ch1", 10, din_seq.instruction_set.action_execute.id)
instruction.set_parameter(din_seq.instruction_set.action_execute.action.id, din_seq.engine.actions['tr_din'])
# compile and run HVI
hvi = sequencer.compile()
hvi.load_to_hw()
hvi.run(hvi.no_wait)
input('press any key to stop HVI')
hvi.sync_sequence.scopes['awg1Engine'].registers['hvi_stop'].write(1)
time.sleep(1)
datas = []
data = din.DAQread(1, points_cycle)
datas.append(data)
data = din.DAQread(1, points_cycle)
datas.append(data)
print('data saved see plots')
fig, axs = plt.subplots(2)
fig.suptitle('data for two cycles')
axs[0].plot(datas[0])
axs[1].plot(datas[1])
input('press any key to stop program')
hvi.release_hw()
# print HVI program graph
output = sequencer.sync_sequence.to_string(kthvi.OutputFormat.DEBUG)
file = open("HVI_program.txt", "w")
file.write(output)
file.close()

awg1.AWGstop(1)
awg1.AWGstop(2)
awg1.close()
din.DAQstop(1)
din.close()
