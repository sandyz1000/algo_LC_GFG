"""
Kth smallest element in a row-wise and column-wise sorted 2D array | Set 1
Given an n x n matrix, where every row and column is sorted in non-decreasing order.
Find the kth smallest element in the given 2D array.

For example, consider the following 2D array.

        10, 20, 30, 40
        15, 25, 35, 45
        24, 29, 37, 48
        32, 33, 39, 50
The 3rd smallest element is 20 and 7th smallest element is 30

"""
from typing import List
INT_MAX = 999999999

# kth largest element in a 2d array sorted row-wise and column-wise
# A structure to store an entry of heap. The entry contains a value from 2D array,
# row and column numbers of the value


class HeapNode(object):
    def __init__(self, val, r=None, c=None):
        self.value = val  # value to be stored
        self.r = r  # Row number of value in 2D array
        self.c = c  # Column number of value in 2D array


def min_heapify(harr: List[HeapNode], i: int, heap_size: int) -> int:
    """
    A utility function to minheapify the node harr[i] of a heap stored in harr[]

    :param harr: List[HeapNode]
    :param i: int
    :param heap_size: int
    :return:
    """
    left = i * 2 + 1
    right = i * 2 + 2
    smallest = i
    if left < heap_size and harr[left].value < harr[smallest].value:
        smallest = left
    if right < heap_size and harr[right].value < harr[smallest].value:
        smallest = right
    if smallest != i:
        harr[i], harr[smallest] = harr[smallest], harr[i]
        min_heapify(harr, smallest, heap_size)


def build_heap(harr: List[HeapNode], n: int):
    """
    A utility function to convert harr[] to a max heap

    :param harr: List[HeapNode]
    :param n: int
    :return: None
    """
    for i in range((n - 1) // 2, -1):
        min_heapify(harr, i, n)


# This function returns kth smallest element in a 2D array mat[][]
def kth_smallest(mat: List[List[int]], n: int, k: int) -> int:
    """
    Time Complexity: The above solution involves following steps.
    1) Build a min heap which takes O(n) time
    2) Heapify k times which takes O(kLogn) time.
    Therefore, overall time complexity is O(n + kLogn) time.
    """
    # k must be greater than 0 and smaller than n*n
    if k <= 0 or k > n * n:
        return INT_MAX

    # Create a min heap of elements from first row of 2D array
    harr = [HeapNode(mat[0][i], 0, i) for i in range(n)]
    build_heap(harr, n)

    for i in range(k):
        hr = harr[0]  # Get current heap root

        # Get next value from column of root's value. If the value stored at root was
        # last value in its column, then assign INFINITE as next value
        next_val = mat[hr.r + 1][hr.c] if (hr.r < (n - 1)) else INT_MAX
        # Update heap root with next value
        harr[0] = HeapNode(next_val, hr.r + 1, hr.c)
        # Heapify root
        min_heapify(harr, 0, n)

    # Return the value at last extracted root
    return hr.value


if __name__ == '__main__':
    mat = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [25, 29, 37, 48],
           [32, 33, 39, 50]]

    print("%dth smallest element is %d " % (3, kth_smallest(mat, 4, 3)))

    print("%dth smallest element is %d " % (7, kth_smallest(mat, 4, 7)))
