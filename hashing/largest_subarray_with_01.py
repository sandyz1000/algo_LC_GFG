"""
Largest subarray with equal number of 0s and 1s

Given an array containing only 0s and 1s, find the largest sub-array which contain equal no of 0s
and 1s. Expected time complexity is O(n).

- - - - - - - - - - - - - - - - - - - - - - - -
Examples:
- - - - - - - - - - - - - - - - - - - - - - - -

Input: arr[] = {1, 0, 1, 1, 1, 0, 0}
Output: 1 to 6 (Starting and Ending indexes of output subarray)

Input: arr[] = {1, 1, 1, 1}
Output: No such subarray

Input: arr[] = {0, 0, 1, 1, 0}
Output: 0 to 3 Or 1 to 4
"""
from __future__ import print_function


class LargestSubArray(object):
    """
    Method 1 (Simple)
    A simple method is to use two nested loops. The outer loop picks a starting point i. The inner
    loop considers all subarrays starting from i. If size of a subarray is greater than maximum
    size so far, then update the maximum size.
    In the below code, 0s are considered as -1 and sum of all values from i to j is calculated. If
    sum becomes 0, then size of this subarray is compared with largest size so far.

    """

    def find_sub_array(self, arr, n):
        """
        This function Prints the starting and ending indexes of the largest subarray with equal
        number of 0s and 1s. Also returns the size of such subarray.
        """
        maxsize, start_index, end_index = -1, 0, 0

        for i in range(n - 1):
            summation = -1 if (arr[i] == 0) else 1
            # Consider all subarrays starting from i
            for j in range(i + 1, n):
                if arr[j] == 0:
                    summation += -1
                else:
                    summation += 1

                # If this is a 0 sum subarray, then compare it with maximum size
                # sub-array calculated so far
                if summation == 0 and maxsize < j - i + 1:
                    maxsize = j - i + 1
                    start_index = i

        end_index = start_index + maxsize - 1
        if maxsize == -1:
            print("No such subarray")
        else:
            print("%d to %d" % (start_index, end_index))
        return maxsize


class LargestSubArray1:
    """
    ==Method 2 (Tricky)==

    Following is a solution that uses O(n) extra space and solves the problem in O(n) time
    complexity. Let input array be arr[] of size n and maxsize be the size of output subarray.

    1) Consider all 0 values as -1. The problem now reduces to find out the maximum length subarray
    with sum = 0.

    2) Create a temporary array sumleft[] of size n. Store the sum of all elements from arr[0] to
    arr[i] in sumleft[i]. This can be done in O(n) time.

    3) There are two cases, the output subarray may start from 0th index or may start from some
    other index. We will return the max of the values obtained by two cases.

    4) To find the maximum length subarray starting from 0th index, scan the sumleft[] and find the
    maximum i where sumleft[i] = 0.

    5) Now, we need to find the subarray where subarray sum is 0 and start index is not 0. This
    problem is equivalent to finding two indexes i & j in sumleft[] such that sumleft[i] =
    sumleft[j] and j-i is maximum. To solve this, we can create a hash table with size =
    max-min+1 where min is the minimum value in the sumleft[] and max is the maximum value in the
    sumleft[]. The idea is to hash the leftmost occurrences of all different values in sumleft[].
    The size of hash is chosen as max-min+1 because there can be these many different possible
    values in sumleft[]. Initialize all values in hash as -1

    6) To fill and use hash[], traverse sumleft[] from 0 to n-1. If a value is not present in hash[
    ], then store its index in hash. If the value is present, then calculate the difference of
    current index of sumleft[] and previously stored value in hash[]. If this difference is more
    than maxsize, then update the maxsize.

    7) To handle corner cases (all 1s and all 0s), we initialize maxsize as -1. If the maxsize
    remains -1, then print there is no such subarray.

    """
    def maxLen(self, arr, n):
        """Returns largest subarray with equal number of 0s and 1s"""
        # Creates an empty hashMap hM
        hM = {}

        summation = 0  # Initialize sum of elements
        max_len = 0  # Initialize result
        ending_index = -1
        for i in range(n):
            arr[i] = -1 if (arr[i] == 0) else 1

        # Traverse through the given array
        for i in range(n):
            # Add current element to sum
            summation += arr[i]

            # To handle sum=0 at last index
            if summation == 0:
                max_len = i + 1
                ending_index = i

            # If this sum is seen before, then update max_len if required
            if summation in hM:
                if max_len < i - hM[summation + n]:
                    max_len = i - hM[summation + n]
                    ending_index = i
            # Else put this sum in hash table
            else:
                hM[summation + n] = i

        for i in range(n):
            arr[i] = 0 if (arr[i] == -1) else 1

        end = ending_index - max_len + 1
        print("%d to %d" % (end, ending_index))
        return max_len


if __name__ == '__main__':
    # Output: 0 to 5
    # Time Complexity: O(n^2)
    # Auxiliary Space: O(1)
    print("\nMethod-1    ")
    sub = LargestSubArray()
    arr = [1, 0, 0, 1, 0, 1, 1]
    size = len(arr)
    sub.find_sub_array(arr, size)

    # Output: 0 to 5
    # Time Complexity: O(n)
    # Auxiliary Space: O(n)
    print("\nMethod-2    ")
    sub = LargestSubArray1()
    arr = [1, 0, 0, 1, 0, 1, 1]
    n = len(arr)
    sub.maxLen(arr, n)
