"""
Given an array A[] and a number x, check for pair in A[] with sum as x

Write a C program that, given an array A[] of n numbers and another number x, determines whether
or not there exist two elements in S whose sum is exactly x.

Example:
Let Array be {1, 4, 45, 6, 10, -8} and sum to find be 16

"""


# Python program to check for the sum condition to be satisified
def has_array_two_candidates(arr, arr_size, summation):
    """
    METHOD 1 (Use Sorting)

    Algorithm:

    hasArrayTwoCandidates (A[], ar_size, sum)
    1) Sort the array in non-decreasing order.
    2) Initialize two index variables to find the candidate elements in the sorted array.
        (a) Initialize first to the leftmost index: l = 0
        (b) Initialize second the rightmost index:  r = ar_size-1
    3) Loop while l < r.
        (a) If (A[l] + A[r] == sum)  then return 1
        (b) Else if( A[l] + A[r] <  sum )  then l++
        (c) Else r--
    4) No candidates in whole array - return 0

    Time Complexity: Depends on what sorting algorithm we use. If we use Merge Sort or Heap Sort
    then (-)(nlogn) in worst case. If we use Quick Sort then O(n^2) in worst case.

    Auxiliary Space : Again, depends on sorting algorithm. For example auxiliary space is O(n) for
    merge sort and O(1) for Heap Sort.

    Example:
    Let Array be {1, 4, 45, 6, 10, -8} and sum to find be 16

    Sort the array
    A = {-8, 1, 4, 6, 10, 45}

    Initialize l = 0, r = 5
    A[l] + A[r] ( -8 + 45) > 16 => decrement r. Now r = 10
    A[l] + A[r] ( -8 + 10) < 2 => increment l. Now l = 1
    A[l] + A[r] ( 1 + 10) < 16 => increment l. Now l = 2
    A[l] + A[r] ( 4 + 10) < 14 => increment l. Now l = 3
    A[l] + A[r] ( 6 + 10) == 16 => Found candidates (return 1)

    Note: If there are more than one pair having the given sum then this algorithm reports only
    one. Can be easily extended for this though.

    """
    # sort the array
    quick_sort(arr, 0, arr_size - 1)
    l = 0
    r = arr_size - 1

    # traverse the array for the two elements
    while l < r:
        if arr[l] + arr[r] == summation:
            return 1
        elif arr[l] + arr[r] < summation:
            l += 1
        else:
            r -= 1
    return 0


def quick_sort(arr, si, ei):
    """
    Implementation of Quick Sort
    arr[] --> Array to be sorted
    si  --> Starting index
    ei  --> Ending index
    """
    if si < ei:
        pi = partition(arr, si, ei)
        quick_sort(arr, si, pi - 1)
        quick_sort(arr, pi + 1, ei)


def partition(A, si, ei):
    """Utility function for partitioning the array(used in quick sort)"""
    x = A[ei]
    i = (si - 1)
    for j in range(si, ei):
        if A[j] <= x:
            i += 1
            # This operation is used to swap two variables is python
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[ei] = A[ei], A[i + 1]
    return i + 1


if __name__ == '__main__':
    A = [1, 4, 45, 6, 10, -8]
    n = 16
    if has_array_two_candidates(A, len(A), n):
        print("Array has two elements with the given sum")
    else:
        print("Array doesn't have two elements with the given sum")