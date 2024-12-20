f = h5py.File(path+'tmp.hdf5', 'w')
f.create_dataset('s21mag', data= data)
dset = f['s21mag']
dset.attrs['fre_start'] = 5.942
dset.attrs['fre_stop'] = 5.953
dset.attrs['fre_step'] = 0.00001
dset.attrs['fre_stop'] = 5.946
dset.attrs['pow_start'] = 0.1
dset.attrs['pow_stop'] = 0.5
dset.attrs['pow_step'] = 0.01
f.close()