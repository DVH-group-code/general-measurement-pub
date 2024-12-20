# General-Measurement
This is the major codes used by DVH group for measurements in general. Main function of the codes include transport measurement using cRIO, lockin, NI-DAQ, Ic distribution measurement, RF and qubit measurement using keysight PXI setup.
## License
The code is under The University of Illinois/NCSA Open Source License. See details in LICENSE.md file. 
## To setup the code

Usually the releases contain the most complete code ready for usage.
1. create your github account
1. ask for access to the DVH-group-code organization
1. clone or fork the code to your own account
1. (optional) create your own branch to keep track on your own change to the code. Use the github desktop app.
1. (optional) create pull request to merge you changes into the organization.
1. The main labview project file for transport measurement is under the "Transport measurement" folder
2. The qubit related file is under "qubit measurement" folder

## Notes
1. need to install vi package gxml
1. qubit code need python package: matplotlab, numpy, scipy, PyVISA, pynput, PyYAML, h5py
1. Current supported Labview version: 2024 64bit Q3, with FPGA, RealTime module, FPGA compile tools.
1. cRIO need the following configuration: Slot1 NI9775 digitizer, Slot2 NI9402 DIO, Slot 3 NI9262 DAC
1. With the latest firmwire of cRIO, you can switch labview environment support to lower version of LabView.

## To Run transport code
1. open labview main project, run non-cRIO VIs.
1. With cRIO LED blinking (RT VI runs), run the cRIO related VI under cRIO VI virtual folder. You need to make sure the cRIO is configured with the RT code to auto start. See below for the setting.
## To setup cRIO from scratch
1. Make sure cRIO is seen under NI Max. Upgrade to the latest firmware through NI MAX, the user name is "admin", no password.
1. In NI Max, open cRIO items
1. Setup IP address or use default in NI Max for cRIO
1. In NI Max, under cRIO-> add/remove software, choose the version of RT Linux image, select labview environment version
1. Install related software for cRIO, network streams, network varible engine, ni scan engine, system state publisher
1. In the main project manager, right click cRIO-> connect, unfold cRIO items
1. Make sure the cRIO is in FPGA mode, not the scan mode. Right click chassis-> deploy
1. In the FPGA part of cRIO, run the build of "AWG IV measurement" then download, do the same for "Simple DAQ"
1. Right click build of RT application-> clean, build, deploy, set as run after restart.
## To test cRIO program
1. Go through the above setup.
1. connect DAC channel to digitizer ch0.
1. the cRIO LED will blink if the RT VI runs automatically
1. In project, run Test cRIO→ test IV and Ic dist. The program should run and show some plotted data and exit normally.



## To use the qubit code
The labview interface folder contains labview program, the lib folder contains all the library files.
The "test and example" folder contains testing codes or codes for certain measurement.
Python files under the parent folder are common used program like for setting default parameters 
or for general measurement.
### Initialize setup
1. connect all hardware
1. turn on the PXI chassis
2. turn on the computer
3. run "InitSetup" labview program, wait until it shows LO initialized without error.
4. Open PyCharm, run codes in the python console using the scientific mode
### Single qubit testing
1. open the "single_qubit_testing.py"
2. run all imports
3. set path to store data
4. run setups for LO signal
5. run bq.setup_io() this will open connection to AWG and Digitizer
6. run bq.setup_hvi() this will compile and prepare the HVI code.
7. If the above does not have errors, you can run measurement codes. The file contains commands for IQ mixer calibration,
measure T1 T2 etc.
### Test AWG and digitizer
## To improve
1. single curve VI and field scan combine for fast and slow
1. use yaml for controls log
1. network reference inside sequence structure
1. Ic vs field VI need to apply different waveform for Ic and IV measurement
## Change Log:
- 2023 July	
	- Adapt labview 2023 64bit Q1						
	- start using cRIO as AWG.
	- Unified cRIO RT VI
	- Added noise measurement for testing qubit setup.
  - Fixed digitizer reading.  
  - Adapt labview 2023 64bit
  - start using cRIO as AWG.
  - Unified cRIO RT VI  
- 2023 August
	- cRIO VIs are now run as standalone RT application, VI server is no longer used.
	- Ic distribution VI now support negative slope trigger.
	- a global VI is made for cRIO parameters like IP address, shared variable refnum, shared varible value etc.
- 2024 September
	- upgraded transport code to LabView 2024 Q3

