"""
Find the smallest and second smallest elements in an array
Write an efficient C program to find smallest and second smallest element in an array.

Example:

Input:  arr = [12, 13, 1, 10, 34, 1]
Output: The smallest element is 1 and second Smallest element is 10
"""

import sys

MAXINT = sys.maxsize


def print2Smallest(arr):
    # Time Complexity: O(n)
    # There should be atleast two elements
    arr_size = len(arr)
    if arr_size < 2:
        print("Invalid Input")
        return

    first = second = MAXINT
    for i in range(0, arr_size):
        # If current element is smaller than first then update both first and second
        if arr[i] < first:
            second = first
            first = arr[i]

        # If arr[i] is in between first and second then update second
        elif arr[i] < second and arr[i] != first:
            second = arr[i]

    if second == MAXINT:
        print("No second smallest element")
    else:
        print('The smallest element is', first, 'and second smallest element is', second)


if __name__ == '__main__':
    arr = [12, 13, 1, 10, 34, 1]
    print2Smallest(arr)
