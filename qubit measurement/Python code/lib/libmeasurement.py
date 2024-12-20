# this file contains measurement routine packaged as function and classes.
import numpy as np
import dataprocess as dp
import sys
import libdatalog
import time


def showprogress(i, n, j=0, jn=1):
    percent = (j * n + i) / ((jn - 1) * n + n - 1) * 100
    sys.stdout.write("\rprogress: {p:.2f} %".format(p=percent))
    sys.stdout.flush()


class Scan:
    def __init__(self, bq, path, name):
        self.bq = bq  # this is the object of the basicqubit module
        self.path = path  # this the file folder to store data
        self.startfre = 10  # start frequency in MHz
        self.stepfre = 0.1
        self.stopfre = 90
        self.startpow = 0.1
        self.steppow = 0.1
        self.stoppow = 0.5
        self.d_amp = 0.1  # drive voltage amplitude of the I channel output from AWG
        self.r_amp = 0.1  # for readout channel
        self.name = name  # measurement name
        self.datai = []
        self.dataq = []
        self.fre = []
        self.datamag = []
        self.datap = []
        self.d_delay = 100  # default pulses define
        self.d_length = 1000
        self.r_delay = 90000
        self.r_length = 2000
        self.ifch = 'drive'  # drive or readout
        self.loch = 2  # LO channel for LO scan
        self.datalog = libdatalog.DataLog(self.path, self.bq.msys)

    def stop_loop(self):
        f = open(self.path + 'stop.txt')
        if f.read() == '1':
            return 1
        else:
            return 0

    def setscanfre(self, start, step, stop):
        self.startfre = start
        self.stopfre = stop
        self.stepfre = step

    def init_data(self):
        self.fre = np.arange(self.startfre, self.stopfre, self.stepfre)
        self.datamag = np.zeros(len(self.fre))
        self.datap = np.zeros(len(self.fre))
        self.datai = np.zeros(len(self.fre))
        self.dataq = np.zeros(len(self.fre))

    def din_data(self, wfile=True):
        if wfile:
            f = self.datalog.createfile(self.name)
        self.datalog.save_parameters()
        self.bq.one_run()
        avg = dp.listavg(self.bq.msys.dataset, self.bq.msys.din_factor)
        if wfile:
            np.savetxt(f, avg)
            f.close()
        return avg

    def test_readout(self, n, wfile=True,
                     t_step=0, r_wave=False):  # keep reading readout pulse to test setup or to test qubit stability
        if wfile:
            f = self.datalog.create_hdf5(self.name)
            self.datalog.c_test_readout_data(f, n)
            pset = f['packet']
            iset = f['integral']
        self.datamag = np.zeros(n)
        self.datap = np.zeros(n)
        self.datai = np.zeros(n)
        self.dataq = np.zeros(n)
        self.datalog.save_parameters()

        self.bq.load_waves(self.d_delay, self.d_length, self.d_amp, self.r_delay, self.r_length, self.r_amp, 1)
        tstart = time.time()
        for i in range(n):
            self.bq.one_run()
            tdata = time.time() - tstart
            avg = dp.listavg(self.bq.msys.dataset, self.bq.msys.din_factor)
            if r_wave:
                packet_i, packet_q = dp.iqtime(self.bq.msys.istart, self.bq.msys.iend, avg,
                                               self.bq.msys.pulse_fre, self.bq.msys.din_rate)
            data = dp.avgiq(self.bq.msys.istart, self.bq.msys.iend, avg, self.bq.msys.pulse_fre, self.bq.msys.din_rate)
            self.datai[i] = data.i
            self.dataq[i] = data.q
            self.datamag[i] = data.mag
            self.datap[i] = data.phase
            showprogress(i, n)
            if wfile:
                if r_wave:
                    pset[i, 0, :] = packet_i
                    pset[i, 1, :] = packet_q
                    pset.flush()
                iset[i, :] = np.array([tdata, data.mag, data.phase, data.i, data.q])
                iset.flush()
            if self.stop_loop() == 1:
                break
            time.sleep(t_step)

        if wfile:
            f.close()

    def scanif(self, wfile=True, comm=''):
        self.init_data()
        if wfile:
            self.datalog.save_parameters()
            f = self.datalog.create_hdf5(self.name)
            n = len(self.fre)
            self.datalog.c_scanif_data(f, self, n, comm)
            pset = f['packet']
            iset = f['integral']

        for i in range(len(self.fre)):
            if self.ifch == 'drive':
                self.bq.msys.drive_i.fre = self.fre[i]
                self.bq.msys.drive_q.fre = self.fre[i]
            elif self.ifch == 'readout':
                self.bq.msys.readout_i.fre = self.fre[i]
                self.bq.msys.readout_q.fre = self.fre[i]
            else:
                print('no if ch selected to scan!')
                break
            self.bq.load_waves(self.d_delay, self.d_length, self.d_amp, self.r_delay, self.r_length, self.r_amp, 1)
            self.bq.one_run()
            avg = dp.listavg(self.bq.msys.dataset, self.bq.msys.din_factor)
            data = dp.avgiq(self.bq.msys.istart, self.bq.msys.iend, avg,
                            self.bq.msys.readout_i.fre, self.bq.msys.din_rate)
            packet_i, packet_q = dp.iqtime(self.bq.msys.istart, self.bq.msys.iend, avg,
                                           self.bq.msys.pulse_fre, self.bq.msys.din_rate)
            data.tomagp()
            self.datamag[i] = data.mag
            self.datap[i] = data.phase
            self.datai[i] = data.i
            self.dataq[i] = data.q
            if wfile:
                pset[i, 0, :] = packet_i
                pset[i, 1, :] = packet_q
                iset[i, :] = np.array([self.fre[i], data.mag, data.phase, data.i, data.q])
                pset.flush()
                iset.flush()
            showprogress(i, n)
            if self.stop_loop() == 1:
                break
        if wfile:
            f.close()

    def scanlo(self, wfile=True):
        if wfile:
            f = self.datalog.createfile(self.name)
            self.datalog.save_parameters()
        self.init_data()
        self.bq.load_waves(self.d_delay, self.d_length, self.d_amp, self.r_delay, self.r_length, self.r_amp, 1)

        for i in range(len(self.fre)):
            self.bq.lo.set_fre(self.loch, self.fre[i])
            self.bq.one_run()
            avg = dp.listavg(self.bq.msys.dataset, self.bq.msys.din_factor)
            iq = dp.avgiq(self.bq.msys.istart, self.bq.msys.iend, avg, self.bq.msys.readout_i.fre, 500)
            iq.tomagp()
            self.datamag[i] = iq.mag
            self.datap[i] = iq.phase
            self.datai[i] = iq.i
            self.dataq[i] = iq.q
            if wfile:
                np.savetxt(f, np.c_[self.fre[i], self.datamag[i], self.datap[i], self.datai[i], self.dataq[i]])
            showprogress(i, len(self.fre))
            if self.stop_loop() == 1:
                break
        if wfile:
            f.close()

    def setpowerrange(self, start, step, stop):
        self.startpow = start
        self.steppow = step
        self.stoppow = stop

    def cavity_power(self):
        power = np.arange(self.startpow, self.stoppow, self.steppow)
        self.datalog.save_parameters()
        f = self.datalog.create_hdf5(self.name)
        self.init_data()

        f.create_dataset('s21', (len(power), 4, len(self.fre)))
        dset = f['s21']
        dset.attrs['measurement'] = 'measure S21 vs fre and power, mag, i, q normalized by power.'
        dset.attrs['dim_instr'] = '[power][mag,p,i,q][fre]'
        dset.attrs['xname'] = 'power dBm'
        dset.attrs['x_offset'] = self.startpow
        dset.attrs['x_step'] = self.steppow
        dset.attrs['yname'] = 'fre GHz'
        dset.attrs['y_offset'] = self.startfre
        dset.attrs['y_step'] = self.stepfre

        for i in range(len(power)):
            self.r_amp = power[i]
            self.scanlo(wfile=False)
            dset[i, 0, :] = self.datamag / power[i]
            dset[i, 1, :] = self.datap
            dset[i, 2, :] = self.datai / power[i]
            dset[i, 3, :] = self.dataq / power[i]
            print(' total' + str(i / len(power) * 100) + '%')
        f.close()

    def readout_time(self, interval, tminutes):  # interval sec, tminutes in min
        f = self.datalog.createfile(self.name)
        tstart = time.time()
        n = int(tminutes * 60 / interval)
        self.datalog.save_parameters()

        self.bq.load_waves(self.d_delay, self.d_length, self.d_amp, self.r_delay, self.r_length, self.r_amp, 1)
        for i in range(n):
            self.bq.one_run()
            avg = dp.listavg(self.bq.msys.dataset, self.bq.msys.din_factor)
            iq = dp.avgiq(self.bq.msys.istart, self.bq.msys.iend, avg,
                          self.bq.msys.readout_i.fre, self.bq.msys.din_rate)
            iq.tomagp()
            tcurrent = time.time() - tstart
            np.savetxt(f, np.c_[tcurrent, iq.mag, iq.phase, iq.i, iq.q])
            time.sleep(interval)
            showprogress(i, n)
            if self.stop_loop() == 1:
                break
        f.close()

    def time_rabi(self, tstart, tstep, tstop, driveend):  # time in ns
        self.datalog.save_parameters()

        pl = np.arange(tstart, tstop, tstep)
        datamag = np.zeros(len(pl))
        datap = np.zeros(len(pl))

        f = self.datalog.create_hdf5(self.name)
        self.datalog.c_timerabi_data(f, pl, self)
        iset = f['integral']

        for i in range(len(pl)):
            self.bq.load_waves(driveend - pl[i], pl[i], self.d_amp, self.r_delay, self.r_length, self.r_amp, 1)
            self.bq.one_run()
            avg = dp.listavg(self.bq.msys.dataset, self.bq.msys.din_factor)
            iq = dp.avgiq(self.bq.msys.istart, self.bq.msys.iend, avg, self.bq.msys.pulse_fre, self.bq.msys.din_rate)
            iq.tomagp()
            datamag[i] = iq.mag
            datap[i] = iq.phase
            iset[i, :] = np.array([pl[i], iq.mag, iq.phase, iq.i, iq.q])
            showprogress(i, len(pl))
            if self.stop_loop() == 1:
                break
        f.close()

    def t1(self, tstart, tstep, tstop, p_length):
        self.datalog.save_parameters()

        dl1 = np.arange(tstart, tstop, tstep)
        dl2 = self.r_delay - p_length - dl1
        datamag = np.zeros(len(dl2))
        datap = np.zeros(len(dl2))

        f = self.datalog.create_hdf5(self.name)
        self.datalog.c_t1_data(f, dl1, p_length, self)
        iset = f['integral']

        for i in range(len(dl2)):
            self.bq.load_waves(dl2[i], p_length, self.d_amp, self.r_delay, self.r_length, self.r_amp, 1)
            self.bq.one_run()
            avg = dp.listavg(self.bq.msys.dataset, self.bq.msys.din_factor)
            iq = dp.avgiq(self.bq.msys.istart, self.bq.msys.iend, avg, self.bq.msys.pulse_fre, self.bq.msys.din_rate)
            iq.tomagp()
            datamag[i] = iq.mag
            datap[i] = iq.phase
            iset[i, :] = np.array([dl1[i], iq.mag, iq.phase, iq.i, iq.q])
            showprogress(i, len(dl2))
            if self.stop_loop() == 1:
                break
        f.close()

    def t2(self, tstart, tstep, tstop, pulse_gen):
        self.datalog.save_parameters()

        dl = np.arange(tstart, tstop, tstep)
        datamag = np.zeros(len(dl))
        datap = np.zeros(len(dl))

        f = self.datalog.create_hdf5(self.name)
        self.datalog.c_t2_data(f, dl, pulse_gen.pi_length, self)
        iset = f['integral']

        for i in range(len(dl)):
            pulse_gen.t2_m = dl[i]
            pulse_gen.drive_delay = pulse_gen.readout_delay - pulse_gen.pi_length - dl[i]
            pulse_gen.setup_t2_pulses()
            self.bq.one_run()
            avg = dp.listavg(self.bq.msys.dataset, self.bq.msys.din_factor)
            iq = dp.avgiq(self.bq.msys.istart, self.bq.msys.iend, avg, self.bq.msys.pulse_fre, self.bq.msys.din_rate)
            iq.tomagp()
            datamag[i] = iq.mag
            datap[i] = iq.phase
            iset[i, :] = np.array([dl[i], iq.mag, iq.phase, iq.i, iq.q])
            showprogress(i, len(dl))
            if self.stop_loop() == 1:
                break
        f.close()

    # check if the qubit is on the right branch (charge qubit), keep measuring readout from Pi pulse
    def readout_once(self, load_waves=False):
        if load_waves:
            self.bq.load_waves(self.d_delay, self.d_length, self.d_amp, self.r_delay, self.r_length, self.r_amp, 1)
        self.bq.one_run()
        avg = dp.listavg(self.bq.msys.dataset, self.bq.msys.din_factor)
        iq = dp.avgiq(self.bq.msys.istart, self.bq.msys.iend, avg, self.bq.msys.pulse_fre, self.bq.msys.din_rate)
        iq.tomagp()
        return iq.mag

    # wait until charge branch is reached
    def wait_branch(self, low, high, pi_length, pi_amp):
        self.bq.load_waves(self.r_delay-pi_length, pi_length, pi_amp, self.r_delay, self.r_length, self.r_amp, 1)
        while True:
            a = self.readout_once()
            if low < a < high:
                break
        return a
