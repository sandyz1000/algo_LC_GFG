"""
Find whether an array is subset of another array | Added Method 3

Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2 is a subset of arr1 or not.
Both the arrays are not in sorted order. It may be assumed that elements in both array are distinct.

----------------------------------------
Examples:
----------------------------------------
Input: arr1 = [11, 1, 13, 21, 3, 7], arr2 = [11, 3, 7, 1]
Output: arr2 is a subset of arr1

Input: arr1 = [1, 2, 3, 4, 5, 6], arr2 = [1, 2, 4]
Output: arr2 is a subset of arr1

Input: arr1 = [10, 5, 2, 23, 19], arr2 = [19, 5, 3]
Output: arr2 is not a subset of arr1
"""


class ArraySubset:
    """
    Method 1 (Simple)
    Use two loops: The outer loop picks all the elements of arr2[] one by one. The inner loop
    linearly searches for the element picked by outer loop. If all elements are found then return
    1, else return 0.

    Time Complexity: O(m*n)
    """
    @staticmethod
    def is_subset(arr1, arr2, m, n):
        """
        :param arr1: list(int)
        :param arr2: list(int)
        :param m: int
        :param n:int
        :return:
        """
        for i in range(n):
            j = 0
            while j < m:
                if arr2[i] == arr1[j]:
                    break
                j += 1

            # If the above inner loop was not broken at all then arr2[i] is not present in arr1[]
            if j == m:
                return 0

        # If we reach here then all elements of arr2[] are present in arr1[]
        return 1


class ArraySubset2:
    """
    Method 2 (Use Sorting and Binary Search)
    1) Sort arr1[] O(mLogm)
    2) For each element of arr2[], do binary search for it in sorted arr1[].
    a) If the element is not found then return 0.
    3) If all elements are present then return 1.

    Time Complexity: O(mLogm + nLogm). Please note that this will be the complexity if an mLogm
    algorithm is used for sorting which is not the case in above code. In above code Quick Sort is
    sued and worst case time complexity of Quick Sort is O(m^2)
    """

    def is_subset(self, arr1, arr2, m, n):
        """Return 1 if arr2[] is a subset of arr1[]"""
        self.quick_sort(arr1, 0, m - 1)
        for i in range(n):
            if self.binary_search(arr1, 0, m - 1, arr2[i]) == -1:
                return False

        # If we reach here then all elements of arr2[] are present in arr1[]
        return True

    def binary_search(self, arr, low, high, x):
        """FOLLOWING FUNCTIONS ARE ONLY FOR SEARCHING AND SORTING PURPOSE
        Standard Binary Search function"""
        if high >= low:
            mid = (low + high) // 2  # low + (high - low)/2
            # Check if arr[mid] is the first occurrence of x. arr[mid] is first occurrence
            # if x is one of the following is true:
            # (i)  mid == 0 and arr[mid] == x
            # (ii) arr[mid-1] < x and arr[mid] == x
            if (mid == 0 or x > arr[mid - 1]) and (arr[mid] == x):
                return mid
            elif x > arr[mid]:
                return self.binary_search(arr, (mid + 1), high, x)
            else:
                return self.binary_search(arr, low, (mid - 1), x)
        return -1

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = (low - 1)
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort(self, arr, low, high):
        """
        Implementation of Quick Sort
        arr --> Array to be sorted
        low  --> Starting index
        high  --> Ending index
        """
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)


class ArraySubset3:
    """
    Method 3 (Use Sorting and Merging )
    1) Sort both arrays: arr1[] and arr2[] O(mLogm + nLogn)
    2) Use Merge type of process to see if all elements of sorted arr2[] are present in sorted
    arr1[].

    Time Complexity: O(mLogm + nLogn) which is better than method 2. Please note that this will be
    the complexity if an nLogn algorithm is used for sorting both arrays which is not the case in
    above code. In above code Quick Sort is sued and worst case time complexity of Quick Sort is O(
    n^2)
    """

    @staticmethod
    def is_subset(arr1, arr2, m, n):
        """Return 1 if arr2[] is a subset of arr1[]"""
        i, j = 0, 0
        if m < n:
            return False
        arr1.sort()
        arr2.sort()

        while i < n and j < m:
            if arr1[j] < arr2[i]:
                j += 1
            elif arr1[j] == arr2[i]:
                j += 1
                i += 1
            elif arr1[j] > arr2[i]:
                return False
        return False if i < n else True


class ArraySubset4:
    """
    Method 4 (Use Hashing)
    1) Create a Hash Table for all the elements of arr1[].
    2) Traverse arr2[] and search for each element of arr2[] in the Hash Table.
    If element is not found then return 0.
    3) If all elements are found then return 1.
    """

    @staticmethod
    def is_subset(arr1, arr2, m, n):
        """Return true if arr2[] is a subset of arr1[]"""
        hset = set()

        # hset stores all the values of arr1
        for i in range(m):
            if arr1[i] not in hset:
                hset.add(arr1[i])

        # loop to check if all elements of arr2 also lies in arr1
        for i in range(n):
            if arr2[i] not in hset:
                return False
        return True


if __name__ == '__main__':
    # Output: arr2 is subset of arr1
    print("\nMethod 1 (Simple)")
    test = ArraySubset()
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]

    m, n = len(arr1), len(arr2)
    if test.is_subset(arr1, arr2, m, n):
        print("arr2[] is subset of arr1")
    else:
        print("arr2[] is not a subset of arr1")

    print("\nMethod 2 (Use Sorting and Binary Search)")
    test = ArraySubset2()
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]
    m, n = len(arr1), len(arr2)

    if test.is_subset(arr1, arr2, m, n):
        print("arr2[] is subset of arr1")
    else:
        print("arr2[] is not a subset of arr1")

    print("\nMethod 3 (Use Sorting and Merging )")
    test = ArraySubset3()
    # Output: arr2 is a subset of arr1
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]
    m, n = len(arr1), len(arr2)
    if test.is_subset(arr1, arr2, m, n):
        print("arr2[] is subset of arr1")
    else:
        print("arr2[] is not a subset of arr1")

    print("\nMethod 4 (Use Hashing)")
    test = ArraySubset4()
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]
    m, n = len(arr1), len(arr2)
    if test.is_subset(arr1, arr2, m, n):
        print("arr2 is a subset of arr1")
    else:
        print("arr2 is not a subset of arr1")
