"""
Divide and Conquer | Set 3 (Maximum Subarray Sum)
You are given a one dimensional array that may contain both positive and negative integers, find
the sum of contiguous subarray of numbers which has the largest sum.

-------------------------------------------
Example:
-------------------------------------------
If the given array is [-2, -5, 6, -2, -3, 1, 5, -6], then the maximum subarray sum is 7
[ 6, -2, -3, 1, 5, ]

Using Divide and Conquer approach, we can find the maximum subarray sum in O(nLogn) time.
Following is the Divide and Conquer algorithm.

1) Divide the given array in two halves
2) Return the maximum of following three
   a) Maximum subarray sum in left half (Make a recursive call)
   b) Maximum subarray sum in right half (Make a recursive call)
   c) Maximum subarray sum such that the subarray crosses the midpoint

The lines 2.a and 2.b are simple recursive calls. How to find maximum subarray sum such that
the subarray crosses the midpoint? We can easily find the crossing sum in linear time. The idea
is simple, find the maximum sum starting from mid point and ending at some point on left of
mid, then find the maximum sum starting from mid + 1 and ending with sum point on right of
mid + 1. Finally, combine the two and return.

Time Complexity: maxSubArraySum() is a recursive method and time complexity can be expressed as
following recurrence relation. T(n) = 2T(n/2) + O(n)
"""
import sys
import typing


# A Divide and Conquer based program for maximum subarray sum problem
INT_MIN = - sys.maxsize


def max_crossing_sum(arr: typing.List[int], low: int, mid: int, high: int):
    """ Find the maximum possible sum in arr[] auch that arr[m] is part of it
    """
    # Include elements on left of mid.
    summation = 0
    left_sum = INT_MIN
    for i in range(mid, low - 1, -1):
        summation += arr[i]
        left_sum = max(summation, left_sum)

    # Include elements on right of mid
    summation = 0
    right_sum = INT_MIN
    for i in range(mid + 1, high + 1):
        summation += arr[i]
        right_sum = max(summation, right_sum)

    # Return sum of elements on left and right of mid
    return left_sum + right_sum


def max_sub_array_sum(arr: typing.List[int], low: int, high: int):
    """
    Returns sum of maxium sum subarray in aa[l..h]
    :param arr: list(int)
    :param l: int
    :param h: int
    :return:
    """
    # Base Case: Only one element
    if low == high:
        return arr[low]
    m = (low + high) // 2  # Find middle point

    # Return maximum of following three possible cases
    # a) Maximum subarray sum in left half
    # b) Maximum subarray sum in right half
    # c) Maximum subarray sum such that the sub-array crosses the midpoint
    return max(max_sub_array_sum(arr, low, m),
               max_sub_array_sum(arr, m + 1, high),
               max_crossing_sum(arr, low, m, high))


if __name__ == '__main__':
    # Output: Maximum contiguous sum is 21
    # arr = [2, 3, 4, 5, 7]
    arr = [-2, -1]
    # arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # arr = [1, 2]
    n = len(arr)
    max_sum = max_sub_array_sum(arr, 0, n - 1)
    print("Maximum contiguous sum is %d" % max_sum)
