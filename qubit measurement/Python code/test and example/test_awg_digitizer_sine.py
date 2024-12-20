#%% import libraries
import basicqubit as bq
import matplotlib.pyplot as plt
#%% parameters
awg_ch = 1
awg_amp = 0.5  # amplitude mean the A in y=A*sin(wt)
awg_fre = 50  # MHz
din_ch = 1
din_scale = 1  # A as in A*sin(wt), 0.0625, 0.125, 0.25, 0.5, 1,2,4
din_points = 1000
bq.msys.din_scale = din_scale  # Vpp
bq.msys.cal_din_scale()
#%% setup
bq.setup_io()
#%%
bq.stop_measurement()
#%% send out sin wave from AWG
bq.km.load_sin(bq.msys.awg, awg_ch, awg_amp, 0, 0, awg_fre)
#%% turn off output or channel amp
bq.msys.awg.channelAmplitude(awg_ch, 0.5)
#%% digitizer reading setup
bq.msys.din.DAQflush(din_ch)
bq.msys.din.channelInputConfig(din_ch, din_scale, bq.km.Sd1.AIN_Impedance.AIN_IMPEDANCE_50,
                               bq.km.Sd1.AIN_Coupling.AIN_COUPLING_DC)
bq.msys.din.DAQconfig(din_ch, din_points, 1, 0, 0)
#%% read data
bq.msys.din.DAQstart(din_ch)
data = bq.msys.din.DAQread(din_ch, din_points, 1000)
data = data * bq.msys.din_factor
