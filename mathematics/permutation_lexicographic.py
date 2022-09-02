"""
Print all permutations in sorted (lexicographic) order

http://www.geeksforgeeks.org/lexicographic-permutations-of-string/

Given a string, print all permutations of it in sorted order. For example, if the input string is
"ABC", then output should be "ABC, ACB, BAC, BCA, CAB, CBA".

We have discussed a program to print all permutations in this post, but here we must print the
permutations in increasing order.

Following are the steps to print the permutations lexicographic-ally

1. Sort the given string in non-decreasing order and print it. The first permutation is always
the string sorted in non-decreasing order.

2. Start generating next higher permutation. Do it until next higher permutation is not possible.
If we reach a permutation where all characters are sorted in non-increasing order, then that
permutation is the last permutation.

Steps to generate the next higher permutation:

1. Take the previously printed permutation and find the rightmost character in it, which is
smaller than its next character. Let us call this character as 'first character'.

2. Now find the ceiling of the 'first character'. Ceiling is the smallest character on right of
'first character', which is greater than 'first character'. Let us call the ceil character as
'second character'.

3. Swap the two characters found in above 2 steps.

4. Sort the substring (in non-decreasing order) after the original index of 'first character'.

Let us consider the string "ABCDEF". Let previously printed permutation be "DCFEBA". The next
permutation in sorted order should be "DEABCF". Let us understand above steps to find next
permutation. The 'first character' will be 'C'. The 'second character' will be 'E'. After
swapping these two, we get "DEFCBA". The final step is to sort the substring after the character
original index of 'first character'. Finally, we get "DEABCF". """

from __future__ import print_function
from functools import cmp_to_key


# Program to print all permutations of a string in sorted order.


# Following function is needed for library function qsort().
# Refer http://www.cplusplus.com/reference/clibrary/cstdlib/qsort/

class PermutationLexicographic:
    def compare(self, a, b):
        return ord(a) - ord(b)

    def find_ceil(self, m_string, first, l, h):
        """
        This function finds the index of the smallest character which is greater than
        'first' and is present in str[l..h]"""
        # initialize index of ceiling element
        ceil_index = l

        # Now iterate through rest of the elements and find the smallest character
        # greater than 'first'
        for i in range(l + 1, h + 1):
            if first < m_string[i] < m_string[ceil_index]:
                ceil_index = i

        return ceil_index

    def sorted_permutations(self, m_string=[]):
        """Print all permutations of str in sorted order"""
        # Get size of string
        size = len(m_string)
        # Sort the string in increasing order
        m_string = sorted(m_string, key=cmp_to_key(self.compare))

        # Print permutations one by one
        is_finished = False
        while not is_finished:
            # print this permutation
            print("".join(m_string))

            # Find the rightmost character which is smaller than its next character.
            # Let us call it 'first char'
            i = size - 2
            while i >= 0:
                if m_string[i] < m_string[i + 1]:
                    break
                i -= 1

            # If there is no such chracter, all are sorted in decreasing order,
            # means we just printed the last permutation and we are done.
            if i == -1:
                is_finished = True
            else:
                # Find the ceil of 'first char' in right of first character.
                # Ceil of a character is the smallest character greater than it
                ceil_index = self.find_ceil(m_string, m_string[i], i + 1, size - 1)

                # Swap first and second characters
                m_string[i], m_string[ceil_index] = m_string[ceil_index], m_string[i]

                # // Sort the string on right of 'first char'
                m_string[i + 1:] = sorted(m_string[i + 1:], key=cmp_to_key(self.compare))


class PermutationLexicographicOptimised:
    """
    The upper bound on time complexity of the above program is O(n^2 x n!). We can optimize step
    4 of the above algorithm for finding next permutation. Instead of sorting the subarray after
    the ‘first character’, we can reverse the subarray, because the subarray we get after
    swapping is always sorted in non-increasing order. This optimization makes the time
    complexity as O(n x n!). See following optimized code.

    An optimized version that uses reverse instead of sort for finding the next permutation
    """

    def reverse(self, m_string, l, h):
        """A utility function to reverse a string str[l..h]"""
        while l < h:
            m_string[l], m_string[h] = m_string[h], m_string[l]
            l += 1
            h -= 1

    def find_ceil(self, m_string, first, l, h):
        """
        This function finds the index of the smallest character which is greater than
        'first' and is present in str[l..h]"""
        # initialize index of ceiling element
        ceil_index = l

        # Now iterate through rest of the elements and find the smallest character
        # greater than 'first'
        for i in range(l + 1, h + 1):
            if first < m_string[i] < m_string[ceil_index]:
                ceil_index = i

        return ceil_index

    def sorted_permutations(self, m_string):
        """Print all permutations of str in sorted order"""
        # Get size of string
        size = len(m_string)

        # Sort the string in increasing order
        m_string = sorted(m_string)

        # Print permutations one by one
        is_finished = False
        while not is_finished:
            # print this permutation
            print(m_string)

            # Find the rightmost character which is smaller than its next character.
            # Let us call it 'first char'
            for i in range(size - 2, -1, -1):
                if m_string[i] < m_string[i + 1]:
                    break

            # If there is no such chracter, all are sorted in decreasing order, means we
            # just printed the last permutation and we are done.
            if i == -1:
                is_finished = True
            else:
                # Find the ceil of 'first char' in right of first character.
                # Ceil of a character is the smallest character greater than it
                ceilIndex = self.find_ceil(m_string, m_string[i], i + 1, size - 1)

                # // Swap first and second characters
                m_string[i], m_string[ceilIndex] = m_string[ceilIndex], m_string[i]

                # // reverse the string on right of 'first char'
                self.reverse(m_string, i + 1, size - 1)


if __name__ == '__main__':
    # Output: ABCD ABDC .... DCAB DCBA
    m_string = "ABCD"
    test = PermutationLexicographic()
    print("\nMethod-1 - - -\n")
    test.sorted_permutations(list(m_string))

    # test = PermutationLexicographicOptimised()
    print("\nMethod-2 - - -\n")
    test.sorted_permutations(list(m_string))
