"""
Three way partitioning of an array around a given range
Given an array and a range [lowVal, highVal], partition the array around the range such that array
is divided in three parts.
1) All elements smaller than lowVal come first.
2) All elements in range lowVal to highVVal come next.
3) All elements greater than highVVal appear in the end.
The individual elements of three sets can appear in any order.

Examples:
---------------
Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32}
        lowVal = 14, highVal = 20
Output: arr[] = {1, 5, 4, 2, 1, 3, 14, 20, 20, 98, 87, 32, 54}

Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32}
       lowVal = 20, highVal = 20
Output: arr[] = {1, 14, 5, 4, 2, 1, 3, 20, 20, 98, 87, 32, 54}

Explanation:
---------------
A simple solution is to sort the array. This solution does a lot of extra rearrangements and
requires O(n Log n) time.
An efficient solution is based on Dutch National Flag based QuickSort. We traverse given array
elements from left. We keep track of two pointers, first (called start in below code) to store
next position of smaller element (smaller than range) from beginning; and second (called end in
below code) to store next position of greater element from end.

Time Complexity : O(n)
Auxiliary Space : O(1)

"""
import typing

# Python program to implement three way partitioning around a given range.


def three_way_partition(arr: typing.List[int], n: int,
                        low_val: int, high_val: int):
    """Partitions arr[0..n-1] around [lowVal..highVal]"""
    # Initialize ext available positions for smaller (than range) and greater elements
    i, start, end = 0, 0, n - 1

    # Traverse elements from left
    while i < end:
        # If current element is smaller than range, put it on next available smaller position.
        if arr[i] < low_val:
            arr[i], arr[start] = arr[start], arr[i]
            i += 1
            start += 1
        # If current element is greater than range, put it on next available greater position.
        elif arr[i] > high_val:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        else:
            i += 1


if __name__ == '__main__':
    # Output: Modified array 1 5 4 2 1 3 14 20 20 98 87 32 54
    arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
    n = len(arr)

    three_way_partition(arr, n, 10, 20)
    print("Modified array \n", arr)
