"""Find the minimum cost to reach destination using a train

There are N stations on route of a train. The train goes from station 0 to N-1. The ticket cost for
all pair of stations (i, j) is given where j is greater than i. Find the minimum cost to reach
the destination.

Consider the following example:

Input:
cost = [[0, 15, 80, 90],
        [INF, 0, 40, 50],
        [INF, INF, 0, 70],
        [INF, INF, INF, 0]]

There are 4 stations and cost[i][j] indicates cost to reach j from i.
The entries where j < i are meaningless.

Output:
The minimum cost is 65
The minimum cost can be obtained by first going to station 1 from 0.
Then from station 1 to station 3."""

from __future__ import print_function
# Python program to find min cost path from station 0 to station N-1

# Time complexity of the above implementation is exponential as it tries every possible path from
#  0 to N-1. The above solution solves same subrpoblems multiple times (it can be seen by drawing
#  recursion tree for minCostPathRec(0, 5).

import sys

N = 4
INF = sys.maxsize


def minCostRec(cost, s, d):
    if s == d or s + 1 == d:
        return cost[s][d]

    min = cost[s][d]

    for i in range(s + 1, d):
        c = minCostRec(cost, s, i) + minCostRec(cost, i, d)
        if c < min:
            min = c
    return min


def min_cost(cost):
    return minCostRec(cost, 0, N - 1)


if __name__ == '__main__':
    # Output: The Minimum cost to reach station 4 is 65
    cost = [[0, 15, 80, 90],
            [INF, 0, 40, 50],
            [INF, INF, 0, 70],
            [INF, INF, INF, 0]]
    print("The Minimum cost to reach station %d is %d" % (N, min_cost(cost)))
