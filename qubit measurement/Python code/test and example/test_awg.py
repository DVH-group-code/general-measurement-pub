import keysightSD1 as Sd1
import libwaveform as lw
ch = 3
amp = 1
awg = Sd1.SD_AOU()
awgid = awg.openWithSlot("", 1, 3)
if awgid < 0:
    print("AWG open error:", awgid)
else:
    print("AWG Module opened:", awgid)
    print("Module name:", awg.getProductName())
    print("slot:", awg.getSlot())
    print("Chassis:", awg.getChassis())
awg.AWGstop(ch)
awg.AWGflush(ch)
awg.channelWaveShape(ch, Sd1.SD_Waveshapes.AOU_AWG)
awg.channelAmplitude(ch, amp)
wf = lw.dc_waveform(100, 1000, 50, 0, 0.1, -0.1)
wave = Sd1.SD_Wave()
wave.newFromArrayDouble(0, wf)
awg.waveformLoad(wave, 1)
awg.AWGqueueWaveform(ch, 1, 0, 0, 1, 0)  # ic, iw, HVI trigger, delay, cycle, prescaler
awg.AWGqueueConfig(ch, 1)  # queue repeat in cyclic mode
awg.AWGqueueSyncMode(ch, 0)  # sync to CLKSYS
awg.AWGstart(ch)
