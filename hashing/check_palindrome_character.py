"""
Check for Palindrome after every character replacement Query

Given a string str and Q queries. Each query contains a pair of integers (i1, i2) and a character
'ch'. We need to replace characters at indexes i1 and i2 with new character 'ch' and then tell if
string str is palindrome or not. (0 <= i1, i2 < string_length)

------------------------------------------------------------
Examples:
------------------------------------------------------------

Input : str = "geeks"  Q = 2
        query 1: i1 = 3 ,i2 = 0, ch = 'e'
        query 2: i1 = 0 ,i2 = 2 , ch = 's'
Output : query 1: "NO"
         query 2: "YES"

Explanation :
        In query 1 : i1 = 3 , i2 = 0 ch = 'e'
                    After replacing char at index i1, i2
                    str[3] = 'e', str[0] = 'e'
                    string become "eeees" which is not
                    palindrome so output "NO"
        In query 2 : i1 = 0 i2 = 2  ch = 's'
                    After replacing char at index i1 , i2
                     str[0] = 's', str[2] = 's'
                    string become "seses" which is
                    palindrome so output "YES"

Input : str = "jasonamat"  Q = 3
        query 1: i1 = 3, i2 = 8 ch = 'j'
        query 2: i1 = 2, i2 = 6 ch = 'n'
        query 3: i1 = 3, i2 = 7 ch = 'a'
Output :
       query 1: "NO"
       query 2: "NO"
       query 3: "YES"
"""
from __future__ import print_function


class CheckIsPalindrome:
    """
    METHOD - 1
    A Simple solution is that for each query , we replace character at indexes (i1 & i2) with a new
    character 'ch' and then check if string is palindrome or not.

    Python program to find if string becomes palindrome after every query.
    Time complexity O(Q*n) (n is length of string )

    METHOD - 2
    An efficient solution is to use hashing. We create an empty hash set that stores indexes that
    are unequal in palindrome (Note: "we have to store indexes only first half of string that are
    unequal").

    Given string "str" and length 'n'.
    Create an empty set S and store unequal indexes in first half.
    Do following for each query :
       1. First replace character at indexes i1 & i2 with new char "ch"

       2. If i1 and/or i2 are/is greater than n/2 then convert into first half index(es)

       3. In this step we make sure that S contains maintains unequal indexes of first half.
          a) If str[i1] == str [n - 1 - i1] means i1 becomes equal after replacement, remove
          it from S (if present) Else add i1 to S

          b) Repeat step a) for i2 (replace i1 with i2)

       4. If S is empty then string is palindrome else NOT

    Time Complexity : O(Q + n) under the assumption that set insert, delete and find operations
    take O(1) time. """

    def is_palindrome(self, mystring):
        """Function to check if string is Palindrome or Not"""
        n = len(mystring)
        for i in range(n // 2):
            if mystring[i] != mystring[n - 1 - i]:
                return False
        return True

    def query(self, in_string, mystring, Q):
        """Takes two inputs for Q queries. For every query, it prints Yes if
        string becomes palindrome and No if not."""
        # Process all queries one by one
        for q in range(Q):
            estring = in_string[q].split()
            i1, i2, ch = int(estring[0]), int(estring[1]), estring[2]

            # query 1: i1 = 3 ,i2 = 0, ch = 'e'
            # query 2: i1 = 0 ,i2 = 2 , ch = 's'
            # replace character at index i1 & i2 with new 'ch'
            mystring[i1] = mystring[i2] = ch

            # check estring is palindrome or not
            print("YES" if (self.is_palindrome(mystring)) else "NO")

    def add_remove_unequal(self, mystr, index, n, S):
        """
        This function makes sure that set S contains unequal characters from first half.
        This is called for every character.
        """

        # If character becomes equal after query
        if mystr[index] == mystr[n - 1 - index]:
            # Remove the current index from set if it is present
            if index < len(S):
                S.remove(index)

        # If not equal after query, insert it into set
        else:
            S.add(index)

    def query2(self, in_string, mystr, Q):
        """Takes two inputs for Q queries. For every query, it prints Yes if string
        becomes palindrome and No if not."""
        n = len(mystr)

        # create an empty set that store indexes of unequal location in palindrome
        S = set()

        # we store indexes that are unequal in palindrome traverse only first half of string
        for i in range(n // 2):
            if mystr[i] != mystr[n - 1 - i]:
                S.add(i)

        # traversal the query
        for q in range(Q):
            # query 1: i1 = 3, i2 = 0, ch = 'e'
            # query 2: i1 = 0, i2 = 2, ch = 's'
            estring = in_string[q].split()
            i1, i2, ch = int(estring[0]), int(estring[1]), estring[2]

            # Replace characters at indexes i1 & i2 with new char 'ch'
            mystr[i1] = mystr[i2] = ch

            # If i1 and/or i2 greater than n/2 then convert into first half index
            if i1 > n // 2:
                i1 = n - 1 - i1
            if i2 > n // 2:
                i2 = n - 1 - i2

            # call addRemoveUnequal function to insert and remove unequal indexes
            self.add_remove_unequal(mystr, i1, n, S)
            self.add_remove_unequal(mystr, i2, n, S)

            # if set is not empty then string is not palindrome
            print("YES" if len(S) == 0 else "NO")


if __name__ == '__main__':
    # Output: "NO" "YES"
    is_palindrome = CheckIsPalindrome()
    mystr = list("geeks")
    in_string = ["3 0 e", "0 2 s"]
    Q = 2
    print("\n--- Method-1 --- ------- -- -- ------ ")
    is_palindrome.query(in_string, mystr[:], Q)
    print("\n--- Method-2 --- ------- -- -- ------ ")
    is_palindrome.query2(in_string, mystr[:], Q)
