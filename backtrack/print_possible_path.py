"""
Print all possible paths from top left to bottom right of a mXn matrix

The problem is to print all the possible paths from top left to bottom right of a mXn matrix with
the constraints that from each cell you can either move only to right or down.

The algorithm is a simple recursive algorithm, from each cell first print all paths by going down
and then print all paths by going right. Do this recursively for each cell encountered.

Note that in the above code, the last line of print_all_paths_util() is commented, If we uncomment
this line, we get all the paths from the top left to bottom right of a nXm matrix if the diagonal
movements are also allowed. And also if moving to some of the cells are not permitted then the
same code can be improved by passing the restriction array to the above function and that is left
as an exercise.

"""
from __future__ import print_function
import numpy as np


class GFG(object):
    """
    mat:  Pointer to the starting of mXn matrix
    i, j: Current position of the robot (For the first call use 0,0)
    m, n: Dimensions of given the matrix
    pi:   Next index to be filed in path array
    path[0..pi-1]: The path traversed by robot till now (Array to hold the path need to have
    space for at least m+n elements)
    """

    def print_all_paths_util(self, mat, i, j, m, n, path, pi):
        # Reached the bottom of the matrix so we are left with only option to move right
        if i == m - 1:
            for k in range(j, n):
                path[pi + k - j] = mat[i * n % m][k]

            for l in range(pi + n - j):
                print(path[l], end=" ")
            print("")
            return

        # Reached the right corner of the matrix we are left with only the downward movement.
        if j == n - 1:
            for k in range(i, m):
                path[pi + k - i] = mat[k * n % m][j]

            for l in range(pi + m - i):
                print(path[l], end=" ")
            print("")
            return

        # Add the current cell to the path being generated
        path[pi] = mat[i * n % m][j]

        # Print all the paths that are possible after moving down
        self.print_all_paths_util(mat, i + 1, j, m, n, path, pi + 1)

        # Print all the paths that are possible after moving right
        self.print_all_paths_util(mat, i, j + 1, m, n, path, pi + 1)

        # Print all the paths that are possible after moving diagonal
        # self.print_all_paths_util(mat, i+1, j+1, m, n, path, pi)

    def print_all_paths(self, mat, m, n):
        """
        The main function that prints all paths from top left to bottom right in a
        matrix 'mat' of size mXn
        """
        path = [0 for i in range(m + n)]
        path = np.zeros((m+n, ), dtype=np.int32)
        self.print_all_paths_util(mat, 0, 0, m, n, path, 0)


if __name__ == '__main__':
    # Output:
    # 1 4 5 6
    # 1 2 5 6
    # 1 2 3 6
    test = GFG()
    mat = [[1, 2, 3],
           [4, 5, 6]]
    test.print_all_paths(mat, 2, 3)
