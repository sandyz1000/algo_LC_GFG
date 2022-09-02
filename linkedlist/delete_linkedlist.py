"""Write a function to delete a Linked List"""
from __future__ import print_function
from collections import namedtuple

# Python program to delete a linked list
# Time Complexity: O(n)
# Auxiliary Space: O(1)


class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def delete_list(self):
        """Function to delete the entire linked list"""
        # deref head to get the real head
        current = self.head
        while current is not None:
            next_node = current.next_node
            del current
            current = next_node
        self.head = None  # deref head_ref to affect the real head back in the caller.

    def push(self, new_data):
        """Given a reference (pointer to pointer) to the head of a list and an int, push a new
        node on the front of the list. """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


if __name__ == '__main__':
    llist = LinkedList()

    # Use push() to construct below list 1->12->1->4->1
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)

    print("\n Deleting linked list")
    llist.delete_list()
    print("\n Linked list deleted")
