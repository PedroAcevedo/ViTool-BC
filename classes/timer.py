from threading import Thread, Event
import time

class simulationTime():

    def __init__(self, reportTime, delay=0, timeout=30):
        self.milliseconds = 0
        self.seconds = 0
        self.minutes = 0
        self.stop = False
        self.timeout = timeout
        self.reportTime = reportTime
        self.started = False
        self.currentTime = '00:00.000'

    def showTime(self, args):
        delay, signals = args
        while True:
            if(not self.stop):
                self.milliseconds += 1
                time.sleep(delay)
                if(self.milliseconds == 1000):
                    self.milliseconds = 0
                    self.seconds += 1
                    
                    if(self.seconds == 60):
                        self.seconds = 0
                        self.minutes += 1

                        if(self.minutes == self.timeout):
                            self.stop = True
                
                self.currentTime = f'{ "0" + str(self.minutes) if self.minutes < 10 else self.minutes}:{ "0" + str(self.seconds) if self.seconds < 10 else self.seconds}.{"00" + str(self.milliseconds) if self.milliseconds < 10 else "0" + str(self.milliseconds) if self.milliseconds < 100 else self.milliseconds}'
                #multiprocessing.Process(target=self.reportTime, args=[self.currentTime]).start()
                #self.reportTime(self.currentTime) 

    def stopTimer(self):
        self.stop = True

    def resume(self):
        self.stop = False

    def start(self, currentTime):
        if(not self.started):
            #self.stupid_parallel(self.showTime,nprocesses=5)([ ]) #multiprocessing.Process(target=self.showTime)#Thread(target=self.showTime)
            self.showTime(currentTime)
            self.started = True
        else:
            if(self.stop):
                self.resume()