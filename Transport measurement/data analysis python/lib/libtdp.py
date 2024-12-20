# this is the python library for subroutines of handling the data from transport measurement.
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)


# This CPPlot1 class is used to analysis data in standard fast IV form
# other data format compatible may also work.
# Data structure:
# 1. folder named as book## and indexed by book number
# 2. IV data are stored in book##_IV.dat
# 3. magnetic field data in book##_Field.dat
# 4. data can contain multiple channels for each field value
# 5. multiple measured channels should be same length arrays, as rows in a file
class CPPlot1:
    def __init__(self, path, book_num, chs=2, i_index=0, v_index=1):
        self.path = path
        self.book_num = book_num
        self.chs = chs
        self.i_index = i_index
        self.v_index = v_index

        self.location = path + 'book' + str(book_num) + '\\'
        self.iv_name = 'book' + str(book_num) + '_IV.dat'
        self.f_field = 'book' + str(book_num) + '_Field.dat'
        self.field = None
        self.n_field = 0
        self.data = None
        self.data_begin = 1000
        self.data_end = 2000
        self.n_current = 0
        self.rdata = None
        self.rdata_n = 0
        self.ic_data = None
        self.ic_index = None
        self.v_threshold = 0
        self.tr_slope = 'pos'

    def load_data(self):
        self.load_field()
        self.data = np.loadtxt(self.location + self.iv_name)
        self.n_current = len(self.data[0])
        diff = self.n_field * 2 - len(self.data)
        if diff > 0:
            for i in range(diff):
                self.data = np.vstack([self.data, np.zeros(self.n_current)])

    def load_field(self):
        f = open(self.location + self.f_field, 'r')
        f_lines = f.readlines()
        field = f_lines[0]  # magnetic field values
        self.field = np.fromstring(field, sep='\t')
        f.close()
        self.n_field = len(self.field)

    def con_data(self):
        # dimension (field, i/v, value)
        self.rdata = np.zeros((self.n_field, self.chs, self.data_end - self.data_begin))
        for i in range(self.n_field):
            m_index = int(i * self.chs)
            self.rdata[i][0][:] = self.data[m_index + self.i_index][self.data_begin:self.data_end]
            self.rdata[i][1][:] = self.data[m_index + self.v_index][self.data_begin:self.data_end]
            self.rdata_n = len(self.rdata)

    # calibrate voltage data by make the zero floor to zero
    def zero_cal(self, zero_start, zero_end):
        for i in range(self.rdata_n):
            self.rdata[i][1] -= avg_range(self.data[i * self.chs + self.v_index], zero_start, zero_end)

    # smooth data by using moving average
    def smooth_data1(self, smooth_depth):
        for i in range(self.rdata_n):
            move_smooth(self.rdata[i][0], smooth_depth)
            move_smooth(self.rdata[i][1], smooth_depth)

    def reduce_data(self, field_begin_index, field_end_index):
        self.field = self.field[field_begin_index:field_end_index]
        self.n_field = len(self.field)
        self.rdata = self.rdata[field_begin_index:field_end_index][:][:]
        self.rdata_n = self.n_field

    def find_ic(self):
        self.ic_data = np.zeros(self.n_field)
        self.ic_index = np.zeros(self.n_field)
        for i in range(self.n_field):
            self.ic_data[i], self.ic_index[i] = ic_search(self.rdata[i][0], self.rdata[i][1],
                                                          self.v_threshold, self.tr_slope)

    def plot1(self, pi, hline=True, xmin=None, xmax=None):  # plot full diffraction pattern with lower bounds
        fig, ax = plt.subplots()
        ax.plot(self.field, self.ic_data)
        rd = RDiffraction(pi.peak - pi.current_offset, pi.x0, pi.x1, pi.current_offset)
        x, y = rd.gen_plot(pi.r_lower, pi.r_upper, pi.r_points)
        ax.plot(x, y)
        ax.yaxis.set_minor_locator(MultipleLocator(0.1))
        if hline:
            plt.axhline(y=pi.current_offset, color='b', linestyle='dashed')
            plt.axhline(y=pi.min_ic, color='b', linestyle='dashed')
        if xmin is not None and xmax is not None:
            plt.xlim(xmin, xmax)
        plt.xlabel('magnetic field mT')
        plt.ylabel('Ic uA')

    def save_p_data1(self, pi):
        path = self.path + 'book' + self.book_num.__str__() + '\\'
        path_d, filename, time_string = timedfilepath(path, name='diffraction')
        path_p, _, _ = timedfilepath(path, name='diffraction', ext='.par')
        f = open(path_d, 'w')
        np.savetxt(f, np.c_[self.field, self.ic_data], header='field\tIc', comments='')
        print(filename)
        f.close()
        f = open(path_p, 'w')
        f.write('voltage threshold = ' + self.v_threshold.__str__()
                + '\nzero current offset = ' + pi.current_offset.__str__()
                + '\nmin_Ic = ' + pi.min_ic.__str__())
        f.close()


class PlotInfo:
    def __init__(self):
        self.current_offset = 0
        self.min_ic = 0
        self.peak = 1
        self.x0 = 0
        self.x1 = 1
        self.r_lower = -3
        self.r_upper = 3
        self.r_points = 500


# calculate average over a range inside an array
def avg_range(data, i_start, i_stop):
    total = 0
    for i in range(i_start, i_stop):
        total += data[i]
    return total / (i_stop - i_start)


# search ic in I and V arrays
def ic_search(data_i, data_v, tr, slope='pos'):
    n = len(data_i)
    ic_i = 0
    for i in range(n):
        ic_i = 0
        if data_v[i] > tr and slope == 'pos':
            ic_i = i
            break
        if data_v[i] < tr and slope == 'neg':
            ic_i = i
            break
    return data_i[ic_i], ic_i


def move_smooth(data, depth):
    n = len(data)
    for i in range(n):
        if i <= n - depth:
            total = 0
            for j in range(depth):
                total += data[i + j]
            data[i] = total / depth
        else:
            total = 0
            for j in range(depth):
                total += data[i - j]
            data[i] = total / depth


# create file for data saving
def timedfilepath(path, name='', ext='.dat', time_string=''):
    ctime = time.localtime()
    if time_string == '':
        time_string = time.strftime("%Y%m%d-%H%M%S ", ctime)
    filepath = path + time_string + name + ext
    filename = time_string + name + ext
    return filepath, filename, time_string


class RDiffraction:
    def __init__(self, a, x0, x1, y0):
        self.a = a
        self.x0 = x0
        self.k = np.pi / (x1 - x0)
        self.y0 = y0

    def f_value(self, x):
        result = np.sin(self.k * (x - self.x0)) / self.k / (x - self.x0)
        result = self.a * np.abs(result) + self.y0
        return result

    def gen_plot(self, x_start, x_stop, points):
        x = np.arange(x_start, x_stop, (x_stop - x_start) / points)
        y = self.f_value(x)
        return x, y
