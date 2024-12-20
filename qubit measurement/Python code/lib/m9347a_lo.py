import pyvisa

rm = pyvisa.ResourceManager()
inst = rm.open_resource('TCPIP0::localhost::hislip1::INSTR')


# change LO frequency
def set_fre(ch, fre):  # frequency in Ghz
    inst.write(':DDS' + str(ch)+':FREQ ' + str(fre)+'GHz')


def set_power(ch, power):  # power in dBm
    inst.write(':DDS' + str(ch)+':POW ' + str(power))


def lo_enable(ch, on):  # enable channel
    if on == 0:
        text = 'off'
    else:
        text = 'on'
    inst.write(':DDS' + str(ch) + ':OUTP:STAT ' + text)


# get lo status
def status():
    fre1 = inst.query(':DDS1:FREQ?')
    fre2 = inst.query(':DDS2:FREQ?')
    pow1 = inst.query(':DDS1:POW?')
    pow2 = inst.query(':DDS2:POW?')
    en1 = inst.query(':DDS1:OUTP:STAT?')
    en2 = inst.query(':DDS2:OUTP:STAT?')
    print('CH1: fre=' + fre1.strip() + ' pow=' + pow1.strip() + ' en=' + en1.strip())
    print('CH2: fre=' + fre2.strip() + ' pow=' + pow2.strip() + ' en=' + en2.strip(), end='')


def close():
    inst.close()

