"""
Dynamic Programming | Set 4 (Longest Common Subsequence)

We have discussed Overlapping Subproblems and Optimal Substructure properties in Set 1 and Set
2 respectively. We also discussed one example problem in Set 3.
Let us discuss Longest Common Subsequence (LCS) problem as one more example problem that can be
solved using Dynamic Programming.

LCS Problem Statement: Given two sequences, find the length of longest subsequence present in
both of them. A subsequence is a sequence that appears in the same relative order,
but not necessarily contiguous. For example, "abc", "abg", "bdf", "aeg", "acefg", .. etc are
subsequences of "abcdefg". So a string of length n has 2^n different possible subsequents.

It is a classic computer science problem, the basis of diff (a file comparison program that
outputs the differences between two files), and has applications in bio-informatics.

Examples:
LCS for input Sequences "ABCDGH" and "AEDFHR" is "ADH" of length 3.
LCS for input Sequences "AGGTAB" and "GXTXAYB" is "GTAB" of length 4.
------------------------------------------------------------------------------------
1) Optimal Substructure:
Let the input sequences be X[0..m-1] and Y[0..n-1] of lengths m and n
respectively. And let L(X[0..m-1], Y[0..n-1]) be the length of LCS of the two sequences X and Y.

Following is the recursive definition of L(X[0..m-1], Y[0..n-1]).

If last characters of both sequences match (or X[m-1] == Y[n-1]) then
L(X[0..m-1], Y[0..n-1]) = 1 + L(X[0..m-2], Y[0..n-2])

If last characters of both sequences do not match (or X[m-1] != Y[n-1]) then
L(X[0..m-1], Y[0..n-1]) = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2])

Examples:
----------
1) Consider the input strings "AGGTAB" and "GXTXAYB". Last characters match for the strings.
So length of LCS can be written as:

L("AGGTAB", "GXTXAYB") = 1 + L("AGGTA", "GXTXAY")

[[0, A, G, G, T, A, B],
 [G, 0, 0, 4, 0, 0, 0],
 [X, 0, 0, 0, 0, 0, 0],
 [T, 0, 0, 0, 3, 0, 0],
 [X, 0, 0, 0, 0, 0, 0],
 [A, 0, 0, 0, 0, 2, 0],
 [Y, 0, 0, 0, 0, 0, 0],
 [B, 0, 0, 0, 0, 0, 0]]

    REFER DIAGRAM
    http://www.geeksforgeeks.org/longest-common-subsequence/

2) Consider the input strings "ABCDGH" and "AEDFHR. Last characters do not match for the strings.
So length of LCS can be written as:

L("ABCDGH", "AEDFHR") = MAX ( L("ABCDG", "AEDFHR"), L("ABCDGH", "AEDFH") )

So the LCS problem has optimal substructure property as the main problem can be solved using
solutions to subproblems.
------------------------------------------------------------------------------------

2) Overlapping Subproblems:

Time complexity of the above naive recursive approach is O(2^n) in worst case and worst case
happens when all characters of X and Y mismatch i.e., length of LCS is 0. Considering the above
implementation, following is a partial recursion tree for input strings "AXYT" and "AYZX"

                         lcs("AXYT", "AYZX")
                       /
         lcs("AXY", "AYZX")            lcs("AXYT", "AYZ")
         /                              /
lcs("AX", "AYZX") lcs("AXY", "AYZ")   lcs("AXY", "AYZ") lcs("AXYT", "AY")

In the above partial recursion tree, lcs("AXY", "AYZ") is being solved twice. If we draw the
complete recursion tree, then we can see that there are many subproblems which are solved again
and again. So this problem has Overlapping Substructure property and recomputation of same
subproblems can be avoided by either using Memoization or Tabulation. Following is a tabulated
implementation for the LCS problem.
"""
import numpy as np


def lcs_rec(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs_rec(X, Y, m - 1, n - 1)
    else:
        return max(lcs_rec(X, Y, m, n - 1), lcs_rec(X, Y, m - 1, n))


def lcs_dp(X: str, Y: str):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    # L = [[None for j in range(n + 1)] for i in range(m + 1)]
    L = np.zeros((m + 1, n + 1), dtype=int)

    # Following steps build L[m+1][n+1] in bottom up fashion
    # Note: L[i][j] contains length of LCS of X[0..i-1] and Y[ 0..j-1]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i, j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i, j] = L[i - 1, j - 1] + 1
            else:
                L[i, j] = max(L[i - 1, j], L[i, j - 1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"

    # print("Length of LCS is ", lcs_rec(X, Y, len(X), len(Y)))
    print("Length of LCS is ", lcs_dp(X, Y))
