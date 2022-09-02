"""Dynamic Programming | Set 18 (Partition problem)

Partition problem is to determine whether a given set can be partitioned into two subsets such
that the sum of elements in both subsets is same.

----------------------------------------------
Examples
----------------------------------------------

arr[] = {1, 5, 11, 5}
Output: true
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false
The array cannot be partitioned into equal sum sets.

----------------------------------------------
Algorithm:
----------------------------------------------

Following are the two main steps to solve this problem:
1)  Calculate sum of the array. If sum is odd, there can not be two subsets with equal
    sum, so return false.
2)  If sum of array elements is even, calculate sum/2 and find a subset of array with
    sum equal to sum/2.

Following are the two main steps to solve this problem:
1)  Calculate sum of the array. If sum is odd, there can not be two subsets with equal sum, so
    return false.
2)  If sum of array elements is even, calculate sum/2 and find a subset of array with sum equal to
    sum/2.

The first step is simple. The second step is crucial, it can be solved either using recursion or
Dynamic Programming."""


def is_subset_sum(arr, n, summation):
    """
    A utility function that returns true if there is
    a subset of arr[] with sun equal to given sum

    Time Complexity: O(2^n) In worst case, this solution tries two possibilities
    (whether to include or exclude) for every element.
    :param arr: list(int)
    :param n: int
    :param sum: int
    :return: bool
    """
    # Base Cases
    if (summation == 0):
        return True

    if not n and summation:
        return False

    # If last element is greater than sum, then ignore it
    if arr[n - 1] > summation:
        return is_subset_sum(arr, n - 1, summation)

    # else, check if sum can be obtained by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return is_subset_sum(arr, n - 1, summation) or is_subset_sum(arr, n - 1, summation - arr[n - 1])


def find_partiion_rec(arr, n):
    """
    Returns true if arr[] can be partitioned in two subsets of equal summ, otherwise false
    :param arr:
    :param n:
    :return:
    """
    # Calculate summ of the elements in _array
    summ = sum(arr)

    # If summ is odd, there cannot be two subsets with equal summ
    if summ % 2:
        return False

    # Find if there is subset with summ equal to half of total summ
    return is_subset_sum(arr, n, summ / 2)


def find_partiion_dp(arr, n):
    """
    Returns true if arr[] can be partitioned in two subsets of
    equal summ, otherwise false
    Time Complexity: O(summ*n)
    Auxiliary Space: O(summ*n)
    :param arr: list(int)
    :param n: int
    :return: bool
    """
    summ = 0
    # int i, j;

    # Caculcate sun of all elements
    # for i in range(n):
    #     summ += arr[i]
    summ = sum(arr)

    if summ % 2:
        return False

    part = [[False] * (n + 1) for j in range((summ // 2 + 1))]

    # initialize top row as true
    for i in range(n + 1):
        part[0][i] = True

    # initialize leftmost column, except part[0][0], as 0
    # for i in range(1, summ // 2 + 1):
    #     part[i][0] = False

    # Fill the partition table in botton up manner
    for i in range(1, summ // 2 + 1):
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
            if i >= arr[j - 1]:
                part[i][j] = part[i][j] or part[i - arr[j - 1]][j - 1]

    # uncomment this part to print table
    for i in range(1, summ // 2 + 1):
        output = []
        for j in range(n + 1):
            output.append("%d" % part[i][j])
        print(output)

    return part[summ // 2][n]


if __name__ == '__main__':
    arr = [3, 1, 5, 9, 12]
    arr = [3, 1, 1, 2, 2, 1]
    n = len(arr)
    if find_partiion_dp(arr, n):
        print("Can be divided into two subsets of equal sum")
    else:
        print("Can not be divided into two subsets of equal sum")
