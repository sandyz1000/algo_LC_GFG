"""
Write a program to reverse an array or string
We are given an array (or string), the task is to reverse the array.

Examples:
---------------
Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}


"""
from __future__ import print_function


def reverse_list(A, start, end):
    """Iterative python program to reverse an array
    Function to reverse A[] from start to end
    Time Complexity: O(n)"""
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1


def reverse_list_rec(A, start, end):
    """
    Recursive python program to reverse an array
    Function to reverse A[] from start to end
    """
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverse_list_rec(A, start + 1, end - 1)


if __name__ == '__main__':
    # Output: [6, 5, 4, 3, 2, 1]
    A = [1, 2, 3, 4, 5, 6]
    print(A)
    reverse_list(A, 0, 5)
    print("Reversed list is")
    print(A)