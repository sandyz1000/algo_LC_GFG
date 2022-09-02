"""
Largest Sum Contiguous Subarray
Write an efficient program to find the sum of contiguous subarray within a one-dimensional
array of numbers which has the largest sum.

Kadane's Algorithm Explanation:
Simple idea of the Kadane's algorithm is to look for all positive contiguous
segments of the array (max_ending_here is used for this). And keep track of maximum sum
contiguous segment among all positive segments (max_so_far is used for this). Each time we get a
positive sum compare it with max_so_far and update max_so_far if it is greater than max_so_far

Lets take the example:

         -------------------
{-2, -3, | 4, -1, -2, 1, 5 | , -3}
         -------------------

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
max_so_far = 4 because max_ending_here greater
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
max_so_far = 7 because max_ending_here is
greater than max_so_far

for i=7,  a[7] =  -3
max_ending_here = max_ending_here + (-3)
max_ending_here = 4

"""
# Python program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
from sys import maxsize


def max_subarray_sum_v1(a, size):
    """
    Time Complexity: O(n)
    :param a: list
    :param size: int
    :return:
    """
    max_so_far = - maxsize - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here += a[i]
        max_so_far = max(max_ending_here, max_so_far)
        max_ending_here = max(0, max_ending_here)
    return max_so_far


def maxSubArraySum_v2(a, size):
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0
        # Do not compare for all elements. Compare only when max_ending_here > 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far


def max_subarray_sum_dp(a, size):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


def maxSubArraySum(a, size):
    """
    Function to find the maximum contiguous subarray
    and print its starting and end index

    Arguments:
        a {[type]} -- [description]
        size {[type]} -- [description]
    """    
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):
        max_ending_here += a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
    
    print("Maximum contiguous sum is %d" % (max_so_far))
    print("Starting Index %d" % (start))
    print("Ending Index %d" % (end))


if __name__ == '__main__':
    arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print("Maximum contiguous sum is", max_subarray_sum_v1(arr, len(arr)))
    print("Maximum contiguous sum is", max_subarray_sum_dp(arr, len(arr)))

    # Driver program to test maxSubArraySum
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    # maxSubArraySum(a, len(a))
