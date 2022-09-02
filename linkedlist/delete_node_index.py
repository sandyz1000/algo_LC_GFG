"""
Given only a pointer/reference to a node to be deleted in a singly linked list, how do you
delete it?

Given a pointer to a node to be deleted, delete the node. Note that we don't have pointer to
head node.

Algorithm:
----------------------------

A simple solution is to traverse the linked list until you find the node you want to delete. But
this solution requires pointer to the head node which contradicts the problem statement.

Fast solution is to copy the data from the next node to the node to be deleted and delete the next
node. Something like following.

Find next node using next pointer
struct Node *temp  = node_ptr->next;

Copy data of next node to this node
node_ptr->data  = temp->data;

Unlink next node
node_ptr->next  = temp->next;

Delete next node
free(temp);

"""


class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def push(self, new_data):
        """
        Given a reference (pointer to pointer) to the head of a list and an int,
        push a new node on the front of the list.
        """
        # allocate node
        new_node = Node(new_data)
        new_node.next_node = self.head  # link the old list off the new node
        self.head = new_node  # move the head to point to the new node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next_node

    def delete_node(self, head):
        temp = head.next_node
        head.data = temp.data
        head.next_node = temp.next_node
        del temp


if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()
    # Use push() to construct below list 1->12->1->4->1
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)

    print("Before deleting \n")
    llist.print_list()
    # I m deleting the head itself. You can check for more cases
    llist.delete_node(llist.head)
    print("\nAfter deleting \n")
    llist.print_list()
