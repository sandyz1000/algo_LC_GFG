"""
Design a data structure that supports insert, delete, search and getRandom in constant time
Design a data structure that supports following operations in Theta(1) time.

insert(x): Inserts an item x to the data structure if not already present.

remove(x): Removes an item x from the data structure if present.

search(x): Searches an item x in the data structure.

getRandom(): Returns a random element from current set of elements

--------------------------------------------------------
Explanation:
--------------------------------------------------------

We can use hashing to support first 3 operations in Theta(1) time. How to do the 4th operation?
The idea is to use a resizable array (ArrayList in Java, vector in C) together with hashing.
Resizable arrays support insert in Θ(1) amortized time complexity.
To implement getRandom(), we can simply pick a random number from 0 to size-1 (size is number of
current elements) and return the element at that index. The hash map stores array values as keys
and array indexes as values.

Following are detailed operations.

insert(x)
1) Check if x is already present by doing a hash map lookup.
2) If not present, then insert it at the end of the array.
3) Add in hash table also, x is added as key and last array index as index.

remove(x)
1) Check if x is present by doing a hash map lookup.
2) If present, then find its index and remove it from hash map.
3) Swap the last element with this element in array and remove the last element.
Swapping is done because the last element can be removed in O(1) time.
4) Update index of last element in hash map.

getRandom()
1) Generate a random number from 0 to last index.
2) Return the array element at the randomly generated index.

search(x)
Do a lookup for x in hash map.
"""
from __future__ import print_function
import random


class MyStructure:
    """
    Python program to design a DS that supports folloiwng operations in Theta(n) time
    a) Insert
    b) Delete
    c) Search
    d) getRandom

    class to represent the required data structure
    """

    def __init__(self):
        # A resizable array
        self.arr = []
        # A hash where keys are array elements and vlaues are indexes in arr[]
        self.map = {}

    def add(self, x):
        """
        A Theta(1) function to add an element to MyDS data structure
        :param x:
        :return:
        """
        # If element is already present, then noting to do
        if x in self.map:
            return

        # Else put element at the end of arr[]
        index = len(self.arr)
        self.arr.append(x)

        # and hashmap also
        self.map[x] = index

    def remove(self, x):
        """function to remove a number to DS in O(1)"""
        # element not found then return
        if x not in self.map:
            return

        index = self.map[x]
        del self.map[x]  # remove element from map

        # swap with last element in arr then remove element at back
        size = len(self.arr)
        last = self.arr[size - 1]
        self.arr[index], self.arr[size - 1] = self.arr[size - 1], self.arr[index]
        self.arr.pop()

        # Update hash table for new index of last element
        self.map[last] = index

    def search(self, x):
        """Returns index of element if element is present, otherwise null"""
        return self.map[x]

    def getRandom(self):
        """Returns a random element from myStructure"""
        # Find a random index from 0 to size - 1
        size = len(self.arr)
        random_index = random.randint(1, size)
        # Return element at randomly picked index
        return self.arr[random_index]


if __name__ == '__main__':
    # Output:
    # 2
    # 3
    # 40
    ds = MyStructure()
    ds.add(10)
    ds.add(20)
    ds.add(30)
    ds.add(40)
    print(ds.search(30))
    ds.remove(20)
    ds.add(50)
    print(ds.search(50))
    print(ds.getRandom())
