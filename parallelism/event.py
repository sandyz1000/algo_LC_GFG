"""
Events are objects that are used for communication between threads. A thread waits for a
signal while another thread outputs it.
Basically, an event object manages an internal flag that can be set to true with the set()
method and reset to false with the clear() method. The wait() method blocks until the flag is true.
"""
import time
import random
from threading import Event, Thread
from random import randint


class Interval(object):
    def __init__(self, time, thresholdCount):
        self.__time = time
        self.__counter = 0
        self.__thresholdCount = thresholdCount
        self.aList = []
        self.__evt = Event()

    def setInteval(self):
        while not self.__evt.wait(self.__time) and self.__counter < self.__thresholdCount:
            self.__counter += 1
            self.getMax()

    def getMax(self):
        self.aList.append(randint(0, 9))


items = []
event = Event()


class Consumer(Thread):
    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        while True:
            time.sleep(2)
            self.event.wait()  # Wait if flag set False and continue if flag is True
            item = self.items.pop()
            print ('Consumer notify : %d popped from list by %s' %(item, self.name))


class Producer(Thread):
    def __init__(self, integers, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        global item
        for i in range(100):
            time.sleep(2)
            item = random.randint(0, 256)
            self.items.append(item)
            print ('Producer notify : item N %d appended to list by %s' % (item, self.name))
            print ('Producer notify : event set by %s' % self.name)
            self.event.set()
            print ('Produce notify : event cleared by %s \n' % self.name)
            self.event.clear()

if __name__ == '__main__':
    # intv = Interval(1, 15)
    # intv.setInteval()
    # print intv.aList
    t1 = Producer(items, event)
    t2 = Consumer(items, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
