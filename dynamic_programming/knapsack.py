"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the
maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[
0..n-1] which represent values and weights associated with n items respectively. Also given an
integer W which represents knapsack capacity, find out the maximum value subset of val[] such
that sum of the weights of this subset is smaller than or equal to W. You cannot break an item,
either pick the complete item, or don't pick it (0-1 property).

1) Optimal Substructure:

To consider all subsets of items, there can be two cases for every item:
(1) the item is included in the optimal subset
(2) not included in the optimal set.

Therefore, the maximum value that can be obtained from n items is max of following two values.
    1) Maximum value obtained by n-1 items and W weight (excluding nth item).
    2) Value of nth item plus maximum value obtained by n-1 items and W minus weight of the nth
    item (including nth item).

If weight of nth item is greater than W, then the nth item cannot be included and case 1 is the
only possibility.


2) Overlapping Sub-problems:

It should be noted that the above function computes the same subproblems again and again. See the
following recursion tree, K(1, 1) is being evaluated twice. Time complexity of this naive
recursive solution is exponential (2^n).

In the following recursion tree, K() refers to knapSack().  The two
parameters indicated in the following recursion tree are n and W.
The recursion tree is for following sample inputs.
wt[] = {1, 1, 1}, W = 2, val[] = {10, 20, 30}

                       K(3, 2)         ---------> K(n, W)
                   /            \
                 /                \
            K(2,2)                  K(2,1)
          /       \                  /    \
        /           \              /        \
       K(1,2)      K(1,1)        K(1,1)     K(1,0)
       /  \         /   \          /   \
     /      \     /       \      /       \
K(0,2)  K(0,1)  K(0,1)  K(0,0)  K(0,1)   K(0,0)
Recursion tree for Knapsack capacity 2 units and 3 items of 1 unit weight.

Time Complexity: O(nW) where n is the number of items and W is the capacity of knapsack.

"""
from typing import List
import numpy as np


def knap_sack_rec(W: int, wt: List[int], val: List[int], n: int):
    """
    Returns the maximum value that can be put in a knapsack of capacity W
    """
    if n == 0 or W == 0:  # Base Case
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if wt[n - 1] > W:
        return knap_sack_rec(W, wt, val, n - 1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) nth item not included
    else:
        return max(val[n - 1] + knap_sack_rec(W - wt[n - 1], wt, val, n - 1),
                   knap_sack_rec(W, wt, val, n - 1))


def knap_sack_dp(total_weight: int, weights: List[int], value: List[int], size: int):
    """
    A Dynamic Programming based Python Program for 0-1 Knapsack problem
    Returns the maximum value that can be put in a knapsack of capacity W
    """
    K = np.zeros((size + 1, total_weight + 1), dtype=int)

    # Build table K[][] in bottom up manner
    for i in range(size):
        for w in range(1, total_weight + 1):
            if weights[i] <= w:
                K[i + 1, w] = max(value[i] + K[i, w - weights[i]], K[i][w])
            else:
                K[i + 1, w] = K[i, w]
    # np.set_printoptions(suppress=False, linewidth=180)
    # print(K)
    return K[size, total_weight]


if __name__ == '__main__':
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 40
    n = len(val)
    # print(knap_sack_rec(W, wt, val, n))
    print(knap_sack_dp(W, wt, val, n))
