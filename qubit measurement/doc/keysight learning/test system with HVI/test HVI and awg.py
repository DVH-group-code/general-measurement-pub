# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 11:02:23 2022

@author: Guang Yue
This program is to test keysight SD1 3 driver and HVI, try to open AWG and compile HVI
"""
import sys
import keysight_hvi as kthvi
sys.path.append(r'C:\Program Files\Keysight\SD1\Libraries\Python')
import keysightSD1 as SD1


AWG1_Slot=3
awg1=SD1.SD_AOU()
awg1id=awg1.openWithSlot("", 1, AWG1_Slot)
if awg1id <0:
    print("awg1 open error:",awg1id)
else:
    print("AWG1 Module opened:",awg1id)
    print("Module name:", awg1.getProductName())
    print("slot:", awg1.getSlot())
    print("Chassis:", awg1.getChassis())
    print()

sys_def = kthvi.SystemDefinition("mySystem")
sys_def.chassis.add_auto_detect()
sys_def.engines.add(awg1.hvi.engines.main_engine, 'SdEngine0')
trigger_resources = [kthvi.TriggerResourceId.PXI_TRIGGER0,
kthvi.TriggerResourceId.PXI_TRIGGER1]
sys_def.sync_resources = trigger_resources
sys_def.non_hvi_core_clocks = [10e6]

sequencer = kthvi.Sequencer("mySequencer", sys_def)
sync_block = sequencer.sync_sequence.add_sync_multi_sequence_block("AWGsequence",30)
sequence = sync_block.sequences['SdEngine0']
test_channel = 1

instrLabel = "awgSetWaveshape"
instruction0 = sequence.add_instruction(instrLabel, 20,
awg1.hvi.instruction_set.set_waveshape.id)
instruction0.set_parameter(awg1.hvi.instruction_set.set_waveshape.channel.id, test_channel)
instruction0.set_parameter(awg1.hvi.instruction_set.set_waveshape.value.id,
awg1.hvi.instruction_set.set_waveshape.value.AOU_SINUSOIDAL)
instrLabel = "awgSetFrequency"
instruction1 = sequence.add_instruction(instrLabel, 20,
awg1.hvi.instruction_set.set_frequency.id)
instruction1.set_parameter(awg1.hvi.instruction_set.set_frequency.channel.id, test_channel)
instruction1.set_parameter(awg1.hvi.instruction_set.set_frequency.value.id, 1e7)
instrLabel = "awgSetAmplitude"
instruction1 = sequence.add_instruction(instrLabel, 20,
awg1.hvi.instruction_set.set_amplitude.id)
instruction1.set_parameter(awg1.hvi.instruction_set.set_amplitude.channel.id, test_channel)
instruction1.set_parameter(awg1.hvi.instruction_set.set_amplitude.value.id, 1)

# Compile HVI sequences
try:
    hvi = sequencer.compile()
except kthvi.CompilationFailed as ex:
    compile_status = ex.compile_status
    print(compile_status.to_string())
    raise ex
print("HVI Compiled")
# Load HVI to HW: load sequences, configure actions/triggers/events, lock resources, etc.
hvi.load_to_hw()
print("HVI Loaded to HW")
# Execute HVI in non-blocking mode
# This mode allows SW execution to interact with HVI execution
hvi.run(hvi.no_wait)
print("HVI Running...")


input("press any key to stop")
awg1.close()

