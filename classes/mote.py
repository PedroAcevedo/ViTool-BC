from statistics import mean
import re, mmap
import math as mt
from datetime import datetime

class ContikiMote():

    def __init__(self, Simulation, ID,x,y,ip,log, batery_level):
        self.ID = ID
        self.x = x
        self.y = y
        self.parentTime = []
        self.parents = []
        self.Sim = Simulation
        self.ip = ip
        self.log = log
        self.actual_consume = 0
        self.dodag_position = None
        self.batery_level = batery_level
        self.sended_packets = {}
        self.diedAt = None    

    def getID(self):
            return self.ID

    def setPosition(self, point):
            self.x, self.y = point


    def setDODAGPos(self, x, y):
            self.dodag_position = (x, y)

    def getDODAGPos(self, scale):
        return (scale*self.dodag_position[0], scale*self.dodag_position[1]) if self.dodag_position != None else (1000, 1000)

    def getPosition(self, scale):
        return (scale*self.x, scale*self.y)

    def getIP(self):
        return self.ip

    def getDistanceToSink(self, sink,origin):
        dx = abs(abs(self.x) - abs(sink[0]))
        if(self.y > 0):
            dy = abs(sink[1]) + self.y
        else:
            dy = abs(abs(self.y) - abs(sink[1]))
        dy = dy
        if sink[0] >= self.x:
            dx = -1*dx
        if sink[1] > self.y:
            dy = -1*dy
        return origin[0]+dx, origin[1]+dy

    def getTraffic(self, sim):
        return f'Mote {self.ID} := { self.Sim.findIPadress(sim,self.ip)} packets'

    def getTrafficTotal(self):
        with open('trafficFiles/sniffer2.0.txt', 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            regex = r'[0-9]*\t+[1-9]*.:'
            mo = re.findall(bytes(regex, 'utf8'), data, re.MULTILINE)
            if mo:
                cont = 0
                for i in range(len(mo)):
                    s = str(mo[i]).split('\\t')
                    if s[1] == str(self.ID) and s[2] !='-' and len(s)==4:
                        cont += 1
                print(f"DATA sending to the sink by the mote {self.ID} is: {cont} UDP packects")

    def setParentList(self, motes):
        with open(self.log, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            regex = fr'ID:{self.ID}\tPreferred parent:.*'
            mo = re.findall(bytes(regex, 'utf8'), data, re.MULTILINE)
            if mo:
                for i in mo:
                    ipp = str(i).split(' ')[2][:-1]
                    self.parents.append([mote.getID() for mote in motes if mote.getIP() == ipp][0])

    def isMultipath(self):
        return len(set(self.parents)) > 1

    def addParent(self, logline, motes):
        if not '(NULL IP addr)' in str(logline):
            ipp = str(logline).split(' ')[2][:-1]
            parentId = [mote.getID()
                                    for mote in motes if mote.getIP() == ipp][0]

            if(parentId != self.actualParent()):
                self.parentTime.append(str( self.Sim.getTime(bytes(logline, "utf-8"))))
                self.parents.append(parentId)

    def actualParent(self):
        return self.parents[-1] if len(self.parents) > 0 else None

    def getParents(self):
        return self.parents

    def getTime(self, i):
        return self.parentTime[i]

    def parentListSize(self):
        return len(self.parents)

    def parentsChange(self):
        return len(set(self.parents))-1

    def actualPacket(self, line):
        self.sended_packets[self.Sim.getHello(line)] =  self.Sim.getTime(bytes(line, 'utf-8')).replace('.', ':')

    def receivePacket(self, line):
        recv =  self.Sim.getTime(bytes(line, 'utf-8')).replace('.', ':')
        hello =  self.Sim.getHello(line)
        if hello in self.sended_packets.keys():
            if  self.sended_packets[hello].split('.') == []:
                self.sended_packets[hello] =  datetime.strptime(recv, '%M:%S:%f') - datetime.strptime(self.sended_packets[hello] ,'%M:%S:%f')
                segs = self.sended_packets[hello].total_seconds()
                self.sended_packets[hello] = str(self.sended_packets[hello])
                return segs

    def getUDPackets(self):
        with open(self.log, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            regex = fr'ID:{self.ID}.*DATA'
            mo = re.findall(bytes(regex, 'utf8'), data, re.MULTILINE)
            if mo:
                print(f"DATA sending to the sink by the mote {self.ID} is: {len(mo)} UDP packects")

    def getEnergyConsume(self):
        with open(self.log, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            # b'03:31.436\tID:1\t18 0 210 0 2570 72 3 0 27756 8303 8243 29286 28015 29728 25960 25376 26988 28261\r\n'
            regex = fr'^.*ID.{self.ID}.*%\)'
            powertrace = re.findall(bytes(regex, 'utf8'), data, re.MULTILINE)
            if powertrace:
                #power = powertrace[-1]
                power = [report for report in powertrace if int(str(report, 'utf8').split(':')[0]) <= self.Sim.lifetime][-1]
                (all_cpu, all_lpm, all_transmit, all_listen) = [float(i) for i in str(power).split()[5:9]]
                return  self.Sim.getEnergyConsumed(all_transmit, all_listen, all_cpu, all_lpm)    

    def getEnergyConsumeByLog(self, logline):
        power = bytes(logline, "utf-8")
        (all_cpu, all_lpm, all_transmit, all_listen) = [float(i) for i in str(power).split()[5:9]]
        return  self.Sim.getEnergyConsumed(all_transmit, all_listen, all_cpu, all_lpm)    

    def getEnergyTrace(self):
        trace = []
        with open(self.log, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            # b'03:31.436\tID:1\t18 0 210 0 2570 72 3 0 27756 8303 8243 29286 28015 29728 25960 25376 26988 28261\r\n'
            regex = fr'^.*ID.{self.ID}.*%\)'
            powertrace = re.findall(bytes(regex, 'utf8'), data, re.MULTILINE)
            if powertrace:
                for power in powertrace:
                    (all_cpu, all_lpm, all_transmit, all_listen) = [float(i) for i in str(power).split()[5:9]]
                    trace.append(
                        f'{ self.Sim.getTime(power)}:\t{round( self.Sim.getEnergyConsumed(all_transmit, all_listen, all_cpu, all_lpm),5)} mJ')
        return trace

    def getAverageLatency(self):
        if (len(self.sended_packets.values()) > 0):
            report = [float(latency) for latency in self.sended_packets.values() if not isinstance(latency, str)]
            return mean(report) if len(report) > 0 else 0
        else:
            return 0

    def getBattery(self):
        return self.batery_level

    def getBatteryLevel(self, consume):
        self.actual_consume = consume
        return mt.floor((self.batery_level - consume)*100/self.batery_level)

    def getRemainingBattery(self):
        return mt.floor((self.batery_level - self.actual_consume)*100/self.batery_level)

    def getState(self, logtime):
        state = 'alive'
        if(self.batery_level - self.actual_consume <= 0):
            self.diedAt = int(logtime.split(":")[0])
            state = 'die'
        return state
