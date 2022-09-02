"""
Dynamic Programming implementation of longest bitonic subsequence problem

Given an array arr[0 ... n-1] containing n positive integers, a subsequence of arr[] is called
Bitonic if it is first increasing, then decreasing. Write a function that takes an array as
argument and returns the length of the longest bitonic subsequence.
A sequence, sorted in increasing order is considered Bitonic with the decreasing part as empty.
Similarly, decreasing order sequence is considered Bitonic with the increasing part as empty.

Examples:

Input arr[] = {1, 11, 2, 10, 4, 5, 2, 1};
Output: 6 (A Longest Bitonic Subsequence of length 6 is 1, 2, 10, 4, 2, 1)

Input arr[] = {12, 11, 40, 5, 3, 1}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 12, 11, 5, 3, 1)

Input arr[] = {80, 60, 30, 40, 20, 10}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 80, 60, 30, 20, 10)

"""
from __future__ import print_function


def lbs(arr):
    """
    lbs() returns the length of the Longest Bitonic Subsequence in
    arr[] of size n. The function mainly creates two temporary arrays
    lis[] and lds[] and returns the maximum lis[i] + lds[i] - 1.

    lis[i] ==> Longest Increasing subsequence ending with arr[i]
    lds[i] ==> Longest decreasing subsequence starting with arr[i]

    Time Complexity: O(n^2)
    Auxiliary Space: O(n)
    :param arr:
    :return:
    """
    n = len(arr)

    # allocate memory for LIS[] and initialize LIS values as 1
    # for all indexes
    lis = [1] * n

    # Compute LIS values from left to right
    for i in range(1, n):
        for j in range(0, i):
            if (arr[i] > arr[j]) and (lis[i] < lis[j] + 1):
                lis[i] = lis[j] + 1

    # allocate memory for LDS and initialize LDS values for
    # all indexes
    lds = [1] * n

    # Compute LDS values from right to left
    for i in range(n - 1, -1, -1):  # loop from n-2 down to 0
        for j in reversed(range(i - 1, n)):  # loop from n-1 down to i-1
            if arr[i] > arr[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1

    # Return the maximum value of (lis[i] + lds[i] - 1)
    maximum = lis[0] + lds[0] - 1
    for i in range(1, n):
        maximum = max((lis[i] + lds[i] - 1), maximum)

    return maximum


if __name__ == '__main__':
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print("Length of LBS is", lbs(arr))