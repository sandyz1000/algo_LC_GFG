"""
Merge Sort for Linked Lists

Merge sort is often preferred for sorting a linked list. The slow random-access performance of a 
linked list makes some other algorithms (such as quicksort) perform poorly, and others (such as 
heapsort) completely impossible. 

Let head be the first node of the linked list to be sorted and headRef be the pointer to head. Note
that we need a reference to head in MergeSort() as the below implementation changes next links to 
sort the linked lists (not data at the nodes), so head node has to be changed if the data at 
original head is not the smallest value in linked list.

MergeSort(headRef)
1) If head is NULL or there is only one element in the Linked List  then return.
2) Else divide the linked list into two halves.
    FrontBackSplit(head, &a, &b); /* a and b are two halves */

3) Sort the two halves a and b.
    MergeSort(a)
    MergeSort(b)

4) Merge the sorted a and b (using SortedMerge() discussed here) and update the head pointer
using headRef.
    *headRef = SortedMerge(a, b)"""

from __future__ import print_function


class Node:
    """Link list node"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, head_ref=None):
        self.head_ref = head_ref

    def printList(self):
        """Function to print nodes in a given linked list"""
        node = self.head_ref
        while node is not None:
            print("%d " % node.data, end=" ")
            node = node.next_node

    def push(self, new_data):
        """Function to insert a node at the beginging of the linked list"""
        # allocate node
        new_node = Node(new_data, self.head_ref)
        # move the head to point to the new node
        self.head_ref = new_node

    def get_middle(self, h):
        """Utility function to get the middle of the linked list"""
        if h is None:  # Base case
            return h

        fastptr = h.next_node
        slowptr = h

        # Move fastptr by two and slow ptr by one Finally slowptr will point to middle node
        while fastptr is not None:
            fastptr = fastptr.next_node
            if fastptr is not None:
                slowptr = slowptr.next_node
                fastptr = fastptr.next_node

        return slowptr

    def merge_sort(self, node):
        """sorts the linked list by changing next pointers (not data)"""

        # Base case -- length 0 or 1
        if (node is None) or (node.next_node is None):
            return node

        # get the middle node of the list
        middle = self.get_middle(node)
        next_of_middle = middle.next_node

        # set the next of middle node to null
        middle.next_node = None

        # Apply mergeSort on left list
        left = self.merge_sort(node)
        right = self.merge_sort(next_of_middle)

        # answer = merge the two sorted lists together
        head_ref = self.sorted_merge(left, right)
        return head_ref

    def sorted_merge(self, a, b):
        """
        See http://www.geeksforgeeks.org/?p=3622 for details of this function

        :type a: Node
        :type b: Node
        :rtype:
        """
        if a is None:  # Base cases
            return b

        elif b is None:
            return a

        # Pick either a or b, and recur
        if a.data <= b.data:
            result = a
            result.next_node = self.sorted_merge(a.next_node, b)
        else:
            result = b
            result.next_node = self.sorted_merge(a, b.next_node)

        return result


if __name__ == '__main__':
    # Output: Fix output
    # Time Complexity: O(n Log n)
    # Start with the empty list
    a = LinkedList()

    # Let us create a unsorted linked lists to test the functions
    # Created lists shall be a: 2->3->20->5->10->15
    a.push(15)
    a.push(10)
    a.push(5)
    a.push(20)
    a.push(3)
    a.push(2)

    # Sort the above created Linked List
    a.head_ref = a.merge_sort(a.head_ref)

    print("\nSorted Linked List is: \n")
    a.printList()
