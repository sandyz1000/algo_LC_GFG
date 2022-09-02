"""
QuickSort on Singly Linked List

QuickSort on Doubly Linked List is discussed here. QuickSort
on Singly linked list was given as an exercise.

The important things about implementation are, it changes pointers rather swapping data and time
complexity is same as the implementation for Doubly Linked List.
"""

from __future__ import print_function
from typing import Optional


# Python program for Quick Sort on Singly Linked List

class Node(object):
    """a node of the singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data    # type: Node
        self.next_node = next_node  # type: Optional[Node]


class Pointer(object):
    def __init__(self, data):
        self.data = data   # type: Optional[int]


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head    # type: Node

    def push(self, new_data):
        """A utility function to insert a node at the beginning of linked list"""
        # allocate node
        new_node = Node(new_data, self.head)
        # move the head to point to the new node
        self.head = new_node

    def print_list(self):
        """A utility function to print linked list"""
        out = []
        node = self.head
        while node is not None:
            out.append("%d" % node.data)
            node = node.next_node
        print("->".join(out))

    def get_tail(self, head):
        """Returns the last node of the list"""
        cur = head
        while cur is not None and cur.next_node is not None:
            cur = cur.next_node
        return cur

    def partition(self, head, end, new_head, new_end):
        """
        Partitions the list taking the last element as the pivot

        :type head: Node
        :type end: Node
        :type new_head: Pointer
        :type new_end: Pointer
        :rtype: int
        """
        pivot = end
        prev = None
        cur = head
        tail = pivot

        # During partition, both the head and end of the list might change
        # which is updated in the newHead and newEnd variables
        while cur is not pivot:
            if cur.data < pivot.data:
                # First node that has a value less than the pivot - becomes the new head
                if new_head.data is None:
                    new_head.data = cur

                prev = cur
                cur = cur.next_node

            # If cur node is greater than pivot Move cur node to next_node of tail, and
            # change tail
            else:
                if prev:
                    prev.next_node = cur.next_node
                tmp = cur.next_node
                cur.next_node = None
                tail.next_node = cur
                tail = cur
                cur = tmp

        # If the pivot data is the smallest element in the current list, pivot becomes the head
        if new_head.data is None:
            new_head.data = pivot

        # Update newEnd to the current last node
        new_end.data = tail

        # Return the pivot node
        return pivot

    def quick_sort_recur(self, head, end):
        """here the sorting happens exclusive of the end node"""
        # base condition
        if not head or head == end:
            return head

        # Partition the list, new_head and new_end will be updated by the partition function
        new_head = Pointer(None)  # type: Pointer
        new_end = Pointer(None)  # type: Pointer
        pivot = self.partition(head, end, new_head, new_end)

        # If pivot is not the smallest element recur for the left part.
        if new_head.data != pivot:
            # Set the node before the pivot node as NULL
            tmp = new_head.data
            while tmp.next_node and tmp.next_node != pivot:
                tmp = tmp.next_node
            tmp.next_node = None

            # Recur for the list before pivot
            new_head.data = self.quick_sort_recur(new_head.data, tmp)

            # Change next of last node of the left half to pivot
            tmp = self.get_tail(new_head.data)
            tmp.next_node = pivot

        # Recur for the list after the pivot element
        pivot.next_node = self.quick_sort_recur(pivot.next_node, new_end.data)
        return new_head.data

    def quick_sort(self):
        """
        The main function for quick sort. This is a wrapper over recursive function
        quick_sort_recur()
        :return:
        """
        self.head = self.quick_sort_recur(self.head, self.get_tail(self.head))
        return


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(5)
    llist.push(20)
    llist.push(4)
    llist.push(3)
    llist.push(30)

    print("Linked List before sorting \n")
    llist.print_list()
    llist.quick_sort()

    print("Linked List after sorting \n")
    llist.print_list()
