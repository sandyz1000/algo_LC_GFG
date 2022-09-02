"""Find the row with maximum number of 1s

Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s.

Example:
------------

Input matrix
0 1 1 1
0 0 1 1
1 1 1 1  # this row has maximum 1s
0 0 0 0

Output: 2  """

from __future__ import print_function

R = 4
C = 4


def first(arr, low, high):
    """
    A function to find the index of first index of 1 in a boolean array arr[]
    :param arr: list(int)
    :param low: int
    :param high: int
    :return:
    """
    if high >= low:
        # get the middle index
        mid = low + (high - low) // 2
        # check if the element at middle index is first 1
        if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
            return mid
        # if the element is 0, recur for right side
        elif arr[mid] == 0:
            return first(arr, (mid + 1), high)
        else:  # If element is not first 1, recur for left side
            return first(arr, low, (mid - 1))
    return -1


def row_with_max1s_method1(mat):
    """
    Method-1

    A simple method is to do a row wise traversal of the matrix, count the number of 1s in each row
    and compare the count with max. Finally, return the index of row with maximum 1s. The time
    complexity of this method is O(m*n) where m is number of rows and n is number of columns in
    matrix.
    We can do better. Since each row is sorted, we can use Binary Search to count of 1s in each row.
    We find the index of first instance of 1 in each row. The count of 1s will be equal to total
    number of columns minus the index of first 1.

    The main function that returns index of row with maximum number of 1s.
    Time Complexity: O(mLogn) where m is number of rows and n is number of columns in matrix.
    """
    max_row_index = 0
    maximum = -1  # Initialize max values

    # Traverse for each row and count number of 1s by finding the index of first 1
    for i in range(R):
        index = first(mat[i], 0, C - 1)
        if index != -1 and C - index > maximum:
            maximum = C - index
            max_row_index = i

    return max_row_index


def row_with_max1s_method2(mat):
    """
    Method-2
    Instead of doing binary search in every row, we first check whether the row has more 1s than max
    so far. If the row has more 1s, then only count 1s in the row. Also, to count 1s in a row,
    we don’t do binary search in complete row, we do search in before the index of last max.

    The worst case time complexity of the above optimized version is also O(mLogn),
    this solution will work better on average."""
    # Initialize max using values from first row.
    max_row_index = 0
    maximum = first(mat[0], 0, C - 1)

    # Traverse for each row and count number of 1s by finding the index of first 1
    for i in range(1, R):
        # Count 1s in this row only if this row has more 1s than max so far
        if maximum != -1 and mat[i][C - maximum - 1] == 1:
            # Note the optimization here also
            index = first(mat[i], 0, C - maximum)
            if index != -1 and C - index > maximum:
                maximum = C - index
                max_row_index = i
        else:
            maximum = first(mat[i], 0, C - 1)

    return max_row_index


if __name__ == '__main__':
    mat = [[0, 0, 0, 1],
           [0, 1, 1, 1],
           [1, 1, 1, 1],
           [0, 0, 0, 0]]
    print("\nPrint method-1--------\n")
    print("Index of row with maximum 1s is %d n" % row_with_max1s_method1(mat))

    print("\nPrint method-2--------\n")
    print("Index of row with maximum 1s is %d n" % row_with_max1s_method2(mat))
