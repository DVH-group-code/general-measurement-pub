#%% load continuous wave and calibrate IQ
bq.km.load_sin(bq.msys.awg, 3, 0.6, 0, 0, 50)
bq.km.load_sin(bq.msys.awg, 4, 0.6, 0, 0, 50)
#%%
bq.km.load_sin(bq.msys.awg, 1, 0.6, 0, 0, 50)
bq.km.load_sin(bq.msys.awg, 2, 0.6, 0, 0, 50)
#%%
bq.load_waves(100, 1000, 0.6, 100, 10000, 0.6, 1)
#%%
stat = iqcal.CalState(bq, 'readout', 0.6, True)
#%%
stat = iqcal.CalState(bq, 'readout', 0.6, False)
#%%
stat = iqcal.CalState(bq, 'qubit', 0.6, True)
#%%
stat = iqcal.CalState(bq, 'qubit', 0.6, False)
#%% measure S21 vs frequency in GHz, LO, channel, frequency parameters, basicqubit and dataprocess object
name = 'cavity.dat'
ctime = time.localtime()
time_string = time.strftime("%Y%m%d-%H%M%S ", ctime)
filename = path+time_string+name
f = open(filename, 'a')
print(time_string+name)
fstart = 5.97
fend = 5.976
fstep = 0.00001
flo = 6.08
fre = np.arange(fstart, fend, fstep)
datamag = np.zeros(len(fre))
datap = np.zeros(len(fre))

bq.load_waves(100, 1000, 0.6, 90500, 2000, 0.08, 1)
for i in range(len(fre)):
    bq.msys.pulse_fre = (flo - fre[i]) * 1000
    bq.load_waves(100, 1000, 0.6, 90500, 2000, 0.6, 1)
    lo.set_fre(2, fre[i])
    bq.one_run()
    avg = dp.listavg(bq.msys.dataset, bq.msys.din_factor)
    iq = dp.avgiq(1500, 2400, avg, 50, 500)
    iq.tomagp()
    datamag[i] = iq.mag
    datap[i] = iq.phase
    np.savetxt(f, np.c_[fre[i], datamag[i], datap[i]])
    per = (fre[i]-fstart+fstep)/(fend-fstart)*100
    sys.stdout.write("\rprogress: {p:.2f} %".format(p=per))
    sys.stdout.flush()
f.close()


#%% S21 at f0 while scan qubit pulse frequency
name = 'qubit.dat'
ctime = time.localtime()
time_string = time.strftime("%Y%m%d-%H%M%S ", ctime)
filename = path+time_string+name
f = open(filename, 'a')
print(time_string+name)
fstart = 72  # scan IF frequency MHz
fend = 92
fstep = 0.01
fre = np.arange(fstart, fend, fstep)
datamag = np.zeros(len(fre))
datap = np.zeros(len(fre))

for i in range(len(fre)):
    # lo.set_fre(1, fre[i])
    bq.msys.drive_i.fre = fre[i]
    bq.msys.drive_q.fre = fre[i]
    bq.load_waves(1000, 89000, 0.1, 90000, 2000, 0.080, 1)
    bq.one_run()
    avg = dp.listavg(bq.msys.dataset, bq.msys.din_factor)
    iq = dp.avgiq(1400, 2100, avg, 50, 500)
    iq.tomagp()
    datamag[i] = iq.mag
    datap[i] = iq.phase
    np.savetxt(f, np.c_[fre[i], datamag[i], datap[i]])
    per = (fre[i]-fstart+fstep)/(fend-fstart)*100
    sys.stdout.write("\rprogress: {p:.2f} %".format(p=per))
    sys.stdout.flush()
f.close()
#%% save data
path = 'C:\\Users\\dvh-collab-user\\Desktop\\20221122 Robert qubit\\'
name = 'Rabi.dat'
if time_string != '':
    filename = path+time_string+name
    f = open(filename, 'a')
    np.savetxt(f, np.c_[pl, datamag, datap])
    f.close()
    print(time_string+name)
    time_string = ''
else:
    print("no time stamp.")
#%% time Rabi measurement
name = 'Rabi.dat'
ctime = time.localtime()
time_string = time.strftime("%Y%m%d-%H%M%S ", ctime)
filename = path+time_string+name
f = open(filename, 'a')
print(time_string+name)

plstart = 10  # scan drive pulse length unit ns
plend = 30000
plstep = 50
driveend = 89500
gap = 500
pl = np.arange(plstart, plend, plstep)
datamag = np.zeros(len(pl))
datap = np.zeros(len(pl))

for i in range(len(pl)):
    bq.load_waves(driveend-pl[i], pl[i], 0.7, driveend+gap, 2000, 0.08, 1)
    bq.one_run()
    avg = dp.listavg(bq.msys.dataset, bq.msys.din_factor)
    iq = dp.avgiq(1400, 2100, avg, 50, 500)
    iq.tomagp()
    datamag[i] = iq.mag
    datap[i] = iq.phase
    np.savetxt(f, np.c_[pl[i], datamag[i], datap[i]])
    per = (pl[i]-plstart+plstep)/(plend-plstart)*100
    sys.stdout.write("\rprogress: {p:.2f} %".format(p=per))
    sys.stdout.flush()
f.close()
