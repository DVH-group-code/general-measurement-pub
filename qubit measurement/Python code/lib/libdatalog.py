import time
import os
import yaml
import h5py
import numpy as np


# compile all parameters into yaml file
# each time a new parameter is added, need to change both the build and reload function
def load_dict(path):
    f = open(path, 'r')
    loaded = yaml.safe_load(f)
    f.close()
    return loaded


class RecordYaml:
    def __init__(self, msys):
        self.main_dict = {}
        self.msys = msys

    def build_dict(self):
        self.main_dict.clear()
        self.main_dict.update({'basic parameters': {}})
        bp = self.main_dict['basic parameters']
        bp.update({'chassis': self.msys.chassis})
        bp.update({'awg_slot': self.msys.awg_slot})
        bp.update({'awg_eng': self.msys.awg_eng})
        bp.update({'awg_crange': self.msys.awg_crange})
        bp.update({'awg_qrange': self.msys.awg_qrange})
        bp.update({'qp_length': self.msys.qp_length})
        bp.update({'cp_length': self.msys.cp_length})
        bp.update({'cp_delay': self.msys.cp_delay})
        bp.update({'pulse_fre': self.msys.pulse_fre})
        bp.update({'finish_delay': self.msys.finish_delay})
        bp.update({'din_slot': self.msys.din_slot})
        bp.update({'din_eng': self.msys.din_eng})
        bp.update({'delay_digitizer': self.msys.delay_digitizer})
        bp.update({'din_ch': self.msys.din_ch})
        bp.update({'din_scale': self.msys.din_scale})
        bp.update({'din_factor': self.msys.din_factor})
        bp.update({'din_points': self.msys.din_points})
        bp.update({'istart': self.msys.istart})
        bp.update({'iend': self.msys.iend})
        bp.update({'din_cycles': self.msys.din_cycles})
        bp.update({'din_rate': self.msys.din_rate})

        self.main_dict.update({'IQ mixer Calibration': {
            'qubit mixer': self.msys.qubit_mixer.to_dict(),
            'cavity mixer': self.msys.cavity_mixer.to_dict()}})

    def export(self, path):
        f = open(path, 'w')
        yaml.dump(self.main_dict, f)
        f.close()

    def dict_to_msys(self):
        bp = self.main_dict['basic parameters']
        self.msys.chassis = bp['chassis']
        self.msys.awg_slot = bp['awg_slot']
        self.msys.awg_eng = bp['awg_eng']
        self.msys.awg_crange = bp['awg_crange']
        self.msys.awg_qrange = bp['awg_qrange']
        self.msys.qp_length = bp['qp_length']
        self.msys.cp_length = bp['cp_length']
        self.msys.cp_delay = bp['cp_delay']
        self.msys.pulse_fre = bp['pulse_fre']
        self.msys.finish_delay = bp['finish_delay']
        self.msys.din_slot = bp['din_slot']
        self.msys.din_eng = bp['din_eng']
        self.msys.delay_digitizer = bp['delay_digitizer']
        self.msys.din_ch = bp['din_ch']
        self.msys.din_scale = bp['din_scale']
        self.msys.din_factor = bp['din_factor']
        self.msys.din_points = bp['din_points']
        self.msys.istart = bp['istart']
        self.msys.iend = bp['iend']
        self.msys.din_cycles = bp['din_cycles']
        self.msys.din_rate = bp['din_rate']

        self.msys.qubit_mixer.read_dict(self.main_dict['IQ mixer Calibration']['qubit mixer'])
        self.msys.cavity_mixer.read_dict(self.main_dict['IQ mixer Calibration']['cavity mixer'])


class DataLog:
    def __init__(self, path, msys):
        self.path = path
        self.msys = msys
        self.recordyaml = RecordYaml(msys)

    def timedfilepath(self, name='-para', ext='.yaml'):
        ctime = time.localtime()
        time_string = time.strftime("%Y%m%d-%H%M%S ", ctime)
        filepath = self.path + time_string + name + ext
        return filepath

    def save_parameters(self):
        tmp_path = self.path + 'lastSaved.yaml'

        self.recordyaml.main_dict.clear()
        self.recordyaml.build_dict()
        if os.path.isfile(tmp_path):
            saved = load_dict(tmp_path)
            if self.recordyaml.main_dict == saved:
                changed = False
            else:
                changed = True
        else:
            changed = True
        if changed:
            self.recordyaml.export(tmp_path)
            self.recordyaml.export(self.timedfilepath('-para', '.yaml'))
            print('New parameter file saved.')
        else:
            print('No change from last saved paramaters.')

    def load_parameters(self, name='lastSaved.yaml'):
        self.recordyaml.main_dict.clear()
        self.recordyaml.main_dict = load_dict(self.path + name)
        self.recordyaml.dict_to_msys()

    def createfile(self, name):
        ctime = time.localtime()
        time_string = time.strftime("%Y%m%d-%H%M%S", ctime)
        filename = self.path + time_string + name + '.dat'
        f = open(filename, 'a')
        print(time_string + name)
        return f

    def create_hdf5(self, name):
        ctime = time.localtime()
        time_string = time.strftime("%Y%m%d-%H%M%S", ctime)
        filename = self.path + time_string + name + '.h5'
        print('hdf5 data file name generated ' + time_string + name)
        f = h5py.File(filename, 'w', libver='latest')
        return f
    def n_after_integral(self):
        raw_points = self.msys.iend - self.msys.istart
        p = round(1.0 * self.msys.din_rate / self.msys.pulse_fre)
        n_points = raw_points / p
        return n_points

    def c_test_readout_data(self, f, n):
        f.create_dataset('packet', (n, 2, self.n_after_integral()), chunks=True)
        pset = f['packet']
        pset.attrs['measurement'] = 'measure readout signal packet many times'
        pset.attrs['dim_instr'] = '[n][i,q][wave packet]'
        pset.attrs['xname'] = 'index'
        pset.attrs['x_offset'] = 0
        pset.attrs['x_step'] = 1
        pset.attrs['yname'] = 'time ns'
        pset.attrs['y_offset'] = 0
        pset.attrs['y_step'] = 1000.0 / self.msys.pulse_fre  # unit ns
        f.create_dataset('integral', (n, 5), chunks=True)
        iset = f['integral']
        iset.attrs['measurement'] = 'measure readout signal then integral'
        iset.attrs['dim_instr'] = '[n][time, mag, phase, i,q]'
        iset.attrs['xname'] = 'index'
        iset.attrs['x_offset'] = 0
        iset.attrs['x_step'] = 1
        f.swmr_mode = True

    def c_scanif_data(self, f, mea, n, comm):
        f.create_dataset('info', np.array([0]))
        aset = f['info']
        aset.attrs['measurement name'] = mea.name
        aset.attrs['comments'] = comm
        aset.attrs['r_amp'] = mea.r_amp
        aset.attrs['d_amp'] = mea.d_amp
        aset.attrs['IF_channel'] = mea.ifch
        aset.attrs['d_delay'] = mea.d_delay
        aset.attrs['d_length'] = mea.d_length
        aset.attrs['r_delay'] = mea.r_delay
        aset.attrs['r_length'] = mea.r_length
        f.create_dataset('packet', (n, 2, self.n_after_integral()), chunks=True)
        pset = f['packet']
        pset.attrs['measurement'] = 'measure readout signal at each IF fre'
        pset.attrs['dim_instr'] = '[n][i,q][wave packet]'
        pset.attrs['xname'] = 'fre'
        pset.attrs['x_offset'] = mea.startfre
        pset.attrs['x_step'] = mea.stepfre
        pset.attrs['yname'] = 'time ns'
        pset.attrs['y_offset'] = 0
        pset.attrs['y_step'] = 1000.0 / self.msys.pulse_fre  # unit ns
        f.create_dataset('integral', (n, 5), chunks=True)
        iset = f['integral']
        iset.attrs['measurement'] = 'measure readout signal then integral'
        iset.attrs['dim_instr'] = '[n][fre, mag, phase, i,q]'
        iset.attrs['xname'] = 'fre'
        iset.attrs['x_offset'] = mea.startfre
        iset.attrs['x_step'] = mea.stepfre
        f.swmr_mode = True

    def c_timerabi_data(self, f, pl, mea):
        f.create_dataset('info', np.array([0]))
        aset = f['info']
        aset.attrs['measurement name'] = mea.name
        aset.attrs['comments'] = 'measure time Rabi, fixed readout pulse, and drive pulse end, vary length of drive ' \
                                 'pulse'
        aset.attrs['r_amp'] = mea.r_amp
        aset.attrs['d_amp'] = mea.d_amp
        aset.attrs['r_delay'] = mea.r_delay
        aset.attrs['r_length'] = mea.r_length
        n = len(pl)
        f.create_dataset('integral', (n, 5), chunks=True)
        iset = f['integral']
        iset.attrs['measurement'] = 'measure readout signal then integral'
        iset.attrs['dim_instr'] = '[n][len ns, mag, phase, i,q]'
        iset.attrs['xname'] = 'length ns'
        iset.attrs['x_offset'] = pl[0]
        iset.attrs['x_step'] = pl[1] - pl[0]
        f.swmr_mode = True

    def c_t1_data(self, f, dl, p_length, mea):
        f.create_dataset('info', np.array([0]))
        aset = f['info']
        aset.attrs['measurement name'] = mea.name
        aset.attrs['comments'] = 'measure t1, pi pulse then delay t then readout, record readout vs t.'
        aset.attrs['r_amp'] = mea.r_amp
        aset.attrs['d_amp'] = mea.d_amp
        aset.attrs['r_delay'] = mea.r_delay
        aset.attrs['r_length'] = mea.r_length
        aset.attrs['p_length'] = p_length
        n = len(dl)
        f.create_dataset('integral', (n, 5), chunks=True)
        iset = f['integral']
        iset.attrs['measurement'] = 'measure readout signal then integral'
        iset.attrs['dim_instr'] = '[n][delay ns, mag, phase, i,q]'
        iset.attrs['xname'] = 'delay ns'
        iset.attrs['x_offset'] = dl[0]
        iset.attrs['x_step'] = dl[1] - dl[0]
        f.swmr_mode = True

    def c_t2_data(self, f, dl, pi_length, mea):
        f.create_dataset('info', np.array([0]))
        aset = f['info']
        aset.attrs['measurement name'] = mea.name
        aset.attrs['comments'] = 'measure t2, pi/2 pulse then delay t then pi/2 then readout, record readout vs t.'
        aset.attrs['r_amp'] = mea.r_amp
        aset.attrs['d_amp'] = mea.d_amp
        aset.attrs['r_delay'] = mea.r_delay
        aset.attrs['r_length'] = mea.r_length
        aset.attrs['pi_length'] = pi_length
        n = len(dl)
        f.create_dataset('integral', (n, 5), chunks=True)
        iset = f['integral']
        iset.attrs['measurement'] = 'measure readout signal then integral'
        iset.attrs['dim_instr'] = '[n][delay ns, mag, phase, i,q]'
        iset.attrs['xname'] = 'delay ns'
        iset.attrs['x_offset'] = dl[0]
        iset.attrs['x_step'] = dl[1] - dl[0]
        f.swmr_mode = True
