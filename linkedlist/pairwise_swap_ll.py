"""
Pairwise swap elements of a given linked list
Given a singly linked list, write a function to swap elements pairwise.

-----------------------------------------
Example:
-----------------------------------------

If the linked list is 1->2->3->4->5 then the function should change it to 2->1->4->3->5, and if the
linked list is 1->2->3->4->5->6 then the function should change it to 2->1->4->3->6->5.

"""


# Python program to swap the elements of linked list pairwise
# Time Complexity: O(n)


class Node(object):
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    # Function to initialize head
    def __init__(self):
        self.head = None

    def pairwise_swap(self):
        """Function to pairwise swap elements of a linked list"""
        temp = self.head

        # There are no nodes in linked list
        if temp is None:
            return

        # Traverse further only if there are at least two left
        while temp is not None and temp.next is not None:
            # Swap data of node with its next node's data
            temp.data, temp.next.data = temp.next.data, temp.data

            # Move temp by 2 fro the next pair
            temp = temp.next.next

    def push(self, new_data):
        """Function to insert a new node at the beginning"""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        """Utility function to prin t the linked LinkedList"""
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)

    print("Linked list before calling pairwise_swap() ")
    llist.print_list()
    llist.pairwise_swap()
    print("\nLinked list after calling pairwise_swap()")
    llist.print_list()