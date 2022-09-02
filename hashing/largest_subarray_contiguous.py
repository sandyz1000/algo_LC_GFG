"""
Length of the largest subarray with contiguous elements | Set 1
Given an array of distinct integers, find length of the longest subarray which contains numbers
that can be arranged in a continuous sequence.

==Examples:==
- - - - - - - - - - - - - - - - - - - - - - - - - - - - +
Input:  arr[] = {10, 12, 11};
Output: Length of the longest contiguous subarray is 3

Input:  arr[] = {14, 12, 11, 20};
Output: Length of the longest contiguous subarray is 2

Input:  arr[] = {1, 56, 58, 57, 90, 92, 94, 93, 91, 45};
Output: Length of the longest contiguous subarray is 5
- - - - - - - - - - - - - - - - - - - - - - - - - - - - +
"""


class LargestLengthSubArray:
    """
    ==Method-1==

    The important thing to note in question is, it is given that all elements are distinct. If all
    elements are distinct, then a subarray has contiguous elements if and only if the difference
    between maximum and minimum elements in subarray is equal to the difference between last and
    first indexes of subarray. So the idea is to keep track of minimum and maximum element in every
    subarray.

    Time Complexity of the above solution is O(n^2).
    """

    @staticmethod
    def find_length(arr, n):
        """Returns length of the longest contiguous subarray"""
        max_len = 1  # Initialize result
        for i in range(n - 1):
            # Initialize min and max for all subarrays starting with i
            mn, mx = arr[i], arr[i]

            # Consider all sub-arrays starting with i and ending with j
            for j in range(i + 1, n):
                # Update min and max in this subarray if needed
                mn = min(mn, arr[j])
                mx = max(mx, arr[j])

                # If current sub-array has all contiguous elements
                if (mx - mn) == j - i:
                    max_len = max(max_len, mx - mn + 1)
        return max_len  # Return result


class LargestLengthSubArrayDuplicate:
    """
    ==Method-2==

    The idea is similar to previous post. In the previous post, we checked whether maximum value
    minus minimum value is equal to ending index minus starting index or not. Since duplicate
    elements are allowed, we also need to check if the subarray contains duplicate elements or not.
    For example, the array {12, 14, 12} follows the first property, but numbers in it are not
    contiguous elements.

    To check duplicate elements in a subarray, we create a hash set for every subarray and if we
    find an element already in hash, we don't consider the current subarray.

    Time complexity of the above solution is O(n^2) under the assumption that hash set
    operations like add() and contains() work in O(1) time
    """

    @staticmethod
    def find_length(arr, n):
        """This function prints all distinct elements"""
        max_len = 1  # Initialize result
        # One by one fix the starting points
        for i in range(n - 1):
            # Create an empty hash set and add i'th element to it.
            setter = set()
            setter.add(arr[i])

            # Initialize max and min in current sub-array
            mn, mx = arr[i], arr[i]

            # One by one fix ending points
            for j in range(i + 1, n):
                # If current element is already in hash set, then this subarray cannot
                # contain contiguous elements
                if arr[j] in setter:
                    break

                # Else add current element to hash set and update min, max if required.
                setter.add(arr[j])
                mn = min(mn, arr[j])
                mx = max(mx, arr[j])

                # We have already cheched for duplicates, now check for other property and
                # update max_len if needed
                if mx - mn == j - i:
                    max_len = max(max_len, mx - mn + 1)
        return max_len  # Return result


if __name__ == '__main__':
    # Output: Length of the longest contiguous subarray is 5
    print("\nMethod-1:  ")
    test = LargestLengthSubArray()
    # arr = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
    # arr = [14, 12, 11, 20]
    arr = [1, 2, 3, 4, 5, 2, 6, 7, 5, 8]
    n = len(arr)
    print("Length of the longest contiguous subarray is ", test.find_length(arr, n))

    # print("\nMethod-2:  ")
    # test = LargestLengthSubArrayDuplicate()
    # # Output: Length of the longest contiguous subarray is 2
    # arr = [10, 12, 12, 10, 10, 11, 10]
    # n = len(arr)
    # print("Length of the longest contiguous subarray is", test.find_length(arr, n))
