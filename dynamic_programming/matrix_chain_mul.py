"""
Matrix Chain Multiplication | DP-8
===================================
https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/

Given a sequence of matrices, find the most efficient way to multiply these matrices together.
The problem is not actually to perform the multiplications, but merely to decide in which order
to perform the multiplications.

We have many options to multiply a chain of matrices because matrix multiplication is associative.
In other words, no matter how we parenthesize the product, the result will be the same. For example,
if we had four matrices A, B, C, and D, we would have:

    (ABC)D = (AB)(CD) = A(BCD) = ....
However, the order in which we parenthesize the product affects the number of simple arithmetic operations
needed to compute the product, or the efficiency. For example, suppose A is a 10 × 30 matrix, B is a 30 × 5 matrix,
and C is a 5 × 60 matrix.

Then,
    (AB)C = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations
    A(BC) = (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.
Clearly the first parenthesization requires less number of operations.

Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of dimension p[i-1] x p[i].
We need to write a function MatrixChainOrder() that should return the minimum number of multiplications needed
to multiply the chain.

----------------------------------------------------------------
Input: p[] = {40, 20, 30, 10, 30}
  Output: 26000
  There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
  Let the input 4 matrices be A, B, C and D.  The minimum number of
  multiplications are obtained by putting parenthesis in following way
  (A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30

  Input: p[] = {10, 20, 30, 40, 30}
  Output: 30000
  There are 4 matrices of dimensions 10x20, 20x30, 30x40 and 40x30.
  Let the input 4 matrices be A, B, C and D.  The minimum number of
  multiplications are obtained by putting parenthesis in following way
  ((AB)C)D --> 10*20*30 + 10*30*40 + 10*40*30

  Input: p[] = {10, 20, 30}
  Output: 6000
  There are only two matrices of dimensions 10x20 and 20x30. So there
  is only one way to multiply the matrices, cost of which is 10*20*30

----------------------------------------------------------------

"""
import sys
from typing import List


def matrix_chain_order_rec(arr: List[int], i: int, j: int):
    """
    A naive recursive implementation that simply follows the above optimal substructure property

    Matrix A[i] has dimension p[i-1] x p[i]
    for i = 1..n

    Arguments:
        arr {[List]} -- [description]
        i {[int]} -- [description]
        j {[int]} -- [description]

    Returns:
        [int] -- Return minimum cost of multiplication
    """
    if i == j:
        return 0

    _min = sys.maxsize

    # place parenthesis at different places between first and last matrix, recursively calculate
    # count of multiplications for each parenthesis placement and return the minimum count
    for k in range(i, j):
        count = (matrix_chain_order_rec(arr, i, k) + matrix_chain_order_rec(arr, k + 1, j) +
                 arr[i - 1] * arr[k] * arr[j])
        _min = min(count, _min)

    return _min


def matrix_chain_order(arr, n):
    """
    Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
    For simplicity of the program, one extra row and one extra column
    are allocated in m[][].  0th row and 0th column of m[][] are not used
    :param p:
    :param n:
    :return:
    """

    min_mul = [[0 for x in range(n)] for x in range(n)]

    # min_mul[i,j] = Minimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where
    # dimension of A[i] is arr[i-1] x arr[i]

    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        min_mul[i][i] = 0

    # L is chain length.
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            min_mul[i][j] = sys.maxsize
            for k in range(i, j):
                count = min_mul[i][k] + min_mul[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                min_mul[i][j] = min(count, min_mul[i][j])

    return min_mul[1][n - 1]


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    size = len(arr)

    print("Minimum number of multiplications is %d " % matrix_chain_order(arr, size))

    # ----------------------------------------
    arr = [1, 2, 3, 4, 3]
    n = len(arr)

    print("Minimum number of multiplications is ", matrix_chain_order_rec(arr, 1, n - 1))

