"""
A typical recursive Python implementation of QuickSort

------------------------------------------------
Discussion:
------------------------------------------------
The recursion method can be optimized in many ways:

1) The above implementation uses last index as pivot. This causes worst-case behavior on already
sorted arrays, which is a commonly occurring case. The problem can be solved by choosing either a
random index for the pivot, or choosing the middle index of the partition or choosing the median
of the first, middle and last element of the partition for the pivot. (See this for details)

2) To reduce the recursion depth, recur first for the smaller half of the array, and use a tail
call to recurse into the other.

3) Insertion sort works better for small subarrays. Insertion sort can be used for invocations on
such small arrays (i.e. where the length is less than a threshold t determined experimentally).
For example, this library implementation of qsort uses insertion sort below size 7."""

from __future__ import print_function


class Stack(object):
    """A Stack has array of Nodes, capacity, and top"""

    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.arry = [None] * capacity

    def is_full(self):
        """A utility function to check if stack is full"""
        return self.top == self.capacity - 1

    def is_empty(self):
        """A utility function to check if stack is empty"""
        return self.top == -1

    def push(self, item):
        """A utility function to push an item to stack"""
        if self.is_full():
            raise IndexError("Cannot push element to full stack")
        self.arry[self.top + 1] = item
        self.top += 1

    def pop(self):
        """A utility function to remove an item from stack"""
        if self.is_empty():
            raise IndexError("Cannot pop Empty stack")
        temp = self.arry[self.top]
        self.arry[self.top] = None
        self.top -= 1
        return temp

    def peek(self):
        """A utility function to get top node of stack"""
        return self.arry[self.top]


def partition(arr, low, high):
    """
    This function takes last element as pivot, places the pivot element at its correct
    position in sorted array, and places all smaller (smaller than pivot) to left of pivot
    and all greater elements to right of pivot
    :param arr:
    :param low:
    :param high:
    :return:
    """
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Function to do Quick sort
def quickSort(arr, low, high):
    """
    The main function that implements QuickSort
    arr[] --> Array to be sorted,
    low  --> Starting index,
    high  --> Ending index
    :param arr:
    :param low:
    :param high:
    :return:
    """
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Python program for implementation of Quicksort
# This function is same in both iterative and recursive
def partition2(arr, l, h):
    i = (l - 1)
    x = arr[h]

    for j in range(l, h):
        if arr[j] <= x:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quick_sort_iterative(arr, l, h):
    """
    The above mentioned optimizations for recursive quick sort can also be applied to iterative
    version.

    1) Partition process is same in both recursive and iterative. The same techniques to choose
    optimal pivot can also be applied to iterative version.
    2) To reduce the stack size, first push the indexes of smaller half.
    3) Use insertion sort when the size reduces below a experimentally calculated threshold.

    Function to do Quick sort
    arr[] --> Array to be sorted,
    l  --> Starting index,
    h  --> Ending index

    :type arr: List[int]
    :type l: int
    :type h: int
    :rtype: void
    """
    size = h - l + 1
    # Create an auxiliary stack
    stack = Stack(size)
    stack.push(l)
    stack.push(h)

    # Keep popping from stack while is not empty
    while stack.top >= 0:
        h = stack.pop()
        l = stack.pop()

        # Set pivot element at its correct position in sorted array
        p = partition2(arr, l, h)

        # If there are elements on left side of pivot, then push left side to stack
        if p - 1 > l:
            stack.push(l)
            stack.push(p-1)
        # If there are elements on right side of pivot, then push right side to stack
        if p + 1 < h:
            stack.push(p+1)
            stack.push(h)


if __name__ == '__main__':
    arr = [4, 3, 5, 2, 1, 3, 2, 3]
    n = len(arr)
    quick_sort_iterative(arr, 0, n - 1)
    print("Sorted array is:")
    for i in range(n):
        print("%d" % arr[i], end=" ")
