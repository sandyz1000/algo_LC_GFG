"""Word Ladder (Length of shortest chain to reach a target word)

Given a dictionary, and two words 'start' and 'target' (both of same length). Find length of the
smallest chain from 'start' to 'target' if it exists, such that adjacent words in the chain only
differ by one character and each word in the chain is a valid word i.e., it exists in the
dictionary. It may be assumed that the 'target' word exists in dictionary and length of all
dictionary words is same.

Example:

Input:  Dictionary = [POON, PLEE, SAME, POIE, PLEA, PLIE, POIN]
        start = TOON
        target = PLEA

Output: 7

Explanation: TOON - POON - POIN - POIE - PLIE - PLEE - PLEA"""

from typing import List


# Time Complexity of the above code is O(n^m) where n is the number of entries originally in the
# dictionary and m is the size of the string
# To check if strings differ by exactly one character
def is_adjacent(a, b):
    count = 0
    n = len(a)

    # Iterate through all characters and return false
    # if there are more than one mismatching characters
    for i in range(n):
        if a[i] != b[i]:
            count += 1
        if count > 1:
            break

    return True if count == 1 else False


# A queue item to store word and minimum chain length to reach the word.
class QItem():
    def __init__(self, word, length):
        self.word = word
        self.len = length


def shortestChainLen(start: str, target: str, D: List[str]):
    """
    Returns length of shortest chain to reach 'target' from 'start' using minimum number of
    adjacent moves.  D is dictionary
    :return:
    """
    # Create a queue for BFS and insert 'start' as source vertex
    Q = []
    item = QItem(start, 1)
    Q.append(item)

    while len(Q) > 0:
        curr = Q.pop()
        # Go through all words of dictionary
        for it in D:
            # Process a dictionary word if it is adjacent to current word (or vertex) of BFS
            temp = it
            if is_adjacent(curr.word, temp):
                item.word = temp  # Add the dictionary word to Q
                item.len = curr.len + 1
                Q.append(item)

                # Remove from dictionary so that this word is not processed again.
                # This is like marking visited
                D.remove(temp)

                # If we reached target
                if temp == target:
                    return item.len


if __name__ == '__main__':
    D = ["poon", "plee", "same", "poie", "plie", "poin", "plea"]
    start = "toon"
    target = "plea"
    print("Length of shortest chain is: %d" % shortestChainLen(start, target, D))
