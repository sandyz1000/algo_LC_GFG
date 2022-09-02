"""
Maximize sum of consecutive differences in a circular array
Given an array of n elements. Consider array as circular array i.e element after an is a1. The
task is to find maximum sum of the difference between consecutive elements with rearrangement of
array element allowed i.e after rearrangement of element
find |a1 - a2| + |a2 - a3| + .... + |(an - 1) - an| + |an - a1|.

---------------------------------------
Examples:
---------------------------------------
Input : arr[] = { 4, 2, 1, 8 }
Output : 18
Rearrange given array as : { 1, 8, 2, 4 }
Sum of difference between consecutive element
= |1 - 8| + |8 - 2| + |2 - 4| + |4 - 1|
= 7 + 6 + 2 + 3
= 18.

Input : arr[] = { 10, 12, 15 }
Output : 10

---------------------------------------
Explanation:
---------------------------------------
The idea is to use Greedy Approach and try to bring elements having greater difference closer.
Consider the sorted permutation of the given array a1, a1, a2,..., an - 1, an such that
a(1) < a(2) < a(3).... < a(n - 1) < a(n).
Now, to obtain the answer having maximum sum of difference between consecutive element, arrange
element in following manner:
a(1), a(n), a(2), a(n-1), ... , a(n/2), a(n/2) + 1
We can observe that the arrangement produces the optimal answer, as all a1, a2, a3,...., a(n/2)-1,
a(n/2) are subtracted twice while a(n/2)+1, a(n/2)+2, a(n/2)+3,...., a(n) - 1, an are added twice.

"""
from __future__ import print_function


# Python program to maximize the sum of difference between consecutive elements in circular array


def max_sum(arr, n):
    """Return the maximum Sum of difference between consecutive elements."""
    summation = 0
    # Sorting the array.
    arr.sort()
    # Subtracting a1, a2, a3,....., a(n/2)-1, a(n/2) twice and adding a(n/2)+1, a(n/2)+2, a(n/2)+3,
    #  .... , a(n) - 1, an twice.
    for i in range(n // 2):
        summation -= (2 * arr[i])
        summation += (2 * arr[n - i - 1])

    return summation


if __name__ == '__main__':
    # Output: 18
    arr = [4, 2, 1, 8]
    n = len(arr)
    print(max_sum(arr, n))
