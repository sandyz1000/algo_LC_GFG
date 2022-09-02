"""
Insertion Sort for Singly Linked List
We have discussed Insertion Sort for arrays. In this article same for linked list is discussed.

Explanation:
------------------------------------
Below is simple insertion sort algorithm for linked list.

1) Create an empty sorted (or result) list
2) Traverse the given list, do following for every node.
    a) Insert current node in sorted way in sorted or result list.
3) Change head of given linked list to head of sorted (or result) list.

"""
from __future__ import print_function


# Python program for insertion sort on a linked list


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.m_sorted = None

    # Function to print linked list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print("%d" % temp.data, end=" ")
            temp = temp.next_node

    # A utility function to insert a node at the beginning of linked list
    def push(self, new_data):
        # allocate node
        new_node = Node(new_data, self.head)
        # move the head to point to the new node
        self.head = new_node

    def insertion_sort(self, head):
        """function to sort a singly linked list using insertion sort"""
        # Initialize sorted linked list
        self.m_sorted = None
        # Traverse the given linked list and insert every node to sorted
        current = head

        while current is not None:
            # Store next for next iteration
            next_node = current.next_node
            # insert current in sorted linked list
            self.sorted_insert(current)
            #  Update current
            current = next_node
        # Update head_ref to point to sorted linked list
        self.head = self.m_sorted
        return

    def sorted_insert(self, new_node):
        """
        function to insert a new_node in a list. Note that this function expects a pointer
        to head_ref as this can modify the head of the input linked list (similar to push())
        """
        # Special case for the head end
        if self.m_sorted is None or self.m_sorted.data >= new_node.data:
            new_node.next_node = self.m_sorted
            self.m_sorted = new_node
        else:
            # Locate the node before the point of insertion
            current = self.m_sorted
            while current.next_node is not None and current.next_node.data < new_node.data:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(5)
    llist.push(20)
    llist.push(4)
    llist.push(3)
    llist.push(30)

    print("Linked List before sorting \n")
    llist.print_list()
    llist.insertion_sort(llist.head)
    print("\nLinked List after sorting \n")
    llist.print_list()
