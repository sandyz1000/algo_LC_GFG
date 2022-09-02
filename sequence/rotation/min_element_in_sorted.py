"""
Find the minimum element in a sorted and rotated array

A sorted array is rotated at some unknown point, find the minimum element in it.

Input: {5, 6, 1, 2, 3, 4}
Output: 1

How to handle duplicates?
It turned out that duplicates can't be handled in O(Logn) time in all cases.
The special cases that cause problems are like {2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 2} and
{2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2}.
It doesn't look possible to go to left half or right half by doing constant number of comparisons
at the middle. So the problem with repetition can be solved in O(n) worst case. """

import typing


def find_min(arr: typing.List[int], low: int, high: int):
    
    # This condition is needed to handle the case when array is not rotated at all
    if high < low:
        return arr[0]

    # If there is only one element left
    if high == low:
        return arr[low]

    # Find mid
    mid = (low + high) // 2

    # Check if element (mid+1) is minimum element. Consider the cases like [3, 4, 5, 1, 2]
    if mid < high and arr[mid + 1] < arr[mid]:
        return arr[mid + 1]

    # Check if mid itself is minimum element
    if mid > low and arr[mid] < arr[mid - 1]:
        return arr[mid]

    # Decide whether we need to go to left half or right half
    if arr[high] > arr[mid]:
        return find_min(arr, low, mid - 1)
    return find_min(arr, mid + 1, high)


if __name__ == '__main__':
    arr1 = [5, 6, 1, 2, 3, 4]
    n1 = len(arr1)
    print("The minimum element is " + str(find_min(arr1, 0, n1 - 1)))
    #
    # arr2 = [1, 2, 3, 4]
    # n2 = len(arr2)
    # print("The minimum element is " + str(find_min(arr2, 0, n2 - 1)))
    #
    # arr3 = [1]
    # n3 = len(arr3)
    # print("The minimum element is " + str(find_min(arr3, 0, n3 - 1)))
    #
    # arr4 = [1, 2]
    # n4 = len(arr4)
    # print("The minimum element is " + str(find_min(arr4, 0, n4 - 1)))
    #
    # arr5 = [2, 1]
    # n5 = len(arr5)
    # print("The minimum element is " + str(find_min(arr5, 0, n5 - 1)))
    #
    # arr6 = [5, 6, 7, 1, 2, 3, 4]
    # n6 = len(arr6)
    # print("The minimum element is " + str(find_min(arr6, 0, n6 - 1)))
    #
    # arr7 = [1, 2, 3, 4, 5, 6, 7]
    # n7 = len(arr7)
    # print("The minimum element is " + str(find_min(arr7, 0, n7 - 1)))

    arr8 = [2, 3, 4, 5, 6, 7, 8, 1]
    n8 = len(arr8)
    print("The minimum element is " + str(find_min(arr8, 0, n8 - 1)))

    arr9 = [3, 4, 5, 1, 2]
    n9 = len(arr9)
    print("The minimum element is " + str(find_min(arr9, 0, n9 - 1)))
