"""
K'th Smallest/Largest Element in Unsorted Array | Set 2 (Expected Linear Time)
We recommend to read following post as a prerequisite of this post.

Given an array and a number k where k is smaller than size of array, we need to find the k'th
smallest element in the given array. It is given that ll array elements are distinct.

------------------------------------------------
Examples:
------------------------------------------------
Input: arr = {7, 10, 4, 3, 20, 15}, k = 3
Output: 7

Input: arr = {7, 10, 4, 3, 20, 15}, k = 4
Output: 10

------------------------------------------------
Explanation:
------------------------------------------------

We already discussed an expected linear time algorithm. In this post, a worst case linear time
method is discussed. The idea in this new method is similar to quickSelect(), we get worst case
linear time by selecting a pivot that divides array in a balanced way (there are not very few
elements on one side and many on other side). After the array is divided in a balanced way,
we apply the same steps as used in quickSelect() to decide whether to go left or right of pivot.
Python implementation of worst case linear time algorithm to find k'th smallest element A simple
function to find median of arr[]. This is called only for an array of size 5 in this program.

Time Complexity:

The worst case time complexity of the above solution is still O(n^2). In worst case,
the randomized function may always pick a corner element. The expected time complexity of above
randomized QuickSelect is Theta(n), see CLRS book or MIT video lecture for proof. The assumption
in the analysis is, random number generator is equally likely to generate any number in the input
range.
"""


from __future__ import print_function

import sys
import random

MAX_VALUE = sys.maxsize


# Python program to find k'th smallest element in expected linear time
class KthSmallest(object):
    """
    This function returns k'th smallest element in arr[l..r] using QuickSort based method.
    ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT """

    def kth_smallest(self, arr, l, r, k):
        """
        Returns k'th smallest element in arr[l..r] in worst case linear time.
        ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT

        :param arr: list(int)
        :param l: int
        :param r: int
        :param k: int
        :return:
        """
        # If k is smaller than number of elements in array
        if 0 < k <= r - l + 1:
            # Partition the array around a random element and get position of pivot element
            # in sorted array
            pos = self.random_partition(arr, l, r)

            # If position is same as k
            if pos - l == k - 1:
                return arr[pos]

            # If position is more, recur for left subarray
            if pos - l > k - 1:
                return self.kth_smallest(arr, l, pos - 1, k)
            # Else recur for right subarray -- (k-1) - (pos - l)
            return self.kth_smallest(arr, pos + 1, r, (k - 1) - (pos - l))

        # If k is more than number of elements in array
        return MAX_VALUE

    def partition(self, arr, l, r):
        """
        Standard partition process of QuickSort(). It considers the last element as pivot and
        moves all smaller element to left of it and greater elements to right. This function is
        used by randomPartition()
        """
        x = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] <= x:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[r] = arr[r], arr[i]
        return i

    def random_partition(self, arr, l, r):
        """
        Picks a random pivot element between l and r and partitions arr[l..r] around the
        randomly picked element using partition() """
        n = r - l + 1
        pivot = random.randint(1, 100) % n
        arr[l + pivot], arr[r] = arr[r], arr[l + pivot]
        return self.partition(arr, l, r)


if __name__ == '__main__':
    # Output: K'th smallest element is 5

    ob = KthSmallest()
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3
    print("K'th smallest element is %d " % ob.kth_smallest(arr, 0, n - 1, k))
