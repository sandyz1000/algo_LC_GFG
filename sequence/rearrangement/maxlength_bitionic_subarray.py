"""
Maximum Length Bitonic Subarray | Set 1 (O(n) tine and O(n) space)

Given an array A[0 ... n-1] containing n positive integers, a subarray A[i ... j] is bitonic if
there is a k with i <= k <= j such that A[i] <= A[i + 1] ... <= A[k] >= A[k + 1] >= .. A[j - 1] >
= A[j]. Write a function that takes an array as argument and returns the length of the maximum
length bitonic subarray.

Expected time complexity of the solution is O(n)

---------------------------------------
Simple Examples:
---------------------------------------
1) A[] = {12, 4, 78, 90, 45, 23}, the maximum length bitonic subarray is {4, 78, 90, 45, 23} which
is of length 5.
2) A[] = {20, 4, 1, 2, 3, 4, 2, 10}, the maximum length bitonic subarray is {1, 2, 3, 4, 2} which
is of length 5.

---------------------------------------
Extreme Examples:
---------------------------------------
1) A[] = {10}, the single element is bitnoic, so output is 1.
2) A[] = {10, 20, 30, 40}, the complete array itself is bitonic, so output is 4.
3) A[] = {40, 30, 20, 10}, the complete array itself is bitonic, so output is 4.

---------------------------------------
Solution:
---------------------------------------
Let us consider the array {12, 4, 78, 90, 45, 23} to understand the solution.
1) Construct an auxiliary array inc[] from left to right such that inc[i] contains length of the
non-decreasing sub-array ending at arr[i].
For for A[] = {12, 4, 78, 90, 45, 23}, inc[] is {1, 1, 2, 3, 1, 1}

2) Construct another array dec[] from right to left such that dec[i] contains length of
non-increasing sub-array starting at arr[i].
For A[] = {12, 4, 78, 90, 45, 23}, dec[] is {2, 1, 1, 3, 2, 1}.

3) Once we have the inc[] and dec[] arrays, all we need to do is find the maximum value of
(inc[i] + dec[i] - 1).
For {12, 4, 78, 90, 45, 23}, the max value of (inc[i] + dec[i] - 1) is 5 for i = 3.

Time Complexity: O(n)
Auxiliary Space: O(n)

==================================================================
Maximum Length Bitonic Subarray | Set 2 (O(n) time and O(1) Space)

Given an array A[0 … n-1] containing n positive integers, a subarray A[i … j] is bitonic if there
is a k with i <= k <= j such that A[i] <= A[i + 1] ... <= A[k] >= A[k + 1] >= .. A[j – 1] > = A[
j]. Write a function that takes an array as argument and returns the length of the maximum length
bitonic subarray.

In this set, we will discuss solution taking constant extra space.

The idea is to check longest bitonic subarray starting at A[i]. From A[i], first we will check
for end of ascent and then end of descent.Overlapping of bitonic subarrays is taken into account
by recording a nextStart position when it finds two equal values when going down the slope of the
current subarray. If length of this subarray is greater than max_len, we will update max_len. We
continue this process till end of array is reached.

"""
from __future__ import print_function


# Python program to find length of the longest bitonic subarray

def bitonic(arr, n):
    # Length of increasing subarray ending at all indexes
    inc = [0] * n
    # Length of decreasing subarray starting at all indexes
    dec = [0] * n
    # length of increasing sequence ending at first index is 1
    inc[0] = 1
    # length of increasing sequence starting at first index is 1
    dec[n - 1] = 1

    # Step 1) Construct increasing sequence array
    for i in range(1, n):
        inc[i] = inc[i - 1] + 1 if arr[i] >= arr[i - 1] else 1

    # Step 2) Construct decreasing sequence array
    for i in range(n - 2, -1, -1):
        dec[i] = dec[i + 1] + 1 if arr[i] >= arr[i + 1] else 1

    # Step 3) Find the length of maximum length bitonic sequence
    maxi = inc[0] + dec[0] - 1
    for i in range(1, n):
        if inc[i] + dec[i] - 1 > maxi:
            maxi = inc[i] + dec[i] - 1

    return maxi


def maxLenBitonic(A, n):
    """ Maximum Length Bitonic Subarray | Set 2 (O(n) time and O(1) Space) """
    if n == 0:  # if A is empty
        return 0

    #  initializing max_len
    maxLen = 1
    start = 0
    nextStart = 0
    j = 0

    while j < n - 1:
        #  look for end of ascent
        while j < n - 1 and A[j] <= A[j + 1]:
            j += 1

        #  look for end of descent
        while j < n - 1 and A[j] >= A[j + 1]:
            # adjusting nextStart this will be necessarily executed at least once, when we detect
            # the start of the descent
            if j < n - 1 and A[j] > A[j + 1]:
                nextStart = j + 1
            j += 1

        #  updating maxLen, if required
        maxLen = max(maxLen, j - (start - 1))
        start = nextStart
    return maxLen


if __name__ == '__main__':
    # Output: Length of max length Bitnoic Subarray is  5
    arr = [12, 4, 78, 90, 45, 23]
    # arr = [10, 20, 30, 40]
    # arr = [40, 30, 20, 10]
    n = len(arr)
    print("Length of max length Bitnoic Subarray is ", bitonic(arr, n))
    print("Length of max length Bitnoic Subarray is ", maxLenBitonic(arr, n))
