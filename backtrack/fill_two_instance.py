"""
Fill two instances of all numbers from 1 to n in a specific way

Given a number n, create an array of size 2n such that the array contains 2 instances of every
number from 1 to n, and the number of elements between two instances of a number i is equal to i.
If such a configuration is not possible, then print the same.

Examples:

Input: n = 3
Output: res[] = {3, 1, 2, 1, 3, 2}

Input: n = 2
Output: Not Possible

Input: n = 4
Output: res[] = {4, 1, 3, 1, 2, 4, 3, 2}

One solution is to Backtracking. The idea is simple, we place two instances of n at a place,
then recur for n-1. If recurrence is successful, we return true, else we backtrack and try
placing n at different location

"""


# A backtracking based Python Program to fill two instances of all
# numbers from 1 to n in a specific way


def fillUtil(res, curr, n):
    """
    A recursive utility function to fill two instances of numbers from 1 to n in res[0..2n-1].
    'curr' is current value of n.

    :param res:
    :param curr:
    :param n:
    :return:
    """
    # If current number becomes 0, then all numbers are filled
    if curr == 0:
        return True

    # Try placing two instances of 'curr' at all possible locations till solution is found
    for i in range(2 * n - curr - 1):
        # Two 'curr' should be placed at 'curr+1' distance
        if res[i] == 0 and res[i + curr + 1] == 0:
            # Place two instances of 'curr'
            res[i] = res[i + curr + 1] = curr

            # Recur to check if the above placement leads to a solution
            if fillUtil(res, curr - 1, n):
                return True
            # If solution is not possible, then backtrack
            res[i] = res[i + curr + 1] = 0
    return False


def fill(n):
    """This function prints the result for input number 'n' using fillUtil()"""
    # Create an array of size 2n and initialize all elements in it as 0
    res = [0 for i in range(2 * n)]

    # If solution is possible, then print it.
    if fillUtil(res, n, n):
        for i in range(2 * n):
            print("%d" % res[i], end=" ")
    else:
        print("Not Possible")


if __name__ == '__main__':
    # Output: 7 3 6 2 5 3 2 4 7 6 5 1 4 1
    fill(7)
