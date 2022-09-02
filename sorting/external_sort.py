"""
https://www.geeksforgeeks.org/external-sorting/

External Sorting

External sorting is a term for a class of sorting algorithms that can handle massive amounts of
data. External sorting is required when the data being sorted do not fit into the main memory of
a computing device (usually RAM) and instead they must reside in the slower external memory (
usually a hard drive). External sorting typically uses a hybrid sort-merge strategy. In the
sorting phase, chunks of data small enough to fit in main memory are read, sorted, and written
out to a temporary file. In the merge phase, the sorted sub-files are combined into a single
larger file.

One example of external sorting is the external merge sort algorithm, which sorts chunks that
each fit in RAM, then merges the sorted chunks together. We first divide the file into runs such
that the size of a run is small enough to fit into main memory. Then sort each run in main memory
using merge sort sorting algorithm. Finally merge the resulting runs together into successively
bigger runs, until the file is sorted.

Prerequisite for the algorithm/code:
MergeSort : Used for sort individual runs (a run is part of file that is small enough to fit in
main memory)
Merge K Sorted Arrays : Used to merge sorted runs.

Below are the steps used in Python implementation.

Inputs:
input_file  : Name of input file. input.txt
output_file : Name of output file, output.txt
run_size : Size of a run (can fit in RAM)
num_ways : Number of runs to be merged

Output:
1) Read input_file such that at most 'run_size' elements are read at a time. Do following for the
     every run read in an array.
      a) Sort the run using MergeSort.
      b) Store the sorted run in a temporary file, say 'i' for i'th run.

2) Merge the sorted files using the approach discussed here


Complexity Analysis:
--------------------
Time Complexity: O(n + run_size log run_size).
Time taken for merge sort is O(nlogn), but there are at most run_size elements. So the time complexity
is O(run_size log run_size) and then to merge the sorted arrays the time complexity is O(n). Therefore,
the overall time complexity is O(n + run_size log run_size).

Auxiliary space:O(run_size).
run_size is the space needed to store the array.
"""
from __future__ import print_function
import sys


# Python program to implement external sorting using merge sort


class MinHeapNode(object):
    """The element to be stored
    """
    def __init__(self, element, i):
        self.element = element
        self.index = i  # index of the array from which the element is taken

    def swap(self, x, y):
        """Prototype of a utility function to swap two min heap nodes"""


class MinHeap(object):
    def __init__(self, arr, size):
        self.harr = arr  # pointer to array of elements in heap
        self.heap_size = size  # size of min heap
        i = (self.heap_size - 1) // 2
        while i >= 0:
            self.MinHeapify(i)
            i -= 1

    def MinHeapify(self, i):
        """
        A recursive method to heapify a subtree with root
        at given index. This method assumes that the
        subtrees are already heapified
        :param i:
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

            self.MinHeapify(smallest)

    def left(self, i):
        """to get index of left child of node at index i"""
        return (2 * i + 1)

    def right(self, i):
        """to get index of right child of node at index i"""
        return (2 * i + 2)

    def getMin(self):
        """to get the root"""
        return self.harr[0]

    def replaceMin(self, x):
        """to replace root with new node x and heapify() new root"""
        self.harr[0] = x
        self.MinHeapify(0)


class ExternalSort(object):
    def merge_sort(self, arr, l, r):
        """l is for left index and r is right index of the sub-array of arr to be sorted"""
        if l < r:
            # Same as (l+r)/2, but avoids overflow for large l and h
            m = l + (r - l) // 2

            # Sort first and second halves
            self.merge_sort(arr, l, m)
            self.merge_sort(arr, m + 1, r)

            self.merge(arr, l, m, r)

    def merge(self, arr, l, m, r):
        """
        Merges two subarrays of arr[].
        First subarray is arr[l..m]
        Second subarray is arr[m+1..r]
        """
        # i, j, k;
        n1 = m - l + 1
        n2 = r - m

        # /* create temp arrays */
        L, R = [arr[l + i] for i in range(n1)], [arr[m + 1 + j] for j in range(n2)]

        # /* Merge the temp arrays back into arr[l..r]*/
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = l  # Initial index of merged subarray
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                k += 1
                i += 1
            else:
                arr[k] = R[j]
                k += 1
                j += 1

        # /* Copy the remaining elements of L[], if there are any */
        while i < n1:
            arr[k] = L[i]
            k += 1
            i += 1

        # /* Copy the remaining elements of R[], if there are any */
        while j < n2:
            arr[k] = R[j]
            k += 1
            i += 1

    def open_file(self, fileName, mode='r'):
        fp = open(fileName, mode)
        if fp is None:
            sys.stderr.write("Error while opening the file.\n")
            exit(1)
        return fp

    def merge_files(self, output_file, n, k):
        """Merges k sorted files.  Names of files are assumed to be 1, 2, 3, ... k"""
        input_fp = [self.open_file(file_name, 'r') for file_name in range(k)]

        # FINAL OUTPUT FILE
        output_fp = self.open_file(output_file, "w")

        # Create a min heap with k heap nodes. Every heap node has first element of
        # scratch output file
        harr = [MinHeapNode(None, i) for i in range(k)]
        size = 0
        for i in range(k):
            for line in input_fp[i]:
                harr[i].element = line

            harr[i].i = i  # Index of scratch output file
            size += 1

        hp = MinHeap(harr, size)  # Create the heap
        count = 0

        # Now one by one get the minimum element from min heap and replace it with next element.
        # run till all filled input files reach EOF
        while count != size:
            # Get the minimum element and store it in output file
            root = hp.getMin()
            print(output_fp, "%d ", root.element)

            # Find the next element that will replace current root of heap. The next
            # element belongs to same input file as the current min element.
            for line in input_file[root.i]:
                root.element = line
            root.element = sys.maxint
            count += 1

            # Replace root with next element of input file
            hp.replaceMin(root)

        # close input and output files
        [input_fp[i].close() for i in range(k)]
        output_file.close()

    def create_initial_runs(self, file_name, run_size, num_ways):
        """
        Using a merge-sort algorithm, create the initial runs and divide them evenly
        among the output files"""
        # k = 10
        input_fp = self.open_file(file_name, 'r')

        # output scratch files
        output_fp = [self.open_file(i, 'w') for i in range(num_ways)]

        # allocate a dynamic array large enough to accommodate runs of size run_size
        arr = [None for _ in range(run_size)]
        more_input = True
        next_output_file = 0
        i = 0
        while (more_input):
            # write run_size elements into arr from input file
            for i in range(run_size):
                arr = [line for line in input_fp[i]]
                if len(arr) == 0:
                    more_input = False
                    break

            # sort array using merge sort
            self.merge_sort(arr, 0, i - 1)

            # write the records to the appropriate scratch output file, can't assume that the
            # loop runs to run_size since the last run's length may be less than run_size
            arr = [j for j in output_fp[next_output_file]]

            next_output_file += 1

        [output_fp[i].close() for i in range(num_ways)]

        # fclose(in);

    def externalSort(self, input_file, output_file, num_ways, run_size):
        """For sorting data stored on disk"""
        # read the input file, create the initial runs, and assign the runs to the
        # scratch output files
        self.create_initial_runs(input_file, run_size, num_ways)

        # Merge the runs using the K-way merging
        self.merge_files(output_file, run_size, num_ways)


if __name__ == '__main__':
    import random

    #  No. of Partitions of input file.
    num_ways = 10

    # The size of each partition
    run_size = 1000

    input_file = "input.txt"
    output_file = "output.txt"

    fp = open(input_file, "w")

    # generate input
    for i in range(num_ways * run_size):
        fp.write(random.randint())

    fp.close()

    ext_sort = ExternalSort()
    ext_sort.externalSort(input_file, output_file, num_ways, run_size)
