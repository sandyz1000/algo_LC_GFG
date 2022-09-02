"""
Insertion Sort for Singly Linked List
We have discussed Insertion Sort for arrays. In this article same for linked list is discussed.

Below is simple insertion sort algorithm for linked list.

1) Create an empty sorted (or result) list
2) Traverse the given list, do following for every node.
    a) Insert current node in sorted way in sorted or result list.
3) Change head of given linked list to head of sorted (or result) list.

"""
from __future__ import print_function


class Link(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class ListInsertionSort(object):
    """Implementation of insertion sorting with linked list"""

    def __init__(self, first=None):
        self.head = first
        self.sorted = None

    def push(self, data):
        # allocate node
        newnode = Link(data)
        # link the old list off the new node
        newnode.next_node = self.head
        # move the head to point to the new node
        self.head = newnode

    def print_list(self):
        p_current = self.head
        while p_current is not None:
            print(p_current.data, end=" ")
            p_current = p_current.next_node
        print("\n")

    def insertion_sort(self):
        self.sorted = None
        current = self.head
        #  Traverse the given linked list and insert every node to sorted
        while current is not None:
            # Store next for next iteration
            next_node = current.next_node
            # insert current in sorted linked list
            self.sorted_insert(current)
            # Update current
            current = next_node

        self.head = self.sorted

    def sorted_insert(self, new_node):
        """
        function to insert a new_node in a list. Note that this function expects a pointer to
        head_ref as this can modify the head of the input linked list (similar to push())
        """
        # Special case for the head end
        if self.sorted is None or self.sorted.data >= new_node.data:
            new_node.next_node = self.sorted
            self.sorted = new_node
        else:
            current = self.sorted
            # Locate the node before the point of insertion
            while current.next_node is not None and current.next_node.data < new_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node


if __name__ == '__main__':
    llist = ListInsertionSort()
    llist.push(5)
    llist.push(20)
    llist.push(4)
    llist.push(3)
    llist.push(30)
    print("Linked List before Sorting..")
    llist.print_list()

    llist.insertion_sort()
    print("Insertion sort of linked list\n")
    llist.print_list()
