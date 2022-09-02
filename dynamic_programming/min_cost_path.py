"""
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns
cost of minimum cost path to reach (m, n) from (0, 0). Each cell of the matrix represents a cost
to traverse through that cell. Total cost of a path to reach (m, n) is sum of all the costs on
that path (including both source and destination). You can only traverse down, right and
diagonally lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j), (i,
j+1) and (i+1, j+1) can be traversed. You may assume that all costs are positive integers.

mC refers to minCost()
                                    mC(2, 2)
                          /            |           \
                         /             |            \
                 mC(1, 1)           mC(1, 2)             mC(2, 1)
              /     |     \       /     |     \           /     |     \
             /      |      \     /      |      \         /      |       \
       mC(0,0) mC(0,1) mC(1,0) mC(0,1) mC(0,2) mC(1,1) mC(1,0) mC(1,1) mC(2,0)
"""
R = 3
C = 3


def min_cost(cost, m, n):
    """
    Instead of following line, we can use int tc[m+1][n+1] or dynamically allocate memory
    to save space.
    The following line is used to keep te program simple and make it working on all compilers.
    :param cost:
    :param m:
    :param n:
    :return:
    """
    tc = [[0 for x in range(C)] for x in range(R)]

    tc[0][0] = cost[0][0]

    # Initialize first column of total cost(tc) arr
    for i in range(1, m + 1):
        tc[i][0] = tc[i - 1][0] + cost[i][0]

    # Initialize first row of tc arr
    for j in range(1, n + 1):
        tc[0][j] = tc[0][j - 1] + cost[0][j]

    # Construct rest of the tc arr
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tc[i][j] = min(tc[i - 1][j - 1], tc[i - 1][j], tc[i][j - 1]) + cost[i][j]

    return tc[m][n]


if __name__ == '__main__':
    cost = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]
    print(min_cost(cost, 2, 2))
