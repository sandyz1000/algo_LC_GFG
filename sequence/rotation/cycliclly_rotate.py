"""
Given an array, cyclically rotate the array clockwise by one.

Examples:

Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}

Time Complexity: O(n)
Auxiliary Space: O(1)

"""
from __future__ import print_function


def rotate(arr, n):
    x = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = x


if __name__ == '__main__':
    # [5, 1, 2, 3, 4]
    arr = [1, 2, 3, 4, 5]
    n = len(arr)

    print("Given array is\n")
    print(arr)
    rotate(arr, n)
    print("\nRotated array is\n")
    print(arr)
