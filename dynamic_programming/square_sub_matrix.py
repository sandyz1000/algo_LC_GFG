"""
Given a binary matrix, find out the maximum size square sub-matrix with all 1s

        [   [0, 1, 1, 0, 1],
            [1, 1, 0, 1, 0],
            #  This is a sub matrix
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0],
            #  -----------------
            [0, 0, 0, 0, 0] ]

Algorithm:
Let the given binary matrix be M[R][C]. The idea of the algorithm is to construct an
auxiliary size matrix S[][] in which each entry S[i][j] represents size of the square sub-matrix
with all 1s including M[i][j] where M[i][j] is the rightmost and bottommost entry in sub-matrix.

Time Complexity: O(m*n) where m is number of rows and n is number of columns in the given matrix.
Auxiliary Space: O(m*n) where m is number of rows and n is number of columns in the given matrix.
Algorithmic Paradigm: Dynamic Programming

"""
from __future__ import print_function

R, C = 6, 5


def get_max_sub_square(M):
    """
    :param M: [[bool]]
    :return:
    """
    S = [[False] * C] * R
    # Set first column of S[][]
    for i in range(R):
        S[i][0] = M[i][0]

    # Set first row of S[][]
    for j in range(C):
        S[0][j] = M[0][j]

    # Construct other entries of S[][]
    for i in range(R):
        for j in range(C):
            if M[i][j] == 1:
                S[i][j] = min(S[i][j - 1], S[i - 1][j], S[i - 1][j - 1]) + 1
            else:
                S[i][j] = 0

    # /* Find the maximum entry, and indexes of maximum entry in S[][] */
    max_of_s, max_i, max_j = S[0][0], 0, 0
    for i in range(R):
        for j in range(C):
            if max_of_s < S[i][j]:
                max_of_s = S[i][j]
                max_i = i
                max_j = j

    print("Maximum size sub-matrix is: \n")
    for i in range(max_i, max_i - max_of_s, -1):
        for j in range(max_j, max_j - max_of_s, -1):
            print("%d " % M[i][j])
        print("\n")


if __name__ == '__main__':
    M = [[0, 1, 1, 0, 1],
         [1, 1, 0, 1, 0],
         [0, 1, 1, 1, 0],
         [1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0]]

    get_max_sub_square(M)
