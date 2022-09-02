"""
Iterative Merge Sort:

The above function is recursive, so uses function call stack to store intermediate values of l and
h. The function call stack stores other bookkeeping information together with parameters. Also,
function calls involve overheads like storing activation record of the caller function and then
resuming execution. Unlike Iterative QuickSort, the iterative MergeSort doesn't require explicit
auxiliary stack."""

from __future__ import print_function


# Iterative Python program for merge sort

# Function to merge the two haves arr[l..m] and arr[m+1..r] of array arr[]
# void merge(int arr[], int l, int m, int r);

# Utility function to find minimum of two integers
# int min(int x, int y) { return (x<y)? x :y; }

def merge_sort(arr, n):
    """Iterative mergesort function to sort arr[0...n-1]"""
    # For current size of subarrays to be merged curr_size varies from 1 to n/2
    curr_size = 1

    # Merge subarrays in bottom up manner. First merge subarrays of size 1 to create sorted
    # subarrays of size 2, then merge subarrays of size 2 to create sorted subarrays of size 4,
    # and so on.

    while curr_size <= n - 1:
        # Pick starting point of different subarrays of current size
        left_start = 0  # For picking starting index of left subarray to be merged

        while left_start < n - 1:
            # Find ending point of left subarray. mid+1 is starting point of right
            mid = left_start + curr_size - 1
            right_end = min(left_start + 2 * curr_size - 1, n - 1)

            # Merge Subarrays arr[left_start...mid] & arr[mid+1...right_end]
            merge(arr, left_start, mid, right_end)
            left_start += 2 * curr_size

        curr_size = 2 * curr_size


def merge(arr, l, m, r):
    """Function to merge the two haves arr[l..m] and arr[m+1..r] of array arr[]"""
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    # Copy data to temp arrays L[] and R[]
    L, R = [arr[l + i] for i in range(n1)], [arr[m + 1 + j] for j in range(n2)]

    # Merge the temp arrays back into arr[l..r]
    i, j, k = 0, 0, l
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


if __name__ == '__main__':
    # Output: Sorted array is 5 6 7 11 12 13
    # Time complexity of above iterative function is same as recursive, i.e., Theta(nLogn).
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)

    print("Given array is \n", arr)
    merge_sort(arr, n)
    print("\nSorted array is \n", arr)
