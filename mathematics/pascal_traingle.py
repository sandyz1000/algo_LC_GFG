"""
Pascal's Triangle
Pascal's triangle is a triangular array of the binomial coefficients. Write a function that takes
an integer value n as input and prints first n lines of the Pascal's triangle.

Following are the first 6 rows of Pascal's Triangle.

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
"""
from __future__ import print_function


def print_pascal2(n):
    """
    Method 2( O(n^2) time and O(n^2) extra space )

    If we take a closer at the triangle, we observe that every entry is sum of the two values
    above it. So we can create a 2D array that stores previously generated values. To generate a
    value in a line, we can use the previously stored values from array. """
    # An auxiliary array to store generated pscal triangle values
    arr = [[0 for i in range(n)] for j in range(n)]

    # Iterate through every line and print integer(s) in it

    for line in range(n):
        # Every line has number of integers equal to line number
        for i in range(line + 1):
            # First and last values in every row are 1
            if line == i or i == 0:
                arr[line][i] = 1
            else:  # Other values are sum of values just above and left of above
                arr[line][i] = arr[line - 1][i - 1] + arr[line - 1][i]
            print("%d " % arr[line][i], end="")
        print("")


def print_pascal3(n):
    """
    Method 3 ( O(n^2) time and O(1) extra space )
    This method is based on method 1. We know that ith entry in a line number line is Binomial
    Coefficient C(line, i) and all lines start with value 1. The idea is to calculate C(line, i)
    using C(line, i-1). It can be calculated in O(1) time using the following.

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    C(line, i)   = line! / ( (line-i)! * i! )
    C(line, i-1) = line! / ( (line - i + 1)! * (i-1)! )
    We can derive following expression from above two expressions.
    C(line, i) = C(line, i-1) * (line - i + 1) / i

    So C(line, i) can be calculated from C(line, i-1) in O(1) time
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    A O(n^2) time and O(1) extra space function for Pascal's Triangle
    """
    for line in range(1, n + 1):
        C = 1  # used to represent C(line, i)
        for i in range(1, line + 1):
            print("%d " % C, end="")  # The first value in a line is always 1
            C = C * (line - i) // i
        print("")


if __name__ == '__main__':
    n = 7
    print("\nMethod-1: -- ")
    print_pascal2(n)

    print("\nMethod-2: -- ")
    print_pascal3(n)
