"""
Merge Sort

Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides input array in two
halves, calls itself for the two halves and then merges the two sorted halves. The merge()
function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that
arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:
             middle m = (l+r)/2
     2. Call mergeSort for first half:
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Python program for implementation of MergeSort
Time Complexity:
Sorting arrays on different machines. Merge Sort is a recursive algorithm and
time complexity can be expressed as following recurrence relation.
T(n) = 2T(n/2) + \Theta(n)

The above recurrence can be solved either using Recurrence Tree method or Master method. It
falls in case II of Master Method and solution of the recurrence is \Theta(nLogn).
Time complexity of Merge Sort is \Theta(nLogn) in all 3 cases (worst, average and best) as
merge sort always divides the array in two halves and take linear time to merge two halves.
----------------------------
Auxiliary Space: O(n)

"""


# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # create temp arrays
    # Copy data to temp arrays L[] and R[]
    L = [arr[left + i] for i in range(0, n1)]
    R = [arr[mid + 1 + j] for j in range(0, n2)]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    """l is for left index and r is right index of the sub-array of arr to be sorted"""
    if left < right:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (left + (right - 1)) // 2

        # Sort first and second halves
        merge_sort(arr, left, m)
        merge_sort(arr, m + 1, right)
        merge(arr, left, m, right)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    print("Given array is")
    for i in range(n):
        print("%d" % arr[i], end=" ")

    merge_sort(arr, 0, n - 1)
    print("\n\nSorted array is")
    for i in range(n):
        print("%d" % arr[i], end=" ")