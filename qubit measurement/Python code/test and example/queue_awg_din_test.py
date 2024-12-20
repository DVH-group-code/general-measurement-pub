awg.AWGstop(3)
awg.AWGflush(3)
awg.AWGqueueWaveform(3,0,0,0,200,0)
awg.AWGqueueWaveform(3,5,0,0,1,0)
awg.AWGstart(3)

awg.AWGstop(3)
awg.AWGflush(3)
awg.AWGqueueWaveform(3, 2, 1, 0, 50, 0)
awg.AWGqueueWaveform(3, 5, 0, 0, 1, 0)
awg.AWGqueueWaveform(3, 2, 0, 0, 10, 0)
awg.AWGqueueWaveform(3, 5, 0, 0, 1, 0)
awg.AWGstart(3)
bq.one_run()
plt.plot(bq.msys.dataset[0])

din.DAQstop(1)
din.DAQconfig(1, 100000, 1, 0,0)
din.DAQstart(1)
data=din.DAQread(1,100000)
plt.plot(data)


import matplotlib.pyplot as plt
import sys
sys.modules[__name__].__dict__.clear()

import importlib
importlib.reload(bq)

