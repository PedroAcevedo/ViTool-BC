<?xml version="1.0" encoding="UTF-8"?>
<simconf>
<project export="discard">[APPS_DIR]/mrm</project>
<project export="discard">[APPS_DIR]/mspsim</project>
<project export="discard">[APPS_DIR]/avrora</project>
<project export="discard">[APPS_DIR]/serial_socket</project>
<project export="discard">[APPS_DIR]/powertracker</project>
<simulation>
<title>mySimulation</title>
<delaytime>0</delaytime>
<randomseed>123456</randomseed>
<motedelay_us>1000000</motedelay_us>
<radiomedium>
      se.sics.cooja.radiomediums.UDGM
      <transmitting_range>70</transmitting_range>
<interference_range>90</interference_range>
<success_ratio_tx>1.0</success_ratio_tx>
<success_ratio_rx>1.0</success_ratio_rx>
</radiomedium>
<events>
<logoutput>40000</logoutput>
</events>
    <motetype>
      se.sics.cooja.mspmote.SkyMoteType
      <identifier>sky1</identifier>
      <description>Sky Mote Type #sky1</description>
      <source EXPORT="discard">[CONTIKI_DIR]-2.7/examples/ipv6/rpl-collect-v2/udp-sink.c</source>
      <commands EXPORT="discard">make udp-sink.sky TARGET=sky</commands>
      <firmware EXPORT="copy">[CONTIKI_DIR]-2.7/examples/ipv6/rpl-collect-v2/udp-sink.sky</firmware>
      <moteinterface>se.sics.cooja.interfaces.Position</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.RimeAddress</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.IPAddress</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.Mote2MoteRelations</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.MoteAttributes</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspClock</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspMoteID</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.SkyButton</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.SkyFlash</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.SkyCoffeeFilesystem</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.Msp802154Radio</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspSerial</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.SkyLED</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspDebugOutput</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.SkyTemperature</moteinterface>
    </motetype>
    <motetype>
      se.sics.cooja.mspmote.SkyMoteType
      <identifier>sky2</identifier>
      <description>Sky Mote Type #sky2</description>
      <source EXPORT="discard">[CONTIKI_DIR]-2.7/examples/ipv6/rpl-collect-v2/udp-sender.c</source>
      <commands EXPORT="discard">make udp-sender.sky TARGET=sky WITH_COMPOWER=1</commands>
      <firmware EXPORT="copy">[CONTIKI_DIR]-2.7/examples/ipv6/rpl-collect-v2/udp-sender.sky</firmware>
      <moteinterface>se.sics.cooja.interfaces.Position</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.RimeAddress</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.IPAddress</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.Mote2MoteRelations</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.MoteAttributes</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspClock</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspMoteID</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.SkyButton</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.SkyFlash</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.SkyCoffeeFilesystem</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.Msp802154Radio</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspSerial</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.SkyLED</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspDebugOutput</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.SkyTemperature</moteinterface>
    </motetype>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-193.68858647303574</x>
<y>95.748477773061</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>1</id>
</interface_config>
<motetype_identifier>sky1</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-134.13435279486285</x>
<y>19.779965141624455</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>2</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-60.79954061839803</x>
<y>192.34232357651516</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>3</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-34.55133404885369</x>
<y>196.55522346993303</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>4</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-129.14009838789303</x>
<y>1.3368711857918214</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>5</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-94.17755492352391</x>
<y>95.87230734189313</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>6</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-74.93199004714978</x>
<y>154.229251641606</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>7</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-19.879427533052073</x>
<y>149.17257404278982</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>8</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-90.0960321839587</x>
<y>98.80928827931344</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>9</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-176.5290118009589</x>
<y>26.619588604655764</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>10</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-164.96653997326038</x>
<y>198.2145291412416</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>11</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-91.71936896887152</x>
<y>167.97790836418886</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>12</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-12.563671471959603</x>
<y>22.237735240925982</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>13</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-190.46307347906907</x>
<y>134.79694140382904</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>14</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-163.69221646929836</x>
<y>22.893844837886768</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>15</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-81.59638417628715</x>
<y>8.12087457058488</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>16</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-161.0112735564658</x>
<y>198.08275428060196</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>17</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-100.8087812451809</x>
<y>140.85616811726794</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>18</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-76.09537431737124</x>
<y>64.39327750847923</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>19</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-26.461970197979156</x>
<y>188.88425693354245</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>20</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>

</simulation>
<plugin>
    se.sics.cooja.plugins.SimControl
    <width>259</width>
<z>2</z>
<height>184</height>
<location_x>0</location_x>
<location_y>0</location_y>
</plugin>
<plugin>
    se.sics.cooja.plugins.Visualizer
    <plugin_config>
<skin>se.sics.cooja.plugins.skins.IDVisualizerSkin</skin>
<skin>se.sics.cooja.plugins.skins.AttributeVisualizerSkin</skin>
<skin>se.sics.cooja.plugins.skins.UDGMVisualizerSkin</skin>
<viewport>1.836243522352668 0.0 0.0 1.836243522352668 -93.43273668589363 192.8080782058222</viewport>
</plugin_config>
<width>666</width>
<z>0</z>
<height>510</height>
<location_x>369</location_x>
<location_y>-8</location_y>
</plugin>
<plugin>
    se.sics.cooja.plugins.LogListener
    <plugin_config>
<filter></filter>
</plugin_config>
<width>1347</width>
<z>4</z>
<height>150</height>
<location_x>0</location_x>
<location_y>438</location_y>
</plugin>
<plugin>
    se.sics.cooja.plugins.ScriptRunner
    <plugin_config>
<script>TIMEOUT(1200000, log.log("last msg: " + msg + "\n"));</script>
<active>true</active>
</plugin_config>
<width>600</width>
<z>-1</z>
<height>700</height>
<location_x>282</location_x>
<location_y>18</location_y>
<minimized>true</minimized>
</plugin>
<plugin>
    se.sics.cooja.plugins.RadioLogger
    <plugin_config>
<split>150</split>
<formatted_time></formatted_time>
<showdups>false</showdups>
<hidenodests>false</hidenodests>
<analyzers name="6lowpan-pcap"></analyzers>
</plugin_config>
<width>500</width>
<z>-1</z>
<height>300</height>
<location_x>182</location_x>
<location_y>64</location_y>
<minimized>true</minimized>
</plugin>
</simconf>
