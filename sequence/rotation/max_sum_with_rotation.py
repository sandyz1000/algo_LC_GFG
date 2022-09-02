"""
Problem 1:
Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed

Given an array, only rotation operation is allowed on array. We can rotate the array as many times
as we want. Return the maximum possible of summation of i*arr[i].

Examples:

Input: arr[] = {1, 20, 2, 10}
Output: 72
We can get 72 by rotating array twice.
{2, 10, 1, 20}
20*3 + 1*2 + 10*1 + 2*0 = 72

Input: arr[] = {10, 1, 2, 3, 4, 5, 6, 7, 8, 9};
Output: 330
We can 330 by rotating array 9 times.
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
0*1 + 1*2 + 2*3 ... 9*10 = 330

Problem 2:

Given an array arr[] of n integers, find the maximum that maximizes sum of value of i*arr[i]
where i varies from 0 to n-1.

Algorithm:
The idea is to compute value of a rotation using value of previous rotation. When we rotate an
array by one, following changes happen in sum of i*arr[i].
1)  Multiplier of arr[i-1] changes from 0 to n-1, i.e., arr[i-1] * (n-1) is added to current
    value.

2)  Multipliers of other terms is decremented by 1. i.e., (cum_sum - arr[i-1]) is subtracted from
    current value where cum_sum is sum of all numbers.

Examples:

Input : arr[] = {8, 3, 1, 2}
Output : 29
Explanation : Let us see all rotations
{8, 3, 1, 2} = 8*0 + 3*1 + 1*2 + 2*3 = 11
{3, 1, 2, 8} = 3*0 + 1*1 + 2*2 + 8*3 = 29
{1, 2, 8, 3} = 1*0 + 2*1 + 8*2 + 3*3 = 27
{2, 8, 3, 1} = 2*0 + 8*1 + 3*2 + 1*1 = 17

Input : arr[] = {3, 2, 1}
Output : 8

"""
from __future__ import print_function


def max_sum_p1(arr):
    """
    A Simple Solution is to find all rotations one by one, check sum of every rotation and return
    the maximum sum. Time complexity of this solution is O(n^2).

    We can solve this problem in O(n) time using an Efficient Solution.

    Let Rj be value of i*arr[i] with j rotations. The idea is to calculate next rotation value
    from previous rotation, i.e., calculate Rj from Rj-1. We can calculate initial value of
    result as R0, then keep calculating next rotation values.

    How to efficiently calculate Rj from Rj-1?
    This can be done in O(1) time. Below are details.

    Let us calculate initial value of i*arr[i] with no rotation
    R0 = 0*arr[0] + 1*arr[1] +...+ (n-1)*arr[n-1]

    After 1 rotation arr[n-1], becomes first element of array, arr[0] becomes second element,
    arr[1] becomes third element and so on.

    R1 = 0*arr[n-1] + 1*arr[0] +...+ (n-1)*arr[n-2]
    R1 - R0 = arr[0] + arr[1] + ... + arr[n-2] - (n-1)*arr[n-1]

    After 2 rotations arr[n-2], becomes first element of previous array, arr[n-1] becomes
    second element, arr[0] becomes third element and so on.

    R2 = 0*arr[n-2] + 1*arr[n-1] +...+ (n-1)*arr[n-3]
    R2 - R1 = arr[0] + arr[1] + ... + arr[n-3] - (n-1)*arr[n-2] + arr[n-1]

    If we take a closer look at above values, we can observe below pattern

    Rj - Rj-1 = arrSum - n * arr[n-j]

    Where arrSum is sum of all array elements, i.e.,

    arrSum = sum( arr[i] )
            i<=0<=n-1

    Python program to find maximum value of Sum(i*arr[i])
    Time Complexity: O(n)
    Auxiliary Space: O(1)
    :param arr:
    :return:
    """
    arr_sum = 0  # stores sum of arr[i]
    curr_val = 0  # stores sum of i*arr[i]
    n = len(arr)
    for i in range(0, n):
        arr_sum += arr[i]
        curr_val += (i * arr[i])
    max_val = curr_val  # initialize result

    # try all rotations one by one and find the maximum rotation sum
    for j in range(1, n):
        curr_val = curr_val + arr_sum - n * arr[n - j]
        if curr_val > max_val:
            max_val = curr_val

    # return result
    return max_val


def max_sum_p2(arr, n):
    """
    An efficient C++ program to compute maximum sum of i*arr[i]
    :param arr: list(int)
    :param n: int
    :return:
    """
    # Compute sum of all array elements
    cum_sum = sum(arr)

    # Compute sum of i*arr[i] for initial configuration.
    curr_val = 0
    for i in range(n):
        curr_val += i*arr[i]

    res = curr_val  # Initialize result

    # Compute values for other iterations
    for i in range(1, n):
        # Compute next value using previous value in O(1) time
        next_val = curr_val - (cum_sum - arr[i-1]) + arr[i-1] * (n-1)

        # Update current value
        curr_val = next_val

        # Update result if required
        res = max(res, next_val)

    return res


if __name__ == '__main__':
    # Problem: 1  Max sum is:  330
    arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Max sum is: ", max_sum_p1(arr))

    # Problem: 2  Max sum is:  29
    arr = [8, 3, 1, 2]
    n = len(arr)
    print("Max sum is: ", max_sum_p2(arr, n))