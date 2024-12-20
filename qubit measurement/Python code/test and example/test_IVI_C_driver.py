#%% IVI C driver for M9300A
import ctypes
#%%
ViChar = ctypes.c_char
ViInt8 = ctypes.c_int8
ViInt16 = ctypes.c_int16
ViUInt16 = ctypes.c_uint16
ViInt32 = ctypes.c_int32
ViUInt32 = ctypes.c_uint32
ViInt64 = ctypes.c_int64
ViString = ctypes.c_char_p
ViReal32 = ctypes.c_float
ViReal64 = ctypes.c_double
# Types that are based on other visatypes
ViBoolean = ViUInt16
VI_TRUE = ViBoolean(True)
VI_FALSE = ViBoolean(False)
ViStatus = ViInt32
ViSession = ViUInt32
ViAttr = ViUInt32
ViConstString = ViString
ViRsrc = ViString
#%%
tkDLL = ctypes.cdll.LoadLibrary(r'C:\Program Files\IVI Foundation\IVI\Bin\AgM9300_64.dll')
session = ViSession()
#%%
resourceName = ctypes.create_string_buffer('PXI0::8-0.0::INSTR'.encode('windows-1251'))
optionString = ctypes.create_string_buffer(' '.encode('windows-1251'))
tkDLL.AgM9300_InitWithOptions(resourceName, VI_FALSE,VI_FALSE, optionString, ctypes.pointer(session))
#%%
mes = ctypes.create_string_buffer('\000'.encode('windows-1251'), 256)
tkDLL.AgM9300_GetAttributeViString(	session, optionString, 	ViAttr(1050512), ViInt32(100), mes)
mes.value.decode('windows-1251')