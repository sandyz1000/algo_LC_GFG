"""
Given a rod of length n inches and an array of prices that contains prices of all pieces of
size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the
pieces.

For example,
==============================
If length of the rod is 8 and the values of different pieces are given as
following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight
pieces of length 1)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 3   5   8   9  10  17  17  20

cR() ---> cutRod()

                             cR(4)
                  /        /
                 /        /
             cR(3)       cR(2)     cR(1)   cR(0)
            /  |         /         |
           /   |        /          |
      cR(2) cR(1) cR(0) cR(1) cR(0) cR(0)
     /        |          |
    /         |          |
  cR(1) cR(0) cR(0)      cR(0)
   /
 /
CR(0)

In the above partial recursion tree, cR(2) is being solved twice. We can see that there are many
sub problems which are solved again and again. Since same suproblems are called again,
this problem has Overlapping Subprolems property. So the Rod Cutting problem has both properties
(see this and this) of a dynamic programming problem. Like other typical Dynamic Programming(DP)
problems, re-computations of same subproblems can be avoided by constructing a temporary array
val[] in bottom up manner.

"""
from typing import List, Tuple
import sys
from functools import lru_cache
INT_MIN = -sys.maxsize


def cut_rod_rec(price: List[int], n: int):
    """
    Returns the best obtainable price for a rod of length n and
    price[] as prices of different pieces

    :param price: int
    :param n: int
    :return:
    """
    if n <= 0:
        return 0
    max_val = INT_MIN

    # Recursively cut the rod in different pieces and compare different configurations
    for i in range(n):
        max_val = max(max_val, price[i] + cut_rod_rec(price, n - i - 1))

    return max_val


def cut_rod_dp(price, n):
    """
    A Dynamic Programming solution for Rod cutting problem Returns the best obtainable price for
    a rod of length n and price[] as prices of different pieces

    Time Complexity is O(n^2)

    :param price: int
    :param n: int
    :return:
    """
    val = [0 for x in range(n + 1)]
    val[0] = 0

    # Build the table val[] in bottom up manner and return the last entry from the table
    for i in range(1, n + 1):
        max_val = INT_MIN
        for j in range(i):
            max_val = max(max_val, price[j] + val[i - j - 1])
        val[i] = max_val

    return val[n]


if __name__ == '__main__':
    # arr = [1, 5, 8, 9, 10, 17, 17, 20]
    pieces = [1, 2, 3, 4, 5, 6, 7, 8]
    arr = [2, 5, 6, 9, 16, 17, 17, 20]
    size = len(arr)
    print("Maximum Obtainable Value is " + str(cut_rod_rec(arr, size)))
