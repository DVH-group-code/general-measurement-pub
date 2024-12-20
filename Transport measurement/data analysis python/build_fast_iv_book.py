# This program is used to generate fast IV like data set from Erik's data format
# I V B dV R...chx for each row, field change after each IV scan.
# %%
import numpy as np

# %% load data into numpy array
path = ('C:\\Users\\yg\\Box\\'
        'Guang Yue uiuc research box folder\\paper\\S-TI-S JJ review paper\\data\\'
        'process erik data\\raw_data.dat')
rdata = np.loadtxt(path)
# %%
n_ch = 3
n_fields = 240
n_points = 241
i_ch = 1
v_ch = 0
r_ch = 7
ivdata = np.zeros((n_fields * n_ch, n_points))


# %%
def extract_ch(period, index, ch):
    part = rdata[period * index:period * (index + 1)]
    return part[:,ch]


#%%
for i in range(int(len(ivdata)/n_ch)):
    ivdata[i * n_ch + 0] = extract_ch(n_points, i, i_ch)
    ivdata[i * n_ch + 1] = extract_ch(n_points, i, v_ch)
    ivdata[i * n_ch + 2] = extract_ch(n_points, i, r_ch)
#%% correct order
edata = np.zeros((240, 241))
for i in range(len(edata)):
    edata[i] = ivdata[i*3+2]
cdata = np.zeros((240, 241))
for i in range(120):
    cdata[i] = edata[239-i]
    cdata[i+120] = edata[i]
#%% save IV data
path1 = ('C:\\Users\\yg\\Box\\'
        'Guang Yue uiuc research box folder\\paper\\S-TI-S JJ review paper\\data\\'
        'process erik data\\iv.dat')
np.savetxt(path1, cdata)
#%% generate field data
field = np.zeros((240))
for i in range(120):
    field[i] = i*(28.0/119)
for i in range(120):
    field[120+i] = -i*(28/119)
path2 = ('C:\\Users\\yg\\Box\\'
        'Guang Yue uiuc research box folder\\paper\\S-TI-S JJ review paper\\data\\'
        'process erik data\\field.dat')
np.savetxt(path2, [field])