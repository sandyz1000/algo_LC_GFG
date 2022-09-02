from __future__ import print_function
from .stack import Stack


class InfixToPostfix(object):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    valid_token = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def __init__(self):
        self.simplestack = Stack()

    def evaluate(self, _string):
        """
        :param _string: list
        :return: string
        """
        postfix_list = []
        for character in _string:
            if character in self.valid_token:
                postfix_list.append(character)
            elif character in self.prec:
                if character == "(":
                    self.simplestack.push(character)
                elif character == ")":
                    top_token = self.simplestack.pop()
                    while top_token != "(":
                        postfix_list.append(top_token)
                        top_token = self.simplestack.pop()
                else:
                    while not self.simplestack.isEmpty() and \
                            self.prec[self.simplestack.peek()] > \
                            self.prec[character]:
                        postfix_list.append(self.simplestack.pop())

                    self.simplestack.push(character)

        while not self.simplestack.isEmpty():
            postfix_list.append(self.simplestack.pop())

        return " ".join(postfix_list)


if __name__ == '__main__':
    infix_to_postfix = InfixToPostfix()
    print(infix_to_postfix.evaluate("A * B + C * D"))  # A B * C D * +
    # A B + C * D E - F G + * -
    print(infix_to_postfix.evaluate("( A + B ) * C - ( D - E ) * ( F + G )"))
