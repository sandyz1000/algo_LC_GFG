"""
Stack | Set 3 (Reverse a string using stack)

Given a string, reverse it using stack. For example "GeeksQuiz" should be converted to "ziuQskeeG".

Following is simple algorithm to reverse a string using stack.
1) Create an empty stack.
2) One by one push all characters of string to stack.
3) One by one pop all characters from stack and put them back to string.

"""
from __future__ import print_function

# Python program to reverse a string using stack

# Function to create an empty stack. It initializes size of stack as 0
def createStack():
    stack = []
    return stack


# Function to determine the size of the stack
def size(stack):
    return len(stack)


# Stack is empty if the size is 0
def isEmpty(stack):
    if size(stack) == 0:
        return True


# Function to add an item to stack . It increases size by 1
def push(stack, item):
    stack.append(item)


# Function to remove an item from stack. It decreases size by 1
def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()


# A stack based function to reverse a string
def reverse(string):
    n = len(string)

    # Create a empty stack
    stack = createStack()

    # Push all characters of string to stack
    for i in range(0, n, 1):
        push(stack, string[i])

    # Making the string empty since all characters are saved in stack
    string = ""

    # Pop all characters of string and put them back to string
    for i in range(0, n, 1):
        string += pop(stack)

    return string


if __name__ == '__main__':
    string = "GeeksQuiz"
    string = reverse(string)
    print("Reversed string is " + string)