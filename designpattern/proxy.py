"""
Proxy pattern provide with an same interface to another class. The client code works directly with
proxy, which will delegate call to the main class.

Advantages:
-------------------------
1. Protect the real component from undue complexity

2. Provide security to main component by wrapping the main class with proxy and add extra level
of indirection

3. Facilitating interaction with remote system, by managing the network connection and
transmission route and deleting call to remote object

4. Can be used to optimize the performance using caching of heavily of frequently used objects.

Disadvantages:
-------------------------
1. Increase in response time, since proxy facilitate lazy initialization the response time will
increase when the connection is established for the first time.
"""
from random import random, randint
from abc import ABCMeta, abstractmethod


class AbstractSubject(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def sort(self, reverse=False):
        pass


class RealSubject(AbstractSubject):
    def __init__(self):
        self.digits = [random() for i in range(10000000)]

    def sort(self, reverse=False):
        self.digits.sort()
        if reverse:
            self.digits.reverse()


class ProxySubject(AbstractSubject):
    cached_object = None
    reference_count = 0

    def __init__(self):
        if ProxySubject.cached_object is None:
            ProxySubject.cached_object = RealSubject()
            ProxySubject.reference_count += 1

    def sort(self, reverse=False):
        self.__class__.sort(reverse)

    def __del__(self):
        if ProxySubject.reference_count > 0:
            ProxySubject.reference_count -= 1

        if ProxySubject.reference_count == 0 and ProxySubject.cached_object is not None:
            del ProxySubject.cached_object
            return True
        return False
