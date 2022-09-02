"""
Lexicographic rank of a string
Given a string, find its rank among all its permutations sorted lexicographically.
For example, rank of "abc" is 1, rank of "acb" is 2, and rank of "cba" is 6.

Examples:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Input : str[] = "acb"
Output : Rank = 2

Input : str[] = "string"
Output : Rank = 598

Input : str[] = "cba"
Output : Rank = 6
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

For simplicity, let us assume that the string does not contain any duplicated characters.

One simple solution is to initialize rank as 1, generate all permutations in lexicographic order.
After generating a permutation, check if the generated permutation is same as given string, if
same, then return rank, if not, then increment the rank by 1. The time complexity of this solution
will be exponential in worst case. Following is an efficient solution.

Let the given string be "STRING". In the input string, 'S' is the first character. There are total
6 characters and 4 of them are smaller than 'S'. So there can be 4 * 5! smaller strings where first
character is smaller than 'S', like following

R X X X X X
I X X X X X
N X X X X X
G X X X X X

Now let us Fix S' and find the smaller strings staring with 'S'.

Repeat the same process for T, rank is 4*5! + 4*4! + ....

Now fix T and repeat the same process for R, rank is 4*5! + 4*4! + 3*3! + ...

Now fix R and repeat the same process for I, rank is 4*5! + 4*4! + 3*3! + 1*2! + ....

Now fix I and repeat the same process for N, rank is 4*5! + 4*4! + 3*3! + 1*2! + 1*1! + ...

Now fix N and repeat the same process for G, rank is 4*5! + 4*4 + 3*3! + 1*2! + 1*1! + 0*0!

Rank = 4*5! + 4*4! + 3*3! + 1*2! + 1*1! + 0*0! = 597

Since the value of rank starts from 1, the final rank = 1 + 597 = 598

"""
from __future__ import print_function


# Python program to find lexicographic rank of a string
def fact(n):
    """
    The time complexity of the above solution is O(n^2) A utility function to find factorial of n
    """
    f = 1
    while n >= 1:
        f = f * n
        n = n - 1
    return f


# A utility function to count smaller
# characters on right of arr[low]
def findSmallerInRight(st, low, high):
    countRight = 0
    i = low + 1
    while i <= high:
        if st[i] < st[low]:
            countRight = countRight + 1
        i = i + 1

    return countRight


# A function to find rank of a string
# in all permutations of characters
def findRank(st):
    ln = len(st)
    mul = fact(ln)
    rank = 1
    i = 0

    while i < ln:
        mul = mul // (ln - i)

        # count number of chars smaller
        # than str[i] fron str[i+1] to
        # str[len-1]
        countRight = findSmallerInRight(st, i, ln - 1)

        rank = rank + countRight * mul
        i = i + 1

    return rank


# Driver program to test above function
st = "string"
print(findRank(st))

# We can reduce the time complexity to O(n) by creating an auxiliary array of size 256.
# See following code.

# A O(n) solution for finding rank of string
MAX_CHAR = 256


class LexicographicRank:
    def fact(self, n):
        return 1 if (n <= 1) else n * fact(n - 1)

    def populate_and_increase_count(self, count, m_string):
        """
        Construct a count array where value at every index contains count of smaller
        characters in whole string"""

        for i, v in enumerate(m_string):
            count[ord(m_string[i])] += 1

        for i in range(1, 256):
            count[i] += count[i - 1]

    def updatecount(self, count, ch):
        """
        Removes a character ch from count[] array constructed by
        populateAndIncreaseCount()"""
        for i in range(ord(ch), MAX_CHAR):
            count[i] -= 1

    def findRank(self, m_string):
        """A function to find rank of a string in all permutations of characters"""
        length = len(m_string)
        mul = fact(length)
        rank = 1

        # all elements of count[] are initialized with 0
        count = [0 for i in range(MAX_CHAR)]

        # Populate the count array such that count[i] contains count of characters
        # which are present in str and are smaller than i
        self.populate_and_increase_count(count, m_string)

        for i in range(length):
            mul //= length - i

            # count number of chars smaller than str[i] fron str[i+1] to str[len-1]
            rank += count[ord(m_string[i]) - 1] * mul

            # Reduce count of characters greater than str[i]
            self.updatecount(count, m_string[i])

        return rank


if __name__ == '__main__':
    m_string = "string"
    print("\nMethod-1: ", findRank(list(m_string)))

    test = LexicographicRank()
    print("\nMethod-2: ", test.findRank(list(m_string)))
