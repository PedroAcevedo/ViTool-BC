# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 05:51:13 2020

@author: Pedro_Acevedo

"""
import csv
import os
import re
import mmap
import random as rnd
from random import choice
import math
import matplotlib.pyplot as plt
from statistics import mean
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw
from classes.mote import ContikiMote
import time

class Simulation():

    cscfile = ''
    RTIMER = 32768
    DIO = 'Receive DIO message' #'DODAG Information Object'
    DIS = 'Receive DIS message'#'RPL Control (DODAG Information Solicitation)'
    DAO = 'Receive DAO message'#'RPL Control (Destination Advertisement Object)'
    LOG_ACTIONS = {
        'energy_report': r'^.*ID.*%\)',
        'send_data': r'DATA send',
        'receive_data': r'DATA recv',
        'parent': r'ID:\d*\tPreferred parent:.*',
        'best': r'ID:\d*\tBest parent:.*'
    }

    def __init__(self, log, csc, pcap=None, BateryEnergy=8000):
        self.pcap = [] #self.openCSV(pcap) over development replace sniffer file
        self.log = log
        self.BEnergy = BateryEnergy
        Simulation.cscfile = csc
        self.topologies = {}
        self.motes = self.defineMotes()
        self.ROOT_DIR = os.path.abspath(os.curdir)
        self.lifetime = None

    def openCSV(self, filename):
        file = []
        with open(filename) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                file.append(row)
        return file

    def defineMotes(self):
        with open(Simulation.cscfile) as file:
            soup = BeautifulSoup(file, "lxml")
            return {node.id.text: ContikiMote(self, node.id.text, float(node.x.text), float(node.y.text), self.IP(node.id.text), self.log, self.BEnergy) for node in soup.find_all("mote") if node.id}

    def getMotes(self):
        return self.motes

    def connectMotes(self):
        for mote in self.motes:
            mote.setParentList(self.motes)

    def getIntervalTime(self, pcap, interval):
        return [self.pcap[i] for i in range(len(self.pcap))
                if float(self.pcap[i]['Time']) > interval[0]
                and float(self.pcap[i]['Time']) < interval[1]]

    def findIPadress(self, ip, packets=['IEEE 802.15.4', '6LoWPAN', 'ICMPv6', 'UDP']):
        return len([i for i in range(len(self.pcap)) if ip in self.pcap[i]['Source'] and self.pcap[i]['Protocol'] in packets])

    def getTotalPackets(self):
        return len([self.pcap[i]['Protocol'] for i in range(len(self.pcap))])

    def getControlOverhead(self):
        #return self.getCount("Info", self.DIO) + self.getCount("Info", self.DIS) + self.getCount("Info", self.DAO)
        with open(self.log, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            # dio = re.findall(bytes(rf'{self.DIO}', 'utf8'), data, re.MULTILINE)
            # dis = re.findall(bytes(rf'{self.DIS}', 'utf8'), data, re.MULTILINE)
            # dao = re.findall(bytes(rf'{self.DAO}', 'utf8'), data, re.MULTILINE)
            rpl_message = 0
            dao = 0
            for line in iter(data.readline, b""):
                strLine = str(line, "utf-8")
                if(self.getTime(line).split(':')[0] == str(self.lifetime)):
                    break
                if('Receive' in strLine):
                    if('DAO' in strLine):
                        dao = dao + 1
                    rpl_message = rpl_message + 1
            print(f"Sended in total --> {rpl_message} RPL messages")
            print("DAO messages --> {}".format(dao))
            return rpl_message
    
    def getCount(self, column, parameter): # Count with help of the PCAP file, now is deprecated
        return len([self.pcap[i][column] for i in range(len(self.pcap))
                    if parameter in self.pcap[i][column]])

    def mosFrequent(self, List):
        return max(set(List), key=List.count)

    def getID(self, logline):
        ID = re.search(bytes(r'ID:\d+', 'utf8'), logline)
        return str(ID.group())[5:-1]

    def getTime(self, logline):
        Time = re.search(bytes(r'^.*\sID', 'utf8'), logline)
        return str(Time.group())[2:-5]

    def getDataSendToSink(self):
        with open(self.log, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            data_to_sink = 0
            for line in iter(data.readline, b""):
                strLine = str(line, "utf-8")
                if(self.getTime(line).split(':')[0] == str(self.lifetime)):
                    break
                if('DATA send' in strLine):
                    data_to_sink = data_to_sink + 1
            # print(f"DATA sending to the sink is: {data_to_sink} UDP packects")
            print(data_to_sink)
            return data_to_sink

    def getDataReceiveBySink(self):
        with open(self.log, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            data_in_sink = 0
            for line in iter(data.readline, b""):
                strLine = str(line, "utf-8")
                if(self.getTime(line).split(':')[0] == str(self.lifetime)):
                    break
                if('DATA recv' in strLine):
                    data_in_sink = data_in_sink + 1
            print('Data Packets --> {}/'.format(str(data_in_sink)), end="")
            # print(f"DATA receive by the sink is: {data_in_sink} UDP packects")
            return data_in_sink

    def getPDR(self):
        return round((self.getDataReceiveBySink()/self.getDataSendToSink())*100, 2)

    def getMoteTraffic(self):
        return [mote.getTrafficTotal() for mote in self.motes]

    def IP(self, moteId):
        with open(self.log, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            regex = 'ID:'+str(moteId)+'\sTentative.*'
            mo = re.findall(bytes(regex, 'utf8'), data, re.MULTILINE)
            if mo:
                # fe80::212:7418:18:1818
                ip = [e.decode('utf8') for e in mo[0].split(b':')]
                for i in [5, 6, 7, 8]:
                    if re.search('[a-z]', ip[i]):
                        j = 0
                        add = ''
                        while(j < len(ip[i])):
                            if(ip[i][j] == '0'):
                                j = j + 1
                            else:
                                add += ip[i][j:]
                                j = len(ip[i])
                        ip[i] = add.strip()
                    else:
                        ip[i] = str(int(ip[i]))
                return 'fe80::' + ip[5] + ':' + ip[6] + ':' + ip[7] + ':' + ip[8]

    def getNumberOfMotes(self):
        return len(self.motes)

    def getNetworkLifetime(self):
        with open(self.log, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            #b'03:31.436\tID:1\t18 0 210 0 2570 72 3 0 27756 8303 8243 29286 28015 29728 25960 25376 26988 28261\r\n'
            regex = r'^.*ID.*%\)'
            powertrace = re.findall(bytes(regex, 'utf8'), data, re.MULTILINE)
            if powertrace:
                for power in powertrace:
                    ID = self.getID(power)
                    Time = self.getTime(power)
                    (all_cpu, all_lpm, all_transmit, all_listen) = [
                        float(i) for i in str(power).split()[5:9]]
                    remaining = self.BEnergy - \
                        (self.getEnergyConsumed(
                            all_transmit, all_listen, all_cpu, all_lpm))
                    if(remaining < 0):
                        # print(power)
                        # print(self.getEnergyConsumed(
                        #     all_transmit, all_listen, all_cpu, all_lpm))
                        print('Node ' + ID + ' DIE at ' + Time + ' seconds')
                        return int(Time.split(':')[0])
            return 0

    def getEnergyConsumed(self, transmit, listen, cpu, lpm):
        # Energy (J) = (Transmit * 19.5 mA + Listen * 21.5 mA + CPU time * 1.8 mA + LPM * 0.0545 mA) * 3 V /32768
        return ((transmit*19.5 + listen*21.5 + cpu*1.8 + lpm*0.0545)*3)/self.RTIMER

    def getHello(self, line):
        return int(re.sub(r"\D", "", str(line).split("'")[1]))

    def getAverageEnergy(self):
        return round((mean([mote.getEnergyConsume() for mote in self.motes.values()])/1000), 2)

    def getEnergyTrace(self):
        trace = []
        with open(self.log, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            #b'03:31.436\tID:1\t18 0 210 0 2570 72 3 0 27756 8303 8243 29286 28015 29728 25960 25376 26988 28261\r\n'
            regex = fr'^.*ID.*%\)'
            powertrace = re.findall(bytes(regex, 'utf8'), data, re.MULTILINE)
            if powertrace:
                for mote in self.motes:
                    regex = fr'^.*ID:{mote.getID()}.*%\)'
                    print(re.findall(bytes(regex, 'utf8'),
                                     powertrace, re.MULTILINE))
                    #(all_cpu, all_lpm, all_transmit, all_listen)=[float(i) for i in str(power).split()[5:9]]
                    #trace.append(Simulation.getEnergyConsumed(Simulation,all_transmit, all_listen, all_cpu, all_lpm))
        return trace

    def compareParametersVsTime(self, A, B, interval, column, parameter, nameColumn):
        Ai = self.getIntervalTime(A, interval)
        Bi = self.getIntervalTime(A, interval)
        X = [Ai[i]['Time'] for i in range(len(Ai))]
        Y = {"y_a": 0, "y_b": 0, "axis": []}
        for i in range(len(Ai)):
            if(Ai[i][column] == parameter):
                Y["y_a"] += 1
            if(Bi[i][column] == parameter):
                Y["y_b"] += 1
            Y['axis'].append(f'{Y["y_a"]}, {Y["y_b"]}')

        print(f'#{nameColumn} Time')
        for i in range(len(X)):
            print(f'{X[i]}, {Y["axis"][i]}')

    def getGeneralInfo(self, filename):
        self.pcap = self.openCSV(filename)
        ICMPV6 = self.getCount("Protocol", "ICMPv6")
        IEEE = self.getCount("Protocol", "IEEE 802.15.4")
        SixLoWPAN = self.getCount("Protocol", "6LoWPAN")
        UDP = self.getCount("Protocol", "UDP")
        controlMessages = {
            'DIO packets': self.getCount("Info", self.DIO),
            'DIS packets': self.getCount("Info", self.DIS),
            'DAO packets': self.getCount("Info", self.DAO),
            'ACK': self.getCount("Info", "Ack")}
        print(f'Total of sending packets: {self.getTotalPackets()}')
        print(f'Number of sending ICMPV6 packets: {ICMPV6}')
        print(controlMessages)
        print(f'Number of sending IEEE 802.15.4 packets: {IEEE}')
        print(f'Number of sending 6LoWPAN packets: {SixLoWPAN}')
        print(f'Number of sending UDP packets: {UDP}')
        return self.pcap

    def evaluateMetric(self, metric, limit=-1):
        switcher = {
            'PDR': self.getPDR,
            'Energy': self.getAverageEnergy,
            'Overhead': self.getControlOverhead,
            'Lifetime': self.getNetworkLifetime,
        }
        if(limit != -1 and self.lifetime == None):
            self.lifetime = limit
        func = switcher.get(metric, "Metric in development")
        return func()

    def readLog(self, args):
        pause, delay, run, signals = args
        with open(self.log, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            for line in iter(data.readline, b""):
                if not pause():
                    signals.logline.emit(str(self.getTime(line)))
                    action = self.getAction(line.decode("utf-8"))
                    if action['action'] != 'no':
                        # control(action)
                        signals.action.emit(action)
                    time.sleep(delay)
                else:
                    while pause():
                        time.sleep(0.01)
                if(not run()):
                    return

    def getAction(self, line):
        active_mote = self.motes[self.getID(bytes(line, 'utf-8'))]
        logtime = self.getTime(bytes(line, 'utf-8'))
        if(re.findall(self.LOG_ACTIONS['energy_report'], line)):
            return {'action': 'energy', 'time': logtime, 'mote': active_mote.getID(), 'energy_report': active_mote.getBatteryLevel(active_mote.getEnergyConsumeByLog(line)), 'state': active_mote.getState(logtime)}
        elif(re.findall(self.LOG_ACTIONS['send_data'], line)):
            active_mote.actualPacket(line)
            return {'action': 'sendData', 'time': logtime, 'mote': active_mote.getID(), 'parent': active_mote.actualParent()}
        elif(re.findall(self.LOG_ACTIONS['receive_data'], line)):
            sender = self.motes[str(
                re.sub(r"\D", "", line.split("\t")[2].split("'")[0]))]
            segs = sender.receivePacket(line)
            return {'action': 'receiveData', 'time': logtime, 'mote': active_mote.getID(), 'sender': sender.getID(), 'segs': segs}
        elif(re.findall(self.LOG_ACTIONS['parent'], line)):
            active_mote.addParent(line, self.motes.values())
            return {'action': 'no'}
        elif(re.findall(self.LOG_ACTIONS['best'], line)):
            active_mote.addParent(line, self.motes.values())
            return {'action': 'buildDODAG', 'time': logtime, 'mote': active_mote.getID(), 'parent': active_mote.actualParent()}
        return {'action': 'no'}

    def getDODAGTrace(self):
        self.motes = {}
        self.motes = self.defineMotes()
        with open(self.log, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            for line in iter(data.readline, b""):
                self.getAction(line.decode("utf-8"))
        treeList = {}
        for mote in self.motes.values():
            for i in range(len(mote.parentTime)):
                line_time = mote.getTime(i).split(":")[0]
                if line_time in treeList.keys():
                    if mote.getID() in treeList[line_time].keys():
                        treeList[line_time][mote.getID()]['parent'] = mote.getParents()[
                            i]
                        treeList[line_time][mote.getID()]['changes'] += 1
                    else:
                        treeList[line_time][mote.getID()] = {'parent': mote.getParents()[
                            i], 'changes': 0}
                else:
                    treeList[line_time] = {
                        mote.getID(): {'parent': mote.getParents()[i], 'changes': 0}
                    }
        return treeList

    def cleanPosInDODAG(self):
        for mote in self.motes:
            self.motes[mote].dodag_position = None

    def sortDODAG(self, tree, time):
        self.topologies[time] = {mote: [] for mote in tree}
        self.cleanPosInDODAG()
        self.topologies[time]['1'] = []

        for mote in tree:
            if tree[mote]['parent'] == '1':
                self.topologies[time]['1'].append(mote)
            else:
                self.topologies[time][tree[mote]['parent']].append(mote)
        self.levels = {}
        self.setPOS('1', self.topologies[time]['1'], 0, time)
        xi = 100
        yi = -50
        back = list(self.levels.keys())
        back.reverse()
        lastLevel = max(back)
        levelX = 100
        for level in back:
            xi = levelX
            for mote in self.levels[level]:
                if self.motes[mote].dodag_position != None:
                    xi = self.motes[mote].dodag_position[0]
                else:
                    self.motes[mote].setDODAGPos(xi, yi + 35*level)

                if mote != '1':
                    parent = tree[mote]['parent']
                    if(self.motes[parent].dodag_position == None):
                        xp = xi + (len(self.topologies[time][parent])-1)*35
                        xp = (xp+xi)/2
                        self.motes[parent].setDODAGPos(xp, yi + 35*(level-1))
                        poslevel = self.levels[level-1].index(parent)
                        if(poslevel == 0):
                            levelX = xp
                        else:
                            levelX = xp - 35*poslevel

                xi = xi + 35

    def setPOS(self, parent, childs, level, time):
        if len(childs) == 0:
            if level in self.levels.keys():
                self.levels[level].append(parent)
            else:
                self.levels[level] = [parent]
        else:
            number_of_childs = sum([len(self.topologies[time][child])
                                    for child in childs])*(len(childs))
            rate = number_of_childs/len(childs)
            for i in range(len(childs)):
                self.setPOS(childs[i], self.topologies[time]
                            [childs[i]], level+1, time)
            if level in self.levels.keys():
                self.levels[level].append(parent)
            else:
                self.levels[level] = [parent]
