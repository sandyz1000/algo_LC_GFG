"""
Match a pattern and String without using regular expressions

Given a string, find out if string follows a given pattern or not without using any regular
expressions.

Examples:
- - - - - - - - - - - - - - - - - - - - -
Input:
string - GraphTreesGraph
pattern - aba
Output:
a->Graph
b->Trees

Input:
string - GraphGraphGraph
pattern - aaa
Output:
a->Graph

Input:
string - GeeksforGeeks
pattern - GfG
Output:
G->Geeks
f->for

Input:
string - GeeksforGeeks
pattern - GG
Output:
No solution exists
- - - - - - - - - - - - - - - - - - - - -

We can solve this problem with the help of Backtracking. For each character in the pattern,
if the character is not seen before, we consider all possible sub-strings and recurse to see if
it leads to the solution or not. We maintain a map that stores sub-string mapped to a pattern
character. If pattern character is seen before, we use the same sub-string present in the map. If
we found a solution, for each distinct character in the pattern, we print string mapped to it
using our map

"""
from __future__ import print_function


# Python program to find out if string follows a given pattern or not

class PatternMatch(object):
    def pattern_match_util(self, string, n, i, pat, m, j, mapp):
        """
        Function to find out if string follows a given pattern or not

        str - given string
        n - length of given string
        i - current index in input string
        pat - given pattern
        m - length of given pattern
        j - current index in given pattern
        map - stores mapping between pattern and string

        :param string: str
        :param n: int
        :param i: int
        :param pat: str
        :param m: int
        :param j: int
        :param mapp: dict

        :return:
        """

        # If both string and pattern reach their end
        if i == n and j == m:
            return True

        # If either string or pattern reach their end
        if i == n or j == m:
            return False

        # read next character from the pattern
        ch = pat[j]

        # if character is seen before
        if ch in mapp:
            s = mapp[ch]
            size = len(s)
            # consider next len characters of str
            subStr = string[i:i+size]
            # if next len characters of string str don't match with s, return false
            if subStr != s:
                return False

            # if it matches, recurse for remaining characters
            return self.pattern_match_util(string, n, i + size, pat, m, j + 1, mapp)

        # If character is seen for first time, try out all remaining characters in the string
        # for (int len = 1; len <= n - i; len++)
        for size in range(1, n - i + 1):
            # consider substring that starts at position i and spans len characters and add it
            # to map
            mapp[ch] = string[i: i+size]

            # see if it leads to the solution
            if self.pattern_match_util(string, n, i + size, pat, m, j + 1, mapp):
                return True

            # if not, remove ch from the map
            del mapp[ch]

        return False

    def pattern_match(self, string, pat, n, m):
        """
        A wrapper over patternMatchUtil()function
        """
        if n < m:
            return False

        # create an empty hash map
        mapp = {}
        # store result in a boolean variable res
        res = self.pattern_match_util(string, n, 0, pat, m, 0, mapp)

        # if solution exists, print the mappings
        for k, v in mapp.items():
            print("%s->%s" % (k, v))

        return res


if __name__ == '__main__':
    # Output:
    # f->for
    # G->Geeks
    m_str = "GeeksforGeeks"
    pat = "GfG"

    n = len(m_str)
    m = len(pat)
    test = PatternMatch()
    if not test.pattern_match(m_str, pat, n, m):
        print("No Solution exists")
