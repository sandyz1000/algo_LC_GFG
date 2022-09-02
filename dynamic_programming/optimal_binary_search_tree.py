"""

Dynamic Programming | Set 24 (Optimal Binary Search Tree)

Given a sorted array keys[0.. n-1] of search keys and an array freq[0.. n-1] of frequency
counts, where freq[i] is the number of searches to keys[i]. Construct a binary search tree of all
keys such that the total cost of all the searches is as small as possible.

Let us first define the cost of a BST. The cost of a BST node is level of that node multiplied by
its frequency. Level of root is 1.

Example 1
Input:  keys[] = {10, 12}, freq[] = {34, 50}
There can be following two possible BSTs
        10                       12
          \                     /
           12                 10
          I                     II

Frequency of searches of 10 and 12 are 34 and 50 respectively.
The cost of tree I is 34*1 + 50*2 = 134
The cost of tree II is 50*1 + 34*2 = 118

Example 2
Input:  keys[] = {10, 12, 20}, freq[] = {34, 8, 50}

There can be following possible BSTs

    10                12                 20         10              20
      \             /    \              /             \            /
      12          10     20           12               20         10
        \                            /                 /           \
         20                        10                12             12
     I               II             III             IV             V

Among all possible BSTs, cost of the fifth BST is minimum.
Cost of the fifth BST is 1*50 + 2*34 + 3*8 = 142

Notes:
1) The time complexity of the above solution is O(n^4). The time complexity can be easily
reduced to O(n^3) by pre-calculating sum of frequencies instead of calling sum() again and again.

2) In the above solutions, we have computed optimal cost only. The solutions can be easily
modified to store the structure of BSTs also. We can create another auxiliary array of size n to
store the structure of tree. All we need to do is, store the chosen 'r' in the innermost loop.

"""
from __future__ import print_function

import sys

INF = sys.maxsize


class BinarySearchTree(object):
    """
    1) Optimal Substructure:
    The optimal cost for freq[i..j] can be recursively calculated using following formula.
    optcost

    - - - - - - - - - - - - - - - - - - - - -
    optCost(i, j) = sum([freq[k] + (r = i...j) min(optCost(i, r-1), optCost(r+1, j)) for k
    in range(i, j+1)])
    - - - - - - - - - - - - - - - - - - - - -

    We need to calculate optCost(0, n-1) to find the result.
    The idea of above formula is simple, we one by one try all nodes as root (r varies from i to
    j in second term). When we make rth node as root, we recursively calculate optimal cost from
    i to r-1 and r+1 to j.
    We add sum of frequencies from i to j (see first term in the above formula), this is added
    because every search will go through root and one comparison will be done for every search.

    2) Overlapping Subproblems

    Time complexity of the above naive recursive approach is exponential. It should be noted that
    the above function computes the same subproblems again and again. We can see many subproblems
    being repeated in the following recursion tree for freq[1..4].

    Since same suproblems are called again, this problem has Overlapping Subprolems property. So
    optimal BST problem has both properties (see this and this) of a dynamic programming problem.
    Like other typical Dynamic Programming(DP) problems, recomputations of same subproblems can
    be avoided by constructing a temporary array cost[][] in bottom up manner.
    """

    def opt_cost(self, freq, i, j):
        """
        # A recursive function to calculate cost of optimal binary search tree
        :param freq:
        :param i:
        :param j:
        :return:
        """
        # Base cases
        if j < i:  # If there are no elements in this sub array
            return 0

        if j == i:  # If there is one element in this sub array
            return freq[i]

        # Get sum of freq[i], freq[i+1], ... freq[j]
        fsum = sum(freq[i:j + 1])

        # Initialize minimum value
        minimum = INF

        # One by one consider all elements as root and recursively find cost
        # of the BST, compare the cost with minimum and update minimum if needed
        for r in range(i, j + 1):
            cost = self.opt_cost(freq, i, r - 1) + self.opt_cost(freq, r + 1, j)
            if cost < minimum:
                minimum = cost

        # Return minimum value
        return minimum + fsum

    def optimal_search_tree(self, keys, freq, n):
        """
        The main function that calculates minimum cost of a Binary Search Tree.
        It mainly uses optCost() to find the optimal cost.
        :param keys: list(int)
        :param freq: list(int)
        :param n: int
        :return:
        """
        # Here array keys[] is assumed to be sorted in increasing order.
        # If keys[] is not sorted, then add code to sort keys, and rearrange
        # freq[] accordingly.
        return self.opt_cost(freq, 0, n - 1)


class BinaryTreeTreeDP(object):
    """
    Dynamic Programming Solution

    Following is C/C++ implementation for optimal BST problem using Dynamic Programming. We use
    an auxiliary array cost[n][n] to store the solutions of subproblems. cost[0][n-1] will hold
    the final result. The challenge in implementation is, all diagonal values must be filled
    first, then the values which lie on the line just above the diagonal. In other words,
    we must first fill all cost[i][i] values, then all cost[i][i+1] values, then all cost[i][i+2]
    values. So how to fill the 2D array in such manner> The idea used in the implementation is
    same as Matrix Chain Multiplication problem, we use a variable 'L' for chain length and
    increment 'L', one by one. We calculate column number 'j' using the values of 'i' and 'L'.
    """

    def optimal_search_tree(self, keys, freq, n):
        """
        A Dynamic Programming based function that calculates minimum cost of
        a Binary Search Tree.
        :param keys: list(int)
        :param freq: list(int)
        :param n: int
        :return:
        """
        # Create an auxiliary 2D matrix to store results of subproblems
        cost = [[0 for j in range(n+1)] for i in range(n+1)]

        # cost[i][j] = Optimal cost of binary search tree that can be formed from keys[i]
        # to keys[j].
        # cost[0][n-1] will store the resultant cost

        # For a single key, cost is equal to frequency of the key
        for i in range(n):
            cost[i][i] = freq[i]

        # Now we need to consider chains of length 2, 3, ... . L is chain length.
        for L in range(2, n + 1):
            # i is row number in cost[][]
            for i in range(n - L + 2):
                # Get column number j from row number i and chain length L
                j = i + L - 1
                cost[i][j] = INF

                # Try making all keys in interval keys[i..j] as root
                for r in range(i, j + 1):
                    # c = cost when keys[r] becomes root of this subtree
                    c = (cost[i][r - 1] if r > i else 0) + (cost[r + 1][j] if r < j else 0) + \
                        sum(freq[i:j + 1])
                    if c < cost[i][j]:
                        cost[i][j] = c

        return cost[0][n - 1]


if __name__ == '__main__':
    test1 = BinarySearchTree()
    test2 = BinaryTreeTreeDP()
    keys = [10, 12, 20]
    freq = [34, 8, 50]
    key_size = len(keys)
    print("Cost of Optimal BST is %d " % test1.optimal_search_tree(keys, freq, key_size))

    print("DP: Cost of Optimal BST is %d " % test2.optimal_search_tree(keys, freq, key_size))
