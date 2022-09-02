"""
Program for n'th node from the end of a Linked List

Given a Linked List and a number n, write a function that returns the value at the n'th node
from end of the Linked List.

-------------------------------------------
Example:
-------------------------------------------

If input is below list and 3 = 2, then output is "B"
HEAD-> A -> B -> C -> D -> NULL
"""

from __future__ import print_function


class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


def static_vars(**kwargs):
    def decorate(func):
        for k, v in kwargs.items():
            setattr(func, k, kwargs[k])
        return func

    return decorate


class LinkedList1(object):
    """
    Method 1 (Use length of linked list)
    1) Calculate the length of Linked List. Let the length be len.
    2) Print the (len - n + 1)th node from the beginning of the Linked List.

    Time Complexity: O(n) where n is the length of linked list.
    """
    def __init__(self, head=None):
        self.head = head

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next_node = self.head  # link the old list off the new node
        self.head = new_node  # move the head to point to the new node

    def nth_from_last(self, head, n):
        length = 0
        temp = head

        # 1) count the number of nodes in Linked List
        while temp is not None:
            temp = temp.next_node
            length += 1

        # check if value of n is not more than length of the linked list
        if length < n:
            return
        temp = head

        # 2) get the (n-len+1)th node from the begining
        for i in range(1, length - n + 1):
            temp = temp.next_node
        return temp.data

    @static_vars(i=0)
    def nth_from_last_rec(self, head, n):
        if head is None:
            return
        self.nth_from_last_rec(head.next_node, n)

        self.nth_from_last_rec.i += 1
        if self.nth_from_last_rec.i == n:
            print("%d", head.data)


class LinkedList2(object):
    """
    Method 2 (Use two pointers)

    Maintain two pointers - reference pointer and main pointer. Initialize both reference and main
    pointers to head. First move reference pointer to n nodes from head. Now move both pointers one
    by one until reference pointer reaches end. Now main pointer will point to nth node from the
    end. Return main pointer.

    Python program to find n'th node from end using slow and fast pointer
    """

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def nth_from_last(self, n):
        main_ptr = self.head
        ref_ptr = self.head

        count = 0
        if self.head is not None:
            while count < n:
                if ref_ptr is None:
                    print("%d is greater than the no. pf nodes in list" % n)
                    return

                ref_ptr = ref_ptr.next
                count += 1

        while ref_ptr is not None:
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next

        return main_ptr.data


if __name__ == '__main__':
    llist = LinkedList2()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(35)

    # llist.nth_from_last(4)
    print("Method-2 Node no. %d from last is %d " % (4, llist.nth_from_last(4)))

    # Start with the empty list
    llist2 = LinkedList1()

    # create linked 35->15->4->20
    llist2.push(20)
    llist2.push(4)
    llist2.push(15)
    llist2.push(35)
    print("Method-1 Node no. %d from last is %d " % (4, llist2.nth_from_last(llist2.head, 4)))
