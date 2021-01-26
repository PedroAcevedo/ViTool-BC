import os


from random import choice
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import math as mt

from classes.simulation import Simulation


fileDir = os.path.dirname(__file__) 

class Topologies():

    def __init__ (self, index, name, nodes, TX, RX, endInterval, startInterval=[0,0], TR=100, IR=120, sink=1):
        self.index = index
        self.name = name
        self.nodes = nodes + 1
        self.source = nodes
        self.TX = str(TX)
        self.RX = str(RX)
        self.TR = str(TR)
        self.IR = str(IR)
        self.endInterval = endInterval
        self.startInterval = startInterval
        self.sink = sink


    def generate(self):
        with open('./examples/topologies/template.csc') as file:
            soup = BeautifulSoup(file, "html.parser")
            soup.title.string = self.name
            soup.transmitting_range.string = self.TR
            soup.interference_range.string = self.IR
            soup.success_ratio_tx.string = self.TX
            soup.success_ratio_rx.string = self.RX
            mote = BeautifulSoup(''.join(self.getMote(i,'sky2') for i in range(1,self.nodes+1)), "html.parser")
            soup.find('motetypesky').insert_after(mote)
            #lines = str(soup).split('\n')
            file = open(os.path.join(fileDir,f'./../examples/topologies/view-nodes{self.nodes}-Sim{self.index}.csc'), 'w')
            lines = str(soup)
            lines = lines.replace('<motetypesky>',"""
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
            """)
            lines = lines.replace('</motetypesky>',"""
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
            """)
            file.write(lines)
            file.close()

    def getMote(self,id, type):
        if(id==1): type='sky1'
        valid = False
        while not valid:
            x = self.getCoordinate(0,id)
            y = self.getCoordinate(1,id)
            if( x not in self.insideRange(id, 0) or y not in self.insideRange(id, 1)):
                valid = True

        return f"""
                <mote>
                <breakpoints />
                <interface_config>
                    se.sics.cooja.interfaces.Position
                    <x>{ x if id!=1 else self.endInterval[0]}</x>
                    <y>{ y if id!=1 else 0.0}</y>
                    <z>0.0</z>
                </interface_config>
                <interface_config>
                    se.sics.cooja.mspmote.interfaces.MspMoteID
                    <id>{id}</id>
                </interface_config>
                <motetype_identifier>{type}</motetype_identifier>
                </mote>
                """

    def getCoordinate(self, axis, id):
        if(self.nodes < 3):
            return choice([i for i in range(int(self.startInterval[axis]/2*self.areaById(id)),int(self.endInterval[axis]/2*self.areaById(id))) if i not in self.insideRange(id, axis)])
        else:
            return choice([i for i in range(int(self.startInterval[axis]*self.areaById(id)),int(self.endInterval[axis]*self.areaById(id)))])


    def areaById (self, id):
        area = ((int(id/10)+1)*10/self.nodes)
        return area if id < self.nodes else 1.0

    def insideRange(self, id, i):
        if(id < 10):
            return range(-10,10)
        else:
            less = 10 if id < self.nodes else 20
            return range(int(self.startInterval[i]*self.areaById(id-less)),int(self.endInterval[i]*self.areaById(id-less)))

## trafficFiles/lg-OF-Sim1-4.txt
## trafficFiles/PCAP-OF-Sim1-4.csv
## trafficFiles/view-nodes40-Sim1-4.csc

def generateGraph(metric, ofs, nodeInterval, folder="sim-1", lifetime=[]):
    data = dict()
    for i in range(len(nodeInterval)):
        path_to = f'examples/{folder}/{nodeInterval[i]}'
        for of in ofs:
            print(f'OF analizada --> {of}')
            sim = Simulation(f'{path_to}/log-{of}-Sim{i+1}.txt', f'{path_to}/view-nodes{nodeInterval[i]}-Sim{i+1}.csc');
            if(metric != 'Lifetime'):
                m = sim.evaluateMetric(metric, limit=lifetime[i])
            else:
                m = sim.evaluateMetric(metric)
            #sim.getGeneralInfo(f'{path_to}/PCAP-{of}.csv')
            if (m == None):
                m = 0 
            if of in data.keys(): 
                data[of].append(m)
            else:
                data[of] = [m]
    print(data)
    df = pd.DataFrame(data, index=nodeInterval)
    print(df)
    plt.xlabel('Number of nodes')
    #plt.style.use('fivethirtyeight')
    if(metric == 'PDR'):
        df.plot(kind='bar', rot=0, ylim=(10,100))
        plt.ylabel('Packet Delivery Rate (PDR)')
    elif(metric == 'Energy'):
        df.plot(kind='area', stacked=False)
        plt.ylabel('Average energy consumption (j)')
    elif(metric == 'Overhead'):
        df.plot(kind='bar',rot=0)
        plt.ylabel('Control Message Overhead')
    elif(metric == 'Lifetime'):
        df.plot(kind='bar', rot=0)
        plt.xlabel('Number of nodes')
        plt.ylabel('Network lifetime (min)')
        for key in data.keys():
            for i, element in enumerate(data[key]):
                if (element == 0):
                    data[key][i] = 1000
        return (min(data.values()))

def generateGraphTraffic(metric, ofs, ppm, nodes, folder="sim-1", lifetime=[]):
    data = dict()
    for i in range(len(ppm)):
        path_to = f'examples/{folder}/{ppm[i]}'
        for of in ofs:
            print(f'OF analizada --> {of}')
            sim = Simulation(f'{path_to}/log-{of}-Sim{i+1}.txt', f'examples/{folder}/view-nodes{nodes}-Sim1.csc');
            if(metric != 'Lifetime'):
                m = sim.evaluateMetric(metric, limit=lifetime[i])
            else:
                m = sim.evaluateMetric(metric)
            #sim.getGeneralInfo(f'{path_to}/PCAP-{of}.csv')
            if (m == None):
                m = 0 
            if of in data.keys(): 
                data[of].append(m)
            else:
                data[of] = [m]
    print(data)
    df = pd.DataFrame(data, index=ppm)
    print(df)
    plt.xlabel('ppm')
    import seaborn as sns
    sns.set(font='DejaVu Sans',
            rc={'axes.axisbelow': False,
                'axes.edgecolor': 'lightgrey',
                'axes.facecolor': 'None',
                'axes.grid': False,
                'axes.labelcolor': 'dimgrey',
                'axes.spines.right': False,
                'axes.spines.top': False,
                'figure.facecolor': 'white',
                'lines.solid_capstyle': 'round',
                'patch.edgecolor': 'w',
                'patch.force_edgecolor': True,
                'text.color': 'dimgrey',
                'xtick.bottom': True,
                'xtick.color': 'dimgrey',
                'xtick.direction': 'out',
                'xtick.top': False,
                'ytick.color': 'dimgrey',
                'ytick.direction': 'out',
                'ytick.left': False,
                'ytick.right': False})
    sns.set_context("notebook", rc={"font.size": 16,
                                    "axes.titlesize": 20,
                                    "axes.labelsize": 18})    
    plt.style.use('fivethirtyeight')
    if(metric == 'PDR'):
        df.plot(kind='bar', rot=0,  ylim=(0,100))
        plt.ylabel('Packet Delivery Rate (PDR)')
    elif(metric == 'Energy'):
        df.plot(kind='area', stacked=False)
        plt.ylabel('Average energy consumption (j)')
    elif(metric == 'Overhead'):
        df.plot(kind='bar',rot=0)
        plt.ylabel('Control Message Overhead')
    elif(metric == 'Lifetime'):
        df.plot(kind='bar', rot=0)
        plt.xlabel('ppm')
        plt.ylabel('Network lifetime (min)')
        for key in data.keys():
            for i, element in enumerate(data[key]):
                if (element == 0):
                    data[key][i] = 1000
        return (min(data.values()))

# Sim = Simulation('trafficFiles/sims/sim-4/30/log-mrhof-Sim3.txt','trafficFiles/sims/sim-4/30/PCAP-mrhof-Sim3.csv','view-nodes30-Sim3.csc')
# print(Sim.motes['3'].getEnergyConsumeByLog('20:01.260	ID:21	 153607 P 0.18 19 2348414 36967561 487180 862161 0 454435 162326 1803549 56121 48775 0 16926 (radio 3.-285% / 5.33% tx 1.-86% / 2.85% listen 2.-200% / 2.48%)'))
# Sim.loadLog()
# print(Sim.getLogByTime('01:00.735'))

# # Sim.getGeneralInfo()
# print(f'Overhead := {Sim.getControlOverhead()}')
# print(f'PDR := {Sim.getPDR()}%')
# print(f'Network Lifetime := {Sim.getNetworkLifetime()}')
# print(f'Average Energy := {Sim.getAverageEnergy()} joules')
# Sim.drawSimulation()

# topologyGenerator(1, 'mySimulation',10,9,1.0,0.0, [75, 75], startInterval=[-75,-75], TR=50, IR=70).generate()
# topologyGenerator(2, 'mySimulation',20,19,1.0,0.0, [75, 75], startInterval=[-75,-75], TR=50, IR=70).generate()
# topologyGenerator(3, 'mySimulatåion',30,29,1.0,0.0, [75, 75], startInterval=[-75,-75], TR=50, IR=70).generate()
# topologyGenerator(4, 'mySimulation',40,39,1.0,0.0, [75, 75], startInterval=[-75,-75], TR=50, IR=70).generate()

# generateGraph('PDR', ['mrhof','rc'],[25])
# generateGraph('Overhead', ['mrhof', 'of0'],[10,20,30])
# generateGraph('Energy', ['mrhof', 'of0'],[10,20,30]) 
# generateGraph('Lifetime', ['mrhof', 'of0'],[10,20,30])
#plt.show()