"""
Program to print Lower triangular and Upper triangular matrix of an array
Prerequisite – Multidimensional Arrays in Python

Given a two dimensional array, Write a program to print lower triangular matrix and upper
triangular matrix.

1)  Lower triangular matrix is a matrix which contain elements below principle diagonal including
    principle diagonal elements and rest of the elements are 0.
2)  Upper triangular matrix is a matrix which contain elements above principle diagonal including
    principle diagonal elements and rest of the elements are 0.

    Lower traingle

    [A(0, 0) 0  0   0 .... 0
    A(1, 0) A(1,1) 0   0 .... 0
    A(2, 0) A(2,1)  A(2, 2) 0 .... 0
    A(3, 0) A(3,1)  A(3,2)  A(3,3) .... 0
    .   ......
    .   ......
    .   ......
    A(row, 0)   A(row, 1)   A(row,2).... A(row, col)]


    Upper traingle

    [A(0,0)  A(0,1)   A(0, 2)  ... A(0, col)
    0   A(1,2)  A(1,2) ... A(1,col)
    0   0   A(2,2)  ... A(2,col)
    .   ......
    .   ......
    .   ......s
    0   0   0   .....   A(row,col)]

Algorithm:
--------------------
1.  For lower triangular matrix, we check the index position i and j i.e row and column
    respectively. If column position is greater than row position we simply make that position 0.
2.  For upper triangular matrix, we check the index position i and j i.e row and column
    respectively. If column position is smaller than row position we simply make that position 0.
"""

from __future__ import print_function


# Python program to print Lower triangular and Upper triangular matrix of an array


def lower(matrix, row, col):
    """Function to form lower triangular matrix"""
    for i in range(row):
        output = []
        for j in range(col):
            if i < j:
                matrix[i][j] = 0
            output.append(matrix[i][j])
        print(output)


def upper(matrix, row, col):
    """Function to form upper triangular marix"""
    for i in range(row):
        output = []
        for j in range(col):
            if i > j:
                matrix[i][j] = 0
            output.append(matrix[i][j])
        print(output)


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    row, col = 3, 3

    print("\nLower triangular matrix:")
    lower(matrix, row, col)

    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print("\nUpper triangular matrix:")
    upper(matrix, row, col)
