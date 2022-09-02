"""

Given an array of integers where each element represents the max number of steps that can be
made forward from that element. Write a function to return the minimum number of jumps to reach
the end of the array (starting from the first element). If an element is 0, then cannot move
through that element. """
import sys
INF = sys.maxsize


def min_jumps(arr, l, h):
    """
    Returns minimum number of jumps to reach arr[h] from arr[l]
    :param arr: list
    :param l: int
    :param h: int
    :return:
    """
    # Base case: when source and destination are same
    if h == l:
        return 0

    # When nothing is reachable from the given source
    if arr[l] == 0:
        return INF

    # Traverse through all the points reachable from arr[l]. Recursively
    # get the minimum number of jumps needed to reach arr[h] from these
    # reachable points.
    minimum = INF
    i = l + 1
    while i <= h and i <= l + arr[l]:
        jumps = min_jumps(arr, i, h)
        if jumps != INF and jumps + 1 < minimum:
            minimum = jumps + 1
        i += 1

    return minimum


def min_jumps_dp(arr, n):
    """
    Dynamic programming approach Returns minimum number of jumps to reach arr[n-1] from arr[0]
    Time Complexity: O(n^2) in worst case.
    :param arr:
    :param n:
    :return:
    """
    jumps = [0] * n  # jumps[n-1] will hold the result

    if n == 0 or arr[0] == 0:
        return INF

    jumps[0] = 0

    # Find the minimum number of jumps to reach arr[i] from arr[0],
    # and assign this value to jumps[i]
    for i in range(1, n):
        jumps[i] = INF
        for j in range(i):
            if i <= j + arr[j] and jumps[j] != INF:
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n - 1]


if __name__ == '__main__':
    arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
    size = len(arr)
    print("Minimum number of jumps to reach end is %d " % min_jumps(arr, 0, size-1))
    print("Minimum number of jumps to reach end is %d " % min_jumps_dp(arr, size))
