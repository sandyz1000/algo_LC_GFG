"""
Print left rotation of array in O(n) time and O(1) space

Given an array of size n and multiple values around which we need to left rotate the array.
How to quickly find multiple left rotations?

Input : arr = [1, 3, 5, 7, 9], k1 = 4
Output : 9 1 3 5 7

Note that the task to find starting address of rotation takes O(1) time.
It is printing the elements that takes O(n) time.
"""
import typing


def preprocess(arr: typing.List[int], n: int, temp: int):
    """
    Fills temp[] with two copies of arr[]
    :param arr:
    :param n:
    :param temp:
    :return:
    """
    # Store arr[] elements at i and i + n
    for i in range(n):
        temp[i] = temp[i + n] = arr[i]


def left_rotate(n, k, temp):
    """
    Function to left rotate an array k times
    :param n: int
    :param k: int
    :param temp: List[int]
    :return:
    """
    # Starting position of array after k rotations in temp[] will be k % n
    start = k % n
    # Print array after k rotations
    print(temp[start:start + n])


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    n = len(arr)

    temp = [0] * (2 * n)
    preprocess(arr, n, temp)

    # [5, 7, 9, 1, 3]
    k = 2
    left_rotate(n, k, temp)

    # [7, 9, 1, 3, 5]
    k = 3
    left_rotate(n, k, temp)

    # [9, 1, 3, 5, 7]
    k = 4
    left_rotate(n, k, temp)
