"""
Find Length of a Linked List (Iterative and Recursive)
Write a Python function to count number of nodes in a given singly linked list.

Head -> 1 -> 3 -> 1 -> 2 -> 1 -> NULL

"""
from __future__ import print_function


# A complete working Python program to find length of a Linked List recursively

class Node(object):
    """Node class"""

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class LinkedList(object):
    """Linked List class contains a Node object"""
    # Function to initialize head
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """
        This function is in LinkedList class. It inserts a new node at the
        beginning of Linked List."""
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(new_data)
        # 3. Make next of new Node as head
        new_node.next = self.head
        # 4. Move the head to point to new Node
        self.head = new_node

    def get_count_iter(self):
        """
        This function counts number of nodes in Linked List iteratively, given 'node' as
        starting node.
        """
        temp = self.head  # Initialise temp
        count = 0  # Initialise count
        # Loop while end of linked list is not reached
        while temp:
            count += 1
            temp = temp.next
        return count

    def get_count_rec(self, node):
        """
        This function counts number of nodes in Linked List recursively, given 'node' as
        starting node.
        """
        if not node:  # Base case
            return 0
        else:
            return 1 + self.get_count_rec(node.next)

    # A wrapper over getCountRec()
    def get_count(self):
        return self.get_count_rec(self.head)


# Code execution starts here
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    print('Count of nodes is :', llist.get_count())
    print('Count of nodes is :', llist.get_count_iter())
