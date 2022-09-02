"""
Linked List | Set 1 (Introduction)

Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not
stored at contiguous location the elements are linked using pointers.

HEAD-> A -> B -> C -> D -> NULL

Why Linked List?
Arrays can be used to store linear data of similar types, but arrays have following limitations.
1)  The size of the arrays is fixed: So we must know the upper limit on the number of elements in
    advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the
    usage.
2)  Inserting a new element in an array of elements is expensive, because room has to be created
    for the new elements and to create room existing elements have to shifted.

For example, in a system if we maintain a sorted list of IDs in an array id[].

id = [1000, 1010, 1050, 2000, 2040].

And if we want to insert a new ID 1005, then to maintain the sorted order, we have to move all the
elements after 1000 (excluding 1000).
Deletion is also expensive with arrays until unless some special techniques are used. For example,
to delete 1010 in id[], everything after 1010 has to be moved.

Advantages over arrays
1) Dynamic size
2) Ease of insertion/deletion

Drawbacks:
1) Random access is not allowed. We have to access elements sequentially starting from the first
node. So we cannot do binary search with linked lists.
2) Extra memory space for a pointer is required with each element of the list.

Representation in C:
A linked list is represented by a pointer to the first node of the linked list. The first node is
called head. If the linked list is empty, then value of head is NULL.
Each node in a list consists of at least two parts:
1) data
2) pointer to the next node

In C, we can represent a node using structures. Below is an example of a linked list node with an
integer data.

In Java, LinkedList can be represented as a class and a Node as a separate class. The LinkedList
class contains a reference of Node class type.

"""
from __future__ import print_function


# A simple Python program to introduce a linked list


class Node(object):
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList(object):
    # Function to initialize head
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """Function to insert a new node at the beginning"""
        new_node = Node(new_data)  # 1 & 2: Allocate the Node & Put in the data
        new_node.next = self.head  # 3. Make next of new Node as head
        self.head = new_node  # 4. Move the head to point to new Node

    def delete_node(self, key):
        """
        Given a reference to the head of a list and a key, delete the first occurrence
        of key in linked list
        :param key:
        :return:
        """
        temp = self.head  # Store head node
        # If head node itself holds the key to be deleted
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the key to be deleted, keep track of the previous node as we need to change
        # 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp is None:
            return

        prev.next = temp.next  # Unlink the node from linked list
        temp = None

    def insert_after(self, prev_node, new_data):
        """This function is in LinkedList class. Inserts a new node after the given
        prev_node. This method is defined inside LinkedList class shown above """
        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        # 2. create new node & Put in the data
        new_node = Node(new_data)
        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next
        # 5. make next of prev_node as new_node
        prev_node.next = new_node

    def append(self, new_data):
        """
        This function is defined in Linked List class Appends a new node at the end. This
        method is defined inside LinkedList class shown above
        """
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

    # Utility function to print the linked list
    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Three nodes have been created.
    # We have references to these three blocks as first,
    # second and third
    #
    # llist.head        second              third
    #      |                |                  |
    #      |                |                  |
    # +----+------+     +----+------+     +----+------+
    # | 1  | None |     | 2  | None |     |  3 | None |
    # +----+------+     +----+------+     +----+------+

    llist.head.next = second  # Link first node with second

    # Now next of first Node refers to second.  So they
    # both are linked.
    #
    # llist.head        second              third
    #      |                |                  |
    #      |                |                  |
    # +----+------+     +----+------+     +----+------+
    # | 1  |  o-------->| 2  | null |     |  3 | null |
    # +----+------+     +----+------+     +----+------+

    second.next = third  # Link second node with the third node

    # Now next of second Node refers to third.  So all three
    # nodes are linked.
    #
    # llist.head        second              third
    #      |                |                  |
    #      |                |                  |
    # +----+------+     +----+------+     +----+------+
    # | 1  |  o-------->| 2  |  o-------->|  3 | null |
    # +----+------+     +----+------+     +----+------+

    # Inserting a node to a linked list
    # Insert 6.  So linked list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7)

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1)

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insert_after(llist.head.next, 8)

    print('Created linked list is:')
    llist.print_list()

    llist.delete_node(1)
    print("\nLinked List after Deletion of 1:")
