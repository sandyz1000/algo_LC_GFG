"""
Arrange given numbers to form the biggest number | Set 1
Given an array of numbers, arrange them in a way that yields the largest value.
------------------------------------
Example:
------------------------------------
If the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 gives the largest value.
And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives
the largest value

Explanation:

A simple solution that comes to our mind is to sort all numbers in descending order, but simply
sorting doesn't work. For example, 548 is greater than 60, but in output 60 comes before 548.
As a second example, 98 is greater than 9, but 9 comes before 98 in output.

So how do we go about it? The idea is to use any comparison based sorting algorithm. In the
used sorting algorithm, instead of using the default comparison, write a comparison function
myCompare() and use it to sort numbers. Given two numbers X and Y, how should myCompare()
decide which number to put first - we compare two numbers XY (Y appended at the end of X) and
YX (X appended at the end of Y). If XY is larger, then X should come before Y in output,
else Y should come before. For example, let X and Y be 542 and 60. To compare X and Y,
we compare 54260 and 60542. Since 60542 is greater than 54260, we put Y first.

The main function that prints the arrangement with the largest value. The
function accepts a vector of strings

"""
from __future__ import print_function
from functools import cmp_to_key


# Following is Python implementation of the above approach. To keep the code simple, numbers are
# considered as strings, and vector is used instead of normal array.

# Given an array of numbers, program to arrange the numbers to form the largest number

def my_compare(X, Y):
    """A comparison function which is used by sort() in printLargest()"""
    # first append Y at the end of X
    XY = X + Y
    # then append X at the end of Y
    YX = Y + X
    # Now see which of the two formed numbers is greater
    return 1 if XY == YX else -1


def print_largest(arr):
    #  Sort the numbers using library sort function. The function uses
    #  our comparison function my_compare() to compare two strings.
    arr.sort(key=cmp_to_key(my_compare))
    print("".join(arr))


if __name__ == '__main__':
    arr = ["54", "546", "548", "60"]
    # output should be 6054854654
    print_largest(arr)

    arr = ["7", "776", "7", "7"]
    #  output should be 777776
    print_largest(arr)

    arr = ["1", "34", "3", "98", "9", "76", "45", "4"]
    # output should be 998764543431
    print_largest(arr)
