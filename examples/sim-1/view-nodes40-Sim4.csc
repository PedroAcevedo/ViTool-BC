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
                    <x>-182.82406641596057</x>
<y>161.54344262070254</y>
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
                    <x>-38.64471464489756</x>
<y>143.30864336533017</y>
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
                    <x>-105.08493099334702</x>
<y>8.314987627483795</y>
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
                    <x>-103.74756267658466</x>
<y>13.523834041677475</y>
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
                    <x>-68.96026484848923</x>
<y>187.61204184019522</y>
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
                    <x>-192.15787206328525</x>
<y>45.75252319889864</y>
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
                    <x>-41.96921559967765</x>
<y>79.13582731341539</y>
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
                    <x>-185.11467521898194</x>
<y>27.527610990983487</y>
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
                    <x>-18.279934158061618</x>
<y>175.6155168883174</y>
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
                    <x>-116.54591445456639</x>
<y>19.06725632329307</y>
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
                    <x>-60.99486639571017</x>
<y>177.35390185513643</y>
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
                    <x>-93.99444985510617</x>
<y>164.371343610243</y>
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
                    <x>-129.23573770072818</x>
<y>133.32649360781122</y>
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
                    <x>-109.1049134718833</x>
<y>83.49913019143642</y>
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
                    <x>-150.77913362129075</x>
<y>73.28412568391374</y>
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
                    <x>-148.83263657467114</x>
<y>77.46731558030535</y>
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
                    <x>-60.95105393954299</x>
<y>71.70974844091693</y>
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
                    <x>-75.64131578029021</x>
<y>0.17570153636314867</y>
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
                    <x>-91.72474972054235</x>
<y>174.44403047490985</y>
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
                    <x>-140.45725247330301</x>
<y>133.4163508685992</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>20</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-198.97366616160704</x>
<y>84.16037003409245</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>21</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-44.422389609911676</x>
<y>178.50451301005583</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>22</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-130.15795847922905</x>
<y>177.70984703401297</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>23</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-122.12047012699811</x>
<y>96.03149761102702</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>24</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-83.5826563385516</x>
<y>105.87234035678479</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>25</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-153.73718365632016</x>
<y>166.9044017447821</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>26</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-105.53817241561619</x>
<y>189.6313751669674</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>27</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-131.84289812795512</x>
<y>83.61210837308428</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>28</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-163.8692810235815</x>
<y>164.96480442231737</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>29</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-75.81514229901177</x>
<y>24.247731221580615</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>30</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-56.92690793872133</x>
<y>64.89650124569086</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>31</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-189.771401901554</x>
<y>120.88934149267547</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>32</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-78.19066993920667</x>
<y>113.01955483685131</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>33</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-175.60536160420895</x>
<y>118.65734531000686</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>34</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-112.79772440301261</x>
<y>164.96666247262675</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>35</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-101.18743610724499</x>
<y>103.64403570251679</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>36</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-23.55872534863788</x>
<y>138.29976024875575</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>37</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-173.6396565634733</x>
<y>86.83627942693623</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>38</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-199.015072756683</x>
<y>158.4975234293197</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>39</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-40.89760886065292</x>
<y>172.525564258671</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>40</id>
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
