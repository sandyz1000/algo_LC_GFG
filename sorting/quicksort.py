"""
QuickSort
=========

Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as
pivot and partitions the given array around the picked pivot. There are many different versions
of quickSort that pick pivot in different ways. 

Always pick first element as pivot.
Always pick last element as pivot (implemented below)
Pick a random element as pivot.
Pick median as pivot.

The key process in quickSort is partition(). Target of partitions is, given an array and an element
x of array as pivot, put x at its correct position in sorted array and put all smaller elements
(smaller than x) before x, and put all greater elements (greater than x) after x. 
All this should be done in linear time.

Illustration of partition():
- - - - - - - - - - - - - - - - - - - - - - - - - - - -
arr[] = {10, 80, 30, 90, 40, 50, 70}
Indexes:  0   1   2   3   4   5   6

low = 0, high = 6, pivot = arr[h] = 70
Initialize index of smaller element, i = -1

Traverse elements from j = low to high-1
j = 0 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
i = 0
arr[] = {10, 80, 30, 90, 40, 50, 70} // No change as i and j are same

j = 1 : Since arr[j] > pivot, do nothing
// No change in i and arr[]

j = 2 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
i = 1
arr[] = {10, 30, 80, 90, 40, 50, 70} // We swap 80 and 30

j = 3 : Since arr[j] > pivot, do nothing
// No change in i and arr[]

j = 4 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
i = 2
arr[] = {10, 30, 40, 90, 80, 50, 70} // 80 and 40 Swapped
j = 5 : Since arr[j] <= pivot, do i++ and swap arr[i] with arr[j]
i = 3
arr[] = {10, 30, 40, 50, 80, 90, 70} // 90 and 50 Swapped

We come out of loop because j is now equal to high-1.
Finally we place pivot at correct position by swapping
arr[i+1] and arr[high] (or pivot)
arr[] = {10, 30, 40, 50, 70, 90, 80} // 80 and 70 Swapped

Now 70 is at its correct place. All elements smaller than 70 are before it and all elements
greater than 70 are after it.

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

Analysis of QuickSort
Time taken by QuickSort in general can be written as following.

- - - - - - - - - - - - - - - - - - - - - - - - - - - -
T(n) = T(k) + T(n-k-1) + theta(n)
- - - - - - - - - - - - - - - - - - - - - - - - - - - -

The first two terms are for two recursive calls, the last term is for the partition process. k is 
the number of elements which are smaller than pivot.
The time taken by QuickSort depends upon the input array and partition strategy. 
Following are three cases.

==Worst Case:==
The worst case occurs when the partition process always picks greatest or smallest
element as pivot. If we consider above partition strategy where last element is always picked as 
pivot, the worst case would occur when the array is already sorted in increasing or decreasing 
order. Following is recurrence for worst case.

T(n) = T(0) + T(n-1) + theta(n) which is equivalent to  
T(n) = T(n-1) + theta(n)

The solution of above recurrence is theta(n2).

==Best Case:==
The best case occurs when the partition process always picks the middle element as pivot.
Following is recurrence for best case.
T(n) = 2T(n/2) + theta(n)
The solution of above recurrence is theta(nLogn). It can be solved using case 2 of Master Theorem.

==Average Case:==
To do average case analysis, we need to consider all possible permutation of array and calculate 
time taken by every permutation which doesn't look easy.
We can get an idea of average case by considering the case when partition puts O(n/9) elements in 
one set and O(9n/10) elements in other set. Following is recurrence for this case.

T(n) = T(n/9) + T(9n/10) + theta(n)
Solution of above recurrence is also O(nLogn)

"""

from __future__ import print_function


# Python program for implementation of Quicksort Sort

def partition(arr, low, high):
    """
    This function takes last element as pivot, places the pivot element at its correct position
    in sorted array, and places all smaller (smaller than pivot) to left of pivot and all greater
    elements to right of pivot
    """
    index = low  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] < pivot:
            arr[index], arr[j] = arr[j], arr[index]
            index += 1

    arr[index], arr[high] = arr[high], arr[index]
    return index + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quick_sort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == '__main__':
    # arr = [10, 7, 8, 9, 1, 5]
    arr = [12, 3, 35, 7, 34, 19, 26]
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    print("Sorted array is:")
    for i in range(n):
        print("%d" % arr[i], end=" ")