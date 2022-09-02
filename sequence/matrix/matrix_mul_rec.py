"""
Matrix Multiplication | Recursive

Given two matrices A and B. The task is to multiply matrix A and matrix B recursively. If matrix
A and matrix B are not multiplicative compatible, then generate output "Not Possible".

Examples:
----------------
Input: A = 12 56
           45 78
       B = 2 6
           5 8
Output: 304 520
        480 894

Input: A = 1 2 3
           4 5 6
           7 8 9
       B = 1 2 3
           4 5 6
           7 8 9

Output: 30  36  42
        66  81  96
       102 126 150

Algorithm:
-----------------
1.  First check if multiplication between matrices is possible or not. For this, check if number of
columns of first matrix is equal to number of rows of second matrix or not. If both are equal than
proceed further otherwise generate output "Not Possible".

2.  In Recursive Matrix Multiplication, we implement three loops of Iteration through recursive
calls. The inner most Recursive call of multiplyMatrix() is to iterate k (col1 or row2). The second
recursive call of multiplyMatrix() is to change the columns and the outermost recursive call is to
change rows.

"""
import typing


class GFG:
    MAX = 100
    i, j, k = 0, 0, 0

    def multiply_matrix_rec(self, row1: int, col1: int,
                            A: typing.List[typing.List[int]],
                            row2: int, col2: int,
                            B: typing.List[typing.List[int]],
                            C: typing.List[typing.List[int]]):
        """ Recursive code for Matrix Multiplication """
        # Note that below variables are static i and j are used to know current cell of
        # result matrix
        # C[][]. k is used to know current column number of A[][] and row number of B[][] to be
        # multiplied

        # If all rows traversed.
        if self.i >= row1:
            return

        # If i < row1
        if self.j < col2:
            if self.k < col1:
                C[self.i][self.j] += A[self.i][self.k] * B[self.k][self.j]
                self.k += 1
                self.multiply_matrix_rec(row1, col1, A, row2, col2, B, C)

            self.k = 0
            self.j += 1
            self.multiply_matrix_rec(row1, col1, A, row2, col2, B, C)

        self.j = 0
        self.i += 1
        self.multiply_matrix_rec(row1, col1, A, row2, col2, B, C)

    def multiply_matrix(self, row1, col1, A, row2, col2, B):
        """Function to multiply two matrices A[][] and B[][]"""
        if row2 != col1:
            print("Not Possible\n")
            return

        C = [[0 for i in range(self.MAX)] for j in range(self.MAX)]
        self.multiply_matrix_rec(row1, col1, A, row2, col2, B, C)

        for i in range(row1):
            print(C[i][:col2])


if __name__ == '__main__':
    test = GFG()
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    B = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    row1, col1, row2, col2 = 3, 3, 3, 3
    test.multiply_matrix(row1, col1, A, row2, col2, B)
