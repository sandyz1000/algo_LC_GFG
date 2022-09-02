"""
Longest Palindromic Substring | Set 1

Given a string, find the longest substring which is palindrome. For example, if the given
string is "forgeeksskeegfor", the output should be "geeksskeeg".

Method 1 ( Brute Force )
------------------------------------
The simple approach is to check each substring whether the substring is
a palindrome or not. We can run three loops, the outer two loops pick all substrings one by one
by fixing the corner characters, the inner loop checks whether the picked substring is palindrome
or not.

Time complexity: O ( n^3 )
Auxiliary complexity: O ( 1 )

Method 2 ( Dynamic Programming )
------------------------------------
The time complexity can be reduced by storing results of
sub-problems. The idea is similar to this post. We maintain a boolean table[n][n] that is filled
in bottom up manner. The value of table[i][j] is true, if the substring is palindrome, otherwise
false. To calculate table[i][j], we first check the value of table[i+1][j-1], if the value is
true and str[i] is same as str[j], then we make table[i][j] true. Otherwise, the value of table[
i][j] is made false.

Method 3 (Without using additional space)
------------------------------------------
Time complexity: O ( n^2 )
Auxiliary Space: O ( n^2 )

The time complexity of the Dynamic Programming based solution is O(n^2) and it requires O(n^2)
extra space. We can find the longest palindrome substring in (n^2) time with O(1) extra space.
The idea is to generate all even length and odd length palindromes and keep track of the longest
palindrome seen so far.

Step to generate odd length palindrome:
Fix a centre and expand in both directions for longer palindromes.

Step to generate even length palindrome
Fix two centre ( low and high ) and expand in both directions for longer palindromes.
"""

from __future__ import print_function


class LongestPalinSubstring(object):
    def print_sub_str(self, stream, low, high):
        """
        A utility function to print a substring str[low..high]
        :param stream:
        :param low:
        :param high:
        :return:
        """
        for i in range(low, high + 1):
            print("%c" % stream[i])

    def longest_pal_substr(self, m_string):
        """
        This function prints the longest palindrome substring of str[].
        It also returns the length of the longest palindrome
        Time complexity: O ( n^2 )
        Auxiliary Space: O ( n^2 )
        :param m_string:
        :return:
        """
        n = len(m_string)  # get length of input string

        # table[i][j] will be false if substring str[i..j] is not palindrome.
        # Else table[i][j] will be true
        table = [[False for i in range(n)] for j in range(n)]

        # All substrings of length 1 are palindromes
        max_length = 1
        for i in range(n):
            table[i][i] = True

        # check for sub-string of length 2.
        start = 0
        for i in range(n - 1):
            if m_string[i] == m_string[i + 1]:
                table[i][i + 1] = True
                start = i
                max_length = 2

        # Check for lengths greater than 2. k is length of substring
        for k in range(3, n + 1):
            # Fix the starting index
            for i in range(n - k + 1):
                # Get the ending index of substring from starting index i and length k
                j = i + k - 1
                # checking for sub-string from ith index to jth index iff str[i+1] to str[j-1] is a
                # palindrome
                if table[i + 1][j - 1] and m_string[i] == m_string[j]:
                    table[i][j] = True
                    if k > max_length:
                        start = i
                        max_length = k

        print("Longest palindrome substring is: ")
        self.print_sub_str(m_string, start, start + max_length - 1)
        return max_length  # return length of LPS


class LongestPalinSubstringOptimised:
    """Method-3"""

    # A O(n^2) time and O(1) space program to find the
    # longest palindromic substring

    # This function prints the longest palindrome substring (LPS)
    # of str[]. It also returns the length of the longest palindrome
    @staticmethod
    def longest_pal_substr(m_string):
        maxLength = 1
        start = 0
        length = len(m_string)

        # One by one consider every character as center point of
        # even and length palindromes
        for i in range(1, length):
            # Find the longest even length palindrome with center
            # points as i-1 and i.
            low = i - 1
            high = i
            while low >= 0 and high < length and m_string[low] == m_string[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1

            # Find the longest odd length palindrome with center
            # point as i
            low = i - 1
            high = i + 1
            while low >= 0 and high < length and m_string[low] == m_string[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1

        print("Longest palindrome substring is:")
        print(m_string[start:start + maxLength])

        return maxLength


if __name__ == '__main__':
    # Longest palindrome substring is: geeksskeeg
    # Length is: 10

    # Time complexity: O ( n^2 )
    # Auxiliary Space: O ( n^2 )
    print("\n ---- Method-2 ---- ")
    string = "forgeeksskeegfor"
    # test = LongestPalinSubstring()
    # print("Length is: %d" % test.longest_pal_substr(string))

    # Time complexity: O ( n^2 ) where n is the length of input string.
    # Auxiliary Space: O ( 1 )
    print("\n ---- Method-3 ---- ")
    test = LongestPalinSubstringOptimised()
    print("Length is: %d" % test.longest_pal_substr(string))
