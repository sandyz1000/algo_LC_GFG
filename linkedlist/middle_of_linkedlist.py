"""
Find the middle of a given linked list in Python

Given a singly linked list, find middle of the linked list. For example, if given linked list is
1->2->3->4->5 then output should be 3.

If there are even nodes, then there would be two middle nodes, we need to print second middle
element. For example, if given linked list is 1->2->3->4->5->6 then output should be 4.

"""
from __future__ import print_function


class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, head_ref=None):
        self.head_ref = head_ref

    def push(self, new_data):
        new_node = Node(new_data)
        # link the old list off the new node
        new_node.next_node = self.head_ref

        # move the head to point to the new node
        self.head_ref = new_node

    def print_list(self):
        """A utility function to print a given linked list"""
        ptr = self.head_ref
        output = []
        while ptr is not None:
            output.append("%d->" % ptr.data)
            ptr = ptr.next_node
        output.append("NULL")
        print("".join(output))


def find_middle1(head):
    """
    Method -2
    Traverse linked list using two pointers. Move one pointer by one and other pointer by two.
    When the fast pointer reaches end slow pointer will reach middle of the linked list.

    Function to get the middle of the linked list
    :param head:
    :return:
    """
    slow_ptr = head
    fast_ptr = head
    if head is not None:
        while fast_ptr and fast_ptr.next_node:
            fast_ptr = fast_ptr.next_node.next_node
            slow_ptr = slow_ptr.next_node
        return slow_ptr.data


def find_middle2(head):
    """
    Method 3:

    Initialize mid element as head and initialize a counter as 0. Traverse the list from head,
    while traversing increment the counter and change mid to mid->next whenever the counter is
    odd. So the mid will move only half of the total length of the list.

    Function to get the middle of the linked list
    :param head: Node
    :return:
    """
    count = 0
    mid = head

    while head is not None:
        # update mid, when 'count' is odd number
        if count & 1:
            mid = mid.next_node
        count += 1
        head = head.next_node

    # if empty list is provided
    if mid is not None:
        return mid.data


if __name__ == '__main__':
    # Start with the empty list
    linked = LinkedList()
    for i in range(5, -1, -1):
        linked.push(i)
        linked.print_list()
        print("Method-1: The middle element is [%d]" % find_middle1(linked.head_ref))
        print("Method-2: The middle element is [%d]" % find_middle2(linked.head_ref))
