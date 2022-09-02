"""
Method-1
Rearrange positive and negative numbers in O(n) time and O(1) extra space

An array contains both positive and negative numbers in random order. Rearrange the array elements
so that positive and negative numbers are placed alternatively. Number of positive and negative
numbers need not be equal. If there are more positive numbers they appear at the end of the array.
If there are more negative numbers, they too appear in the end of the array.

For example, if the input array is [-1, 2, -3, 4, 5, 6, -7, 8, 9], 
then the output should be [9, -7, 8, -3, 5, -1, 2, 4, 6]

------------------------------------------------------
Explanation:
------------------------------------------------------

The solution is to first separate positive and negative numbers using partition process of
QuickSort. In the partition process, consider 0 as value of pivot element so that all negative
numbers are placed before positive numbers. Once negative and positive numbers are separated,
we start from the first negative number and first positive number, and swap every alternate
negative number with next positive number.

------------------------------------------------------
Method-2
Rearrange positive and negative numbers with constant extra space

Given an array of positive and negative numbers, arrange them such that all negative integers
appear before all the positive integers in the array without using any additional data structure
like hash table, arrays, etc. The order of appearance should be maintained.

Examples:

Input:  [12 11 -13 -5 6 -7 5 -3 -6]
Output: [-13 -5 -7 -3 -6 12 11 6 5]

Approach 2: Optimized Merge Sort
--------------------------------

Merge method of standard merge sort algorithm can be modified to solve this problem. While
merging two sorted halves say left and right, we need to merge in such a way that negative part
of left and right sub-array is copied first followed by positive part of left and right sub-array.

Time complexity of above solution is O(n log n). The problem with this approach is we are using
auxiliary array for merging but we're not allowed to use any data structure to solve this
problem. We can do merging in-place without using any data-structure.

"""
import typing


class Rearrangement:
    """
    Python program to put positive numbers at even indexes (0,  2, 4,..) and
    negative numbers at odd indexes (1, 3, 5, ..)

    Time Complexity: O(n) where n is number of elements in given array.
    Auxiliary Space: O(1)
    """

    def rearrange(self, arr: typing.List[int], n: int):
        """
        The main function that rearranges elements of given array. It puts  positive
        elements at even indexes (0, 2, ..) and negative numbers at odd indexes (1, 3, ..).
        """
        # The following few lines are similar to partition process of QuickSort. The idea is
        # to consider 0 as pivot and divide the array around it.
        i = -1
        for j in range(n):
            if arr[j] < 0:
                i += 1
                # swapping of arr
                arr[i], arr[j] = arr[j], arr[i]

        # Now all positive numbers are at end and negative numbers at the beginning of array.
        # Initialize indexes for starting point of positive and negative numbers to be swapped
        pos, neg = i + 1, 0

        # Increment the negative index by 2 and positive index by 1, i.e., swap every alternate
        # negative number with next positive number
        while n > pos > neg and arr[neg] < 0:
            # swapping of arr
            arr[neg], arr[pos] = arr[pos], arr[neg]
            pos += 1
            neg += 2

    def printArray(self, arr, n):
        """A utility function to print an array"""
        for i in range(n):
            print(arr[i], end=" ")
        print("-----------------------")


class RearrangementWithSpace:
    """
    Python program to Rearrange positive and negative numbers in a array
    Time complexity of above solution is O(n log n), O(Log n) space for recursive calls,
    and no additional data structure.
    """

    def merge(self, arr: typing.List[int], l: int, m: int, r: int):
        """
        Merges two subarrays of arr[]. First subarray is arr[l..m] Second subarray
        is arr[m+1..r]
        """
        n1 = m - l + 1
        n2 = r - m

        # Copy data to temp arrays L[] and R[]
        L = [arr[l + i] for i in range(n1)]
        R = [arr[m + 1 + j] for j in range(n2)]

        # Merge the temp arrays back into arr[l..r]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = l  # Initial index of merged subarray

        # Note the order of appearance of elements should be maintained - we copy elements of
        # left subarray first followed by that of right subarray

        # copy negative elements of left subarray
        while i < n1 and L[i] < 0:
            arr[k] = L[i]
            k += 1
            i += 1

        # copy negative elements of right subarray
        while j < n2 and R[j] < 0:
            arr[k] = R[j]
            k += 1
            j += 1

        # copy positive elements of left subarray
        while i < n1:
            arr[k] = L[i]
            k += 1
            i += 1

        # copy positive elements of right subarray
        while j < n2:
            arr[k] = R[j]
            k += 1
            j += 1

    def rearrange_pos_neg_method(self, arr: typing.List[int], l: int, r: int):
        """Function to Rearrange positive and negative numbers in a array"""
        if l < r:
            # Same as (l + r)/2, but avoids overflow for large l and h
            m = l + (r - l) // 2

            # Sort first and second halves
            self.rearrange_pos_neg_method(arr, l, m)
            self.rearrange_pos_neg_method(arr, m + 1, r)
            self.merge(arr, l, m, r)

    def print_array(self, arr, n):
        """A utility function to print an array"""
        for i in range(n):
            print(arr[i], end=" ")


class RearrangementOptimized:
    """
    Let Ln and Lp denotes the negative part and positive part of left sub-array respectively.
    Similarly, Rn and Rp denotes the negative and positive part of right sub-array respectively.
    Below are the steps to convert [Ln Lp Rn Rp] to [Ln Rn Lp Rp] without using extra space.

    1. Reverse Lp and Rn. We get [Lp] -> [Lp'] and [Rn] -> [Rn']
        [Ln Lp Rn Rp] -> [Ln Lp' Rn' Rp]

    2. Reverse [Lp' Rn']. We get [Rn Lp].
        [Ln Lp' Rn' Rp] -> [Ln Rn Lp Rp]

    """

    def reverse(self, arr, l, r):
        """
        Function to reverse an array. An array can be reversed in O(n) time and O(1)
        space.
        """
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
            self.reverse(arr, l, r)

    def merge(self, arr, l, m, r):
        """
        Merges two subarrays of arr[]. First subarray is arr[l..m] Second subarray is
        arr[m+1..r]
        """
        i = l  # Initial index of 1st subarray
        j = m + 1  # Initial index of IInd
        while i <= m and arr[i] < 0:
            i += 1

        while j <= r and arr[j] < 0:
            j += 1

        self.reverse(arr, i, m)  # reverse positive part of left sub-array (arr[i..m])
        self.reverse(arr, m + 1, j - 1)  # reverse negative part of right sub-array (arr[m+1..j-1])
        self.reverse(arr, i, j - 1)  # reverse arr[i..j-1]

    def rearrange_pos_neg_method(self, arr, l, r):
        """Function to Rearrange positive and negative numbers in a array"""
        if l < r:
            # Same as (l+r)/2, but avoids overflow for large l and h
            m = l + (r - l) // 2

            # Sort first and second halves
            self.rearrange_pos_neg_method(arr, l, m)
            self.rearrange_pos_neg_method(arr, m + 1, r)
            self.merge(arr, l, m, r)

    def print_array(self, arr, n):
        """A utility function to print an array"""
        for i in range(n):
            print(arr[i], end=" ")


if __name__ == '__main__':
    print("\n------ Method-1-----")
    rear = RearrangementWithSpace()
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    # arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    arr_size = len(arr)
    rear.rearrange_pos_neg_method(arr, 0, arr_size - 1)
    rear.print_array(arr, arr_size)

    print("\n------ Method-2-----")
    rear = RearrangementOptimized()
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    # arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    arr_size = len(arr)
    rear.rearrange_pos_neg_method(arr, 0, arr_size - 1)
    rear.print_array(arr, arr_size)

    print("\n ---- Method-3 -------")
    print("Rearrange positive and negative numbers in alternative order")
    rear = Rearrangement()
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    # arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    n = len(arr)
    rear.rearrange(arr, n)
    rear.printArray(arr, n)
