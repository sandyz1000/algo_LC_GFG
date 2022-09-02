from .stack import Stack


class DecimalToBinary(object):
    """
    On conversion of decimal to binary no we will divide the no by 2 and save each reminder in
    stack and finally we will pop element from the stack and append it t form the result
    """

    def __init__(self):
        self.stack = Stack()
        self.digit = "0123456789ABCDEF"

    def decimalToBinary(self, decNumber, base):
        outputStr = ""
        while self.decNumber > 0:
            reminder = self.decNumber % base
            self.stack.push(reminder)
            decNumber //= base

        while not self.stack.isEmpty():
            outputStr += self.digit[self.stack.pop()]

        return outputStr


def decimal_binary_rec(number, base):
    if number == 0: 
        return 0
    return number % base + 10 * decimal_binary_rec(number // base)