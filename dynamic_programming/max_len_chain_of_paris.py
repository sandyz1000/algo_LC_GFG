"""

You are given n pairs of numbers. In every pair, the first number is always smaller than the
second number. A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be
formed in this fashion. Find the longest chain which can be formed from a given set of pairs.
Source: Amazon Interview | Set 2

For example, if the given pairs are {{5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90} }, then the
longest chain that can be formed is of length 3, and the chain is {{5, 24}, {27, 40}, {50, 90}}

This problem is a variation of standard Longest Increasing Subsequence problem. Following is a
simple two step process.

1) Sort given pairs in increasing order of first (or smaller) element.
2) Now run a modified LIS process where we compare the second element of already finalized LIS with
the first element of new LIS being constructed.

"""


class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


def max_chain_length(arr, n):
    """
    This function assumes that arr[] is sorted in increasing order
    according the first (or smaller) values in pairs.
    Time Complexity: O(n^2) where n is the number of pairs.
    :param arr: list(Pair)
    :param n: int
    :return: int
    """
    i, j, maximum = 0, 0, 0

    # Initialize MCL (maximum chain length) values for all indexes
    mcl = [1] * n
    # Compute optimized chain length values in bottom up manner
    for i in range(1, n):
        for j in range(i):
            if arr[i].a > arr[j].b and mcl[i] < mcl[j] + 1:
                mcl[i] = mcl[j] + 1

    # mcl[i] now stores the maximum chain length ending with pair i

    # Pick maximum of all MCL values
    for i in range(n):
        if maximum < mcl[i]:
            maximum = mcl[i]

    return maximum


if __name__ == '__main__':
    arr = [Pair(5, 24), Pair(15, 25), Pair(27, 40), Pair(50, 60)]
    n = len(arr)
    print("Length of maximum size chain is %d\n" % max_chain_length(arr, n))