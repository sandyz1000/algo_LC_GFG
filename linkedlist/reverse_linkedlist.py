"""Reverse a linked list

Given pointer to the head node of a linked list, the task is to reverse the linked list. We need to
reverse the list by changing links between nodes.

Examples:
-------------------------
Input:  Head of following linked list
        1->2->3->4->NULL
Output: Linked list should be changed to,
        4->3->2->1->NULL

Input : Head of following linked list
        1->2->3->4->5->NULL
Output: Linked list should be changed to,
        5->4->3->2->1->NULL

Input : NULL
Output : NULL

Input  : 1->NULL
Output : 1->NULL  """

from __future__ import print_function

# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)


class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    # Function to initialize head
    def __init__(self):
        self.head = None

    def reverse(self):
        """Function to reverse the linked list"""
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def reverse_util(self, curr, prev):
        # If last node mark it head
        if curr.next is None:
            self.head = curr
            curr.next = prev  # Update next to prev node
            return

        next_node = curr.next  # Save curr.next node for recursive call
        curr.next = prev  # And update next

        self.reverse_util(next_node, curr)

    def reverse_rec(self):
        """Simple and tail recursive Python program to reverse a linked list. This function
        mainly calls reverseUtil() with previous as None"""
        if self.head is None:
            return
        self.reverse_util(self.head, None)

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,)
            temp = temp.next


if __name__ == '__main__':

    # Driver program to test above functions
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)

    print("Given Linked List")
    llist.printList()
    llist.reverse()
    print("\nReversed Linked List")
    llist.printList()

    llist = LinkedList()
    llist.push(8)
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)

    print("Given linked list")
    llist.printList()

    llist.reverse_rec()

    print("\nReverse linked list")
    llist.printList()
