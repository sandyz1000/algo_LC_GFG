"""Find median in row wise sorted matrix

We are given a row wise sorted matrix of size r*c, we need to find the median of the matrix given.
It is assumed that r*c is always odd.

----------------------------------------
Examples:
----------------------------------------
Input : 1 3 5
        2 6 9
        3 6 9
Output : Median is 5
If we put all the values in a sorted
array A[] = 1 2 3 3 5 6 6 9 9)

Input: 1 3 4
       2 5 6
       7 8 9
Output: Median is 5

----------------------------------------
Simple Method:
----------------------------------------
The simplest method to solve this problem is to store all the elements of the given
matrix in an array of size r*c. Then find the median element in this array.This seems to be the
simplest method but it would take extra memory.

Time Complexity = O(r*c)
Auxiliary Space = O(r*c)

----------------------------------------
Method-2
----------------------------------------
An efficient approach for this problem is to use binary search algorithm. The idea is that for a
number to be median there should be exactly (n/2) numbers which are less than this number. So,
we try to find the count of numbers less than all the numbers. Below is the step by step
algorithm for this approach:

----------------------------------------
Algorithm:
----------------------------------------
1.  First we find the minimum and maximum elements in the matrix. Minimum element can be easily
    found by comparing the first element of each row, and similarly the maximum element can be
    found by comparing the last element of each row.
2.  Then we use binary search on our range of numbers from minimum to maximum, we find the mid of
    the min and max, and get count of numbers less than our mid. And accordingly change the min or
    max.
3.  For a number to be median, there should be (r*c)/2 numbers smaller than that number. So for
    every number, we get the count of numbers less than that by using upper_bound() in each row of
    matrix, if it is less than the required count, the median must be greater than the selected
    number, else the median must be less than or equal to the selected number.
"""

from __future__ import print_function
from bisect import bisect_right as upper_bound

# Python program to find median of matrix sorted row wise
MAX = 100


def binary_median(m, r, c):
    """Function to find median in the matrix"""
    mi = m[0][0]
    mx = 0
    for i in range(r):
        if m[i][0] < mi:
            mi = m[i][0]
        if m[i][c - 1] > mx:
            mx = m[i][c - 1]

    desired = (r * c + 1) // 2

    while mi < mx:
        mid = mi + (mx - mi) // 2
        place = [0]

        # Find count of elements smaller than mid
        for i in range(r):
            j = upper_bound(m[i], mid)
            place[0] = place[0] + j
        if place[0] < desired:
            mi = mid + 1
        else:
            mx = mid
    print("Median is", mi)
    return


if __name__ == '__main__':
    # Time Complexity: O(32 * r * log(c)). The upper bound function will take log(c) time and is
    # performed for each row. And since the numbers will be max of 32 bit, so binary search of
    # numbers from min to max will be performed in at most 32 ( log2(2^32) = 32 ) operations.
    # Auxiliary Space : O(1)

    r = 3
    c = 3
    m = [[1, 3, 5],
         [2, 6, 9],
         [3, 6, 9]]
    binary_median(m, r, c)
