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
my_system.engines.add(awg.hvi.engines.main_engine, 'awg1Engine')
# define front panel trigger
fp_trigger = my_system.engines['awg1Engine'].triggers.add(awg.hvi.triggers.front_panel_1, "FP Trigger")
fp_trigger.config.direction = kthvi.Direction.OUTPUT
fp_trigger.config.polarity = kthvi.Polarity.ACTIVE_HIGH
fp_trigger.config.hw_routing_delay = 0
fp_trigger.config.trigger_mode = kthvi.TriggerMode.LEVEL
# HVI sequencer
sequencer = kthvi.Sequencer("mySequencer", my_system)  # define sequencer
# define HVI registers
hvi_status = sequencer.sync_sequence.scopes['awg1Engine'].registers.add('hvi_status', kthvi.RegisterSize.SHORT)
hvi_status.initial_value = 0  # 0 is waiting for start, 1 is run 2 is to stop
# define main while
sync_while_condition = kthvi.Condition.register_comparison(hvi_status, kthvi.ComparisonOperator.NOT_EQUAL_TO, 2)
sync_while0 = sequencer.sync_sequence.add_sync_while("main while", 90, sync_while_condition)
statement1 = sync_while0.sync_sequence.add_sync_multi_sequence_block("loop body", 260)
# AWG HVI
awg_seq = statement1.sequences['awg1Engine']
instruction = awg_seq.add_instruction("FP Trigger ON", 10, awg_seq.instruction_set.trigger_write.id)
instruction.set_parameter(awg_seq.instruction_set.trigger_write.sync_mode.id,
                          awg_seq.instruction_set.trigger_write.sync_mode.immediate)
instruction.set_parameter(awg_seq.instruction_set.trigger_write.trigger.id, fp_trigger)
instruction.set_parameter(awg_seq.instruction_set.trigger_write.value.id,
                          awg_seq.instruction_set.trigger_write.value.on)
instruction = awg_seq.add_instruction("FP Trigger OFF", 20, awg_seq.instruction_set.trigger_write.id)
instruction.set_parameter(awg_seq.instruction_set.trigger_write.sync_mode.id,
                          awg_seq.instruction_set.trigger_write.sync_mode.immediate)
instruction.set_parameter(awg_seq.instruction_set.trigger_write.trigger.id, fp_trigger)
instruction.set_parameter(awg_seq.instruction_set.trigger_write.value.id,
                          awg_seq.instruction_set.trigger_write.value.off)
# compile HVI
hvi = sequencer.compile()
hvi_text = sequencer.sync_sequence.to_string(kthvi.OutputFormat.DEBUG)
