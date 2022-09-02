"""Dynamic Programming | Set 17 (Palindrome Partitioning)

Given a string, a partitioning of the string is a palindrome partitioning if every substring
of the partition is a palindrome.

For example, "aba|b|bbabb|a|b|aba" is a palindrome partitioning of "ababbbabbababa".
Determine the fewest cuts needed for palindrome partitioning of a given string.

For example, minimum 3 cuts are needed for "ababbbabbababa".
The three cuts are "a|babbbab|b|ababa".

1) If a string is palindrome, then minimum 0 cuts are needed.
2) If a string of length n containing all different characters, then minimum n-1 cuts are needed.

========================================
Examples :

Input : str = “geek”
Output : 2
We need to make minimum 2 cuts, i.e., “g ee k”

Input : str = “aaaa”
Output : 0
The string is already a palindrome.

Input : str = “abcde”
Output : 4

Input : str = “abbac”
Output : 1
========================================

This problem is a variation of Matrix Chain Multiplication problem. If the string is a palindrome, 
then we simply return 0. Else, like the Matrix Chain Multiplication problem, we try making cuts at 
all possible places, recursively calculate the cost for each cut and return the minimum value.

Let the given string be str and minPalPartion() be the function that returns the fewest cuts needed 
for palindrome partitioning. following is the optimal substructure property.

Using Recursion
================
// i is the starting index and j is the ending index. i must be passed as 0 and j as n-1
minPalPartion(str, i, j) = 0 if i == j. // When string is of length 1.
minPalPartion(str, i, j) = 0 if str[i..j] is palindrome.

// If none of the above conditions is true, then minPalPartion(str, i, j) can be 
// calculated recursively using the following formula.
minPalPartion(str, i, j) = Min { minPalPartion(str, i, k) + 1 +
                                 minPalPartion(str, k+1, j) } 
                           where k varies from i to j-1
================
"""
import sys


def isPalindrome(x):
    return x == x[::-1]


def minPalPartionRec(string, i, j):
    if i >= j or isPalindrome(string[i:j + 1]):
        return 0
    ans = float('inf')
    for k in range(i, j):
        count = (1 + minPalPartionRec(string, i, k) + minPalPartionRec(string, k + 1, j))
        ans = min(ans, count)
    return ans


def min_pal_partion(m_string):
    """
    This problem is a variation of Matrix Chain Multiplication problem. If the string is
    palindrome, then we simply return 0. Else, like the Matrix Chain Multiplication problem,
    we try making cuts at all possible places, recursively calculate the cost for each cut
    and return the minimum value.

    Let the given string be str and minPalPartion() be the function that returns the fewest
    cuts needed for palindrome partitioning. following is the optimal substructure property.

    ========================================================================================
    Returns the minimum number of cuts needed to partition a string
    such that every part is a palindrome
    Time Complexity: O(n3)
    :param m_string:
    :return:
    """
    # Get the length of the string
    n = len(m_string)

    # Create two arrays to build the solution in bottom up manner C[i][j] = Minimum number of
    # cuts needed for palindrome partitioning of substring str[i..j] P[i][j] = true if substring
    # str[i..j] is palindrome, else false Note that C[i][j] is 0 if P[i][j] is True
    C = [[0 for i in range(n)] for j in range(n)]
    P = [[False for i in range(n)] for j in range(n)]

    # Every substring of length 1 is a palindrome
    for index in range(n):
        P[index][index] = True
        C[index][index] = 0

    # L is substring length. Build the solution in bottom up manner by considering all
    # substrings of length starting from 2 to n. The loop structure is same as Matrix Chain
    # Multiplication problem ( See http://www.geeksforgeeks.org/archives/15553 )
    for L in range(2, n + 1):
        # For substring of length L, set different possible starting indexes
        for index in range(n - L + 1):
            j = index + L - 1  # Set ending index

            # If L is 2, then we just need to compare two characters. Else need to check two
            # corner characters and value of P[i+1][j-1]
            if L == 2:
                P[index][j] = (m_string[index] == m_string[j])
            else:
                P[index][j] = (m_string[index] == m_string[j]) and P[index + 1][j - 1]

            # IF str[i..j] is palindrome, then C[i][j] is 0
            if P[index][j]:
                C[index][j] = 0
            else:
                # Make a cut at every possible localtion starting from i to j,
                # and get the minimum cost cut.
                C[index][j] = sys.maxsize
                for k in range(index, j):
                    C[index][j] = min(C[index][j], C[index][k] + C[k + 1][j] + 1)

    # Return the min cut value for complete string. i.e., str[0..n-1]
    return C[0][n - 1]


def min_pal_partion_optimised(m_string):
    """
    An optimization to above approach
    In above approach, we can calculating minimum cut while finding all palindromic substring.
    If we finding all palindromic substring 1st and then we calculate minimum cut, time
    complexity will reduce to O(n2).

    ================================================================================    
    Returns the minimum number of cuts needed to partition a string
    such that every part is a palindrome
    Time Complexity: O(n2)
    :param m_string:
    :return:
    """
    # Get the length of the string
    n = len(m_string)

    # Create two arrays to build the solution in bottom up manner C[i] = Minimum number of
    # cuts needed for palindrome partitioning of substring str[0..i] P[i][j] = true if substring
    # str[i..j] is palindrome, else false Note that C[i] is 0 if P[0][i] is True
    C = [[0 for i in range(n)] for j in range(n)]
    P = [[False for i in range(n)] for j in range(n)]

    # Every substring of length 1 is a palindrome
    for i in range(n):
        P[i][i] = True

    # L is substring length. Build the solution in bottom up manner by considering all
    # substrings of length starting from 2 to n.
    for L in range(2, n + 1):
        # For substring of length L, set different possible starting indexes
        for i in range(n - L + 1):
            j = i + L - 1  # Set ending index

            # If L is 2, then we just need to compare two characters.
            # Else need to check two corner characters and value of P[i+1][j-1]
            if L == 2:
                P[i][j] = (m_string[i] == m_string[j])
            else:
                P[i][j] = (m_string[i] == m_string[j]) and P[i + 1][j - 1]

    for i in range(n):
        if P[0][i]:
            C[i] = 0
        else:
            C[i] = sys.maxsize
            for j in range(i):
                if P[j + 1][i] and 1 + C[j] < C[i]:
                    C[i] = 1 + C[j]

    # Return the min cut value for complete string. i.e., str[0..n-1]
    return C[n - 1]


if __name__ == '__main__':
    string = "ababbbabbababa"
    
    print(
        "Min cuts needed for Palindrome Partitioning is ",
        minPalPartionRec(string, 0, len(string) - 1),
    )

    print("Method-1: Min cuts needed for Palindrome Partitioning is %d", min_pal_partion(string))

    print("Method-2: Min cuts needed for Palindrome Partitioning is %d", min_pal_partion_optimised(string))
