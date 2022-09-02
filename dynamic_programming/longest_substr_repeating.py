"""
Length of the longest substring without repeating characters

Given a string, find the length of the longest substring without repeating characters. For
example, the longest substrings without repeating characters for "ABDEFGABEF" are "BDEFGA" and
"DEFGAB", with length 6. For "BBBB" the longest substring is "B", with length 1. For
"GEEKSFORGEEKS", there are two longest substrings shown in the below diagrams, with length 7.

    ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']

    ['G', 'E', |'E'|, |'K'|, |'S'|, |'F'|, |'O'|, |'R'|, |'G'|, 'E', 'E', 'K', 'S']

    ['G', 'E', 'E', |'K'|, |'S'|, |'F'|, |'O'|, |'R'|, |'G'|, |'E'|, 'E', 'K', 'S']


The desired time complexity is O(n) where n is the length of the string.

------------------------------------
Method 1 (Simple)
------------------------------------
We can consider all substrings one by one and check for each substring whether it contains all
unique characters or not. There will be n*(n+1)/2 substrings. Whether a substirng contains all
unique characters or not can be checked in linear time by scanning it from left to right and
keeping a map of visited characters. Time complexity of this solution would be O(n^3).


------------------------------------
Method 2 (Linear Time)
------------------------------------
Let us talk about the linear time solution now. This solution uses extra space to store the last
indexes of already visited characters. The idea is to scan the string from left to right,
keep track of the maximum length Non-Repeating Character Substring (NRCS) seen so far. Let the
maximum length be max_len. When we traverse the string, we also keep track of length of the
current NRCS using cur_len variable. For every new character, we look for it in already processed
part of the string (A temp array called visited[] is used for this purpose). If it is not
present, then we increase the cur_len by 1. If present, then there are two cases:

a) The previous instance of character is not part of current NRCS (The NRCS which is under
process). In this case, we need to simply increase cur_len by 1.

b) If the previous instance is part of the current NRCS, then our current NRCS changes. It
becomes the substring staring from the next character of previous instance to currently scanned
character. We also need to compare cur_len and max_len, before changing current NRCS (or changing
cur_len).

"""

from __future__ import print_function
# Python program to find the length of the longest substring without repeating characters
NO_OF_CHARS = 256


def longestUniqueSubsttr(string):
    n = len(string)
    cur_len = 1  # To store the lenght of current substring
    max_len = 1  # To store the result
    prev_index = 0  # To store the previous index
    i = 0

    # Initialize the visited array as -1, -1 is used to indicate that character has not
    # been visited yet.
    visited = [-1] * NO_OF_CHARS

    # Mark first character as visited by storing the index of first character in visited array.
    visited[ord(string[0])] = 0

    # Start from the second character. First character is already processed (cur_len and
    # max_len are initialized as 1, and visited[str[0]] is set
    for i in range(1, n):
        prev_index = visited[ord(string[i])]

        # If the current character is not present in the already processed substring or it is
        # not part of the current NRCS, then do cur_len++
        if prev_index == -1 or (i - cur_len > prev_index):
            cur_len += 1

        # If the current character is present in currently considered NRCS, then update NRCS to
        # start from the next character of previous instance.
        else:
            # Also, when we are changing the NRCS, we should also check whether length of the
            # previous NRCS was greater than max_len or not.
            if cur_len > max_len:
                max_len = cur_len

            cur_len = i - prev_index

        # update the index of current character
        visited[ord(string[i])] = i

    # Compare the length of last NRCS with max_len and update max_len if needed
    if cur_len > max_len:
        max_len = cur_len

    return max_len


if __name__ == '__main__':
    # Time Complexity: O(n + d) where n is length of the input string and d is number of
    # characters in input string alphabet. For example, if string consists of lowercase English
    # characters then value of d is 26.
    # Auxiliary Space: O(d)

    string = "ABDEFGABEF"
    print("The input string is %s " % string)
    length = longestUniqueSubsttr(string)
    print("The length of the longest non-repeating character substring is " + str(length))
