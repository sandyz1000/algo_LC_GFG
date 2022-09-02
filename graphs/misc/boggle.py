"""
Boggle (Find all possible words in a board of characters) | Set 1
https://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/

Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one
character.
Find all possible words that can be formed by a sequence of adjacent characters. Note
that we can move to any of 8 adjacent characters, but a word should not have multiple instances of
same cell.

Example:

Input: dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
       boggle = {{'G','I','Z'},
                {'U','E','K'},
                {'Q','S','E'}};
      isWord(str): returns true if str is present in dictionary else false.

Output:  Following words of dictionary are present
         GEEKS
         QUIZ

"""
from __future__ import print_function


class Boggle(object):
    """
    The idea is to consider every character as a starting character and find all words starting
    with it. All words starting from a character can be found using Depth First Traversal. We do
    depth first traversal starting from every cell. We keep track of visited cells to make sure
    that a cell is considered only once in a word.
    """
    M = 3
    N = 3

    # Let the given dictionary be following
    dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
    size_n = len(dictionary)

    def __init__(self, m_string=""):
        # Initialize current string
        self.m_string = m_string

    def is_word(self, m_string):
        """
        A given function to check if a given string is present in dictionary.
        The implementation is naive for simplicity. As per the question dictionary is given to us.
        """
        # Linearly search all words
        for i in range(self.size_n):
            if m_string == self.dictionary[i]:
                return True
        return False

    def find_words_util(self, boggle, visited, i, j):
        """
        A recursive function to print all words present on boggle
        :param boggle: list(str)
        :param visited: list(bool)
        :param i:
        :param j:
        :return:
        """
        # Mark current cell as visited and append current character to str
        visited[i][j] = True
        self.m_string += boggle[i][j]

        # If str is present in dictionary, then print it
        if self.is_word(self.m_string):
            print(self.m_string)

        # Traverse 8 adjacent cells of boggle[i][j]
        row = i - 1
        while row <= i + 1 and row < self.M:
            col = j - 1
            while col <= j + 1 and col < self.N:
                if row >= 0 and col >= 0 and not visited[row][col]:
                    self.find_words_util(boggle, visited, row, col)
                col += 1
            row += 1
        # Erase current character from string and mark visited of current cell as false
        self.m_string = self.m_string[:-1]
        visited[i][j] = False

    def find_words(self, boggle):
        """
        Prints all words present in dictionary.
        :param boggle:
        :return:
        """
        # Mark all characters as not visited
        visited = [[False for i in range(self.M)] for j in range(self.N)]

        # Consider every character and look for all words starting with this character
        for i in range(self.M):
            for j in range(self.N):
                self.find_words_util(boggle, visited, i, j)


if __name__ == '__main__':
    # Note that the above solution may print same word multiple times. For example, if we add "SEEK"
    # to dictionary, it is printed multiple times. To avoid this, we can use hashing to keep
    # track of all printed words.

    # Output: Following words of dictionary are present: GEEKS, QUIZ
    test = Boggle("")
    boggle = [['G', 'I', 'Z'],
              ['U', 'E', 'K'],
              ['Q', 'S', 'E']]

    print("Following words of dictionary are present\n")
    test.find_words(boggle)
