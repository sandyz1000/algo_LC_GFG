"""
Observer design pattern try to facilitate one to many relationship in software engineering.
Eg: Several even listener
will listen handle mouse click on the user interface item.
Advantages:
1. Maintain loose coupling between subject and observer
2. Subject can keep any no of observer
3. An observer can be changed at runtime.
"""

from __future__ import print_function
import time
from abc import ABCMeta, abstractmethod
from datetime import datetime


class AbstractSubject(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

    @abstractmethod
    def unregister_observer(self, observer):
        pass


class Subject(AbstractSubject):
    def __init__(self):
        self.observer_list = []
        self.cur_time = None

    def register_observer(self, observer):
        if observer not in self.observer_list:
            self.observer_list.append(observer)
            return True
        return False

    def unregister_observer(self, observer):
        if observer in self.observer_list:
            self.observer_list.remove(observer)
            return True
        return False

    def notify_observers(self):
        self.cur_time = time.time()
        for item in self.observer_list:
            item.notify(self.cur_time)


class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def notify(self, unix_timestamp):
        pass


class EUTimeObserver(Observer):
    def __init__(self, name):
        self.name = name

    def notify(self, unix_timestamp):
        _time = datetime.fromtimestamp(int(unix_timestamp)).strftime("%Y-%m-%d %H:%M:%S")
        print('Observer {} says {}'.format(self.name, _time))


class USATimeObserver(Observer):
    def __init__(self, name):
        self.name = name

    def notify(self, unix_timestamp):
        _time = datetime.fromtimestamp(int(unix_timestamp)).strftime("%Y-%m-%d %I:%M:%S%p")
        print('Observer {} says {}'.format(self.name, _time))


if __name__ == '__main__':
    subject = Subject()

    observer_1 = EUTimeObserver("EU Time")
    subject.register_observer(observer_1)

    observer_2 = USATimeObserver("USA Time")
    subject.register_observer(observer_2)

    time.sleep(2)

    subject.notify_observers()
    time.sleep(2)
    print("Notifying observers completed")
