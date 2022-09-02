"""
Maximum circular subarray sum
Given n numbers (both +ve and -ve), arranged in a circle, find the maximum sum of consecutive
number.

------------------------------------------------
Examples:
------------------------------------------------
Input: a[] = {8, -8, 9, -9, 10, -11, 12}
Output: 22 (12 + 8 - 8 + 9 - 9 + 10)

Input: a[] = {10, -3, -4, 7, 6, 5, -4, -1}
Output:  23 (7 + 6 + 5 - 4 -1 + 10)

Input: a[] = {-1, 40, -14, 7, 6, 5, -4, -1}
Output: 52 (7 + 6 + 5 - 4 - 1 - 1 + 40)

------------------------------------------------
Explanation:
------------------------------------------------

Simple idea of the Kadane's algorithm is to look for all positive contiguous segments of the
array (max_ending_here is used for this). And keep track of maximum sum contiguous segment
among all positive segments (max_so_far is used for this). Each time we get a positive sum
compare it with max_so_far and update max_so_far if it is greater than max_so_far

Lets take the example:
{-2, -3, 4, -1, -2, 1, 5, -3}

max_so_far = max_ending_here = 0

for i=0,  a[0] =  -2
max_ending_here = max_ending_here + (-2)
Set max_ending_here = 0 because max_ending_here < 0

for i=1,  a[1] =  -3
max_ending_here = max_ending_here + (-3)
Set max_ending_here = 0 because max_ending_here < 0

for i=2,  a[2] =  4
max_ending_here = max_ending_here + (4)
max_ending_here = 4
max_so_far is updated to 4 because max_ending_here greater
than max_so_far which was 0 till now

for i=3,  a[3] =  -1
max_ending_here = max_ending_here + (-1)
max_ending_here = 3

for i=4,  a[4] =  -2
max_ending_here = max_ending_here + (-2)
max_ending_here = 1

for i=5,  a[5] =  1
max_ending_here = max_ending_here + (1)
max_ending_here = 2

for i=6,  a[6] =  5
max_ending_here = max_ending_here + (5)
max_ending_here = 7
max_so_far is updated to 7 because max_ending_here is
greater than max_so_far

for i=7,  a[7] =  -3
max_ending_here = max_ending_here + (-3)
max_ending_here = 4


There can be two cases for the maximum sum:

Case 1: The elements that contribute to the maximum sum are arranged such that no wrapping is
there. Examples: {-10, 2, -1, 5}, {-2, 4, -1, 4, -1}. In this case, Kadane's algorithm will
produce the result.

Case 2: The elements which contribute to the maximum sum are arranged such that wrapping is
there. Examples: {10, -12, 11}, {12, -5, 4, -8, 11}. In this case, we change wrapping to
non-wrapping. Let us see how. Wrapping of contributing elements implies non wrapping of non
contributing elements, so find out the sum of non contributing elements and subtract this sum
from the total sum. To find out the sum of non contributing, invert sign of each element and then
run Kadane's algorithm.

Our array is like a ring and we have to eliminate the maximum continuous negative that implies
maximum continuous positive in the inverted arrays.

Finally we compare the sum obtained by both cases, and return the maximum of the two sums.
"""


# Python program for maximum contiguous circular sum problem
# Time Complexity: O(n) where n is the number of elements in input array.

def kadane(a):
    """
    Standard Kadane's algorithm to find maximum subarray sum
    """
    n = len(a)
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, n):
        max_ending_here = max_ending_here + a[i]

        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far


def max_circular_sum(a):
    """The function returns maximum circular contiguous sum in a[]
    """
    n = len(a)

    # Case 1: get the maximum sum using standard kadane's algorithm
    max_kadane = kadane(a)

    # Case 2: Now find the maximum sum that includes corner elements.
    max_wrap = 0
    for i in range(0, n):
        max_wrap += a[i]
        a[i] = -a[i]

    # Max sum with corner elements will be: array-sum - (-max subarray sum of inverted array)
    max_wrap = max_wrap + kadane(a)

    # The maximum circular sum will be maximum of two sums
    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane


if __name__ == '__main__':
    # Maximum circular sum is 31
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print("Maximum contiguous sum is", kadane(arr))

    # a = [11, 10, -20, 5, -3, -5, 8, -13, 10]
    # print("Maximum circular sum is", max_circular_sum(a))
