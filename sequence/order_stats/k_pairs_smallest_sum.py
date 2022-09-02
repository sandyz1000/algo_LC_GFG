"""
Find k pairs with smallest sums in two arrays

Given two integer arrays arr1[] and arr2[] sorted in ascending order and an integer k.
Find k pairs with smallest sums such that one element of a pair belongs to arr1[] and other
element belongs to arr2[]

Examples:

Input :  arr1 = [1, 7, 11]
         arr2 = [2, 4, 6]
         k = 3
Output : [1, 2],
         [1, 4],
         [1, 6]

Explanation:
The first 3 pairs are returned
from the sequence [1, 2], [1, 4], [1, 6], [7, 2], [7, 4], [11, 2], [7, 6], [11, 4], [11, 6]

"""
import sys
import typing

INT_MAX = sys.maxsize


# Prints first k pairs with least sum from two arrays.
def k_smallest_pair(arr1: typing.List[int], n1: int, arr2: typing.List[int], n2: int, k: int):
    """
    We one by one find k smallest sum pairs, starting from least sum pair. The idea is to keep
    track of all elements of arr2[] which have been already considered for every element arr1[i1]
    so that in an iteration we only consider next element. For this purpose, we use an index
    array index2[] to track the indexes of next elements in the other array. It simply means that
    which element of second array to be added with the element of first array in each and every
    iteration. We increment value in index array for the element that forms next minimum value
    pair.

    #### Time Complexity : O(k*n1)

    Function to find k pairs with least sum such that one element of a pair is from arr1[] and
    other element is from arr2[]

    :return:
    """
    if k > n1 * n2:
        print("k pairs don't exist")
        return

    # Stores current index in arr2[] for every element of arr1[]. Initially all values are
    # considered 0. Here current index is the index before which all elements are considered as
    # part of output.
    # index will be arr1 index and value be arr2 index
    index2 = [0] * n1

    while k > 0:
        # Initialize current pair sum as infinite
        min_sum = INT_MAX
        min_index = 0

        # To pick next pair, traverse for all elements of arr1[], for every element,
        # find corresponding current element in arr2[] and pick minimum of all formed pairs.
        for i1 in range(n1):
            # Check if current element of arr1[] plus element of array2 to be used gives minimum sum
            if index2[i1] < n2 and arr1[i1] + arr2[index2[i1]] < min_sum:
                min_index = i1  # Update index that gives minimum
                min_sum = arr1[i1] + arr2[index2[i1]]  # update minimum sum

        print("(%d, %d) " % (arr1[min_index], arr2[index2[min_index]]))
        index2[min_index] += 1
        k -= 1


# NOTE: Write own implementation


if __name__ == '__main__':
    # Output
    # (1, 2)
    # (1, 4)
    # (3, 2)
    # (3, 4)

    arr1 = [1, 3, 11]
    n1 = len(arr1)
    arr2 = [2, 4, 8]
    n2 = len(arr2)

    k = 4
    k_smallest_pair(arr1, n1, arr2, n2, k)
