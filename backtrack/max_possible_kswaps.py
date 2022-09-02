"""
Find Maximum number possible by doing at-most K swaps

Given a positive integer, find maximum integer possible by doing at-most K swap operations on
its digits.

Examples:

Input: M = 254, K = 1
Output: 524

Input: M = 254, K = 2
Output: 542

Input: M = 68543, K = 1
Output: 86543

Input: M = 7599, K = 2
Output: 9975

Input: M = 76543, K = 1
Output: 76543

Input: M = 129814999, K = 4
Output: 999984211

Idea is to consider every digit and swap it with digits following it one at a time and see if it
leads to the maximum number. We repeat the process K times. The code can be further optimized if
we swap only if current digit is less than the following digit.

"""
from __future__ import print_function


class Maximum(object):
    def __init__(self, value):
        self.val = value


def findMaximumNum(m_string, k, maximum):
    """
    Python program to find maximum integer possible by doing at-most K swap operations on its
    digits. function to find maximum integer possible by doing at-most K swap operations on its
    digits

    :param m_string: List[str]
    :param k: int
    :param maximum: Maximum
    :return:
    """
    # return if no swaps left
    if k == 0:
        return

    n = len(m_string)

    # consider every digit
    for i in range(n-1):
        # and compare it with all digits after it
        for j in range(i+1, n):
            # if digit at position i is less than digit at position j, swap it and check for
            # maximum number so far and recurse for remaining swaps
            if m_string[i] < m_string[j]:
                # swap str[i] with str[j]
                m_string[i], m_string[j] = m_string[j], m_string[i]

                # If current num is more than maximum so far
                if m_string > maximum.val:
                    maximum.val = m_string[:]

                # recurse of the other k - 1 swaps
                findMaximumNum(m_string, k - 1, maximum)

                # backtrack
                m_string[i], m_string[j] = m_string[j], m_string[i]


if __name__ == '__main__':
    # Output: 999984211
    m_string = list("129814999")
    k = 4

    maximum = Maximum(m_string[:])
    findMaximumNum(m_string, k, maximum)
    print("".join(maximum.val))