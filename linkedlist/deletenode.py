"""
Delete a Linked List node at a given position
Given a singly linked list and a position, delete a linked list node at the given position.

Example:
-------------------------
Input: position = 1, Linked List = 8->2->3->1->7
Output: Linked List =  8->3->1->7

Input: position = 0, Linked List = 8->2->3->1->7
Output: Linked List = 2->3->1->7

Explanation:
-------------------------
If node to be deleted is root, simply delete it. To delete a middle node, we must have pointer
to the node previous to the node to be deleted. So if positions is not zero, we run a loop
position-1 times and get pointer to the previous node.
"""


class Node:
    # Python program to delete a node in a linked list at a given position
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    # Constructor to initialize head
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """Function to insert a new node at the beginning"""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, position):
        """
        Given a reference to the head of a list and a position, delete the node at a given
        position
        """
        # If linked list is empty
        if self.head is None:
            return

        # Store head node
        temp = self.head

        # If head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Find previous node of the node to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If position is more than number of nodes
        if temp is None or temp.next is None:
            return

        # Node temp.next is the node to be deleted store pointer to the
        # next_node of node to be deleted
        next_node = temp.next.next

        # Unlink the node from linked list
        temp.next = None
        temp.next = next_node

    def print_list(self):
        """Utility function to print the linked LinkedList"""
        temp = self.head
        while temp:
            print(" %d " % temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    llist.push(8)

    print("Created Linked List: ")
    llist.print_list()
    llist.delete_node(2)
    print("\nLinked List after Deletion at position 4: ")
    llist.print_list()
