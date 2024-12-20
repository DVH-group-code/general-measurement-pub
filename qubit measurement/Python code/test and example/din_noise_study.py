# Noise measurements
# Study noise from digitizer reading
# %% import library
import matplotlib.pyplot as plt
import dataprocess as dp
import basicqubit as bq
import iqmixercal as iqcal
import libmeasurement as lm

# %%
path = 'C:\\Users\\dvh-collab-user\\Desktop\\20230622 Noise study\\'
# %%
scan = lm.Scan(bq, path, 'tmp')
# %% setup din parameters
bq.msys.din_ch = 1
bq.msys.din_scale = 0.0625
bq.msys.din_points = 1000000
bq.msys.din_cycles = 1
bq.msys.cal_din_scale()
# %% Setup hardware and hvi
bq.setup_io()
bq.setup_hvi()
# %%
bq.stop_all()
# %%
scan.datalog.save_parameters()
# %% load parameter
scan.datalog.load_parameters()
# %%
bq.reload_all()
# %% run
scan.name = '-noise'
avg = scan.din_data()
# %% load sin wave on AWG

