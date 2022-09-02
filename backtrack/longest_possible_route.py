"""
Longest Possible Route in a Matrix with Hurdles

Given an M x N matrix, with a few hurdles arbitrarily placed, calculate the length of longest
possible route possible from source to destination within the matrix. We are allowed to move to
only adjacent cells which are not hurdles. The route cannot contains any diagonal moves and a
location once visited in a particular path cannot be visited again.

For example, longest path with no hurdles from source to destination is highlighted for below
matrix. The length of the path is 24.


    [
        { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
        { 1, 1, 0, 1, 1, 0, 1, 1, 0, 1 },
        { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 }
    ]

The idea is to use Backtracking. We start from the source cell of the matrix, move forward in all
four allowed directions and recursively checks if they leads to the solution or not. If
destination is found, we update the value of longest path else if none of the above solutions
work we return false from our function.

"""

import sys

# Python program to find Longest Possible Route in a matrix with hurdles

R = 3
C = 10
INT_MAX = sys.maxsize
INT_MIN = - sys.maxsize


class Pair(object):
    """
    A Pair to store status of a cell. found is set to true of destination is reachable and
    value stores distance of longest path
    """

    def __init__(self, found, value):
        # true if destination is found
        self.found = found
        # stores cost of longest path from current cell to destination cell
        self.value = value


def find_longest_path_util(mat, i, j, x, y, visited):
    """
    Function to find Longest Possible Route in the matrix with hurdles. If the destination is not
    reachable the function returns false with cost INT_MAX. (i, j) is source cell and (x,
    y) is destination cell.

    :param mat: List[List[int]]
    :param i: int
    :param j: int
    :param x: int
    :param y: int
    :param visited: List[List[bool]]
    :return:
    """

    # if (i, j) itself is destination, return true
    if i == x and j == y:
        p = Pair(True, 0)
        return p

    # if not a valid cell, return false
    if i < 0 or i >= R or j < 0 or j >= C or mat[i][j] == 0 or visited[i][j]:
        p = Pair(False, INT_MAX)
        return p

    # include (i, j) in current path i.e. set visited(i, j) to true
    visited[i][j] = True

    # res stores longest path from current cell (i, j) to destination cell (x, y)
    res = INT_MIN

    # go left from current cell
    sol = find_longest_path_util(mat, i, j - 1, x, y, visited)

    # if destination can be reached on going left from current cell, update res
    if sol.found:
        res = max(res, sol.value)

    # go right from current cell
    sol = find_longest_path_util(mat, i, j + 1, x, y, visited)

    # if destination can be reached on going right from current cell, update res
    if sol.found:
        res = max(res, sol.value)

    # go up from current cell
    sol = find_longest_path_util(mat, i - 1, j, x, y, visited)

    # if destination can be reached on going up from current cell, update res
    if sol.found:
        res = max(res, sol.value)

    # go down from current cell
    sol = find_longest_path_util(mat, i + 1, j, x, y, visited)

    # if destination can be reached on going down from current cell, update res
    if sol.found:
        res = max(res, sol.value)

    # Backtrack
    visited[i][j] = False

    # if destination can be reached from current cell, return true
    if res != INT_MIN:
        p = Pair(True, 1 + res)
        return p

    # if destination can't be reached from current cell, return false
    else:
        p = Pair(False, INT_MAX)
        return p


def find_longest_path(mat, i, j, x, y):
    """A wrapper function over findLongestPathUtil()"""
    # create a boolean matrix to store info about cells already visited in current route
    visited = [[False for col in range(C)] for row in range(R)]

    # find longest route from (i, j) to (x, y) and print its maximum cost
    p = find_longest_path_util(mat, i, j, x, y, visited)
    if p.found:
        print("Length of longest possible route is ", p.value)

    # If the destination is not reachable
    else:
        print("Destination not reachable from given source")


if __name__ == '__main__':
    # Output: Length of longest possible route is 24
    # input matrix with hurdles shown with number 0
    mat = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    # find longest path with source (0, 0) and destination (1, 7)
    find_longest_path(mat, 0, 0, 1, 7)
