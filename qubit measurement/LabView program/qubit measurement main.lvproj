<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="23008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Lib" Type="Folder">
			<Item Name="chassis" Type="Folder">
				<Item Name="check chassis status.vi" Type="VI" URL="../library/check chassis status.vi"/>
			</Item>
			<Item Name="Data" Type="Folder">
				<Item Name="2d array to distribution.vi" Type="VI" URL="../library/2d array to distribution.vi"/>
				<Item Name="create data file.vi" Type="VI" URL="../../../Transport measurement/VIs/create data file.vi"/>
				<Item Name="create data folder.vi" Type="VI" URL="../../../Transport measurement/VIs/create data folder.vi"/>
				<Item Name="create distribution plot hdf.vi" Type="VI" URL="../library/create distribution plot hdf.vi"/>
				<Item Name="create distribution plot.vi" Type="VI" URL="../library/create distribution plot.vi"/>
				<Item Name="create single curve file path.vi" Type="VI" URL="../../../Transport measurement/VIs/create single curve file path.vi"/>
				<Item Name="Field sweep Generator.vi" Type="VI" URL="../../../Transport measurement/VIs/Field sweep Generator.vi"/>
				<Item Name="gen_axis_data.vi" Type="VI" URL="../library/gen_axis_data.vi"/>
				<Item Name="gen_data_paths_from_list.vi" Type="VI" URL="../library/gen_data_paths_from_list.vi"/>
				<Item Name="generate intensity cavity_power_iq.vi" Type="VI" URL="../library/generate intensity cavity_power_iq.vi"/>
				<Item Name="generate intensity plot data.vi" Type="VI" URL="../library/generate intensity plot data.vi"/>
				<Item Name="get integrated iq from h5.vi" Type="VI" URL="../library/get integrated iq from h5.vi"/>
				<Item Name="get readout test data.vi" Type="VI" URL="../library/get readout test data.vi"/>
				<Item Name="timestring.vi" Type="VI" URL="../../../Transport measurement/VIs/timestring.vi"/>
				<Item Name="xyyy plot.vi" Type="VI" URL="../library/xyyy plot.vi"/>
			</Item>
			<Item Name="functions" Type="Folder">
				<Item Name="add pair to buddle.vi" Type="VI" URL="../library/add pair to buddle.vi"/>
				<Item Name="Build plots.vi" Type="VI" URL="../library/Build plots.vi"/>
				<Item Name="Calculate amplitude of array.vi" Type="VI" URL="../library/Calculate amplitude of array.vi"/>
				<Item Name="Digitizer to Amp.vi" Type="VI" URL="../library/Digitizer to Amp.vi"/>
				<Item Name="extractReIm.vi" Type="VI" URL="../library/extractReIm.vi"/>
				<Item Name="gaussian wave function.vi" Type="VI" URL="../library/gaussian wave function.vi"/>
				<Item Name="generate signal array.vi" Type="VI" URL="../library/generate signal array.vi"/>
				<Item Name="plot gaussian wave.vi" Type="VI" URL="../library/plot gaussian wave.vi"/>
				<Item Name="ReImToMagPhase.vi" Type="VI" URL="../library/ReImToMagPhase.vi"/>
			</Item>
			<Item Name="M3102A Digitizer" Type="Folder">
				<Item Name="Close M3102A.vi" Type="VI" URL="../library/Close M3102A.vi"/>
				<Item Name="Init M3102A.vi" Type="VI" URL="../library/Init M3102A.vi"/>
				<Item Name="M3102A channel daq config.vi" Type="VI" URL="../library/M3102A channel daq config.vi"/>
				<Item Name="M3102A get data.vi" Type="VI" URL="../library/M3102A get data.vi"/>
				<Item Name="M3102A test reading.vi" Type="VI" URL="../library/M3102A test reading.vi"/>
				<Item Name="Setup Digitizer.vi" Type="VI" URL="../library/Setup Digitizer.vi"/>
			</Item>
			<Item Name="M3202A AWG" Type="Folder">
				<Item Name="M3202 awg gaussian.vi" Type="VI" URL="../library/M3202 awg gaussian.vi"/>
				<Item Name="M3202 generate wave.vi" Type="VI" URL="../library/M3202 generate wave.vi"/>
			</Item>
			<Item Name="M9300A" Type="Folder">
				<Item Name="M9300A_set_one_ch.vi" Type="VI" URL="../library/M9300A_set_one_ch.vi"/>
				<Item Name="M9300A_setall.vi" Type="VI" URL="../library/M9300A_setall.vi"/>
				<Item Name="M9300A_status.vi" Type="VI" URL="../library/M9300A_status.vi"/>
			</Item>
			<Item Name="M9347 LO" Type="Folder">
				<Item Name="checkM9347driver.vi" Type="VI" URL="../library/checkM9347driver.vi"/>
				<Item Name="M9347 Enable.vi" Type="VI" URL="../library/M9347 Enable.vi"/>
				<Item Name="M9347 Frequency.vi" Type="VI" URL="../library/M9347 Frequency.vi"/>
				<Item Name="M9347 Init.vi" Type="VI" URL="../library/M9347 Init.vi"/>
				<Item Name="M9347 phase.vi" Type="VI" URL="../library/M9347 phase.vi"/>
				<Item Name="M9347 power.vi" Type="VI" URL="../library/M9347 power.vi"/>
				<Item Name="M9347 Set Clock.vi" Type="VI" URL="../library/M9347 Set Clock.vi"/>
			</Item>
			<Item Name="P9374A NA" Type="Folder">
				<Item Name="Agilent NA CreateMeasurement.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent NA/Examples/Agilent NA CreateMeasurement.vi"/>
				<Item Name="P9374A Init for S.vi" Type="VI" URL="../library/P9374A Init for S.vi"/>
				<Item Name="P9374A NA close session.vi" Type="VI" URL="../library/P9374A NA close session.vi"/>
				<Item Name="P9374A NA port source enable.vi" Type="VI" URL="../library/P9374A NA port source enable.vi"/>
				<Item Name="P9374A NA scpi.vi" Type="VI" URL="../library/P9374A NA scpi.vi"/>
				<Item Name="P9374A NA set power.vi" Type="VI" URL="../library/P9374A NA set power.vi"/>
				<Item Name="P9374A NA setsweep.vi" Type="VI" URL="../library/P9374A NA setsweep.vi"/>
				<Item Name="P9374A NA Sweep single point frequency.vi" Type="VI" URL="../library/P9374A NA Sweep single point frequency.vi"/>
			</Item>
			<Item Name="VISA" Type="Folder">
				<Item Name="VISA IO GUI.vi" Type="VI" URL="../library/VISA IO GUI.vi"/>
				<Item Name="VISA IO.vi" Type="VI" URL="../library/VISA IO.vi"/>
			</Item>
		</Item>
		<Item Name="main tasks" Type="Folder">
			<Item Name="Customized NA.vi" Type="VI" URL="../VIs/Customized NA.vi"/>
			<Item Name="find qubit resonance.vi" Type="VI" URL="../VIs/find qubit resonance.vi"/>
			<Item Name="InitSetup.vi" Type="VI" URL="../VIs/InitSetup.vi"/>
			<Item Name="LO M9347A.vi" Type="VI" URL="../library/LO M9347A.vi"/>
			<Item Name="P9374A measure S curve.vi" Type="VI" URL="../library/P9374A measure S curve.vi"/>
			<Item Name="VNA S curve vs Power.vi" Type="VI" URL="../VIs/VNA S curve vs Power.vi"/>
		</Item>
		<Item Name="Plots" Type="Folder">
			<Item Name="ContourPlot multi-channel v1.6.vi" Type="VI" URL="../../../Transport measurement/VIs/ContourPlot multi-channel v1.6.vi"/>
			<Item Name="general data plot.vi" Type="VI" URL="../VIs/general data plot.vi"/>
			<Item Name="readout test plot.vi" Type="VI" URL="../VIs/readout test plot.vi"/>
		</Item>
		<Item Name="test" Type="Folder">
			<Item Name="integral plot.vi" Type="VI" URL="../library/integral plot.vi"/>
			<Item Name="RF pulse and readout sequence.vi" Type="VI" URL="../VIs/RF pulse and readout sequence.vi"/>
		</Item>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="instr.lib" Type="Folder">
				<Item Name="Apply.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent M9300/Public/Action-Status/Apply.vi"/>
				<Item Name="Channel Measurement Fetch Complex.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent NA/Public/Data/Fetch/Channel Measurement Fetch Complex.vi"/>
				<Item Name="Channel Measurement Fetch Formatted.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent NA/Public/Data/Fetch/Channel Measurement Fetch Formatted.vi"/>
				<Item Name="Channel Measurement Fetch X.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent NA/Public/Data/Fetch/Channel Measurement Fetch X.vi"/>
				<Item Name="Channel Source Power Set Level.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent NA/Public/Configure/Channel/Source Power/Channel Source Power Set Level.vi"/>
				<Item Name="Channel Stimulus Range Configure Start Stop.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent NA/Public/Configure/Channel/Stimulus Range/Channel Stimulus Range Configure Start Stop.vi"/>
				<Item Name="Channel Trigger Sweep.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent NA/Public/Configure/Channel/Channel Trigger Sweep.vi"/>
				<Item Name="Channels Add.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent NA/Public/Action Status/Channels/Channels Add.vi"/>
				<Item Name="Channels Delete All.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent NA/Public/Action Status/Channels/Channels Delete All.vi"/>
				<Item Name="Close.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent M9300/Close.vi"/>
				<Item Name="Close.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent NA/Close.vi"/>
				<Item Name="Initialize.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent M9300/Initialize.vi"/>
				<Item Name="Initialize.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent NA/Initialize.vi"/>
				<Item Name="Read String.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent NA/Public/Data/ScpiPass Through/Read String.vi"/>
				<Item Name="SetAttributeViBoolean.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent M9300/Public/Configure/Low Level/SetAttributeViBoolean.vi"/>
				<Item Name="SetAttributeViInt32.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent NA/Public/Configure/Low Level/SetAttributeViInt32.vi"/>
				<Item Name="Write String.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent NA/Public/Action Status/System/ScpiPass Through/Write String.vi"/>
			</Item>
			<Item Name="vi.lib" Type="Folder">
				<Item Name="AWGqueueWaveform.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/AOU/AWG/AWGqueueWaveform.vi"/>
				<Item Name="AWGstart.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/AOU/AWG/AWGstart.vi"/>
				<Item Name="AWGstopMultiple.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/AOU/AWG/AWGstopMultiple.vi"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="channelAmplitude.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/AOU/channelAmplitude.vi"/>
				<Item Name="channelFrequency.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/AOU/channelFrequency.vi"/>
				<Item Name="channelInputConfig.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/AIN/channelInputConfig.vi"/>
				<Item Name="channelWaveShape.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/AOU/channelWaveShape.vi"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Close File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Close File+.vi"/>
				<Item Name="close.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/Common/close.vi"/>
				<Item Name="compatReadText.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatReadText.vi"/>
				<Item Name="Concatenate GXML Strings.vi" Type="VI" URL="/&lt;vilib&gt;/NI/GXML/Utility VIs/Concatenate GXML Strings.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="DAQconfig_AIN.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/DAQ/base/DAQconfig_AIN.vi"/>
				<Item Name="DAQflush.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/DAQ/DAQflush.vi"/>
				<Item Name="DAQread.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/DAQ/DAQread.vi"/>
				<Item Name="DAQread_AIN.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/DAQ/base/DAQread_AIN.vi"/>
				<Item Name="DAQstart.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/DAQ/DAQstart.vi"/>
				<Item Name="DAQstop.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/DAQ/DAQstop.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="ex_CorrectErrorChain.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_CorrectErrorChain.vi"/>
				<Item Name="Find First Error.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find First Error.vi"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="General Error Handler Core CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler Core CORE.vi"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="Generator.vi" Type="VI" URL="/&lt;vilib&gt;/NI/GXML/Generator.vi"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="H5Dclose.vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/dataset.llb/H5Dclose.vi"/>
				<Item Name="H5Dget_space.vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/dataset.llb/H5Dget_space.vi"/>
				<Item Name="H5Dread (Variant).vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/dataset.llb/H5Dread (Variant).vi"/>
				<Item Name="H5Fclose.vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/file.llb/H5Fclose.vi"/>
				<Item Name="H5Fopen.vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/file.llb/H5Fopen.vi"/>
				<Item Name="H5G_obj_t.ctl" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/group.llb/H5G_obj_t.ctl"/>
				<Item Name="H5Sclose.vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/dataspace.llb/H5Sclose.vi"/>
				<Item Name="H5Sget_simple_extent_dims.vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/dataspace.llb/H5Sget_simple_extent_dims.vi"/>
				<Item Name="H5Sselect_hyperslab.vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/dataspace.llb/H5Sselect_hyperslab.vi"/>
				<Item Name="HDF5 Ref.ctl" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/library.llb/HDF5 Ref.ctl"/>
				<Item Name="HDF5 Ref.lvclass" Type="LVClass" URL="/&lt;vilib&gt;/UPVI/lvhdf5/library.llb/HDF5 Ref.lvclass"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="LVH5AreadWDTAttrs.vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/attribute.llb/private/LVH5AreadWDTAttrs.vi"/>
				<Item Name="LVH5D Operation.ctl" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/dataset.llb/LVH5D Operation.ctl"/>
				<Item Name="LVH5F Operation.ctl" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/file.llb/LVH5F Operation.ctl"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="NI_AALPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALPro.lvlib"/>
				<Item Name="NI_Data Type.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/Data Type/NI_Data Type.lvlib"/>
				<Item Name="NI_Gmath.lvlib" Type="Library" URL="/&lt;vilib&gt;/gmath/NI_Gmath.lvlib"/>
				<Item Name="NI_MABase.lvlib" Type="Library" URL="/&lt;vilib&gt;/measure/NI_MABase.lvlib"/>
				<Item Name="NI_MAPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/measure/NI_MAPro.lvlib"/>
				<Item Name="Not an HDF5 Refnum Constant.vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/identifier.llb/Not an HDF5 Refnum Constant.vi"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Open File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Open File+.vi"/>
				<Item Name="OpenCreateReplace Dataset.vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/dataset.llb/OpenCreateReplace Dataset.vi"/>
				<Item Name="openWithSlot.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/Common/openWithSlot.vi"/>
				<Item Name="Read Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Read Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (I64).vi"/>
				<Item Name="Read Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (string).vi"/>
				<Item Name="Read Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet.vi"/>
				<Item Name="Read File+ (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read File+ (string).vi"/>
				<Item Name="Read Lines From File (with error IO).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Lines From File (with error IO).vi"/>
				<Item Name="Read Multiple Attributes (Variant).vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/attribute.llb/Read Multiple Attributes (Variant).vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Select HDF5 Dialog (File and Object).vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/utility.llb/Select HDF5 Dialog (File and Object).vi"/>
				<Item Name="Select HDF5 Dialog (Object Only).vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/utility.llb/Select HDF5 Dialog (Object Only).vi"/>
				<Item Name="Select HDF5 Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/utility.llb/Select HDF5 Dialog.vi"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="Simple Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Simple Error Handler.vi"/>
				<Item Name="Simple H5Dread (Variant).vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/dataset.llb/Simple H5Dread (Variant).vi"/>
				<Item Name="subDisplayMessage.vi" Type="VI" URL="/&lt;vilib&gt;/express/express output/DisplayMessageBlock.llb/subDisplayMessage.vi"/>
				<Item Name="subTimeDelay.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/TimeDelayBlock.llb/subTimeDelay.vi"/>
				<Item Name="System Exec.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/system.llb/System Exec.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="To HDF5 Ref.vi" Type="VI" URL="/&lt;vilib&gt;/UPVI/lvhdf5/common.llb/To HDF5 Ref.vi"/>
				<Item Name="Trim Whitespace One-Sided.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace One-Sided.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="waveformFlush.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/Wave/waveformFlush.vi"/>
				<Item Name="waveformLoadInt16.vi" Type="VI" URL="/&lt;vilib&gt;/Keysight_SD1/Wave/base/waveformLoadInt16.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="Write Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Write Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (I64).vi"/>
				<Item Name="Write Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (string).vi"/>
				<Item Name="Write Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet.vi"/>
				<Item Name="Write Spreadsheet String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Spreadsheet String.vi"/>
				<Item Name="Write XML to File.vi" Type="VI" URL="/&lt;vilib&gt;/NI/GXML/Write XML to File.vi"/>
			</Item>
			<Item Name="Agilent M9300.lvlib" Type="Library" URL="../../../../../../../Program Files (x86)/Agilent/M938x/LabVIEW Driver/20xx/Agilent M9300/Agilent M9300.lvlib"/>
			<Item Name="AgM9300_64.dll" Type="Document" URL="AgM9300_64.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="GetInfo.vi" Type="VI" URL="../../../Transport measurement/VIs/GetInfo.vi"/>
			<Item Name="global.vi" Type="VI" URL="../../../Transport measurement/VIs/global.vi"/>
			<Item Name="Keysight MPxiChassis.lvlib" Type="Library" URL="../../../../../../../Program Files (x86)/Keysight/MPxiChassis/LabVIEW Driver/20xx/Keysight MPxiChassis/Keysight MPxiChassis.lvlib"/>
			<Item Name="KtMPxiChassis_64.dll" Type="Document" URL="KtMPxiChassis_64.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="lvanlys.dll" Type="Document" URL="/&lt;resource&gt;/lvanlys.dll"/>
			<Item Name="SaveControlValues.vi" Type="VI" URL="../../../Transport measurement/VIs/SaveControlValues.vi"/>
			<Item Name="SD1core.dll" Type="Document" URL="SD1core.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="SD1vi.dll" Type="Document" URL="SD1vi.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="InitSetup" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{4CBA8AFA-9EE4-40E0-8035-83B17659BA1E}</Property>
				<Property Name="App_INI_GUID" Type="Str">{FEFFA1A1-3E22-4460-9FBD-148B8D0913DF}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{743A4427-EB4E-42AF-8A23-B28C4AF336A4}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">InitSetup</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/InitSetup</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{89F115FF-4CE4-403C-9771-4562017E8A35}</Property>
				<Property Name="Bld_version.build" Type="Int">3</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">InitSetup.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/InitSetup/InitSetup.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/InitSetup/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{B782235B-7B61-4F01-A9CC-0473F58A8C0F}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/main tasks/InitSetup.vi</Property>
				<Property Name="Source[1].properties[0].type" Type="Str">Run when opened</Property>
				<Property Name="Source[1].properties[0].value" Type="Bool">true</Property>
				<Property Name="Source[1].propertiesCount" Type="Int">1</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_fileDescription" Type="Str">InitSetup</Property>
				<Property Name="TgtF_internalName" Type="Str">InitSetup</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright ? 2023 </Property>
				<Property Name="TgtF_productName" Type="Str">InitSetup</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{43200992-53C8-4B41-BFB1-8716D6981F6C}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">InitSetup.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
			<Item Name="LO M9347A" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{AD9AC0DC-BE7E-49AC-9E6E-9C17FB4AB01A}</Property>
				<Property Name="App_INI_GUID" Type="Str">{E6A51865-55F6-419B-A180-2A25F1E722E5}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{665B221B-F007-4CFC-BBE8-21A04E3F9607}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">LO M9347A</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/LO M9347A</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{2385C95A-EA33-498F-8E91-F141C93BFC42}</Property>
				<Property Name="Bld_version.build" Type="Int">6</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">LO M9347A control.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/LO M9347A/LO M9347A control.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/LO M9347A/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{B782235B-7B61-4F01-A9CC-0473F58A8C0F}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/main tasks/LO M9347A.vi</Property>
				<Property Name="Source[1].properties[0].type" Type="Str">Run when opened</Property>
				<Property Name="Source[1].properties[0].value" Type="Bool">false</Property>
				<Property Name="Source[1].propertiesCount" Type="Int">1</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_fileDescription" Type="Str">LO M9347A</Property>
				<Property Name="TgtF_internalName" Type="Str">LO M9347A</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright ? 2022 </Property>
				<Property Name="TgtF_productName" Type="Str">LO M9347A</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{CD211505-D786-4F75-9344-5D9C9D3E235A}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">LO M9347A control.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
			<Item Name="VISA IO GUI" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{207FCDC7-5755-40EC-AA26-17E419786F7B}</Property>
				<Property Name="App_INI_GUID" Type="Str">{65BB3456-42EF-41BF-9C7E-9589B5F5449B}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{E6E512C1-9C0F-4D38-9150-510BB7ADA7CD}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">VISA IO GUI</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/VISA IO GUI</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{8B6B98A0-0F09-4255-A18F-36AD6BF8CB72}</Property>
				<Property Name="Bld_version.build" Type="Int">3</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">VISA IO GUI.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/VISA IO GUI/VISA IO GUI.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/VISA IO GUI/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{EFE1896B-7FA3-4AC5-B50A-B1688A65FA47}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Lib/VISA/VISA IO GUI.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">UIUC</Property>
				<Property Name="TgtF_fileDescription" Type="Str">VISA IO GUI</Property>
				<Property Name="TgtF_internalName" Type="Str">VISA IO GUI</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright ? 2021 UIUC</Property>
				<Property Name="TgtF_productName" Type="Str">VISA IO GUI</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{CB27C12B-A1FD-4BAE-A138-C4746727C577}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">VISA IO GUI.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>
