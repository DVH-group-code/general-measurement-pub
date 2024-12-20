<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="17008000">
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
		<Item Name="lib" Type="Folder">
			<Item Name="Choose heater range.vi" Type="VI" URL="../Choose heater range.vi"/>
			<Item Name="Fridge Turbo.vi" Type="VI" URL="../Fridge Turbo.vi"/>
			<Item Name="Read Temp T8.vi" Type="VI" URL="../Read Temp T8.vi"/>
			<Item Name="RI_OPEN.vi" Type="VI" URL="../Triton VIs/RI_OPEN.vi"/>
			<Item Name="Set Target Temp T8.vi" Type="VI" URL="../Set Target Temp T8.vi"/>
			<Item Name="TRITON_REMOTE_Command.vi" Type="VI" URL="../TRITON_REMOTE_Command.vi"/>
			<Item Name="TRITON_RI_CLOSE.vi" Type="VI" URL="../Triton VIs/TRITON_RI_CLOSE.vi"/>
			<Item Name="TRITON_SEND_RECEIVE.vi" Type="VI" URL="../Triton VIs/TRITON_SEND_RECEIVE.vi"/>
			<Item Name="TRITON_TCP_COMS.vi" Type="VI" URL="../Triton VIs/TRITON_TCP_COMS.vi"/>
			<Item Name="TRITON_TCP_DETAILS.vi" Type="VI" URL="../Triton VIs/TRITON_TCP_DETAILS.vi"/>
			<Item Name="TRITON_TEMP_SPEC.vi" Type="VI" URL="../Triton VIs/TRITON_TEMP_SPEC.vi"/>
		</Item>
		<Item Name="Control Triton Temp 0-2K.vi" Type="VI" URL="../Control Triton Temp 0-2K.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="ex_CorrectErrorChain.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_CorrectErrorChain.vi"/>
				<Item Name="subDisplayMessage.vi" Type="VI" URL="/&lt;vilib&gt;/express/express output/DisplayMessageBlock.llb/subDisplayMessage.vi"/>
				<Item Name="subTimeDelay.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/TimeDelayBlock.llb/subTimeDelay.vi"/>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
