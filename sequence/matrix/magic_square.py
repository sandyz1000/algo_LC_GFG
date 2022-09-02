"""
Magic Square
============

A magic square of order n is an arrangement of n^2 numbers, usually distinct integers, in a square,
such that the n numbers in all rows, all columns, and both diagonals sum to the same constant. A
magic square contains the integers from 1 to n^2.

The constant sum in every row, column and diagonal is called the magic constant or magic sum, M.
The magic constant of a normal magic square depends only on n and has the following value:
M = n(n^2+1)/2

For normal magic squares of order n = 3, 4, 5, ...,
the magic constants are: 15, 34, 65, 111, 175, 260, ...

Example:
------------

Magic Square of size 3
-----------------------
  2   7   6
  9   5   1
  4   3   8
Sum in each row & each column = 3*(3^2+1)/2 = 15


Magic Square of size 5
----------------------
  9   3  22  16  15
  2  21  20  14   8
 25  19  13   7   1
 18  12   6   5  24
 11  10   4  23  17
Sum in each row & each column = 5*(5^2+1)/2 = 65


Magic Square of size 7
----------------------
 20  12   4  45  37  29  28
 11   3  44  36  35  27  19
  2  43  42  34  26  18  10
 49  41  33  25  17   9   1
 40  32  24  16   8   7  48
 31  23  15  14   6  47  39
 22  21  13   5  46  38  30

Sum in each row & each column = 7*(7^2+1)/2 = 175


Did you find any pattern in which the numbers are stored?
In any magic square, the first number i.e. 1 is stored at position (n/2, n-1). Let this position be
(i,j). The next number is stored at position (i-1, j+1) where we can consider each row & column as
circular array i.e. they wrap around.

------------------------------------------------

Three conditions hold:
1.  The position of next number is calculated by decrementing row number of previous number by 1,
    and incrementing the column number of previous number by 1. At any time, if the calculated row
    position becomes -1, it will wrap around to n-1. Similarly, if the calculated column position
    becomes n, it will wrap around to 0.
2.  If the magic square already contains a number at the calculated position, calculated column
    position will be decremented by 2, and calculated row position will be incremented by 1.
3.  If the calculated row position is -1 & calculated column position is n, the new position would
    be: (0, n-2).

Magic Square of size 3
----------------------
 2  7  6
 9  5  1
 4  3  8

Steps:
1. position of number 1 = (3/2, 3-1) = (1, 2)
2. position of number 2 = (1-1, 2+1) = (0, 0)
3. position of number 3 = (0-1, 0+1) = (3-1, 1) = (2, 1)
4. position of number 4 = (2-1, 1+1) = (1, 2)
   Since, at this position, 1 is there. So, apply condition 2.
   new position=(1+1,2-2)=(2,0)
5. position of number 5=(2-1,0+1)=(1,1)
6. position of number 6=(1-1,1+1)=(0,2)
7. position of number 7 = (0-1, 2+1) = (-1,3) // this is tricky, see condition 3
   new position = (0, 3-2) = (0,1)
8. position of number 8=(0-1,1+1)=(-1,2)=(2,2) //wrap around
9. position of number 9=(2-1,2+1)=(1,3)=(1,0) //wrap around

"""
from __future__ import print_function


def generate_square(n):
    # 2-D array with all slots set to 0
    magic_square = [[0 for x in range(n)] for y in range(n)]
    i = n // 2  # initialize position of 1
    j = n - 1

    # Fill the magic square by placing values
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:  # third condition
            j = n - 2
            i = 0
        else:
            if j == n:  # next number goes out of right side of square
                j = 0
            if i < 0:  # next number goes out of upper side
                i = n - 1
        if magic_square[i][j]:  # 2nd condition
            j = j - 2
            i = i + 1
            continue
        else:
            magic_square[i][j] = num
            num = num + 1
        j = j + 1
        i = i - 1  # 1st condition

    print("Magic Square for n = ", n)
    print("Sum of each row or column", n * (n * n + 1) / 2)
    for i in range(0, n):
        print(magic_square[i])


if __name__ == '__main__':
    n = 7  # Works only when n is odd
    n = 3
    generate_square(n)
