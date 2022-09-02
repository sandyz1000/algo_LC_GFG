"""
Given a linked list which is sorted, how will you insert in sorted way

Given a sorted linked list and a value to insert, write a function to insert the value in sorted
way.

---------------------------------------------
Example:
---------------------------------------------

HEAD -> 2 -> 5 -> 7 -> 10 -> 15 -> NULL

Linked List after insertion of 9

HEAD -> 2 -> 5 -> 7 -> 9 -> 10 -> 15 -> NULL

---------------------------------------------
Discussion:
---------------------------------------------

Shorter Implementation using double pointers
The code uses double pointer to keep track of the next pointer of the previous node (after which
new node is being inserted).

Note that below line in code changes current to have address of next pointer in a node.
current = current.next_node

Also, note below comments.
    # Copies the value-at-address current to new_node's next pointer
    new_node.next_node = current
    # Fix next pointer of the node (using it's address) after which new_node is being inserted
    current = new_node

"""
# Python program to insert in sorted list
# Time Complexity: O(n)


class Node(object):
    # Constructor to initialize the node object
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    # Function to initialize head
    def __init__(self):
        self.head = None

    def sorted_insert(self, new_node):
        # Special case for the empty linked list
        if self.head is None:
            new_node.next_node = self.head
            self.head = new_node

        # Special case for head at end
        elif self.head.data >= new_node.data:
            new_node.next_node = self.head
            self.head = new_node

        else:
            # Locate the node before the point of insertion
            current = self.head
            while current.next_node is not None \
                    and current.next_node.data < new_node.data:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next_node = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next_node


if __name__ == '__main__':
    llist = LinkedList()
    new_node = Node(5)
    llist.sorted_insert(new_node)
    new_node = Node(10)
    llist.sorted_insert(new_node)
    new_node = Node(7)
    llist.sorted_insert(new_node)
    new_node = Node(3)
    llist.sorted_insert(new_node)
    new_node = Node(1)
    llist.sorted_insert(new_node)
    new_node = Node(9)
    llist.sorted_insert(new_node)
    print("Create Linked List")
    llist.print_list()
