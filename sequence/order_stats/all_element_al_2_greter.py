"""
Find all elements in array which have at-least two greater elements
Given an array of n distinct elements, the task is to find all elements in array which
have at-least two greater elements than themselves.

Examples:

Input : arr = [2, 8, 7, 1, 5]
Output : 2  1  5
The output three elements have two or more greater elements

Input  : arr = [7, -2, 3, 4, 9, -1]
Output : -2  3  4 -1
"""
from __future__ import print_function
import sys

INT_MIN = - sys.maxsize


# Time Complexity : O(n)
# Python program to find all elements in array which have at-least two greater elements
# itself.

def find_elements(arr, n):
    """
    (Efficient)

    In second method we simply calculate second maximum element of array and print all
    element which is less than or equal to second maximum.
    """
    first, second = INT_MIN, INT_MIN

    for i in range(n):
        # If current element is smaller than first then update both first and second
        if arr[i] > first:
            second = first
            first = arr[i]
        # If arr[i] is in between first and second then update second
        elif arr[i] > second:
            second = arr[i]

    for i in range(n):
        if arr[i] < second:
            print(arr[i], end=" ")


if __name__ == '__main__':
    arr = [2, -6, 3, 5, 1]
    n = len(arr)
    find_elements(arr, n)
