import numpy as np


# average of dataset (made of list of array of numbers)
def listavg(dataset, scalefactor=1.0):
    total = np.zeros(len(dataset[0]))
    for i in range(len(dataset)):
        total += dataset[i]
    total = total/len(dataset)
    return total*scalefactor


# select range of points in a list and calculate i, q
class IQPoint:
    def __init__(self):
        self.i = 0
        self.q = 0
        self.mag = 0
        self.phase = 0

    def tomagp(self):
        self.mag = np.sqrt(self.i**2+self.q**2)
        self.phase = np.arctan(self.i/self.q)


def avgiq(istart, iend, data, fre, rate):   # Fre MHz, Rate MSa/sec
    rdata = IQPoint()
    p = round(1.0 * rate / fre)
    n = (iend-istart)/p
    isum = 0
    qsum = 0
    for i in range(iend-istart):
        isum += data[istart+i] * np.sin(2 * np.pi * fre / rate * i)
        qsum += data[istart+i] * np.cos(2 * np.pi * fre / rate * i)
    rdata.i = isum/p/n*2
    rdata.q = qsum/p/n*2
    rdata.tomagp()
    return rdata


# calculate I, Q vs time one period per point
def iqtime(istart, iend, data, fre, rate):
    l_data = iend - istart + 1
    period = int(rate / fre)
    n = int(l_data // period)
    idata = np.zeros(n)
    qdata = np.zeros(n)
    for i in range(n):
        isum = 0
        qsum = 0
        for j in range(period):
            isum += data[istart + i*period+j] * np.sin(2 * np.pi * fre / rate * j)
            qsum += data[istart + i*period+j] * np.cos(2 * np.pi * fre / rate * j)
        idata[i] = isum / period * 2
        qdata[i] = qsum / period * 2
    return idata, qdata


class IQdata:
    def __init__(self):
        self.dataI = []
        self.dataQ = []


def if_integral(fre, rate, data): # MHz, MSa/sec, 2d array
    datai = []
    dataq = []
    l = len(data[0])
    p = round(1.0*rate/fre)
    n = int(l/p)
    for i in range(len(data)):
        datai.append([])
        dataq.append([])
        for j in range(n):
            si = 0
            sq = 0
            for k in range(p):
                si += data[i][p*j+k]*np.sin(2*np.pi*fre/rate*(p*j+k))
                sq += data[i][p*j+k]*np.cos(2*np.pi*fre/rate*(p*j+k))
            datai[i].append(si/p)
            dataq[i].append(sq/p)
    rdata = IQdata()
    rdata.dataI = datai
    rdata.dataQ = dataq
    return rdata


class PulseTest:
    def __init__(self):
        self.SpI = []
        self.SpQ = []
        self.Fre = []
        self.SpA = []
        self.SpP = []


def iqaverage(iq, start, end, afre):
    rdata = PulseTest()
    rdata.Fre = np.atleast_2d(afre)
    points = end - start + 1
    for i in range(len(afre)):
        ti = 0
        tq = 0
        for j in range(points):
            ti += iq.dataI[i][j+start]
            tq += iq.dataQ[i][j+start]
        ti = ti / points
        tq = tq / points
        rdata.SpI.append(ti)
        rdata.SpQ.append(tq)
        rdata.SpA.append(np.sqrt(ti**2+tq**2))
        rdata.SpP.append(np.arctan(ti/tq))
    return rdata


def save_pulsetest(path, dataS):
    f = open(path, 'a')
    np.savetxt(f, np.atleast_2d(dataS.Fre))
    np.savetxt(f, np.atleast_2d(dataS.SpA))
    np.savetxt(f, np.atleast_2d(dataS.SpP))
    np.savetxt(f, np.atleast_2d(dataS.SpI))
    np.savetxt(f, np.atleast_2d(dataS.SpQ))
    f.close()


