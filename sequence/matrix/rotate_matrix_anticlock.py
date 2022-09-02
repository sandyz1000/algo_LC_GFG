"""Rotate each ring of matrix anticlockwise by K elements

Given a matrix of order M*N and a value K, the task is to rotate each ring of the matrix
anticlockwise by K elements. If in any ring elements are less than and equal K then don't rotate
it.

Examples:
------------

Input : k = 3
        mat = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]]

Output: 4 8  12 16
        3 10  6 15
        2 11  7 14
        1  5  9 13

Input : k = 2
        mat = [[1, 2, 3, 4],
               [10, 11, 12, 5],
               [9, 8, 7, 6]]

Output: 3 4  5  6
        2 11 12 7
        1 10  9 8


Algorithm:
------------
The idea is to traverse matrix in spiral form. Here is the algorithm to solve this problem :
1.  Make an auxiliary array temp[] of size M*N.
2.  Start traversing matrix in spiral form and store elements of current ring in temp[] array.
    While storing the elements in temp, keep track of starting and ending positions of current ring.
3.  For every ring that is being stored in temp[], rotate that subarray temp[]
4.  Repeat this process for each ring of matrix.
5.  In last traverse matrix again spirally and copy elements of temp[] array to matrix.

"""

# Time Complexity : O(M*N)
# Auxiliary space : O(M*N)

# Python program to rotate individual rings by k in spiral order traversal.

MAX = 100


def rotate(pS, pD, r, c):
    for row in range(r):
        for col in range(c):
            pD[c - col - 1][row] = pS[row][col]


class RotateKElement:
    def fill_spiral(self, mat, m, n, temp):
        """
        Fills temp array into mat[][] using spiral order traveral.
        :param mat: 2d-array
        :param m: int
        :param n: int
        :param temp: list(int)
        :return:
        """
        i, k, l = 0, 0, 0
        # k - starting row index
        # m - ending row index
        # l - starting column index
        # n - ending column index

        t_idx = 0  # Index in temp array
        while k < m and l < n:
            # first row from the remaining rows
            for i in range(l, n):
                mat[k][i] = temp[t_idx]
                t_idx += 1
            k += 1

            # last column from the remaining columns
            for i in range(k, m):
                mat[i][n - 1] = temp[t_idx]
                t_idx += 1
            n -= 1

            # last row from the remaining rows
            if k < m:
                for i in range(n - 1, l - 1, -1):
                    mat[m - 1][i] = temp[t_idx]
                    t_idx += 1
                m -= 1

            # first column from the remaining columns
            if l < n:
                for i in range(m - 1, k - 1, -1):
                    mat[i][l] = temp[t_idx]
                    t_idx += 1
                l += 1

    def spiral_rotate(self, mat, M, N, k):
        """
        Function to spirally traverse matrix and rotate each ring of matrix by K elements
        mat[][] --> matrix of elements
        M     --> number of rows
        N    --> number of columns
        :param mat:
        :param M:
        :param N:
        :param k:
        :return:
        """
        # Create a temporary array to store the result
        temp = [0] * (M * N)

        # s - starting row index
        # m - ending row index
        # l - starting column index
        # n - ending column index;
        m, n, s, l = M, N, 0, 0
        start = 0  # Start position of current ring
        t_idx = 0  # Index in temp
        while s < m and l < n:
            # Initialize end position of current ring
            end = start

            # copy the first row from the remaining rows
            for i in range(l, n):
                temp[t_idx] = mat[s][i]
                t_idx += 1
                end += 1
            s += 1

            # copy the last column from the remaining columns
            for i in range(s, m):
                temp[t_idx] = mat[i][n - 1]
                t_idx += 1
                end += 1
            n -= 1

            # copy the last row from the remaining rows
            if s < m:
                for i in range(n - 1, l - 1, -1):
                    temp[t_idx] = mat[m - 1][i]
                    t_idx += 1
                    end += 1
                m -= 1

            # copy the first column from the remaining columns
            if l < n:
                for i in range(m - 1, s - 1, -1):
                    temp[t_idx] = mat[i][l]
                    t_idx += 1
                    end += 1
                l += 1

            # if elements in current ring greater than k then rotate elements of current ring
            if end - start > k:
                # Rotate current ring using reversal algorithm for rotation
                temp[start:start + k] = list(reversed(temp[start:start + k]))
                temp[start + k: end] = list(reversed(temp[start + k: end]))
                temp[start: end] = list(reversed(temp[start: end]))

                # Reset start for next ring
                start = end

            # There are less than k elements in ring
            else:
                break

        # Fill tenp array in original matrix.
        self.fill_spiral(mat, M, N, temp)

    def print_arr(self, mat):
        for item in mat:
            print(item)


if __name__ == '__main__':
    # Output:
    # 4 8  12 16
    # 3 10  6 15
    # 2 11  7 14
    # 1  5  9 13

    M, N, k = 4, 4, 3
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]

    pDestination = [[0 for i in range(M)] for j in range(N)]
    rotate(mat, pDestination, M, N)

    test = RotateKElement()
    test.spiral_rotate(mat, M, N, k)
    test.print_arr(mat)
