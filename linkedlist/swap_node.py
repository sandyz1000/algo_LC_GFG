"""
Swap nodes in a linked list without swapping data

Given a linked list and two keys in it, swap nodes for two given keys. Nodes should be swapped by
changing links. Swapping data of nodes may be expensive in many situations when data contains many
fields.

It may be assumed that all keys in linked list are distinct.

---------------------------------------------
Examples:
---------------------------------------------
Input:  10->15->12->13->20->14,  x = 12, y = 20
Output: 10->15->20->13->12->14

Input:  10->15->12->13->20->14,  x = 10, y = 20
Output: 20->15->12->13->10->14

Input:  10->15->12->13->20->14,  x = 12, y = 13
Output: 10->15->13->12->20->14

---------------------------------------------
Explanation:
---------------------------------------------
This may look a simple problem, but is interesting question as it has following cases to be handled.
1) x and y may or may not be adjacent.
2) Either x or y may be a head node.
3) Either x or y may be last node.
4) x and/or y may not be present in linked list.

How to write a clean working code that handles all of the above possibilities.


The idea it to first search x and y in given linked list. If any of them is not present, then
return. While searching for x and y, keep track of current and previous pointers. First change next
of previous pointers, then change next of current pointers.

"""

from __future__ import print_function


class Node(object):
    def __init__(self, d):
        self.data = d
        self.next = None


# Python program to swap two given nodes of a linked list
class LinkedList(object):
    def __init__(self):
        self.head = None

    def swap_nodes(self, x, y):
        """Function to swap Nodes x and y in linked list by changing links"""
        # Nothing to do if x and y are same
        if x == y:
            return

        # Search for x (keep track of prevX and CurrX)
        prevX = None
        currX = self.head
        while currX is not None and currX.data != x:
            prevX = currX
            currX = currX.next

        # Search for y (keep track of prevY and currY)
        prevY = None
        currY = self.head
        while currY is not None and currY.data != y:
            prevY = currY
            currY = currY.next

        # If either x or y is not present, nothing to do
        if currX is None or currY is None:
            return

        # If x is not head of linked list
        if prevX is not None:
            prevX.next = currY
        # make y the new head
        else:
            self.head = currY

        # If y is not head of linked list
        if prevY is not None:
            prevY.next = currX
        # make x the new head
        else:
            self.head = currX

        # Swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def push(self, new_data):
        """Function to add Node at beginning of list."""
        new_Node = Node(new_data)  # 1. alloc the Node and put the data
        new_Node.next = self.head  # 2. Make next of new Node as head
        self.head = new_Node  # 3. Move the head to point to new Node

    # This function prints contents of linked list starting from the given Node
    def print_list(self):
        tNode = self.head
        while tNode is not None:
            print(tNode.data)
            tNode = tNode.next


if __name__ == '__main__':
    llist = LinkedList()
    # The constructed linked list is: 1->2->3->4->5->6->7
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print("Linked list before calling swapNodes() ")
    llist.print_list()
    llist.swap_nodes(4, 3)
    print("\nLinked list after calling swapNodes() ")
    llist.print_list()
