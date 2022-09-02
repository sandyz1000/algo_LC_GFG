"""
Group Shifted String
Given an array of strings (all lowercase letters), the task is to group them in such a way that all
strings in a group are shifted versions of each other.

Two string S and T are called shifted if,
- - - - - - - - - - - - - - - - - - - - - - - +

S.length = T.length
and
S[i] = T[i] + K for 1 <= i <= S.length  for a constant integer K

- - - - - - - - - - - - - - - - - - - - - - - +

==Example:==

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +

strings {acd, dfg, wyz, yab, mop} are shifted versions of each other.
Input  : str = ["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]
Output : a x
         acd dfg wyz yab mop
         bdfh moqs

All shifted strings are grouped together.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +

"""
from __future__ import print_function
from collections import defaultdict

ALPHA = 26  # Total lowercase letter


def get_diff_string(m_string):
    """
    We can see a pattern among string of one group, the difference between consecutive characters
    for all character of string are equal. As in above example take acd, dfg and mop

    a c d -> 2 1
    d f g -> 2 1
    m o p -> 2 1

    Since the differences are same, we can use this to identify strings that belong to same group.
    The idea is to form a string of differences as key. If a string with same difference string is
    found, then this string also belongs to same group. For example, above three strings have same
    difference string, that is "21".

    In below implementation, we add 'a' to every difference and store "21" as "ba"

    Python  program to print groups of shifted strings together.
    """
    shift = ""
    for i in range(1, len(m_string)):
        dif = ord(m_string[i]) - ord(m_string[i - 1])
        if dif < 0:
            dif += ALPHA
        # Representing the difference as char
        shift += chr(dif + ord('a'))
    # This string will be 1 less length than str
    return shift


def group_shifted_string(m_string, n):
    """Method for grouping shifted string"""
    # map for storing indices of string which are in same group
    groupMap = defaultdict(list)

    for i in range(n):
        diffStr = get_diff_string(m_string[i])
        groupMap[diffStr].append(i)

    # iterating through map to print group
    for key, it in groupMap.items():
        v = it
        for i, item in enumerate(v):
            print(m_string[item], end=" ")
        print("")


if __name__ == '__main__':
    # Output:
    # a x
    # acd dfg wyz yab mop
    # bdfh moqs

    m_string = ["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]
    n = len(m_string)
    group_shifted_string(m_string, n)
