from __future__ import print_function
from .stack import Stack


class ParanthesisChecker(object):
    def __init__(self):
        self.stack = Stack()

    def check(self, param=""):
        parList = param.split()
        balanced = True
        index = 0
        while index < len(parList) and balanced:
            symbol = parList[index]
            if symbol == "(":
                self.stack.push(symbol)
            elif self.stack.isEmpty():
                balanced = False
            else:
                self.stack.pop()
            index += 1

        if not balanced and self.stack.isEmpty():
            return False
        else:
            return True


class GeneralParanthesisChecker(ParanthesisChecker):
    """
        General parenthesis checker which will check opening and closing bracket
        args -> [{()}], {{([][])}()}, [{()]
    """

    def check(self, param=""):
        parList = param.split()
        balanced = True
        index = 0
        while index < len(parList) and balanced:
            symbol = parList[index]
            if symbol in "([{":
                self.stack.push(symbol)
            else:
                top = self.pop()
                if not GeneralParanthesisChecker.matches(top, symbol):
                    balanced = False
            index += 1

        if not balanced and self.stack.isEmpty():
            return False
        else:
            return True

    @staticmethod
    def matches(open, close):
        opens = "([{"
        closes = ")]}"
        return opens.index(open) == closes.index(close)
