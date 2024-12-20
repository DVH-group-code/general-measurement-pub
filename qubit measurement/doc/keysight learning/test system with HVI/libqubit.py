# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 15:33:26 2022

@author: Guang Yue
"""
import numpy as np

def gauss_wave(t, f, sd, x0,p0): #ns, MHz, Pi
    p=np.exp(-0.5*(t-x0)**2/sd**2)
    s=np.sin(2*np.pi*f*t*0.001+np.pi*p0)
    return p*s

def gwaveform(delay, length, f,sd,p0): #unit ns, MHz, Pi
    w=np.array([])
    for x in range(length):
        w=np.append(w,gauss_wave(x, f, sd,delay,p0))
    return w.tolist()

"""
Test Code
w=np.array([])
for x in range(1500):
    w=np.append(w,libqubit.gauss_wave(x*0.001, 50, 0.05,1,1))


"""

