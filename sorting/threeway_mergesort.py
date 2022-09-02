"""
3-way Merge Sort
================

Prerequisite - Merge Sort

Merge sort involves recursively splitting the array into 2 parts, sorting and finally merging them.
A variant of merge sort is called 3-way merge sort where instead of splitting the array into 2
parts we split it into 3 parts.

Merge sort recursively breaks down the arrays to sub-arrays of size half. Similarly, 3-way Merge
sort breaks down the arrays to sub-arrays of size one third.

------------------------------------------
Examples:
------------------------------------------
Input  : 45, -2, -45, 78, 30, -42, 10, 19, 73, 93
Output : -45 -42 -2 10 19 30 45 73 78 93

Input  : 23, -19
Output : -19  23

Here, we first copy the contents of data array to another array called fArray. Then, sort the
array by finding midpoints that divide the array into 3 parts and called sort function on each
array respectively. The base case of recursion is when size of array is 1 and it returns from the
function. Then merging of arrays starts and finally the sorted array will be in fArray which is
copied back to gArray.

Time Complexity: In case of 2-way Merge sort we get the equation: T(n) = 2T(n/2) + O(n)
Similarly, in case of 3-way Merge sort we get the equation: T(n) = 3T(n/3) + O(n)

By solving it using Master method, we get its complexity as O(n log 3n).. Although time
complexity looks less compared to 2 way merge sort, the time taken actually may become higher
because number of comparisons in merge function go higher. Please refer Why is Binary Search
preferred over Ternary Search? for details.
"""
import typing


class MergeSort3Way(object):
    # Python program to perform 3 way Merge Sort
    def merge_sort3_way(self, gArray: typing.List[int]):
        """ Function for 3-way merge sort process
        """
        # if array of size is zero returns null
        if gArray is None:
            return
        # creating duplicate of given array
        # copying elements of given array into duplicate array
        fArray = gArray[:]

        # sort function
        self.merge_sort3_way_rec(fArray, 0, len(gArray), gArray)

        # copy back elements of duplicate array to given array
        for index, value in enumerate(fArray):
            gArray[index] = value

    def merge_sort3_way_rec(self, gArray: typing.List[int], low: int,
                            high: int, destArray: typing.List[int]):
        """
        Performing the merge sort algorithm on the given array of values in the range of indices
        [low, high).  low is minimum index, high is maximum index (exclusive)

        :type gArray: List[int]
        :type low:
        :type high:
        :type destArray: List[int]
        :rtype: None
        """
        # If array size is 1 then do nothing
        if high - low < 2:
            return

        # Splitting array into 3 parts
        mid1 = low + ((high - low) // 3)
        mid2 = low + 2 * ((high - low) // 3) + 1

        # Sorting 3 arrays recursively
        self.merge_sort3_way_rec(destArray, low, mid1, gArray)
        self.merge_sort3_way_rec(destArray, mid1, mid2, gArray)
        self.merge_sort3_way_rec(destArray, mid2, high, gArray)

        # Merging the sorted arrays
        self.merge(destArray, low, mid1, mid2, high, gArray)

    def merge(self, gArray: typing.List[int], low: int, mid1: int,
              mid2: int, high: int, dest_array: typing.List[int]):
        """
        Merge the sorted ranges [low, mid1), [mid1, mid2) and [mid2, high) mid1 is first midpoint
        index in overall range to merge mid2 is second midpoint index in overall range to merge
        """
        i, j, k = low, mid1, mid2
        index = low

        # choose smaller of the smallest in the three ranges
        while (i < mid1) and (j < mid2) and (k < high):
            if gArray[i] < gArray[j]:
                if gArray[i] < gArray[k]:
                    dest_array[index] = gArray[i]
                    i += 1
                    index += 1
                else:
                    dest_array[index] = gArray[k]
                    index += 1
                    k += 1
            else:
                if gArray[j] < gArray[k]:
                    dest_array[index] = gArray[j]
                    index += 1
                    j += 1
                else:
                    dest_array[index] = gArray[k]
                    index += 1
                    k += 1

        # case where first and second ranges have remaining values
        while (i < mid1) and (j < mid2):
            if gArray[i] < gArray[j]:
                dest_array[index] = gArray[i]
                index += 1
                i += 1
            else:
                dest_array[index] = gArray[j]
                index += 1
                j += 1

        # case where second and third ranges have remaining values
        while (j < mid2) and (k < high):
            if gArray[j] < gArray[k]:
                index += 1
                j += 1
                dest_array[index] = gArray[j]
            else:
                dest_array[index] = gArray[k]
                index += 1
                k += 1

        # case where first and third ranges have remaining values
        while (i < mid1) and (k < high):
            if gArray[i] < gArray[k]:
                dest_array[index] = gArray[i]
                index += 1
                i += 1
            else:
                dest_array[index] = gArray[k]
                index += 1
                k += 1

        # copy remaining values from the first range
        while i < mid1:
            dest_array[index] = gArray[i]
            index += 1
            i += 1

        # copy remaining values from the second range
        while j < mid2:
            dest_array[index] = gArray[j]
            index += 1
            j += 1

        # copy remaining values from the third range
        while k < high:
            dest_array[index] = gArray[k]
            index += 1
            k += 1


if __name__ == '__main__':
    # Output: After 3 way merge sort: -45 -42 -2 10 19 30 45 73 78 93
    test = MergeSort3Way()
    data = [45, -2, -45, 78, 30, -42, 10, 19, 73, 93]
    test.merge_sort3_way(data)
    print("After 3 way merge sort: ", data)
