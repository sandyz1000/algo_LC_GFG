from __future__ import print_function, absolute_import


class StackX(object):
    def __init__(self, max_size):
        self.__size = max_size
        self.__v = [None] * max_size
        self.top = 0

    def push(self, value):
        self.top += 1
        self.__v[self.top] = value

    def pop(self, value):
        temp = self.__v[self.top]
        self.__v[self.top] = None
        self.top -= 1
        return temp

    def peek(self):
        return self.__v[self.top]

    def sizeof(self):
        return self.__size


class Stack(object):
    """
    Stack is a ordered data structure where the last element is in the top of the stack. The item
    which is inserted on the top will be the first to be removed.
    Formation of stack data structure with python list where the last element inserted is the top
    of the stack
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        item = self.items.pop()
        return item

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class StackY(object):
    """
    Formation of stack data structure with python list where the first element appended is the
    top of the stack
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        pass

    def push(self, item):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def size(self):
        pass
