import keysightSD1 as Sd1
import keysight_hvi as kthvi


# open awg for chassis and slot
def open_awg(chassis, slot):
    awg = Sd1.SD_AOU()
    awgid = awg.openWithSlot("", chassis, slot)
    if awgid < 0:
        print("AWG open error:", awgid)
    else:
        print("AWG Module opened:", awgid)
        print("Module name:", awg.getProductName())
        print("slot:", awg.getSlot())
        print("Chassis:", awg.getChassis())
    return awg


# load waveform to AWG
def load_wave_awg(awg, wavedata, idnum):
    wave = Sd1.SD_Wave()
    wave.newFromArrayDouble(0, wavedata)
    awg.waveformLoad(wave, idnum)


# stop AWG and flush queued waveforms on all channels
def stop_flush_all_ch(awg):
    awg.AWGstopMultiple(15)  # all channels
    for n in [1, 2, 3, 4]:
        awg.AWGflush(n)


# queue dc pulse for a channel, HVI trigger
# ch is the channel, amp the amplitude
# nwave is the waveform number, delay is the delay of ns (has to be 10s of ns and less than 40us)
def queue_dc_pulse(awg, ch, amp, nwave, delay=0):
    awg.channelWaveShape(ch, Sd1.SD_Waveshapes.AOU_AWG)
    awg.channelAmplitude(ch, amp)
    awg.AWGqueueWaveform(ch, nwave, 1, delay, 1, 0)  # ic, iw, HVI trigger, delay, cycle, prescaler
    awg.AWGqueueConfig(ch, 1)  # queue repeat in cyclic mode
    awg.AWGqueueSyncMode(ch, 0)  # sync to CLKSYS
    awg.AWGstart(ch)


# queue IF pulse with delay and IF waveform
def queue_delay_pulse(awg, pulse):
    awg.AWGstop(pulse.awg_ch)
    awg.AWGflush(pulse.awg_ch)
    awg.channelWaveShape(pulse.awg_ch, Sd1.SD_Waveshapes.AOU_AWG)
    awg.channelAmplitude(pulse.awg_ch, pulse.awg_range)
    awg.AWGqueueWaveform(pulse.awg_ch, pulse.delay_wave_id,
                         pulse.awg_trig, 0, int(pulse.delay/pulse.delay_unit_time), 0)  # ic, iw, HVI trigger, delay, cycle, prescaler
    awg.AWGqueueWaveform(pulse.awg_ch, pulse.pulse_wave_id, 0, 0, 1, 0)
    awg.AWGqueueConfig(pulse.awg_ch, 1)  # queue repeat in cyclic mode
    awg.AWGqueueSyncMode(pulse.awg_ch, 0)  # sync to CLKSYS
    awg.AWGstart(pulse.awg_ch)


# all awg ch
def awg_stop_all(awg):
    awg.AWGstopMultiple(15)


# setup continuous wave
def load_sin(awg, ch, amp, phase, offset, fre):
    awg.AWGstop(ch)
    awg.channelAmplitude(ch, amp)  # Sets output amplitude for awg
    awg.channelFrequency(ch, fre * 1000000)  # Sets output frequency Hz for awg
    awg.channelWaveShape(ch, Sd1.SD_Waveshapes.AOU_SINUSOIDAL)
    awg.channelPhase(ch, phase)  # degrees
    awg.channelOffset(ch, offset)
    awg.AWGstart(ch)


# open DIN
def open_din(chassis, slot):
    din = Sd1.SD_AIN()
    dinid = din.openWithSlot("", chassis, slot)
    if dinid < 0:
        print("Module open error:", dinid)
    else:
        print("Module opened:", dinid)
        print("Module name:", din.getProductName())
        print("slot:", din.getSlot())
        print("Chassis:", din.getChassis())
    return din


# DIN setup
def din_setup(din, ch, scale, points, cycles):
    din.DAQflush(ch)
    din.channelInputConfig(ch, scale, Sd1.AIN_Impedance.AIN_IMPEDANCE_50, Sd1.AIN_Coupling.AIN_COUPLING_DC)
    din.DAQconfig(ch, points, cycles, 0, 1)  # HVI trigger


# din stop all channel
def din_stop_all(din):
    din.DAQstopMultiple(15)


# HVI code
# define HVI system, assume only one chassis
def hvi_define_system(chassis):
    my_system = kthvi.SystemDefinition("mysystem")
    my_system.chassis.add(chassis)
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
    return my_system


# hvi code for spectroscopy measurement
def hvi_spectroscopy_code(msys):
    my_system = hvi_define_system(msys.chassis)
    my_system.engines.add(msys.awg.hvi.engines.main_engine, msys.awg_eng)
    my_system.engines.add(msys.din.hvi.engines.main_engine, msys.din_eng)
    # define front panel trigger
    fp_trigger = my_system.engines[msys.awg_eng].triggers.add(msys.awg.hvi.triggers.front_panel_1, "FP Trigger")
    fp_trigger.config.direction = kthvi.Direction.OUTPUT
    fp_trigger.config.polarity = kthvi.Polarity.ACTIVE_HIGH
    fp_trigger.config.hw_routing_delay = 0
    fp_trigger.config.trigger_mode = kthvi.TriggerMode.LEVEL
    # add all awg triggers as actions, and DIN trigger
    action_id = getattr(msys.awg.hvi.actions, "awg1_trigger")
    my_system.engines[msys.awg_eng].actions.add(action_id, 'tr_awg_ch1')
    action_id = getattr(msys.awg.hvi.actions, "awg2_trigger")
    my_system.engines[msys.awg_eng].actions.add(action_id, 'tr_awg_ch2')
    action_id = getattr(msys.awg.hvi.actions, "awg3_trigger")
    my_system.engines[msys.awg_eng].actions.add(action_id, 'tr_awg_ch3')
    action_id = getattr(msys.awg.hvi.actions, "awg4_trigger")
    my_system.engines[msys.awg_eng].actions.add(action_id, 'tr_awg_ch4')
    action_id = getattr(msys.din.hvi.actions, 'daq'+str(msys.din_ch)+'_trigger')
    my_system.engines[msys.din_eng].actions.add(action_id, 'tr_din')
    # HVI sequencer
    sequencer = kthvi.Sequencer("mySequencer", my_system)  # define sequencer
    # define HVI registers
    hvi_status = sequencer.sync_sequence.scopes[msys.awg_eng].registers.add('hvi_status', kthvi.RegisterSize.SHORT)
    # 0 is waiting for start, 1 is run in din cycle mode 2 is to stop 3 continuous awg mode without DIN
    hvi_status.initial_value = 0
    hvi_cycle = sequencer.sync_sequence.scopes[msys.awg_eng].registers.add('hvi_cycle', kthvi.RegisterSize.SHORT)
    hvi_cycle.initial_value = 0
    hvi_maxcycle = sequencer.sync_sequence.scopes[msys.awg_eng].registers.add('max_cycle', kthvi.RegisterSize.SHORT)
    hvi_maxcycle.initial_value = 0
    hvi_afterdelay = sequencer.sync_sequence.scopes[msys.awg_eng].registers.add(
        'finish_delay', kthvi.RegisterSize.SHORT)
    hvi_afterdelay.initial_value = 0
    din_delay = sequencer.sync_sequence.scopes[msys.din_eng].registers.add('din_delay', kthvi.RegisterSize.SHORT)
    din_delay.initial_value = 0
    # define main while
    sync_while_condition = kthvi.Condition.register_comparison(hvi_status, kthvi.ComparisonOperator.NOT_EQUAL_TO, 2)
    sync_while0 = sequencer.sync_sequence.add_sync_while("main while", 90, sync_while_condition)
    sync_while_condition = kthvi.Condition.register_comparison(hvi_status, kthvi.ComparisonOperator.EQUAL_TO, 1)
    sync_while1 = sync_while0.sync_sequence.add_sync_while("onoff loop", 820, sync_while_condition)
    sync_while_condition = kthvi.Condition.register_comparison(
        hvi_cycle, kthvi.ComparisonOperator.LESS_THAN, hvi_maxcycle)
    sync_while2 = sync_while1.sync_sequence.add_sync_while("core while", 570, sync_while_condition)
    statement1 = sync_while2.sync_sequence.add_sync_multi_sequence_block("loop body", 260)
    # AWG HVI
    awg_seq = statement1.sequences[msys.awg_eng]
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
    instruction = awg_seq.add_instruction("trigger awg qubit", 10, awg_seq.instruction_set.action_execute.id)
    instruction.set_parameter(awg_seq.instruction_set.action_execute.action.id, awg_seq.engine.actions)
    instruction = awg_seq.add_instruction("increase cycle counter", 10, awg_seq.instruction_set.add.id)
    instruction.set_parameter(awg_seq.instruction_set.add.destination.id, hvi_cycle)
    instruction.set_parameter(awg_seq.instruction_set.add.left_operand.id, hvi_cycle)
    instruction.set_parameter(awg_seq.instruction_set.add.right_operand.id, 1)
    awg_seq.add_wait_time("wait for finish", 20, hvi_afterdelay)
    # DIN HVI
    din_seq = statement1.sequences[msys.din_eng]
    din_seq.add_wait_time("delay", 40, din_delay)
    instruction = din_seq.add_instruction("trigger DIN ch", 10, din_seq.instruction_set.action_execute.id)
    instruction.set_parameter(din_seq.instruction_set.action_execute.action.id, din_seq.engine.actions['tr_din'])
    # finalize
    statement2 = sync_while1.sync_sequence.add_sync_multi_sequence_block("finish", 260)
    awg_seq = statement2.sequences[msys.awg_eng]
    instruction = awg_seq.add_instruction("update status", 10, awg_seq.instruction_set.assign.id)
    instruction.set_parameter(awg_seq.instruction_set.assign.destination.id, hvi_status)
    instruction.set_parameter(awg_seq.instruction_set.assign.source.id, 0)
    instruction = awg_seq.add_instruction("update cycle", 10, awg_seq.instruction_set.assign.id)
    instruction.set_parameter(awg_seq.instruction_set.assign.destination.id, hvi_cycle)
    instruction.set_parameter(awg_seq.instruction_set.assign.source.id, 0)
    # continuous awg while
    sync_while_condition = kthvi.Condition.register_comparison(hvi_status, kthvi.ComparisonOperator.EQUAL_TO, 3)
    sync_while3 = sync_while0.sync_sequence.add_sync_while("inf loop", 820, sync_while_condition)
    statement3 = sync_while3.sync_sequence.add_sync_multi_sequence_block("inf loop body", 260)
    # AWG HVI
    awg_seq = statement3.sequences[msys.awg_eng]
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
    instruction = awg_seq.add_instruction("trigger awg qubit", 10, awg_seq.instruction_set.action_execute.id)
    instruction.set_parameter(awg_seq.instruction_set.action_execute.action.id, awg_seq.engine.actions)
    awg_seq.add_wait_time("wait for finish", 20, hvi_afterdelay)
    # compile HVI
    hvi = sequencer.compile()
    hvi_text = sequencer.sync_sequence.to_string(kthvi.OutputFormat.DEBUG)
    msys.hvi = hvi
    msys.hvi_text = hvi_text
