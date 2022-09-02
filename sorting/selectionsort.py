"""
Selection Sort

The selection sort algorithm sorts an array by repeatedly finding the minimum element (
considering ascending order) from unsorted part and putting it at the beginning. The algorithm
maintains two sub-arrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the
unsorted subarray is picked and moved to the sorted subarray.

Following example explains the above steps:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
arr[] = 64 25 12 22 11

// Find the minimum element in arr[0...4] and place it at beginning
11 25 12 22 64

// Find the minimum element in arr[1...4] and place it at beginning of arr[1...4]
11 12 25 22 64

// Find the minimum element in arr[2...4] and place it at beginning of arr[2...4]
11 12 22 25 64

// Find the minimum element in arr[3...4] and place it at beginning of arr[3...4]
11 12 22 25 64

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""

from __future__ import print_function
from copy import deepcopy

# Time Complexity: O(n2) as there are two nested loops.
# Auxiliary Space: O(1)


class SelectionSort:
    def __init__(self, arr):
        self.arr = deepcopy(arr)
        self.size = len(self.arr)

    def sort(self):
        for i in range(0, self.size):
            min_index = i
            for j in range(i, self.size):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j

            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]

    def get_arr(self):
        return self.arr


if __name__ == "__main__":
    ss = SelectionSort([64, 25, 12, 22, 11])
    ss.sort()  # Sort operation
    print(ss.get_arr())
