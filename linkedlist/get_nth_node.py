"""
Write a function to get Nth node in a Linked List

Write a GetNth() function that takes a linked list and an integer index and returns the data value
stored in the node at that index position.

Example:
-----------------------------------
Input:  1->10->30->14,  index = 2
Output: 30
The node at index 2 is 30

"""

# Time Complexity: O(n)
# A complete working Python program to find n'th node in a linked list


class Node(object):
    # Function to initialise the node object
    def __init__(self, data, next_node=None):
        self.data = data  # Assign data
        self.next_node = next_node  # Initialize next as null


class LinkedList(object):
    """Linked List class contains a Node object"""
    # Function to initialize head
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """
        This function is in LinkedList class. It inserts a new node at the
        beginning of Linked List.
        """
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(new_data)
        # 3. Make next of new Node as head
        new_node.next_node = self.head
        # 4. Move the head to point to new Node
        self.head = new_node

    # Returns data at given index in linked list
    def getNth(self, index):
        current = self.head  # Initialise temp
        count = 0  # Index of current node

        # Loop while end of linked list is not reached
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next_node


if __name__ == '__main__':
    llist = LinkedList()
    # Use push() to construct below list 1->12->1->4->1
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)

    n = 3
    print("Element at index 3 is :", llist.getNth(n))