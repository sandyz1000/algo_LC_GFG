"""
Find the Rotation Count in Rotated Sorted array

Consider an array of distinct numbers sorted in increasing order. The array has been rotated
(anti-clockwise) k number of times. Given such an array, find the value of k.

------------------------------------
Examples:
------------------------------------
Input : arr[] = {15, 18, 2, 3, 6, 12}
Output: 2
Explanation : Initial array must be {2, 3, 6, 12, 15. 18}. We get the given array after
rotating the initial array twice.

Input : arr[] = {7, 9, 11, 12, 5}
Output: 4

Input: arr[] = {7, 9, 11, 12, 15};
Output: 0

Time Complexity : O(Log n)
Auxiliary Space : O(1) if we use iterative Binary Search is used

"""
import typing


def count_rotations(arr: typing.List[int], low: int, high: int):
    """
    Returns count of rotations for an array which is first sorted
    in ascending order, then rotated
    """
    # This condition is needed to handle the case when array is not rotated at all
    if high < low:
        return 0

    # If there is only one element left
    if high == low:
        return low

    # Find mid
    mid = low + (high - low) // 2  # (low + high) // 2

    # Check if element (mid+1) is minimum element.
    # Consider the cases like {3, 4, 5, 1, 2}
    if mid < high and arr[mid + 1] < arr[mid]:
        return mid + 1

    # Check if mid itself is minimum element
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid

    # Decide whether we need to go to left half or right half
    if arr[high] > arr[mid]:
        return count_rotations(arr, low, mid - 1)

    return count_rotations(arr, mid + 1, high)


if __name__ == '__main__':
    arr = [15, 18, 2, 3, 6, 12]
    n = len(arr)
    print(count_rotations(arr, 0, n - 1))
