"""
Sort a nearly sorted (or K sorted) array

Given an array of n elements, where each element is at most k away from its target position, devise
an algorithm that sorts in O(n log k) time.

Example:
Let us consider k is 2, an element at index 7 in the sorted array, can be at indexes
5, 6, 7, 8, 9 in the given array.

Other Example:
Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
        k = 3 
Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50}
        k = 4
Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}

The Min Heap based method takes O(nLogk) time and uses O(k) auxiliary space."""

import typing


def insertionSort(A: typing.List[int], size: int):
    """
    We can use Insertion Sort to sort the elements efficiently.
    Following is the Python code for standard Insertion Sort.

    The inner loop will run at most k times. To move every element to its correct place,
    at most k elements need to be moved. So overall complexity will be O(nk)

    Function to sort an array using insertion sort
    :type A: List[int]
    :type size: int
    :rtype: void
    """
    for i in range(1, size):
        key = A[i]
        j = i - 1

        # Move elements of A[0..i-1], that are greater than key, to one position ahead of
        # their current position. This loop will run at most k times
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key


class MinHeap(object):
    """
    We can sort such arrays more efficiently with the help of Heap data structure.
    Following is the detailed process that uses Heap.
    1) Create a Min Heap of size k+1 with first k+1 elements. This will take O(k) time
      (See this GFact)
    2) One by one remove min element from heap, put it in result array, and add a new element to
      heap from remaining elements.

    Removing an element and adding a new element to min heap will take Logk time.
    So overall complexity will be O(k) + O((n-k)*logK)

    The Min Heap based method takes O(nLogk) time and uses O(k) auxiliary space.

    ---------------------------------------------------------------------------------------
    We can also use a Balanced Binary Search Tree instead of Heap to store K+1 elements. The
    insert and delete operations on Balanced BST also take O(Logk) time. So Balanced BST based
    method will also take O(nLogk) time, but the Heap based method seems to be more efficient as
    the minimum element will always be at root. Also, Heap doesn't need extra space for left and
    right pointers.

    """

    def __init__(self, arr, size):
        self.harr = arr  # pointer to array of elements in heap
        self.heap_size = size  # size of min heap
        for i in range((self.heap_size - 1) // 2, -1, -1):
            self.min_heapify(i)

    def min_heapify(self, i):
        """
        to heapify a subtree with root at given index
        """
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < self.heap_size and self.harr[l] < self.harr[i]:
            smallest = l

        if r < self.heap_size and self.harr[r] < self.harr[smallest]:
            smallest = r

        if smallest != i:
            self.harr[i], self.harr[smallest] = self.harr[smallest], self.harr[i]
            self.min_heapify(smallest)

    # to get index of left child of node at index i
    def left(self, i):
        return 2 * i + 1

    # to get index of right child of node at index i
    def right(self, i):
        return 2 * i + 2

    # to remove min (or root), add a new value x, and return old root
    def replace_min(self, x):
        root = self.harr[0]
        self.harr[0] = x
        if root < x:
            self.min_heapify(0)
        return root

    # to extract the root which is the minimum element
    def extract_min(self):
        root = self.harr[0]
        if self.heap_size > 1:
            self.harr[0] = self.harr[self.heap_size - 1]
            self.heap_size -= 1
            self.min_heapify(0)
        return root

    @staticmethod
    def sort_k(arr, n, k):
        """
        Given an array of size n, where every element is k away from its target
        position, sorts the array in O(nLogk) time.
        :type arr: List[]
        :type n:
        :type k:
        :rtype:
        """
        # Create a Min Heap of first (k+1) elements from input array
        harr = [0] * (k + 1)
        i = 0
        # i < n condition is needed when k > n
        while i <= k and i < n:
            harr[i] = arr[i]
            i += 1
        hp = MinHeap(harr, k + 1)

        # i is index for remaining elements in arr[] and ti
        # is target index of for current minimum element in MinHeap 'hp'.
        i, ti = k + 1, 0
        while ti < n:
            # If there are remaining elements, then place root of heap at target index and
            # add arr[i] to Min Heap
            if i < n:
                arr[ti] = hp.replace_min(arr[i])
            # Otherwise place root at its target index and reduce heap size
            else:
                arr[ti] = hp.extract_min()

            i += 1
            ti += 1


if __name__ == '__main__':
    # Following is sorted array: 2 3 6 8 12 56
    k = 3
    arr = [2, 6, 3, 12, 56, 8]
    n = len(arr)
    MinHeap.sort_k(arr, n, k)

    print("Following is sorted array")
    print(arr)
