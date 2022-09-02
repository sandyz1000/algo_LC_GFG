"""
Sort numbers stored on different machines
---------------------------------------------
Given N machines. Each machine contains some numbers
in sorted form. But the amount of numbers, each machine has is not fixed. Output the numbers from
all the machine in sorted non-decreasing form.

Example:
Machine M1 contains 3 numbers: {30, 40, 50}
Machine M2 contains 2 numbers: {35, 45}
Machine M3 contains 5 numbers: {10, 60, 70, 80, 100}

Output: {10, 30, 35, 40, 45, 50, 60, 70, 80, 100}

Representation of stream of numbers on each machine is considered as linked list. A Min Heap can
be used to print all numbers in sorted order.

Following is the detailed process

1.  Store the head pointers of the linked lists in a minHeap of size N where N is number of
    machines.
2.  Extract the minimum item from the minHeap. Update the minHeap by replacing the head of the
    minHeap with the next number from the linked list or by replacing the head of the minHeap with
    the last number in the minHeap followed by decreasing the size of heap by 1.
3.  Repeat the above step 2 until heap is not empty. """

from __future__ import print_function
from copy import deepcopy
import typing


class ListNode(object):
    """A Linked List node"""

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def push(self, new_data):
        """
        A utility function to insert a new node at the beginning of linked list
        :param new_data:
        :return:
        """
        new_node = ListNode(new_data)  # allocate node
        new_node.next_node = self.head  # link the old list off the new node
        # move the head to point to the new node
        self.head = new_node


class MinHeapNode(object):
    def __init__(self, head):
        self.head = head


class MinHeap(object):
    """
    A Min Heap (Collection of Min Heap nodes)
    """

    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity
        self.arr = [MinHeapNode(None) for j in range(self.capacity)]

    def min_heapify(self, idx: int):
        """
        The standard min_heapify function.
        :param idx:
        :return:
        """
        left = 2 * idx + 1
        right = 2 * idx + 2
        smallest = idx

        if left < self.count and \
                self.arr[left].head.data < self.arr[smallest].head.data:
            smallest = left

        if right < self.count and \
                self.arr[right].head.data < self.arr[smallest].head.data:
            smallest = right

        if smallest != idx:
            self.arr[smallest], self.arr[idx] = self.arr[idx], self.arr[smallest]
            self.min_heapify(smallest)

    def is_empty(self):
        """ A utility function to check whether a Min Heap is empty or not """
        return self.count == 0

    def build_min_heap(self):
        """
        A standard function to build a heap
        """
        n = self.count - 1
        for i in range((n - 1) // 2, -1, -1):
            self.min_heapify(i)

    def populate_min_heap(self, arr: typing.List[LinkedList], n: int):
        """
        This function inserts array elements to heap and then calls buildHeap for heap
        property among nodes
        """
        for i in range(n):
            self.arr[self.count].head = arr[i].head
            self.count += 1

        self.build_min_heap()

    def extract_min(self):
        """ Return minimum element from all linked lists """
        if self.is_empty():
            return None

        # The root of heap will have minimum value
        temp = deepcopy(self.arr[0])

        # Replace root either with next node of the same list.
        if temp.head.next_node:
            self.arr[0].head = temp.head.next_node
        # If list empty, then reduce heap size
        else:
            self.arr[0] = self.arr[self.count - 1]
            self.count -= 1

        self.min_heapify(0)
        return temp.head

    @staticmethod
    def external_sort(arr: typing.List[LinkedList], N: int):
        """
        The main function that takes an array of lists from N machines and
        generates the sorted output

        :param arr:
        :param N:
        :return:
        """
        # Create a min heap of size equal to number of machines
        min_heap = MinHeap(N)
        # populate first item from all machines
        min_heap.populate_min_heap(arr, N)

        while not min_heap.is_empty():
            temp = min_heap.extract_min()
            print("%d " % temp.data, end=" ")


if __name__ == '__main__':
    N = 3  # Number of machines
    # an array of pointers storing the head nodes of the linked lists
    arr = []

    # Create a Linked List 30->40->50 for first machine
    llist = LinkedList()
    llist.push(50)
    llist.push(40)
    llist.push(30)
    arr.append(llist)

    # Create a Linked List 35->45 for second machine
    llist = LinkedList()
    llist.push(45)
    llist.push(35)
    arr.append(llist)

    # Create Linked List 10->60->70->80 for third machine
    llist = LinkedList()
    llist.push(100)
    llist.push(80)
    llist.push(70)
    llist.push(60)
    llist.push(10)
    arr.append(llist)

    # Sort all elements
    MinHeap.external_sort(arr, N)
