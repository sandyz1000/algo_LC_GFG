"""
Binary Insertion Sort

We can use binary search to reduce the number of comparisons in normal insertion sort.
Binary Insertion Sort find use binary search to find the proper location to insert the selected
item at each iteration.

--------------------------------------------------
Explanation:
--------------------------------------------------
In normal insertion, sort it takes O(i) (at ith iteration) in worst case. we can reduce it to
O(logi) by using binary search.

--------------------------------------------------
Time Complexity:
--------------------------------------------------
The algorithm as a whole still has a running worst case running time of O(n^2) because of the
series of swaps required for each insertion.
"""

from __future__ import print_function


# Python program for implementation of binary insertion sort
def binary_search(a, item, low, high):
    """
    A binary search based function to find the position where item should
    be inserted in a[low..high]

    :param a:
    :param item:
    :param low:
    :param high:
    :return:
    """
    if high <= low:
        return low + 1 if item > a[low] else low

    mid = (low + high) // 2
    if item == a[mid]:
        return mid + 1

    if item > a[mid]:
        return binary_search(a, item, mid + 1, high)
    else:
        return binary_search(a, item, low, mid - 1)


def insertion_sort(a, n):
    """Function to sort an array a[] of size 'n'"""
    for i in range(1, n):
        j = i - 1
        selected = a[i]
        # find location where selected should be inserted
        loc = binary_search(a, selected, 0, j)

        # Move all elements after location to create space
        while j >= loc:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = selected


if __name__ == '__main__':
    # Output: [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
    arr = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    arr = [12, 11, 13, 5, 6]
    n = len(arr)

    insertion_sort(arr, n)
    print("Sorted array: \n", arr)
