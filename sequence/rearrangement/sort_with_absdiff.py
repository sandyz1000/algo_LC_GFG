"""
Sort an array according to absolute difference with given value
Given an array of n distinct elements and a number x, arrange array elements according to the
absolute difference with x, i. e., element having minimum difference comes first and so on.
Note : If two or more elements are at equal distance arrange them in same sequence as in the
given array.

------------------------------------
Examples :
------------------------------------
Input : arr[] : x = 7, arr[] = {10, 5, 3, 9, 2}
Output : arr[] = {5, 9, 10, 3, 2}
Explanation:
7 - 10 = 3(abs)
7 - 5 = 2
7 - 3 = 4
7 - 9 = 2(abs)
7 - 2 = 5

So according to the difference with X, elements are arranged as 5, 9, 10, 3, 2.

Input : x = 6, arr[] = {1, 2, 3, 4, 5}
Output :  arr[] = {5, 4, 3, 2, 1}

Input : x = 5, arr[] = {2, 6, 8, 3}
Output :  arr[] = {6, 3, 2, 8}

------------------------------------
Explanation:
------------------------------------
The idea is to use a self balancing binary search tree. We traverse input array and for every
element, we find its difference with x and store the difference as key and element as value in
self balancing binary search tree. Finally we traverse the tree and print its inorder traversal
which is required output.

Time Complexity : O(n Log n)
Auxiliary Space : O(n)

It can also be done with compare and swap method
"""

from functools import cmp_to_key

# Python program to sort an array according absolute difference with x.


class Pair:
    def __init__(self) -> None:
        self.first, self.second = None, None


def rearrange(arr, n, x):
    """Function to sort an array according absolute difference with x."""
    # Store values in a map with the difference with X as key
    m = [Pair(abs(x - arr[i]), arr[i]) for i in range(n)]
    m.sort(key=cmp_to_key(lambda a, b: a.first - b.first))

    i = 0  # Update the values of array
    for item in m:
        arr[i] = item.second
        i += 1


if __name__ == '__main__':
    # Output: 5 9 10 3 2
    arr = [10, 5, 3, 9, 2]
    n = len(arr)
    x = 7
    rearrange(arr, n, x)
    print(arr)