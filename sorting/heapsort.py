"""
Heap Sort

Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is
similar to selection sort where we first find the maximum element and place the maximum element at
the end. We repeat the same process for remaining element.

What is Binary Heap?
Let us first define a Complete Binary Tree. A complete binary tree is a binary tree in which every
level, except possibly the last, is completely filled, and all nodes are as far left as possible.

A Binary Heap is a Complete Binary Tree where items are stored in a special order such that value
in a parent node is greater(or smaller) than the values in its two children nodes. The former is
called as max heap and the latter is called min heap. The heap can be represented by binary tree
or array.

Why array based representation for Binary Heap?
Since a Binary Heap is a Complete Binary Tree, it can be easily represented as array and array
based representation is space efficient. If the parent node is stored at index I, the left child
can be calculated by 2 * I + 1 and right child by 2 * I + 2 (assuming the indexing starts at 0).

Heap Sort Algorithm for sorting in increasing order:
1.  Build a max heap from the input data.
2.  At this point, the largest item is stored at the root of the heap. Replace it with the last
    item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of tree.
3.  Repeat above steps while size of heap is greater than 1.

How to build the heap?
Heapify procedure can be applied to a node only if its children nodes are heapified. So the
heapification must be performed in the bottom up order.

Input data: 4, 10, 3, 5, 1
            
            4(0)
            /   \
        10(1)   3(2)
        /   \
     5(3)   1(4)

The numbers in bracket represent the indices in the array representation of data.

Applying heapify procedure to index 1:

        4(0)
        /   \
    10(1)    3(2)
           /   \
    5(3)    1(4)

Applying heapify procedure to index 0:
            10(0)
            /  \
        5(1)  3(2)
        /   \
     4(3)    1(4)

The heapify procedure calls itself recursively to build heap in top down manner. """

from __future__ import print_function


# Time Complexity: Time complexity of heapify is O(Logn).
# Time complexity: Of create_and_build_heap() is O(n) and
# Overall Time complexity: Heap Sort is O(nLogn).

def heapify(arr, n, i):
    """To heapify subtree rooted at index i. n is size of heap"""
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:  # Change root, if needed
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)  # Heapify the root.


def heapSort(arr):
    """The main function to sort an array of given size"""
    n = len(arr)
    for i in range(n // 2, -1, -1):  # Build a maxheap.
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    heapSort(arr)
    n = len(arr)
    print("Sorted array is")
    for i in range(n):
        print("%d" % arr[i], end=" ")
