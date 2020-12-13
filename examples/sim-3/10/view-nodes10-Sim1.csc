<?xml version="1.0" encoding="UTF-8"?>
<simconf>
  <project EXPORT="discard">[APPS_DIR]/mrm</project>
  <project EXPORT="discard">[APPS_DIR]/mspsim</project>
  <project EXPORT="discard">[APPS_DIR]/avrora</project>
  <project EXPORT="discard">[APPS_DIR]/serial_socket</project>
  <project EXPORT="discard">[APPS_DIR]/collect-view</project>
  <project EXPORT="discard">[APPS_DIR]/powertracker</project>
  <simulation>
    <title>z1_simulation_prueba1</title>
    <randomseed>123456</randomseed>
    <motedelay_us>1000000</motedelay_us>
    <radiomedium>
      se.sics.cooja.radiomediums.UDGM
      <transmitting_range>50.0</transmitting_range>
      <interference_range>100.0</interference_range>
      <success_ratio_tx>1.0</success_ratio_tx>
      <success_ratio_rx>1.0</success_ratio_rx>
    </radiomedium>
    <events>
      <logoutput>40000</logoutput>
    </events>
    <motetype>
      se.sics.cooja.mspmote.Z1MoteType
      <identifier>z11</identifier>
      <description>Z1 Mote Type #z11</description>
      <source EXPORT="discard">[CONTIKI_DIR]-2.7/examples/ipv6/rpl-collect-v2/udp-sink.c</source>
      <commands EXPORT="discard">make udp-sink.z1 TARGET=z1</commands>
      <firmware EXPORT="copy">[CONTIKI_DIR]-2.7/examples/ipv6/rpl-collect-v2/udp-sink.z1</firmware>
      <moteinterface>se.sics.cooja.interfaces.Position</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.RimeAddress</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.IPAddress</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.Mote2MoteRelations</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.MoteAttributes</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspClock</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspMoteID</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspButton</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.Msp802154Radio</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspDefaultSerial</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspLED</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspDebugOutput</moteinterface>
    </motetype>
    <motetype>
      se.sics.cooja.mspmote.Z1MoteType
      <identifier>z12</identifier>
      <description>Z1 Mote Type #z12</description>
      <source EXPORT="discard">[CONTIKI_DIR]-2.7/examples/ipv6/rpl-collect-v2/udp-sender.c</source>
      <commands EXPORT="discard">make udp-sender.z1 TARGET=z1 WITH_COMPOWER=1</commands>
      <firmware EXPORT="copy">[CONTIKI_DIR]-2.7/examples/ipv6/rpl-collect-v2/udp-sender.z1</firmware>
      <moteinterface>se.sics.cooja.interfaces.Position</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.RimeAddress</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.IPAddress</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.Mote2MoteRelations</moteinterface>
      <moteinterface>se.sics.cooja.interfaces.MoteAttributes</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspClock</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspMoteID</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspButton</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.Msp802154Radio</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspDefaultSerial</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspLED</moteinterface>
      <moteinterface>se.sics.cooja.mspmote.interfaces.MspDebugOutput</moteinterface>
    </motetype>
    <mote>
      <breakpoints />
      <interface_config>
        se.sics.cooja.interfaces.Position
        <x>7.527933679315353</x>
        <y>-48.53045547539827</y>
        <z>0.0</z>
      </interface_config>
      <interface_config>
        se.sics.cooja.mspmote.interfaces.MspMoteID
        <id>1</id>
      </interface_config>
      <motetype_identifier>z11</motetype_identifier>
    </mote>
    <mote>
      <breakpoints />
      <interface_config>
        se.sics.cooja.interfaces.Position
        <x>22.99336060512998</x>
        <y>-31.348484240966826</y>
        <z>0.0</z>
      </interface_config>
      <interface_config>
        se.sics.cooja.mspmote.interfaces.MspMoteID
        <id>2</id>
      </interface_config>
      <motetype_identifier>z12</motetype_identifier>
    </mote>
    <mote>
      <breakpoints />
      <interface_config>
        se.sics.cooja.interfaces.Position
        <x>-13.402345430203306</x>
        <y>-24.276721713298098</y>
        <z>0.0</z>
      </interface_config>
      <interface_config>
        se.sics.cooja.mspmote.interfaces.MspMoteID
        <id>3</id>
      </interface_config>
      <motetype_identifier>z12</motetype_identifier>
    </mote>
    <mote>
      <breakpoints />
      <interface_config>
        se.sics.cooja.interfaces.Position
        <x>11.390672437129428</x>
        <y>-20.356463871282095</y>
        <z>0.0</z>
      </interface_config>
      <interface_config>
        se.sics.cooja.mspmote.interfaces.MspMoteID
        <id>4</id>
      </interface_config>
      <motetype_identifier>z12</motetype_identifier>
    </mote>
    <mote>
      <breakpoints />
      <interface_config>
        se.sics.cooja.interfaces.Position
        <x>34.852039654740324</x>
        <y>13.770004988292069</y>
        <z>0.0</z>
      </interface_config>
      <interface_config>
        se.sics.cooja.mspmote.interfaces.MspMoteID
        <id>5</id>
      </interface_config>
      <motetype_identifier>z12</motetype_identifier>
    </mote>
    <mote>
      <breakpoints />
      <interface_config>
        se.sics.cooja.interfaces.Position
        <x>-12.474376486262083</x>
        <y>8.202191324644728</y>
        <z>0.0</z>
      </interface_config>
      <interface_config>
        se.sics.cooja.mspmote.interfaces.MspMoteID
        <id>6</id>
      </interface_config>
      <motetype_identifier>z12</motetype_identifier>
    </mote>
    <mote>
      <breakpoints />
      <interface_config>
        se.sics.cooja.interfaces.Position
        <x>58.05126325327091</x>
        <y>36.041259642881435</y>
        <z>0.0</z>
      </interface_config>
      <interface_config>
        se.sics.cooja.mspmote.interfaces.MspMoteID
        <id>7</id>
      </interface_config>
      <motetype_identifier>z12</motetype_identifier>
    </mote>
    <mote>
      <breakpoints />
      <interface_config>
        se.sics.cooja.interfaces.Position
        <x>19.07656760773952</x>
        <y>38.82516647470511</y>
        <z>0.0</z>
      </interface_config>
      <interface_config>
        se.sics.cooja.mspmote.interfaces.MspMoteID
        <id>8</id>
      </interface_config>
      <motetype_identifier>z12</motetype_identifier>
    </mote>
    <mote>
      <breakpoints />
      <interface_config>
        se.sics.cooja.interfaces.Position
        <x>38.56391543050521</x>
        <y>-6.645311778414849</y>
        <z>0.0</z>
      </interface_config>
      <interface_config>
        se.sics.cooja.mspmote.interfaces.MspMoteID
        <id>9</id>
      </interface_config>
      <motetype_identifier>z12</motetype_identifier>
    </mote>
    <mote>
      <breakpoints />
      <interface_config>
        se.sics.cooja.interfaces.Position
        <x>-23.610003813556766</x>
        <y>35.11329069894021</y>
        <z>0.0</z>
      </interface_config>
      <interface_config>
        se.sics.cooja.mspmote.interfaces.MspMoteID
        <id>10</id>
      </interface_config>
      <motetype_identifier>z12</motetype_identifier>
    </mote>
  </simulation>
  <plugin>
    se.sics.cooja.plugins.SimControl
    <width>280</width>
    <z>1</z>
    <height>160</height>
    <location_x>400</location_x>
    <location_y>0</location_y>
  </plugin>
  <plugin>
    se.sics.cooja.plugins.Visualizer
    <plugin_config>
      <moterelations>true</moterelations>
      <skin>se.sics.cooja.plugins.skins.IDVisualizerSkin</skin>
      <viewport>2.1552445403029323 0.0 0.0 2.1552445403029323 165.88533181569963 170.32227192903937</viewport>
    </plugin_config>
    <width>400</width>
    <z>-1</z>
    <height>400</height>
    <location_x>1</location_x>
    <location_y>1</location_y>
    <minimized>true</minimized>
  </plugin>
  <plugin>
    se.sics.cooja.plugins.ScriptRunner
    <plugin_config>
      <script>/*&#xD;
 * Example Contiki test script (JavaScript).&#xD;
 * A Contiki test script acts on mote output, such as via printf()'s.&#xD;
 * The script may operate on the following variables:&#xD;
 *  Mote mote, int id, String msg&#xD;
 */&#xD;
&#xD;
/* Make test automatically fail (timeout) after 100 simulated seconds */&#xD;
//TIMEOUT(100000); /* milliseconds. no action at timeout */&#xD;
TIMEOUT(1800000, log.log("last msg: " + msg + "\n")); /* milliseconds. print last msg at timeout */</script>
      <active>true</active>
    </plugin_config>
    <width>600</width>
    <z>-1</z>
    <height>500</height>
    <location_x>120</location_x>
    <location_y>120</location_y>
    <minimized>true</minimized>
  </plugin>
  <plugin>
    se.sics.cooja.plugins.LogListener
    <plugin_config>
      <filter />
      <formatted_time />
      <coloring />
    </plugin_config>
    <width>785</width>
    <z>0</z>
    <height>240</height>
    <location_x>-8</location_x>
    <location_y>116</location_y>
  </plugin>
</simconf>

