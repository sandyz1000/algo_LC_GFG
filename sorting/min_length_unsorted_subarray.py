"""
Find the Minimum length Unsorted Subarray, sorting which makes the complete array sorted
Given an unsorted array arr[0..n-1] of size n, find the minimum length subarray arr[s..e] such that 
sorting this subarray makes the whole array sorted.

---------------------------------
Examples:
---------------------------------
1) If the input array is [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60], your program should be able 
to find that the subarray lies between the indexes 3 and 8.
2) If the input array is [0, 1, 15, 25, 6, 7, 30, 40, 50], your program should be able to find that 
the subarray lies between the indexes 2 and 5.

"""

from __future__ import print_function


def print_unsorted(arr, n):
    """Time Complexity: O(n)"""
    s, e, i = 0, n - 1, 0
    # step 1(a) of above algo
    for s in range(n - 1):
        if arr[s] > arr[s + 1]:
            break

    if s == n - 1:
        print("The complete array is sorted")
        return

    # step 1(b) of above algorithm
    for e in range(n - 1, 0, -1):
        if arr[e] < arr[e - 1]:
            break

    # step 2(a) of above algo
    maximum = arr[s]
    minimum = arr[s]
    for i in range(s + 1, e + 1):
        if arr[i] > maximum:
            maximum = arr[i]

        if arr[i] < minimum:
            minimum = arr[i]

    # step 2(b) of above algo
    for i in range(s):
        if arr[i] > minimum:
            s = i
            break

    # step 2(c) of above algo
    for i in range(n - 1, e + 2, -1):
        if arr[i] < maximum:
            e = i
            break

    # step 3 of above algo
    print("The unsorted subarray which makes the given array sorted lies "
          "between the indexes %d and %d" % (s, e))
    return


if __name__ == '__main__':
    arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
    arr_size = len(arr)
    print_unsorted(arr, arr_size)
