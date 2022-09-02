"""
Write a program to calculate pow(x,n)

Given two integers x and n, write a function to compute xn. We may assume that x and n
are small and overflow doesn't happen.

Input : x = 2, n = 3
Output : 8
Input : x = 7, n = 2
Output : 49
"""
from __future__ import print_function


def power_ver_1(x, y):
    """
    Function to calculate x raised to the power y
    Time Complexity: O(n)
    Space Complexity: O(1)
    Algorithmic Paradigm: Divide and conquer.
    Above function can be optimized to O(logn) by calculating power(x, y/2) only
    once and storing it.

    :param x: int
    :param y: int
    :return:
    """
    if y == 0:
        return 1
    elif y % 2 == 0:
        return power_ver_1(x, y // 2) * power_ver_1(x, y // 2)
    else:
        return x * power_ver_1(x, y // 2) * power_ver_1(x, y // 2)


def power_ver_2(x, y):
    """
    # Time Complexity of optimized solution: O(logn)
    # Let us extend the pow function to work for negative y and float x.
    :param x: int
    :param y: int
    :return:
    """
    if y == 0:
        return 1

    temp = power_ver_2(x, y // 2)
    if y % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp


def power_ver_3(x, y):
    """
    Extended version of power function that can work for float x and negative y
    :param x:
    :param y:
    :return:
    """
    if y == 0:
        return 1
    temp = power_ver_3(x, y // 2)
    if y % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp if (y > 0) else (temp * temp) // x


if __name__ == '__main__':
    print("Power version 1")
    x = 2
    y = 3
    print("%f" % power_ver_1(x, y))

    print("Power version 2")
    x, y = 2, 3
    print("%f" % power_ver_2(x, y))

    print("Power version 3")
    x, y = 2, 3
    print("%f" % power_ver_3(x, y))
