"""Rotate Matrix Elements

Given a matrix, clockwise rotate elements in it.

Examples:
---------------------
Input
1    2    3
4    5    6
7    8    9

Output:
4    1    2
7    5    3
8    9    6

For 4*4 matrix
Input:
1    2    3    4
5    6    7    8
9    10   11   12
13   14   15   16

Output:
5    1    2    3
9    10   6    4
13   11   7    8
14   15   16   12

------------------------------------------
Explanation:
------------------------------------------
The idea is to use loops similar to the program for printing a matrix in spiral form. One by one
rotate all rings of elements, starting from the outermost. To rotate a ring, we need to do
following.
1) Move elements of top row.
2) Move elements of last column.
3) Move elements of bottom row.
4) Move elements of first column.
Repeat above steps for inner ring while there is an inner ring. """

from __future__ import print_function


# Python program to rotate a matrix
def rotate_matrix(mat):
    """Function to rotate a matrix"""
    if not len(mat):
        return

    """
        top : starting row index
        bottom : ending row index
        left : starting column index
        right : ending column index
    """

    top = 0
    bottom = len(mat) - 1

    left = 0
    right = len(mat[0]) - 1

    while left < right and top < bottom:

        # Store the first element of next row,
        # this element will replace first element of
        # current row
        prev = mat[top + 1][left]

        # Move elements of top row one step right
        for i in range(left, right + 1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr

        top += 1

        # Move elements of rightmost column one step downwards
        for i in range(top, bottom + 1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr

        right -= 1

        # Move elements of bottom row one step left
        for i in range(right, left - 1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr

        bottom -= 1

        # Move elements of leftmost column one step upwards
        for i in range(bottom, top - 1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr

        left += 1

    return mat


# Utility Function
def print_matrix(mat):
    for row in mat:
        print(row)


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    # Test case 2
    # matrix = [[1, 2, 3],
    #           [4, 5, 6],
    #           [7, 8, 9]]

    matrix = rotate_matrix(matrix)
    # Print modified matrix
    print_matrix(matrix)
