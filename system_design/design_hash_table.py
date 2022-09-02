"""
Design and implement a hash table which uses chaining (linked lists) to handle collisions

Suppose we are implementing a hash table that looks like Hash<K, V>. That is, the hash table maps
from objects of type K to objects of type V.

Another common implementation for a hash table is to use a binary search tree as the underlying
 data structure. Retrieving an element will no longer be 0(1) (although, technically it's not
0(1) if there are many collisions), but it prevents us from creating an unnecessarily large
array to hold items.

"""


# At we might think our data structure would look something like this:
class Hash1:
    def __init__(self):
        self.items = []

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def hashCodeOfKey(self, key):
        """
        Note that items is an array of linked lists, where items [i] is a linked list of all
        objects with keys that map to index i (that is, all the objects that collided at i).

        This would seem to work until we think more deeply about collisions.
        Suppose we have a very simple hash function that uses the string length.
        :param key:
        :return:
        """
        return key.toString().length() % len(self.items)


class Hash:
    """
    The keys jim and bob will map to the same index in the array, even though they are different
    keys. We need to search through the linked list to find the actual object that corresponds to
    these keys. But how would we do that? All we've stored in the linked list is the value,
    not the original key.
    This is why we need to store both the value and the original key.
    One way to do that is to create another object called Cell which pairs keys and values. With
    this implementation, our linked list is of type Cell.
    """

    MAX_SIZE = 10

    def __init__(self):
        self.items = [None] * self.MAX_SIZE

    # Really, really stupid hash.
    def hashCodeOfKey(self, key):
        return len(str(key)) % len(self.items)

    def put(self, key, value):
        x = self.hashCodeOfKey(key)
        if self.items[x] is None:
            self.items[x] = []

        collided = self.items[x]

        # Look for items with same key and replace if found
        for c in collided:
            if c.equivalent(key):
                collided.remove(c)
                break

        cell = Cell(key, value)
        collided.append(cell)

    def get(self, key):
        x = self.hashCodedOfKey(key)
        if self.items[x] is None:
            return None

        collided = self.items[x]
        for c in collided:
            if c.equivalent(key):
                return c.getValue()

        return None


class Cell:
    """
    The Cell class pairs the data value and its key. This will allow us to search through the
    linked list (created by "colliding," but different, keys) and find the object with the exact
    key value.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def equivalent(self, c):
        # return equivalence.getKey())
        pass

    def _equivalent(self, k):
        return self.key.equals(k)

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value


if __name__ == '__main__':
    # Map < String, Integer > map = new Map <> ();
    # map.add("this", 1);
    # map.add("coder", 2);
    # map.add("this", 4);
    # map.add("hi", 5);
    # System.out.println(map.size());
    # System.out.println(map.remove("this"));
    # System.out.println(map.remove("this"));
    # System.out.println(map.size());
    # System.out.println(map.isEmpty());
    pass