"""
Dynamic Programming | Set 5 (Edit Distance)
http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/

Given two strings str1 and str2 and below operations that can performed on str1. Find minimum
number of edits (operations) required to convert 'str1' into 'str2'.

Insert
Remove
Replace

What are the sub problems in this case?

The idea is process all characters one by one staring from either from left or right sides of both
strings.

Let we traverse from right corner, there are two possibilities for every pair of character being
traversed.

m: Length of str1 (first string)
n: Length of str2 (second string)

If last characters of two strings are same, nothing much to do. Ignore last characters and get
count for remaining strings. So we recur for lengths m-1 and n-1.
Else (If last characters are not same), we consider all operations on 'str1', consider all three
operations on last character  of first string, recursively compute minimum cost for all three
operations and take minimum of three values.

Insert: Recur for m and n-1
Remove: Recur for m-1 and n
Replace: Recur for m-1 and n-1

Time Complexity: O(m x n)
Auxiliary Space: O(m x n)

"""


def edit_distance(str1: str, str2: str, m: int, n: int):
    """
    A Naive recursive Python program to fin minimum number operations to convert str1 to str2
    """
    # If first string is empty, the only option is to insert all characters of second
    # string into first
    if m == 0:
        return n

    # If second string is empty, the only option is to remove all characters of first string
    if n == 0:
        return m

    # If last characters of two strings are same, nothing much to do. Ignore last characters and
    # get count for remaining strings.
    if str1[m - 1] == str2[n - 1]:
        return edit_distance(str1, str2, m - 1, n - 1)

    # If last characters are not same, consider all three operations on last character of first
    # string, recursively compute minimum cost for all three operations and take minimum of three
    # values.
    return 1 + min(edit_distance(str1, str2, m, n - 1),  # Insert
                   edit_distance(str1, str2, m - 1, n),  # Remove
                   edit_distance(str1, str2, m - 1, n - 1)  # Replace
                   )


def edit_dist_dp(str1: str, str2: str, m: int, n: int):
    """
    A Dynamic Programming based Python program for edit distance problem
    """
    # Create a table to store results of sub problems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            # If first string is empty, only option is to insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If last character are different, consider all possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]


if __name__ == '__main__':
    str1 = "sunday"
    str2 = "saturday"
    print(edit_distance(str1, str2, len(str1), len(str2)))
    print(edit_dist_dp(str1, str2, len(str1), len(str2)))
