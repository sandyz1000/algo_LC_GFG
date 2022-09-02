"""
Minimum Cost Polygon Triangulation
https://www.geeksforgeeks.org/minimum-cost-polygon-triangulation/

A triangulation of a convex polygon is formed by drawing diagonals between non-adjacent vertices (corners)
such that the diagonals never intersect. The problem is to find the cost of triangulation with the minimum cost.
The cost of a triangulation is sum of the weights of its component triangles. Weight of each triangle is its
perimeter (sum of lengths of all sides)

See following example taken from this source (REFER IMAGE FROM SOURCE).

:!:!:......::::................:!:!:.....:::!:..............
:::!:::::::::::................:::!:::::::::::..............
..%&@@@@@@@&&@*:.................@@@@@@@@@&&$*:.............
..$&&&&&&&&&&&&&$*:..............@&&&&&&&&&&&&@$!:..........
..$&&&&&&&&&&&&&&&&$*:...........@&&&&&&&&&&&&&&&@%!:.......
..$&&&&&&&&&&&&&&&&&&@$*:::::....@&&&&&&&&&&&&&&&&&&@%!:::::
..$&&&&&&&&&&&&&&&&&&&&$!::::....@&&&&&&&&&&&&&&&&&&&@%:::::
..$&&&&&&&&&&&&&&&&&$*:..........@&&&&&&&&&&&&&&&&@%!.......
..$&&&&&&&&&&&&&&$*:.............@&&&&&&&&&&&&&@$!:.........
..$#&&&&&&&&&&$*:................&#&&&&&&&&&&$*:............
.:!**********!..................:***********:...............
:!:!:......::!!................:!:!:.....:::!:..............


Two triangulations of the same convex pentagon. The triangulation on the left has a cost of 8 + 2√2 + 2√5
(approximately 15.30), the one on the right has a cost of 4 + 2√2 + 4√5 (approximately 15.77).

Solution:
=========

This problem has recursive substructure. The idea is to divide the polygon into three parts: a single triangle,
the sub-polygon to the left, and the sub-polygon to the right. We try all possible divisions like this and find
the one that minimizes the cost of the triangle plus the cost of the triangulation of the two sub-polygons.

------------------------------------------------------------------------
Let Minimum Cost of triangulation of vertices from i to j be minCost(i, j)
If j < i + 2 Then
  minCost(i, j) = 0
Else:
  minCost(i, j) = Min { minCost(i, k) + minCost(k, j) + cost(i, k, j) }
                  Here k varies from 'i+1' to 'j-1'

Cost of a triangle formed by edges (i, j), (j, k) and (k, i) is
  cost(i, j, k)  = dist(i, j) + dist(j, k) + dist(k, i)
------------------------------------------------------------------------

The above problem is similar to Matrix Chain Multiplication. The following is recursion tree for mTC(points[], 0, 4).

                                (0, 4)
                      /     /       |    \     \
                   (0,1)  (1,4)     (0,2) (0,3) (3,4)
                        /   / \  \   
                    (1,2)(2,4)(1,3)(3,4)  
It can be easily seen in the above recursion tree that the problem has many overlapping subproblems. 
Since the problem has both properties: Optimal Substructure and Overlapping Subproblems, it can be efficiently
solved using dynamic programming.

"""
from typing import List, Tuple
from math import sqrt
import sys
# Recursive implementation for minimum cost convex polygon triangulation

MAX = sys.maxsize


def dist(p1: Tuple[int], p2: Tuple[int]):
    # A utility function to find distance between two points in a plane
    # sqrt((x1-x2)**2 + (y1-y2)**2)
    return sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) +
                (p1[1] - p2[1]) * (p1[1] - p2[1]))


def cost(points: List[Tuple[int]], i: int, j: int, k: int):
    # A utility function to find cost of a triangle. The cost is considered
    # as perimeter (sum of lengths of all edges) of the triangle
    p1 = points[i]
    p2 = points[j]
    p3 = points[k]
    return dist(p1, p2) + dist(p2, p3) + dist(p3, p1)


def mTC(points: List[Tuple[int]], i: int, j: int):
    """
    A recursive function to find minimum cost of polygon triangulation
    The polygon is represented by points[i..j].
    """
    # There must be at least three points between i and j (including i and j)
    if (j < i + 2):
        return 0

    # Initialize result as infinite
    res = MAX

    # Find minimum triangulation by considering all
    for k in range(i + 1, j):
        res = min(res, (mTC(points, i, k) +
                        mTC(points, k, j) +
                        cost(points, i, k, j)))

    return round(res, 4)


# A Dynamic programming based function to find minimum cost for convex polygon triangulation.
# Time complexity of the above dynamic programming solution is O(n3).
def mTCDP(points: List[Tuple[int]], n: int):
    # There must be at least 3 points to form a triangle
    if (n < 3):
        return 0

    # table to store results of subproblems. table[i][j] stores cost of triangulation of points from i to j.
    # The entry table[0][n-1] stores the final result.
    table = [[n for _ in range(n)] for _ in range(n)]

    # Fill table using above recursive formula. Note that the table is filled in diagonal fashion
    # i.e., from diagonal elements to table[0][n-1] which is the result.
    for gap in range(n):
        i, j = 0, gap
        while j < n:
            if (j < i + 2):
                table[i][j] = 0.0
            else:
                table[i][j] = MAX
                for k in range(i + 1, j):
                    val = table[i][k] + table[k][j] + cost(points, i, j, k)
                    if (table[i][j] > val):
                        table[i][j] = val
            i += 1
            j += 1
    return round(table[0][n - 1], 4)


if __name__ == "__main__":
    points = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]]
    n = len(points)
    print(mTC(points, 0, n - 1))
    print(mTCDP(points, n))
