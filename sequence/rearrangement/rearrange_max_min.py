"""
Rearrange an array in maximum minimum form | Set 2 (O(1) extra space)
Given a sorted array of positive integers, rearrange the array alternately i.e first element should
be the maximum value, second minimum value, third-second max, fourth-second min and so on.

------------------------------------------------
Examples:
------------------------------------------------
Input  : arr[] = {1, 2, 3, 4, 5, 6, 7}
Output : arr[] = {7, 1, 6, 2, 5, 3, 4}

Input  : arr[] = {1, 2, 3, 4, 5, 6}
Output : arr[] = {6, 1, 5, 2, 4, 3}

------------------------------------------------
Explanation:
------------------------------------------------
In this post a solution that requires O(n) time and O(1) extra space is discussed. The idea is to
use multiplication and modular trick to store two elements at an index.

even index : remaining maximum element.
odd index  : remaining minimum element.

max_index : Index of remaining maximum element (Moves from right to left)
min_index : Index of remaining minimum element (Moves from left to right)

Initialize: max_index = 'n-1'
            min_index = 0
            max_element = arr[max_index] + 1

For i = 0 to n-1
    IF 'i' is even
       arr[i] += arr[max_index] % max_element * max_element
       max_index--
    ELSE # if 'i' is odd
       arr[i] +=  arr[min_index] % max_element * max_element
       min_index++

How does expression "arr[i] += arr[max_index] % max_element * max_element" work ?

The purpose of this expression is to store two elements at index arr[i]. arr[max_index] is stored
as multiplier and "arr[i]" is stored as remainder. For example in {1 2 3 4 5 6 7 8 9}, max_element
is 10 and we store 91 at index 0. With 91, we can get original element as 91%10 and new element as
91/10.

"""
from __future__ import print_function


# Python program to rearrange an array in minimum maximum form
def rearrange(arr, n):
    """
    Prints max at first position, min at second position second max at third position,
    second min at fourth position and so on.
    :param arr:
    :param n:
    :return:
    """
    # initialize index of first minimum and first maximum element
    max_idx, min_idx = n - 1, 0
    # store maximum element of array
    max_elem = arr[n - 1] + 1
    # traverse array elements
    for i in range(n):
        # at even index : we have to put maximum element
        if i % 2 == 0:
            arr[i] += (arr[max_idx] % max_elem) * max_elem
            # arr[i] += (arr[max_idx]) * max_elem
            max_idx -= 1

        else:  # at odd index : we have to put minimum element
            arr[i] += (arr[min_idx] % max_elem) * max_elem
            # arr[i] += (arr[min_idx]) * max_elem
            min_idx += 1

    # array elements back to it's original form
    for i in range(n):
        arr[i] = arr[i] // max_elem


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(arr)

    print("\nOriginal Array\n", arr)
    rearrange(arr, n)
    print("\nModified Array\n", arr)
