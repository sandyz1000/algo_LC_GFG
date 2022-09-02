"""
Call Center Design

Imagine you have a call center with three levels of employees: respondent, manager and director.
An incoming telephone call must be first allocated to a respondent who is free. If the respondent
can't handle the call, he or she must escalate the call to a manager. If the manager is not free
or not able to handle it, then the call should be escalated to a director. Design the classes and
data structures for this problem. Implement a method dispatchCaLL() which assigns a call to the
first available employee.

==SOLUTION==

All three ranks of employees have different work to be done, so those specific functions are
profile specific. We should keep these things within their respective class.
There are a few things which are common to them, like address, name, job title, and age. These
things can be kept in one class and can be extended or inherited by others.
Finally, there should be one CallHandler class which would route the calls to the correct person.

Note that on any object-oriented design question, there are many ways to design the objects.
Discuss the trade-offs of different solutions with your interviewer. You should usually design
for long-term code flexibility and maintenance.

"""
from abc import ABCMeta, abstractmethod
from collections import deque
from enum import Enum


class Rank(Enum):
    OPERATOR = 0
    SUPERVISOR = 1
    DIRECTOR = 2


class Employee(object):
    """
    Employee is a super class for the Director, Manager, and Respondent classes. It is
    implemented as an abstract class since there should be no reason to instantiate an Employee
    type directly
    """
    __metaclass__ = ABCMeta

    def __init__(self, employee_id, name, rank, call_center):
        self.employee_id = employee_id
        self.name = name
        self.rank = rank
        self.call = None
        self.call_center = call_center

    def take_call(self, call):
        """Assume the employee will always successfully take the call."""
        self.call = call
        self.call.employee = self
        self.call.state = CallState.IN_PROGRESS

    def complete_call(self):
        self.call.state = CallState.COMPLETE
        self.call_center.notify_call_completed(self.call)

    @abstractmethod
    def escalate_call(self):
        pass

    def _escalate_call(self):
        self.call.state = CallState.READY
        call = self.call
        self.call = None
        self.call_center.notify_call_escalated(call)


class Operator(Employee):
    def __init__(self, employee_id, name):
        super(Operator, self).__init__(employee_id, name, Rank.OPERATOR, None)

    def escalate_call(self):
        self.call.level = Rank.SUPERVISOR
        self._escalate_call()


class Supervisor(Employee):
    def __init__(self, employee_id, name):
        super(Supervisor, self).__init__(employee_id, name, Rank.SUPERVISOR, None)

    def escalate_call(self):
        self.call.level = Rank.DIRECTOR
        self._escalate_call()


class Director(Employee):
    def __init__(self, employee_id, name):
        super(Director, self).__init__(employee_id, name, Rank.DIRECTOR, None)

    def escalate_call(self):
        raise NotImplemented('Directors must be able to handle any call')


class CallState(Enum):
    READY = 0
    IN_PROGRESS = 1
    COMPLETE = 2


class Call(object):
    """
    Call represents a call from a user. A call has a minimum rank and is assigned to the first
    employee who can handle it.
    """

    def __init__(self, rank):
        self.state = CallState.READY
        self.rank = rank
        self.employee = None


class CallCenter(object):
    def __init__(self, operators, supervisors, directors):
        self.operators = operators
        self.supervisors = supervisors
        self.directors = directors
        self.queued_calls = deque()

    def dispatch_call(self, call):
        if call.rank not in (Rank.OPERATOR, Rank.SUPERVISOR, Rank.DIRECTOR):
            raise ValueError('Invalid call rank: {}'.format(call.rank))
        employee = None
        if call.rank == Rank.OPERATOR:
            employee = self._dispatch_call(call, self.operators)
        if call.rank == Rank.SUPERVISOR or employee is None:
            employee = self._dispatch_call(call, self.supervisors)
        if call.rank == Rank.DIRECTOR or employee is None:
            employee = self._dispatch_call(call, self.directors)
        if employee is None:
            self.queued_calls.append(call)

    def _dispatch_call(self, call, employees):
        for employee in employees:
            if employee.call is None:
                employee.take_call(call)
                return employee
        return None

    def notify_call_escalated(self, call):  # ...
        pass

    def notify_call_completed(self, call):  # ...
        pass

    def dispatch_queued_call_to_newly_freed_employee(self, call, employee):  # ...
        pass


if __name__ == '__main__':
    pass
