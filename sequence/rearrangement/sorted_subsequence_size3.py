"""
Find a sorted sub-sequence of size 3 in linear time
Given an array of n integers, find the 3 elements such that a[i] < a[j] < a[k] and
i < j < k in 0(n) time. If there are multiple such triplets, then print any one of them.

Examples:
------------
Input:  arr[] = {12, 11, 10, 5, 6, 2, 30}
Output: 5, 6, 30

Input:  arr[] = {1, 2, 3, 4}
Output: 1, 2, 3 OR 1, 2, 4 OR 2, 3, 4

Input:  arr[] = {4, 3, 2, 1}
Output: No such triplet

Solution:
------------
1) Create an auxiliary array smaller[0..n-1]. smaller[i] should store the index of a number which
is smaller than arr[i] and is on left side of arr[i]. smaller[i] should contain -1 if there is no
such element.

2) Create another auxiliary array greater[0..n-1]. greater[i] should store the index of a number
which is greater than arr[i] and is on right side of arr[i]. greater[i] should contain -1 if there
is no such element.

3) Finally traverse both smaller[] and greater[] and find the index i for which both smaller[i]
and greater[i] are not -1.

Time Complexity: O(n)
Auxliary Space: O(n)

"""
from __future__ import print_function


# Python program to fund a sorted sub-sequence of size 3

def find3numbers(arr):
    n = len(arr)
    maximum = n - 1  # Index of maximum element from right side
    minimum = 0  # Index of minimum element from left side

    # Create an array that will store index of a smaller
    # element on left side. If there is no smaller element
    # on left side, then smaller[i] will be -1.
    smaller = [0] * 10000
    smaller[0] = -1
    for i in range(1, n):
        if arr[i] <= arr[minimum]:
            minimum = i
            smaller[i] = -1
        else:
            smaller[i] = minimum

    # Create another array that will store index of a
    # greater element on right side. If there is no greater
    # element on right side, then greater[i] will be -1.
    greater = [0] * 10000
    greater[n - 1] = -1

    for i in range(n - 2, -1, -1):
        if arr[i] >= arr[maximum]:
            maximum = i
            greater[i] = -1

        else:
            greater[i] = maximum

    # Now find a number which has both a greater number on
    # right side and smaller number on left side
    for i in range(0, n):
        if smaller[i] != -1 and greater[i] != -1:
            print(arr[smaller[i]], arr[i], arr[greater[i]])
            return

    # If we reach here, then there are no such 3 numbers
    print("No triplet found")
    return


if __name__ == '__main__':
    # Output: 5 6 30
    arr = [12, 11, 10, 5, 6, 2, 30]
    find3numbers(arr)
