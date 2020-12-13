<?xml version="1.0" encoding="UTF-8"?>
<simconf>
  <project EXPORT="discard">[APPS_DIR]/mrm</project>
  <project EXPORT="discard">[APPS_DIR]/mspsim</project>
  <project EXPORT="discard">[APPS_DIR]/avrora</project>
  <project EXPORT="discard">[APPS_DIR]/serial_socket</project>
  <project EXPORT="discard">[APPS_DIR]/powertracker</project>
  <simulation>
    <title></title>
    <delaytime>0</delaytime>
    <randomseed>123456</randomseed>
    <motedelay_us>1000000</motedelay_us>
    <radiomedium>
      se.sics.cooja.radiomediums.UDGM
      <transmitting_range></transmitting_range>
      <interference_range></interference_range>
      <success_ratio_tx></success_ratio_tx>
      <success_ratio_rx></success_ratio_rx>
    </radiomedium>
    <events>
      <logoutput>40000</logoutput>
    </events>
    <motetypesky>
    </motetypesky>
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
      <filter />
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
      <script>TIMEOUT(1800000, log.log("last msg: " + msg + "\n"));</script>
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
      <formatted_time />
      <showdups>false</showdups>
      <hidenodests>false</hidenodests>
      <analyzers name="6lowpan-pcap" />
    </plugin_config>
    <width>500</width>
    <z>-1</z>
    <height>300</height>
    <location_x>182</location_x>
    <location_y>64</location_y>
    <minimized>true</minimized>
  </plugin>
</simconf>

