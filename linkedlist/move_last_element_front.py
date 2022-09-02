"""
Move last element to front of a given Linked List
Write a C function that moves last element to front in a given Singly Linked List.

Example:
-----------------------
If the given Linked List is 1->2->3->4->5, then the function should change the list
to 5->1->2->3->4.

Algorithm:
-----------------------
Traverse the list till last node. Use two pointers: one to store the address of last node and other
for address of second last node. After the end of loop do following operations.
1)  Make second last as last (secLast->next = NULL).
2)  Set next of last as head (last->next = *head_ref).
3)  Make last as head ( *head_ref = last)

"""
from __future__ import print_function

# Python Program to move last element to front in a given linked list
# Time Complexity: O(n) where n is the number of nodes in the given Linked List.


class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def moveToFront(self):
        """
        We are using a double pointer head_ref here because we change head of the
        linked list inside this function.
        """
        # If linked list is empty, or it contains only one node, then nothing needs to be done,
        # simply return
        if self.head is None or self.head.next_node is None:
            return

        # Initialize second last and last pointers
        sec_last = None
        last = self.head

        # After this loop sec_last contains address of second last node and
        # last contains address of last node in Linked List
        while last.next_node is not None:
            sec_last = last
            last = last.next_node

        # Set the next of second last as NULL
        sec_last.next_node = None
        # Set next of last as head node
        last.next_node = self.head

        # Change the head pointer to point to last node now
        self.head = last

    def push(self, new_data):
        """Function to add a node at the beginning of Linked List"""
        # allocate node
        new_node = Node(new_data)

        # link the old list off the new node
        new_node.next_node = self.head

        # move the head to point to the new node
        self.head = new_node

    def printList(self):
        """Function to print nodes in a given linked list"""
        node = self.head
        while node is not None:
            print("%d " % node.data)
            node = node.next_node


if __name__ == '__main__':
    start = LinkedList()
    # The constructed linked list is: 1->2->3->4->5
    start.push(5)
    start.push(4)
    start.push(3)
    start.push(2)
    start.push(1)

    print("\n Linked list before moving last to front\n")
    start.printList()
    start.moveToFront()

    print("\n Linked list after removing last to front\n")
    start.printList()
