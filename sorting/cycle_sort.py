"""
Cycle Sort

http://www.geeksforgeeks.org/cycle-sort/

Cycle sort is an in-place sorting Algorithm, unstable sorting algorithm, a comparison sort that is
theoretically optimal in terms of the total number of writes to the original array.

1. It is optimal in terms of number of memory writes. It minimizes the number of memory writes to
sort (Each value is either written zero times, if it's already in its correct position,
or written one time to its correct position.)

2. It is based on the idea that array to be sorted can be divided into cycles. Cycles can be
visualized as a graph. We have n nodes and an edge directed from node i to node j if the element
at i-th index must be present at j-th index in the sorted array.

Example:
--------------------------------
Cycle in arr = [4, 5, 2, 1, 5]

    2 --> 4 --> 1   ---->---
    |           |   |      |
    |           |   5      3
    ------<------   |      |
                    ---<----

Cycle in arr = [4, 3, 2, 1]

    ------<------
    |   --<--   |
    |   |   |   |
    4   3   2   1
    |   |   |   |
    |   -->--   |
    ------>-----

We one by one consider all cycles. We first consider the cycle that includes first element.
We find correct position of first element, place it at its correct position, say j. We consider
old value of arr[j] and find its correct position, we keep doing this till all elements of current
cycle are placed at correct position, i.e., we don't come back to cycle starting point.

Explanation :
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
arr[] = {10, 5, 2, 3}
index =  0   1   2   3
cycle_start = 0
item = 10 = arr[0]

Find position where we put the item
pos = cycle_start
while (arr[i] < item)
    pos++;

We put 10 at arr[3] and change item to old value of arr[3].
arr[] = {10, 5, 2, 10}
item = 3

Again rotate rest cycle that start with index '0'
Find position where we put the item = 3 we swap item with element at arr[1] now
arr[] = {10, 3, 2, 10}
item = 5

Again rotate rest cycle that start with index '0' and item = 5 we swap item with element at arr[2].
arr[] = {10, 3, 5, 10 }
item = 2

Again rotate rest cycle that start with index '0' and item = 2
arr[] = {2 ,3 , 5, 10}

Above is one iteration for cycle_stat = 0.
Repeat above steps for cycle_start = 1, 2, ..n-2

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Time Complexity : O(n^2)
Worst Case : O(n^2)
Average Case: O(n^2)
Best Case : O(n^2)
"""


from __future__ import print_function


# Python program to implement cycle sort

def cycle_sort(arr, n):
    """
    Function sort the array using Cycle sort
    :type arr: List[int]
    :type n: int
    :rtype: None
    """
    # count number of memory writes
    writes = 0

    # traverse array elements and put it to on the right place
    for cycle_start in range(n - 3):
        # initialize item as starting point
        item = arr[cycle_start]

        # Find position where we put the item. We basically
        # count all smaller elements on right side of item.
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1

        # If item is already in correct position
        if pos == cycle_start:
            continue
        # ignore all duplicate  elements
        while item == arr[pos]:
            pos += 1

        # put the item to it's right position
        if pos != cycle_start:
            item, arr[pos] = arr[pos], item
            writes += 1

        # Rotate rest of the cycle
        while pos != cycle_start:
            pos = cycle_start
            # Find position where we put the element
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
            # ignore all duplicate  elements
            while item == arr[pos]:
                pos += 1
            # put the item to it's right position
            if item != arr[pos]:
                item, arr[pos] = arr[pos], item
                writes += 1
                # Number of memory writes or swaps
                # print(writes)


if __name__ == '__main__':
    arr = [1, 8, 3, 9, 10, 10, 2, 4]
    n = len(arr)
    cycle_sort(arr, n)
    print("After sort : ", arr)
