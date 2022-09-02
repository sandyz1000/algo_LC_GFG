"""
http://www.geeksforgeeks.org/cuckoo-hashing/

Cuckoo Hashing – Worst case O(1) Lookup!

--------------------------------------------------
Background :
--------------------------------------------------

There are three basic operations that must be supported by a hash table (or a dictionary):

==Lookup(key):== return true if key is there in the table, else false
==Insert(key):== adds the item 'key' to the table if not already present
==Delete(key):== removes 'key' from the table

Collisions are very likely even if we have a big table to store keys. Using the results from the
birthday paradox: with only 23 persons, the probability that two people share the same birth date
is 50%! There are 3 general strategies towards resolving hash collisions:

==Closed addressing or Chaining:== store colliding elements in an auxiliary data structure like a
linked list or a binary search tree.

==Open addressing:== allow elements to overflow out of their target bucket and into other spaces.

Although above solutions provide expected lookup cost as O(1), the expected worst-case cost of a
lookup in Open Addressing (with linear probing) is Ω(log n) and Θ(log n / log log n) in simple
chaining (Source : Standford Lecture Notes). To close the gap of expected time and worst case
expected time, two ideas are used:

    ==Multiple-choice hashing:== Give each element multiple choices for positions where it can
    reside in the hash table

    ==Relocation hashing:== Allow elements in the hash table to move after being placed

"""
from __future__ import print_function

# Below is Python implementation of Cuckoo hashing
# Python program to demonstrate working of Cuckoo hashing.
MAXN = 11  # upper bound on number of elements in our set
ver = 2  # choices for position
INT_MIN = -999999


class CuckooHashing:
    """
    --------------------------------------------------
    Cuckoo Hashing :
    --------------------------------------------------

    Cuckoo hashing applies the idea of multiple-choice and relocation together and guarantees O(1)
    worst case lookup time!

    ==Multiple-choice:== We give a key two choices h1(key) and h2(key) for residing.

    ==Relocation:== It may happen that h1(key) and h2(key) are preoccupied. This is resolved by
    imitating the Cuckoo bird: it pushes the other eggs or young out of the nest when it hatches.
    Analogously, inserting a new key into a cuckoo hashing table may push an older key to a
    different location. This leaves us with the problem of re-placing the older key.

        1. If alternate position of older key is vacant, there is no problem.

        2. Otherwise, older key displaces another key. This continues until the procedure finds a
        vacant position, or enters a cycle. In case of cycle, new hash functions are chosen and
        the whole data structure is 'rehashed'. Multiple rehashes might be necessary before
        Cuckoo succeeds.

    ==Insertion== is expected O(1) (amortized) with high probability, even considering the
    possibility rehashing, as long as the number of keys is kept below half of the capacity of
    the hash table, i.e., the load factor is below 50%.

    ==Deletion== is O(1) worst-case as it requires inspection of just two locations in the hash
    table.

    Generalizations of cuckoo hashing that use more than 2 alternative hash functions can be
    expected to utilize a larger part of the capacity of the hash table efficiently while
    sacrificing some lookup and insertion speed. Example: if we use 3 hash functions, it's safe
    to load 91% and still be operating within expected bounds

    --------------------------------------------------
    Illustration :
    --------------------------------------------------
    Input:
    {20, 50, 53, 75, 100, 67, 105, 3, 36, 39}

    Hash Functions:

    h1(key) = key%11
    h2(key) = (key/11)%11

        ----- DIAGRAM GOES HERE -----


    """
    # Auxiliary space bounded by a small multiple of MAXN, minimizing wastage
    hashtable = [[0 for i in range(MAXN)] for j in range(ver)]

    # Array to store possible positions for a key
    pos = [0] * ver

    def init_table(self):
        """
        function to fill hash table with dummy value
        dummy value: INT_MIN
        number of hashtables: ver
        :return:
        """
        for j in range(MAXN):
            for i in range(ver):
                self.hashtable[i][j] = INT_MIN

    def hashing(self, function, key):
        """
        return hashed value for a key
        function: ID of hash function according to which key has to hashed
        key: item to be hashed
        :param function:
        :param key:
        :return:
        """
        if function == 1:
            return key % MAXN

        if function == 2:
            return (key // MAXN) % MAXN

    def place(self, key, tableID, cnt, n):
        """
        function to place a key in one of its possible positions

        tableID: table in which key has to be placed, also equal to function according to which
        key must be hashed

        cnt: number of times function has already been called in order to place the first input key

        n: maximum number of times function can be recursively called before stopping and declaring
        presence of cycle

        :param key:
        :param tableID:
        :param cnt:
        :param n:
        :return:
        """
        # if function has been recursively called max number of times, stop and
        # declare cycle. Rehash.
        if cnt == n:
            print(" %d unpositioned\n" % key, end=" ")
            print("Cycle present. REHASH.\n", end=" ")
            return

        # calculate and store possible positions for the key.
        # check if key already present at any of the positions.
        # If YES, return.
        for i in range(ver):
            self.pos[i] = self.hashing(i + 1, key)
            if self.hashtable[i][self.pos[i]] == key:
                return

        # check if another key is already present at the position for the new key in the table
        # If YES: place the new key in its position and place the older key in an
        # alternate position for it in the next table
        if self.hashtable[tableID][self.pos[tableID]] != INT_MIN:
            dis = self.hashtable[tableID][self.pos[tableID]]
            self.hashtable[tableID][self.pos[tableID]] = key
            self.place(dis, (tableID + 1) % ver, cnt + 1, n)
        else:  # place the new key in its position
            self.hashtable[tableID][self.pos[tableID]] = key

    def print_table(self):
        """function to print hash table contents"""
        print("Final hash tables:\n", end=" ")
        for i in range(ver):
            for j in range(MAXN):
                print("-" if self.hashtable[i][j] == INT_MIN else self.hashtable[i][j], end=" ")
            print("\n")

    def cuckoo(self, keys, n):
        """
        function for Cuckoo-hashing keys
         keys[]: input array of keys
         n: size of input array

        :param keys:
        :param n:
        :return:
        """
        # initialize hash tables to a dummy value (INT-MIN) indicating empty position
        self.init_table()

        # start with placing every key at its position in the first hash table according
        # to first hash function
        i, cnt = 0, 0
        while i < n:
            self.place(keys[i], 0, cnt, n)
            i += 1

        # print the final hash tables
        self.print_table()


if __name__ == '__main__':
    # Output:
    # Final hash tables:
    # - 100 - 36 - - 50 - - 75 - 3 20 - 39 53 - 67 - - 105 -
    #
    # 105 unpositioned
    # Cycle present. REHASH.
    # Final hash tables:
    # - 67 - 3 - - 39 - - 53 - 6 20 - 36 50 - 75 - - 100 -

    # following array doesn't have any cycles and hence  all keys will be inserted without any
    # rehashing
    cuckoo_hash = CuckooHashing()
    keys_1 = [20, 50, 53, 75, 100, 67, 105, 3, 36, 39]
    n = len(keys_1)
    cuckoo_hash.cuckoo(keys_1, n)

    # following array has a cycle and hence we will have to rehash to position every key
    keys_2 = [20, 50, 53, 75, 100, 67, 105, 3, 36, 39, 6]
    m = len(keys_2)
    cuckoo_hash.cuckoo(keys_2, m)
