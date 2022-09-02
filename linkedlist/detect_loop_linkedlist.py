"""
Detect loop in a linked list

Given a linked list, check if the the linked list has loop or not. Below diagram shows a
linked list with a loop.

    1 -> 2 -> 3
         A    |
         |    V
         5 <- 4

"""
from __future__ import print_function


# Python program to detect loop in the linked list


class Node(object):
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next_node = None


class DetectLoopHashing(object):
    """
    Use Hashing:

    Traverse the list one by one and keep putting the node addresses in a Hash Table.
    At any point, if NULL is reached then return false and if next of current node
    points to any of the previously stored nodes in Hash then return true.

    Mark Visited Nodes:

    This solution requires modifications to basic linked list data structure. Have a
    visited flag with each node. Traverse the linked list and keep marking visited
    nodes. If you see a visited node again then there is a loop. This solution works in
    O(n) but requires additional information with each node.

    A variation of this solution that doesn't require modification to basic data
    structure can be implemented using hash. Just store the addresses of visited nodes
    in a hash and if you see an address that already exists in hash then there is a loop.
    """
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """Function to insert a new node at the beginning"""
        new_node = Node(new_data)
        new_node.next_node = self.head
        self.head = new_node

    def detect_loop(self):
        """
        Returns true if there is a loop in linked list else returns false.
        """
        stack = set({})
        h = self.head
        while h is not None:
            # If we have already has this node in hash map it means their is a cycle
            # (Because you we encountering the node second time).
            if h in stack:
                return True

            # If we are seeing the node for the first time, insert it in hash
            stack.add(h)
            h = h.next_node
        return False


class LinkedList(object):
    """
    Floyd's Cycle-Finding Algorithm:

    This is the fastest method. Traverse linked list using two pointers.  Move one
    pointer by one and other pointer by two.  If these pointers meet at some node then
    there is a loop. If pointers do not meet then linked list doesn't have loop.

    Time Complexity: O(n)
    Auxiliary Space: O(1)
    """
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """Function to insert a new node at the beginning"""
        new_node = Node(new_data)
        new_node.next_node = self.head
        self.head = new_node

    def detect_loop(self):
        slow_p = self.head
        fast_p = self.head
        while slow_p and fast_p and fast_p.next_node:
            slow_p = slow_p.next_node
            fast_p = fast_p.next_node.next_node
            if slow_p == fast_p:
                return True


if __name__ == '__main__':
    # Time Complexity: O(n)
    # Auxiliary Space: O(1)
    print("\n------Method-1 -------")
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)

    # Create a loop for testing
    llist.head.next_node.next_node.next_node.next_node = llist.head
    print("Loop found" if llist.detect_loop() else "No Loop")

    print("\n------Method-2 -------")
    llist = DetectLoopHashing()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)

    # Create a loop for testing
    llist.head.next_node.next_node.next_node.next_node = llist.head
    print("Loop found" if llist.detect_loop() else "No Loop")
