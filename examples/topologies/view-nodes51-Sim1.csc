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
<success_ratio_rx>0.9</success_ratio_rx>
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
                    <x>100</x>
<y>0.0</y>
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
                    <x>-9</x>
<y>-19</y>
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
                    <x>-8</x>
<y>16</y>
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
                    <x>-2</x>
<y>15</y>
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
                    <x>14</x>
<y>-10</y>
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
                    <x>11</x>
<y>9</y>
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
                    <x>4</x>
<y>-13</y>
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
                    <x>18</x>
<y>-14</y>
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
                    <x>16</x>
<y>-5</y>
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
                    <x>12</x>
<y>-30</y>
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
                    <x>4</x>
<y>37</y>
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
                    <x>-38</x>
<y>32</y>
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
                    <x>-37</x>
<y>-15</y>
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
                    <x>-20</x>
<y>37</y>
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
                    <x>-11</x>
<y>-34</y>
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
                    <x>-10</x>
<y>22</y>
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
                    <x>-32</x>
<y>-10</y>
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
                    <x>15</x>
<y>35</y>
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
                    <x>34</x>
<y>-27</y>
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
                    <x>46</x>
<y>27</y>
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
                    <x>24</x>
<y>50</y>
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
                    <x>53</x>
<y>-30</y>
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
                    <x>-46</x>
<y>3</y>
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
                    <x>38</x>
<y>52</y>
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
                    <x>-2</x>
<y>-51</y>
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
                    <x>14</x>
<y>-42</y>
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
                    <x>47</x>
<y>-33</y>
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
                    <x>55</x>
<y>-18</y>
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
                    <x>24</x>
<y>51</y>
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
                    <x>-78</x>
<y>-11</y>
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
                    <x>66</x>
<y>11</y>
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
                    <x>-65</x>
<y>36</y>
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
                    <x>51</x>
<y>72</y>
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
                    <x>-67</x>
<y>20</y>
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
                    <x>60</x>
<y>66</y>
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
                    <x>59</x>
<y>47</y>
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
                    <x>-76</x>
<y>25</y>
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
                    <x>-11</x>
<y>-67</y>
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
                    <x>71</x>
<y>-46</y>
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
                    <x>97</x>
<y>65</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>40</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-83</x>
<y>-7</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>41</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>93</x>
<y>-47</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>42</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>1</x>
<y>87</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>43</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-20</x>
<y>92</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>44</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-32</x>
<y>83</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>45</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>17</x>
<y>-95</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>46</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>2</x>
<y>-83</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>47</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-15</x>
<y>-91</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>48</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-84</x>
<y>64</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>49</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-112</x>
<y>-73</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>50</id>
</interface_config>
<motetype_identifier>sky2</motetype_identifier>
</mote>
<mote>
<breakpoints></breakpoints>
<interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>-88</x>
<y>-38</y>
<z>0.0</z>
</interface_config>
<interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>51</id>
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
<script>TIMEOUT(1800000, log.log("last msg: " + msg + "\n"));

battery_level = 9000;
while(1) {
        YIELD();
   msgArray = msg.split(' ');
   if(msgArray.length &gt; 2){
        if(msgArray[2].equals("P")) {
           consume = ((msgArray[7]*19.5 +  msgArray[8]*21.5 +
msgArray[5]*1.8 + msgArray[6]*0.0545)*3)/32768;
           log.log("Energy consume by mote " + id + " is " + consume +  "  mJ\n");
           remaining = battery_level - consume;
           if(remaining &lt;= 0){
            log.log("mote " + id + " out of energy\n");
            mote.getSimulation().removeMote(mote);
           }
        }
   }
}</script>
<active>true</active>
</plugin_config>
<width>600</width>
<z>-1</z>
<height>700</height>
<location_x>282</location_x>
<location_y>18</location_y>
<minimized>true</minimized>
</plugin>
</simconf>
