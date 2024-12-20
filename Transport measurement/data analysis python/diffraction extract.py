# initially the programs only works for data with multiple rows as channels of measurement
# every certain number of rows measured under one magnetic field point
# %%
import libtdp as ld

plt = ld.plt
# %% setup parameters
folder_path = ('C:\\Users\\yg\\Box\\Guang Yue uiuc research box folder\\paper\\S-TI-S JJ review paper\\'
               'data\\process erik data\\')
book_num = 1
total_chs = 3  # total measurement channel per magnetic field point
i_index = 0  # current channel index
v_index = 2  # voltage channel index, can be dV
cpp = ld.CPPlot1(folder_path, book_num, total_chs, i_index, v_index)
# %% import raw data
cpp.load_data()  # raw data after import
# %% plot field data
plt.plot(cpp.field)
#%% check full fast IV
plt.plot(cpp.data[0])
#%%
plt.plot(cpp.data[1])
# %% reconstruct data
cpp.data_begin = 0
cpp.data_end = 60  # the last index does not count
cpp.con_data()
#%% plot IV curves and check
f_index_0 = 0
f_index_max = cpp.n_field-1
plt.plot(cpp.rdata[f_index_0][0][:], cpp.rdata[f_index_0][1][:])
plt.plot(cpp.rdata[f_index_max][0][:], cpp.rdata[f_index_max][1][:])
#%% calibrate voltage offset
zero_start = 0
zero_end = 1
cpp.zero_cal(zero_start, zero_end)
# %% reduce data to selected field range
field_begin_index = 0
field_end_index = 200
cpp.reduce_data(field_begin_index, field_end_index)
# %% smooth rdata use moving average
smooth_depth = 10
cpp.smooth_data1(smooth_depth)
# %% plot zero field IV
zero_n = 0
ref_n1 = 119
ref_n2 = 0
v_threshold = 2.1
plt.plot(cpp.rdata[zero_n][0][:], cpp.rdata[zero_n][1][:])
plt.plot(cpp.rdata[ref_n1][0][:], cpp.rdata[ref_n1][1][:])
plt.plot(cpp.rdata[ref_n2][0][:], cpp.rdata[ref_n2][1][:])
plt.axhline(v_threshold)
# %% find Ic based on rdata
cpp.v_threshold = v_threshold
cpp.tr_slope = 'pos'
cpp.find_ic()
# %%
plt.plot(cpp.field, cpp.ic_data)
# %%
plt.plot(cpp.field, cpp.ic_index)
# %%
plt.plot(range(cpp.n_field), cpp.ic_data)
# %% complete plot
pi = ld.PlotInfo
pi.current_offset = 0
pi.min_ic = -0.075
pi.peak = -3.157
pi.x0 = -1.22
pi.x1 = -0.83
pi.r_lower = -3.6
pi.r_upper = 2
pi.r_points = 500
cpp.plot1(pi)  # plot full diffraction pattern with lower bounds
#%% plot zoom
cpp.plot1(pi, hline=False, xmin=-2, xmax=0)
# %% save data
cpp.save_p_data1(pi)
#%% tests


