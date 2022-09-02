"""
Print all elements in sorted order from row and column wise sorted matrix

Given an n x n matrix, where every row and column is sorted in non-decreasing order.
Print all elements of matrix in sorted order.

==Example:==
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Input: mat = [{10, 20, 30, 40},
             {15, 25, 35, 45},
             {27, 29, 37, 48},
             {32, 33, 39, 50}]

Output: 10 15 20 25 27 29 30 32 33 35 37 39 40 45 48 50
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""


import sys

N = 4


class MinHeapNode(object):
    def __init__(self, element, i, j):
        self.element = element  # The element to be stored
        self.i = i  # index of the row from which the element is taken
        self.j = j  # index of the next element to be picked from row


class MinHeap(object):
    """
    The idea is to use a Min Heap of size N which stores elements of first column. The do extract
    minimum. In extract minimum, replace the minimum element with the next element of the row from
    which the element is extracted. Time complexity of this solution is O(N^2LogN).
    """
    def __init__(self, a, size):
        self.heap_size = size  # size of min heap
        self.harr = a  # pointer to array of elements in heap
        i = (self.heap_size - 1) // 2
        while i >= 0:
            self.min_heapify(i)
            i -= 1

    def min_heapify(self, i):
        """
        A recursive method to heapify a subtree with root at given index
        This method assumes that the subtrees are already heapified
        to heapify a subtree with root at given index
        :return:
        """
        l = self.left(i)
        r = self.right(i)
        smallest = i

        if l < self.heap_size and self.harr[l].element < self.harr[i].element:
            smallest = l

        if r < self.heap_size and self.harr[r].element < self.harr[smallest].element:
            smallest = r

        if smallest != i:
            self.harr[i], self.harr[smallest] = self.harr[smallest], self.harr[i]
            self.min_heapify(smallest)

    def left(self, i):
        # to get index of left child of node at index i
        return 2 * i + 1

    def right(self, i):
        # to get index of right child of node at index i
        return 2 * i + 2

    def getMin(self):
        # to get the root
        return self.harr[0]

    def replaceMin(self, x):
        # to replace root with new node x and heapify() new root
        self.harr[0] = x
        self.min_heapify(0)

    @staticmethod
    def print_sorted(mat):
        """
        This function prints elements of a given matrix in non-decreasing order.
        It assumes that ma[][] is sorted row wise sorted.
        :param mat:
        :return:
        """
        # Create a min heap with k heap nodes. Every heap node has first element of an array
        harr = [MinHeapNode(mat[i][0], i, 1) for i in range(N)]
        hp = MinHeap(harr, N)  # Create the min heap

        # Now one by one get the minimum element from min
        # heap and replace it with next element of its array
        for count in range(N * N):
            # Get the minimum element and store it in output
            root = hp.getMin()
            print(root.element, end=" ")

            # Find the next element that will replace current root of heap.
            # The next element belongs to same array as the current root.
            if root.j < N:
                root.element = mat[root.i][root.j]
                root.j += 1

            else:  # If root was the last element of its array
                root.element = sys.maxsize

            # Replace root with next element of array
            hp.replaceMin(root)


if __name__ == '__main__':
    mat = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [27, 29, 37, 48],
           [32, 33, 39, 50]]
    MinHeap.print_sorted(mat)
