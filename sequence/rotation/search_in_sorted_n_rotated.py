"""
Search an element in a sorted and rotated array

An element in a sorted array can be found in O(log n) time via binary search. But suppose we
rotate an ascending order sorted array at some pivot unknown to you beforehand. So for instance,
1 2 3 4 5 might become 3 4 5 1 2.

Devise a way to find an element in the rotated array in O(logn) time.

Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
         key = 3
Output : Found at index 8

------------------------------------
Explanation:
------------------------------------
All solutions provided here assume that all elements in array are distinct.

The idea is to find the pivot point, divide the array in two sub-arrays and call binary
search. The main idea for finding pivot is - for a sorted (in increasing order) and pivoted
array, pivot element is the only element for which next element to it is smaller than it.
Using above criteria and binary search methodology we can get pivot element in O(logn) time

Input arr = [3, 4, 5, 1, 2]
Element to Search = 1
1) Find out pivot point and divide the array in two sub-arrays. (pivot = 2) # Index of 5
2) Now call binary search for one of the two sub-arrays.
    (a) If element is greater than 0th element then search in left array
    (b) Else Search in right array (1 will go in else as 1 < 0th element(3))
3) If element is found in selected sub-array then return index Else return -1.

"""
import typing


def pivoted_binary_search(arr: typing.List[int], n: int, key: int):
    """
    Searches an element key in a pivoted sorted array arrp[] of size n
    :param arr:
    :param n: int
    :param key: int
    :return:
    """
    pivot = find_pivot(arr, 0, n - 1)

    # If we didn't find a pivot, then array is not rotated at all
    if pivot == -1:
        return binary_search(arr, 0, n - 1, key)

    # If we found a pivot, then first compare with pivot and then
    # search in two sub arrays around pivot
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binary_search(arr, 0, pivot - 1, key)
    return binary_search(arr, pivot + 1, n - 1, key)


def find_pivot(arr: typing.List[int], low: int, high: int):
    """
    Function to get pivot. For array 3, 4, 5, 6, 1, 2 it returns 3 (index of 6)
    :param arr:
    :param low:
    :param high:
    :return:
    """
    # base cases
    if high < low:
        return -1

    if high == low:
        return low

    mid = (low + high) // 2
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid

    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1

    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid - 1)
    else:
        return find_pivot(arr, mid + 1, high)


def binary_search(arr, low, high, key):
    """Standard Binary Search function
    """
    if high < low:
        return -1

    mid = (low + high) // 2
    if key == arr[mid]:
        return mid

    if key > arr[mid]:
        return binary_search(arr, (mid + 1), high, key)

    return binary_search(arr, low, (mid - 1), key)


if __name__ == '__main__':
    # Output: 8
    # Let us search 3 in below array
    arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    n = len(arr1)
    key = 3
    print("Index: %d" % pivoted_binary_search(arr1, n, key))
