"""
Given an array arr[], find the maximum j - i such that arr[j] > arr[i]

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Input: [34, 8, 10, 3, 2, 80, 30, 33, 1]
Output: 6  (j = 7, i = 1)

Input: [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
Output: 8 ( j = 8, i = 0)

Input:  [1, 2, 3, 4, 5, 6]
Output: 5  (j = 5, i = 0)

Input:  [6, 5, 4, 3, 2, 1]
Output: -1
"""


def max_index_diff(arr, n):
    """
    Method 2 (Efficient)

    To solve this problem, we need to get two optimum indexes of arr[]: left index i and right
    index j. For an element arr[i], we do not need to consider arr[i] for left index if there is
    an element smaller than arr[i] on left side of arr[i]. Similarly, if there is a greater
    element on right side of arr[j] then we do not need to consider this j for right index. So we
    construct two auxiliary arrays LMin[] and RMax[] such that LMin[i] holds the smallest element
    on left side of arr[i] including arr[i], and RMax[j] holds the greatest element on right side
    of arr[j] including arr[j]. After constructing these two auxiliary arrays, we traverse both
    of these arrays from left to right. While traversing LMin[] and RMa[] if we see that LMin[i]
    is greater than RMax[j], then we must move ahead in LMin[] (or do i++) because all elements
    on left of LMin[i] are greater than or equal to LMin[i]. Otherwise we must move ahead in
    RMax[j] to look for a greater j - i value.

    For a given array arr[], returns the maximum j - i such that arr[j] > arr[i]
    Time Complexity: O(n)
    Auxiliary Space: O(n)
    """
    LMin = [0] * n
    RMax = [0] * n

    # Construct LMin[] such that LMin[i] stores the minimum value from (arr[0], arr[1], ...arr[i])
    LMin[0] = arr[0]
    for i in range(1, n):
        LMin[i] = min(arr[i], LMin[i - 1])

    # Construct RMax[] such that RMax[j] stores the maximum value from
    # (arr[j], arr[j+1], ..arr[n-1])
    RMax[n - 1] = arr[n - 1]
    for j in range(n - 2, -1, -1):
        RMax[j] = max(arr[j], RMax[j + 1])

    # Traverse both arrays from left to right to find optimum j - i This process is similar to
    # merge() of MergeSort
    i, j, max_diff = 0, 0, -1
    while j < n and i < n:
        if LMin[i] < RMax[j]:
            max_diff = max(max_diff, j - i)
            j = j + 1
        else:
            i = i + 1
    return max_diff


if __name__ == '__main__':
    # arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
    arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
    # arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    maxDiff = max_index_diff(arr, n)
    print("%d" % maxDiff)
