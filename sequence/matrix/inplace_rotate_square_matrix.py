"""
Method-1
-------------------------------------------------
Inplace rotate square matrix by 90 degrees | Set 1
Given an square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra
space.

Examples:
------------------------

Input
 1  2  3
 4  5  6
 7  8  9

Output:
 3  6  9
 2  5  8
 1  4  7

Input:
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16

Output:
 4  8 12 16
 3  7 11 15
 2  6 10 14
 1  5  9 13

Explanation:
------------------------
How to do without extra space?
Below are some important observations.

First row of source -> First column of destination, elements filled in opposite order
Second row of source -> Second column of destination, elements filled in opposite order
so.. on
Last row of source -> Last column of destination, elements filled in opposite order.

An N x N matrix will have floor(N/2) square cycles. For example, a 4 X 4 matrix will have 2 cycles.
The first cycle is formed by its 1st row, last column, last row and 1st column. The second cycle is
formed by 2nd row, second-last column, second-last row and 2nd column.

The idea is for each square cycle, we swap the elements involved with the corresponding cell in the
matrix in anti-clockwise direction i.e. from top to left, left to bottom, bottom to right and from
right to top one at a time. We use nothing but a temporary variable to achieve this.

Method-2
------------------------------------------------------------
Rotate a matrix by 90 degree without using any extra space | Set 2

Explanation:-
There are two steps :
1) Find transpose of matrix.
2) Reverse columns of the transpose.

"""
import typing


N = 4
R, C = 4, 4
            

# Python program to rotate a matrix by 90 degrees
def rotate_matrix(mat: typing.List[typing.List[int]]):
    """An Inplace function to rotate a N x N matrix by 90 degrees in anti-clockwise direction"""
    # Consider all squares one by one
    for x in range(N // 2):
        # Consider elements in group of 4 in current square
        for y in range(x, N - x - 1):
            # store current cell in temp variable
            temp = mat[x][y]
            # move values from right to top
            mat[x][y] = mat[y][N - 1 - x]
            # move values from left to bottom
            mat[y][N - 1 - x] = mat[N - 1 - x][N - 1 - y]
            # move values from bottom to right
            mat[N - 1 - x][N - 1 - y] = mat[N - 1 - y][x]
            # assign temp to left
            mat[N - 1 - y][x] = temp


def display_matrix(mat):
    """Function to print the matrix"""
    for i in range(N):
        print(mat[i])


# Method-2
# Python program for left rotation of matrix by 90 degree without using extra space
# After transpose we swap elements of column one by one for finding left rotation of matrix
# by 90 degree

def reverse_columns(arr):
    for i in range(C):
        j, k = 0, C - 1
        while j < k:
            arr[j][i], arr[k][i] = arr[k][i], arr[j][i]
            j += 1
            k -= 1


def transpose(arr):
    """Function for do transpose of matrix"""
    for i in range(R):
        for j in range(i, C):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


def print_matrix(arr):
    """Function for print matrix"""
    for i in range(R):
        for j in range(C):
            print(arr[i][j])
        print('\n')


def rotate_90(arr):
    """Function to anticlockwise rotate matrix by 90 degree"""
    transpose(arr)
    reverse_columns(arr)


# Method - 3 
def rotate(pS, pD, r, c):
    for row in range(r):
        for col in range(c):
            pD[c - col - 1][row] = pS[row][col]


if __name__ == '__main__':
    # Test Case 1
    print("\n----- Method-1 ------\n")
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]

    # mat = [[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]]

    # mat = [[1, 2],
    #        [4, 5]]

    rotate_matrix(mat)
    display_matrix(mat)

    # Method-2
    print("\n----- Method-2 ------\n")
    arr = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
    rotate_90(arr)
    display_matrix(arr)

    # Method-3 (using extra space)
    arr = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
    R, C = 4, 4
    pDest = [[0 for _ in range(C)] for _ in range(R)]
    rotate(arr, pDest, R, C)
    display_matrix(pDest)
