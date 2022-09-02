"""
Write a function that counts the number of times a given int occurs in a Linked List
Given a singly linked list and a key, count number of occurrences of given key in linked list.

Example:
------------------------------
If given linked list is 1->2->1->2->1->3->1 and given key is 1, then output should be 4.

"""
# Python program to count the number of time a given int occurs in a linked list


class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def count(self, search_for):
        """Counts the no of occurrences of a node (seach_for) in a linked list (head)"""
        current = self.head
        count = 0
        while current is not None:
            if current.data == search_for:
                count += 1
            current = current.next
        return count

    def push(self, new_data):
        """Function to insert a new node at the beginning"""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        """Utility function to print the linked LinkedList"""
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    # Time Complexity: O(n)
    # Auxiliary Space: O(1)
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)

    # Check for the count function
    print("count of 1 is %d" % (llist.count(1)))
