"""
Count 1's in a sorted binary array

Given a binary array sorted in non-increasing order, count the number of 1's in it.

------------------------------------------
Examples:
------------------------------------------
Input: arr = [1, 1, 0, 0, 0, 0, 0]
Output: 2

Input: arr = [1, 1, 1, 1, 1, 1, 1]
Output: 7

Input: arr = [0, 0, 0, 0, 0, 0, 0]
Output: 0

------------------------------------------
Explanation:
------------------------------------------
A simple solution is to linearly traverse the array. The time complexity of the simple solution
is O(n). We can use Binary Search to find count in O(Logn) time. The idea is to look for last
occurrence of 1 using Binary Search. Once we find the index last occurrence, we return index + 1
as count.

"""

from __future__ import print_function


# Python program to count one's in a boolean array
def count_ones(arr, low, high):
    """
    Returns counts of 1's in arr[low..high]. The array is assumed to be
    sorted in non-increasing order
    :param arr:
    :param low:
    :param high:
    :return:
    """
    if high >= low:
        # get the middle index
        mid = low + (high - low) // 2
        # check if the element at middle index is last 1
        if (mid == high or arr[mid + 1] == 0) and (arr[mid] == 1):
            return mid + 1

        # If element is not last 1, recur for right side
        if arr[mid] == 1:
            return count_ones(arr, (mid + 1), high)

        # else recur for left side
        return count_ones(arr, low, mid - 1)

    return 0


if __name__ == '__main__':
    # Output: Count of 1's in given array is 4
    # Time complexity of the above solution is O(Logn)
    arr = [1, 1, 1, 1, 0, 0, 0]
    print("Count of 1's in given array is", count_ones(arr, 0, len(arr) - 1))
