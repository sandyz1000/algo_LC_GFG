"""
Given k sorted arrays of size n each, merge them and print the sorted output.

Input:
k = 3, n =  4
arr = [[1, 3, 5, 7],
       [2, 4, 6, 8],
       [0, 9, 10, 11]]

Output:
0 1 2 3 4 5 6 7 8 9 10 11

A simple solution is to create an output array of size n*k and one by one copy all arrays to it.
Finally, sort the output array using any O(nLogn) sorting algorithm.

Time Complexity:
The main step is 3rd step, the loop runs n*k times. In every iteration of loop, we call heapify
which takes O(Logk) time. Therefore, the time complexity is O(nk Logk).

"""
from __future__ import print_function, absolute_import

# Python program to merge k sorted arrays of size n each.
import sys

n = 4


# A min heap node
class MinHeapNode(object):
    def __init__(self, element, i, j):
        self.element = element  # The element to be stored
        self.i = i  # index of the array from which the element is taken
        self.j = j  # index of the next element to be picked from array


# A class for Min Heap
class MinHeap(object):
    def __init__(self, arr, size):
        self.harr = arr  # pointer to array of elements in heap
        self.heap_size = size  # size of min heap
        i = (self.heap_size - 1) // 2
        while i >= 0:
            self.min_heapify(i)
            i -= 1

    def min_heapify(self, i):
        """
        to heapify a subtree with root at given index
        """
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < self.heap_size and self.harr[left].element < self.harr[i].element:
            smallest = left

        if right < self.heap_size and self.harr[right].element < self.harr[smallest].element:
            smallest = right

        if smallest != i:
            self.harr[i], self.harr[smallest] = self.harr[smallest], self.harr[i]
            self.min_heapify(smallest)

    # to replace root with new node x and heapify() new root
    def replace_min(self, x):
        self.harr[0] = x
        self.min_heapify(0)

    # to extract the root which is the minimum element
    def get_min(self):
        return self.harr[0]

    @staticmethod
    def merge_k_arrays(arr, k):
        """
        This function takes an array of arrays as an argument and All arrays are assumed to
        be sorted. It merges them together and prints the final sorted output.
        """
        output = [0] * (n * k)  # To store output array

        # Create a min heap with k heap nodes.  Every heap node
        # has first element of an array
        harr = [MinHeapNode(arr[i][0], i, 1) for i in range(k)]

        hp = MinHeap(harr, k)  # Create the heap

        # Now one by one get the minimum element from min
        # heap and replace it with next element of its array
        for count in range(n * k):
            # Get the minimum element and store it in output
            root = hp.get_min()
            output[count] = root.element

            # Find the next element that will replace current root of heap.
            # The next element belongs to same array as the current root.
            if root.j < n:
                root.element = arr[root.i][root.j]
                root.j += 1
            else:  # If root was the last element of its array
                root.element = sys.maxsize

            # Replace root with next element of array
            hp.replace_min(root)
        return output


if __name__ == '__main__':
    # Output: Merged array is  [1, 2, 6, 9, 12, 20, 23, 34, 34, 90, 1000, 2000]
    # Change n at the top to change number of elements in an array
    arr = [[2, 6, 12, 34],
           [1, 9, 20, 1000],
           [23, 34, 90, 2000]]
    k = len(arr)
    output = MinHeap.merge_k_arrays(arr, k)

    print("Merged array is \n")
    print(output)
