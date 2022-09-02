"""
-- METHOD 1
Inversion Count for an array indicates - how far (or close) the array is from being sorted. If
array is already sorted then inversion count is 0. If array is sorted in reverse order that
inversion count is the maximum. Formally speaking, two elements a[i] and a[j] form an inversion
if a[i] > a[j] and i < j

-- METHOD 2
Suppose we know the number of inversions in the left half and right half of the array (let be
inv1 and inv2) what kinds of inversions are not accounted for in Inv1 + Inv2 ?

The answer is - the inversions we have to count during the merge step. Therefore, to get number of
inversions, we need to add number of inversions in left sub array, right sub array and merge()

How to get number of inversions in merge()?
In merge process, let i is used for indexing left sub-array and j for right sub-array.
At any step in merge(), if a[i] is greater than a[j], then there are (mid - i) inversions.
because left and right subarrays are sorted, so all the remaining elements in left-subarray
(a[i+1], a[i+2] - a[mid]) will be greater than a[j]

"""
from __future__ import print_function


def get_inv_count(arr, n):
    """
    Method - 1
    :param arr: list(int)
    :param n: int
    :return:
    """
    inv_count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1

    return inv_count


class MergeSort(object):
    """ Method -2 """

    @staticmethod
    def merge(arr, temp, left, mid, right):
        """
        This funt merges two sorted arrays and returns inversion count in the arrays.
        :param arr: list(int)
        :param temp: list(int)
        :param left: int
        :param mid: int
        :param right: int
        :return:
        """
        inv_count = 0
        i = left  # i is index for left subarray
        j = mid  # j is index for right subarray
        k = left  # k is index for resultant merged subarray
        while (i <= mid - 1) and (j <= right):
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                k += 1
                i += 1
            else:
                temp[k] = arr[j]
                k += 1
                i += 1

            # this is tricky -- see above explanation/diagram for merge()
            inv_count = inv_count + (mid - i)

        # Copy the remaining elements of left subarray (if there are any) to temp
        while i <= mid - 1:
            temp[k] = arr[i]
            k += 1
            i += 1

        # Copy the remaining elements of right subarray (if there are any) to temp*/
        while j <= right:
            temp[k] = arr[j]
            k += 1
            j += 1

        # Copy back the merged elements to original arr*/
        for i in range(left, right + 1):
            arr[i] = temp[i]

        return inv_count

    @staticmethod
    def merge_sort(arr, array_size):
        """
        This function sorts the input arr and returns the number of inversions in the arr
        :param arr: list(int)
        :param array_size: int
        :return:
        """
        temp = [0] * array_size
        return MergeSort._merge_sort(arr, temp, 0, array_size - 1)

    @staticmethod
    def _merge_sort(arr, temp, left, right):
        """
        An auxiliary recursive function that sorts the input arr and returns the number of
        inversions in the arr.
        :param arr: list(int)
        :param temp: list(int)
        :param left: int
        :param right: int
        :return:
        """
        mid, inv_count = 0, 0
        if right > left:
            # Divide the arr into two parts and call __merge_sort() for each of
            # the parts
            mid = (right + left) // 2

            # Inversion count will be sum of inversions in left-part, right-part and number
            # of inversions in merging */
            inv_count = MergeSort._merge_sort(arr, temp, left, mid)
            inv_count += MergeSort._merge_sort(arr, temp, mid + 1, right)

            # Merge the two parts
            inv_count += MergeSort.merge(arr, temp, left, mid + 1, right)

        return inv_count


if __name__ == '__main__':
    print("METHOD-1\n")
    arr = [1, 20, 6, 4, 5]
    print(" Number of inversions are %d \n" % get_inv_count(arr, len(arr)))

    print("-----------------------")
    print("METHOD-2\n")
    merge_sort = MergeSort()
    arr = [1, 20, 6, 4, 5]
    print(" Number of inversions are %d \n" % merge_sort.merge_sort(arr, 5))
