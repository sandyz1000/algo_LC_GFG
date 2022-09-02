"""
Maximum difference between two elements such that larger element appears after the smaller number
Given an array arr[] of integers, find out the difference between any two elements such that larger
element appears after the smaller number in arr[].

Examples:
If array is [2, 3, 10, 6, 4, 8, 1] then returned value should be 8 (Diff between 10 and 2).
If array is [ 7, 9, 5, 6, 3, 2 ] then returned value should be 2 (Diff between 7 and 9)

----------------------------------------------------------------
Method 2 (Tricky and Efficient)
----------------------------------------------------------------
In this method, instead of taking difference of the picked element with every other element,
we take the difference with the minimum element found so far. So we need to keep track of 2 things:

1)  Maximum difference found so far (max_diff).
2)  Minimum number visited so far (min_element)

"""


def max_diff(arr, arr_size):
    """
    The function assumes that there are at least two elements in array. The function returns a
    negative value if the array is sorted in decreasing order. Returns 0 if elements are equal

    :param arr: list(int)
    :param arr_size: int
    :return:
    """
    max_diff_var = arr[1] - arr[0]
    min_element = arr[0]
    for i in range(1, arr_size):
        if arr[i] - min_element > max_diff_var:
            max_diff_var = arr[i] - min_element
        if arr[i] < min_element:
            min_element = arr[i]
    return max_diff_var


if __name__ == '__main__':
    arr = [1, 2, 6, 80, 100]
    # arr = [7, 9, 5, 6, 3, 2]
    size = len(arr)
    print("Maximum difference is %d" % max_diff(arr, size))
