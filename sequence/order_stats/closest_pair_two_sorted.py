"""
Find the closest pair from two sorted arrays
Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair
has an element from each array.

We are given two arrays ar1[0..m-1] and ar2[0..n-1] and a number x, we need to
find the pair ar1[i] + ar2[j] such that absolute value of (ar1[i] + ar2[j] - x) is minimum.

------------------------------------
Example:
------------------------------------

Input:  ar1 = [1, 4, 5, 7]
        ar2 = [10, 20, 30, 40]
        x = 32
Output: 1 and 30

Input:  ar1 = [1, 4, 5, 7]
        ar2 = [10, 20, 30, 40]
        x = 50
Output: 7 and 40

Python program to find the pair from two sorted arrays such that the sum of pair is closest to
a given number x

ar1[0..m-1] and ar2[0..n-1] are two given sorted arrays and x is given number. This function
prints the pair from both arrays such that the sum of the pair is closest to x.

"""

import sys

INT_MAX = sys.maxsize


def print_closest(ar1, ar2, m, n, x):
    """
    A Simple Solution is to run two loops. The outer loop considers every element of first array
    and inner loop checks for the pair in second array. We keep track of minimum difference
    between ar1[i] + ar2[j] and x.

    We can do it in O(n) time using following steps.

    1) Merge given two arrays into an auxiliary array of size m+n using merge process of merge
    sort. While merging keep another boolean array of size m+n to indicate whether the current
    element in merged array is from ar1[] or ar2[].

    2) Consider the merged array and use the linear time algorithm to find the pair with sum
    closest to x. One extra thing we need to consider only those pairs which have one element
    from ar1[] and other from ar2[], we use the boolean array for this purpose.

    Can we do it in a single pass and O(1) extra space?
    The idea is to start from left side of one array and right side of another array, and use
    the algorithm same as step 2 of above approach.

    --------------------------------------------------------
    Following is detailed algorithm.
    --------------------------------------------------------

    1) Initialize a variable diff as infinite (Diff is used to store the difference between pair
    and x). We need to find the minimum diff.

    2) Initialize two index variables l and r in the given sorted array.
        (a) Initialize first to the leftmost index in ar1:  l = 0
        (b) Initialize second  the rightmost index in ar2:  r = n-1
    3) Loop while l < m and r >= 0
        (a) If  abs(ar1[l] + ar2[r] - sum) < diff  then update diff and result
        (b) Else if(ar1[l] + ar2[r] <  sum )  then l++
        (c) Else r--
    4) Print the result.

    :param ar1: List[int]
    :param ar2: List[int]
    :param m: int
    :param n: int
    :param x: int
    :return:
    """
    # Initialize the diff between pair sum and x.
    diff = INT_MAX
    # res_l and res_r are result indexes from ar1[] and ar2[] respectively
    res_l, res_r = 0, 0

    # Start from left side of ar1[] and right side of ar2[]
    l, r = 0, n - 1
    while l < m and r >= 0:
        # If this pair is closer to x than the previously found closest, then update res_l,
        # res_r and diff
        if abs(ar1[l] + ar2[r] - x) < diff:
            res_l = l
            res_r = r
            diff = abs(ar1[l] + ar2[r] - x)

        # If sum of this pair is more than x, move to smaller side
        if ar1[l] + ar2[r] > x:
            r -= 1
        # move to the greater side
        else:
            l += 1

    # Print the result
    print("The closest pair is [{0}, {1}] \n".format(ar1[res_l], ar2[res_r]))


if __name__ == '__main__':
    ar1 = [1, 4, 5, 7]
    ar2 = [10, 20, 30, 40]
    m = len(ar1)
    n = len(ar2)
    x = 38
    print_closest(ar1, ar2, m, n, x)
