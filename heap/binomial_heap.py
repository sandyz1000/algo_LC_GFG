"""
http:www.growingwiththeweb.com/data-structures/binomial-heap/overview/

Binomial Heap:
A Binomial Heap is a set of Binomial Trees where each Binomial Tree follows Min Heap property.
And there can be at-most one Binomial Tree of any degree.

Examples Binomial Heap:

12------------10-------------------- 20
             /  \                 /  |  \
           15    50             70  50  40
           |                  / |    |
           30               80  85  65
                            |
                           100

A Binomial Heap with 13 nodes. It is a collection of 3 Binomial Trees of orders 0, 2 and 3
from left to right.

    10-------------------- 20
   /  \                 /  |  \
 15    50             70  50  40
 |                  / |    |
 30               80  85  65
                  |
                 100

A Binomial Heap with 12 nodes. It is a collection of 2 Binomial Trees of orders 2 and 3
from left to right.

Binary Representation of a number and Binomial Heaps

A Binomial Heap with n nodes has number of Binomial Trees equal to the number of set bits in
Binary representation of n. For example let n be 13, there 3 set bits in binary representation of
n (00001101), hence 3 Binomial Trees. We can also relate degree of these Binomial Trees with
positions of set bits. With this relation we can conclude that there are O(Logn) Binomial Trees
in a Binomial Heap with 'n' nodes.

==Operations of Binomial Heap:==
The main operation in Binomial Heap is union(), all other operations mainly use this operation.
The union() operation is to combine two Binomial Heaps into one.
Let us first discuss other operations, we will discuss union later.

1) insert(H, k): Inserts a key 'k' to Binomial Heap 'H'. This operation first creates a Binomial
Heap with single key 'k', then calls union on H and the new Binomial heap.

2) getMin(H): A simple way to getMin() is to traverse the list of root of Binomial Trees and
return the minimum key. This implementation requires O(Logn) time. It can be optimized to O(1) by
maintaining a pointer to minimum key root.

3) extractMin(H): This operation also uses union(). We first call getMin() to find the minimum
key Binomial Tree, then we remove the node and create a new Binomial Heap by connecting all
subtrees of the removed minimum node. Finally we call union() on H and the newly created Binomial
Heap. This operation requires O(Logn) time.

4) delete(H): Like Binary Heap, delete operation first reduces the key to minus infinite, then
calls extractMin().

5) decreaseKey(H): decreaseKey() is also similar to Binary Heap. We compare the decreases key
with it parent and if parent's key is more, we swap keys and recur for parent. We stop when we
either reach a node whose parent has smaller key or we hit the root node. Time complexity of
decreaseKey() is O(Logn).

======Union operation in Binomial Heap:======
Given two Binomial Heaps H1 and H2, union(H1, H2) creates a single Binomial Heap.

1) The first step is to simply merge the two Heaps in non-decreasing order of degrees. In the
following diagram, figure(b) shows the result after merging.

2) After the simple merge, we need to make sure that there is at-most one Binomial Tree of any
order. To do this, we need to combine Binomial Trees of same order. We traverse the list of
merged roots, we keep track of three pointers, prev, x and next-x. There can be following 4 cases
when we traverse the list of roots.

-- Case 1: Orders of x and next-x are not same, we simply move ahead.

In following 3 cases orders of x and next-x are same.
-- Case 2: If order of next-next-x is also same, move ahead.
-- Case 3: If key of x is smaller than or equal to key of next-x, then make next-x as a child of
    x by linking it with x.
-- Case 4: If key of x is greater than or equal to key of next-x, then make x as child of next.

==How to represent Binomial Heap?==
A Binomial Heap is a set of Binomial Trees. A Binomial Tree must be represented in a way that
allows sequential access to all siblings, starting from the leftmost sibling (We need this in and
extractMin() and delete()). The idea is to represent Binomial Trees as leftmost child and
right-sibling representation, i.e., every node stores two pointers, one to the leftmost child and
other to the right sibling.


==Implementation of Binomial Heap==
In previous article, we have discussed about the concepts related to Binomial heap.

Examples Binomial Heap:


12------------10--------------------20
             /  \                 /  | \
           15    50             70  50  40
           |                  / |    |
           30               80  85  65
                            |
                           100

A Binomial Heap with 13 nodes. It is a collection of 3 Binomial Trees of orders 0, 2 and 3
from left to right.

    10--------------------20
   /  \                 /  | \
 15    50             70  50  40
 |                  / |    |
 30               80  85  65
                  |
                 100

In this article, implementation of Binomial Heap is discussed. Following functions implemented :

1.  insert(H, k): Inserts a key 'k' to Binomial Heap 'H'. This operation first creates a Binomial
    Heap with single key 'k', then calls union on H and the new Binomial heap.

2.  getMin(H): A simple way to getMin() is to traverse the list of root of Binomial Trees and
    return the minimum key. This implementation requires O(Logn) time. It can be optimized to O(1)
    by maintaining a pointer to minimum key root.

3.  extractMin(H): This operation also uses union(). We first call getMin() to find the minimum key
    Binomial Tree, then we remove the node and create a new Binomial Heap by connecting all
    subtrees of the removed minimum node. Finally we call union() on H and the newly created
    Binomial Heap. This operation requires O(Logn) time.

Refer diagram shown in
http://www.geeksforgeeks.org/binomial-heap-2/

"""
import typing


class Node(object):
    def __init__(self, key, degree=0, parent=None, child=None, sibling=None):
        self.key = key
        self.degree = degree
        self.parent = parent
        self.child = child
        self.sibling = sibling

    def compare_to(self, other):
        return self.key.compare_to(other.key)

# ======= IMPLEMENTATION 2 ========== #


class BinomialHeap(object):
    def __init__(self, _heap: typing.List[int] = []):
        self.heap = _heap

    def swap(self, b1, b2):
        """
        :param b1: Node
        :param b2: Node
        :return:
        """
        pass

    def merge_binomial_trees(self, b1, b2):
        # Make sure b1 is smaller
        # Case 4: If key of x is greater than or equal to key of next-x, then make x as
        # child of next.
        if b1.key > b2.key:
            b1, b2 = b2, b1

        # Case 3: If key of x is smaller than or equal to key of next-x, then make next-x as
        # a child of x by linking it with x.
        # We basically make larger valued tree a child of smaller valued tree
        b2.parent = b1
        b2.sibling = b1.child
        b1.child = b2
        b1.degree += 1

        return b1

    def union_bionomial_heap(self, l1: typing.List[int], l2: typing.List[int]):
        """
        Merge the two Heaps in non-decreasing order of degrees.
        This function perform union operation on two binomial heap i.e. l1 & l2.

        :param l1:
        :param l2:
        :return:
        """
        # _new to another binomial heap which contain new heap after merging l1 & l2
        _new = []
        it, ot = 0, 0

        while it < len(l1) and ot < len(l2):
            if l1[it].degree <= l2[ot].degree:  # if D(l1) <= D(l2)
                _new.append(l1[it])
                it += 1
            else:  # if D(l1) > D(l2)
                _new.append(l2[ot])
                ot += 1

        # if there remains some elements in l1 binomial heap
        while it < len(l1):
            _new.append(l1[it])
            it += 1

        # if there remains some elements in l2 binomial heap
        while ot < len(l2):
            _new.append(l2[ot])
            ot += 1

        return _new

    def adjust(self, _heap):
        """
        adjust function rearranges the heap so that heap is in increasing order of degree and no
        two binomial trees have same degree in this heap

        :param _heap: list(Node)
        :return:
        """
        if len(_heap) <= 1:
            return _heap

        it1, it2, it3 = 0, 0, 0
        if len(_heap) == 2:
            it2 = it1
            it2 += 1
            it3 = len(_heap)
        else:
            it2 += 1
            it3 = it2
            it3 += 1

        while it1 < len(_heap):
            # if only one element remains to be processed
            if it2 == len(_heap):
                it1 += 1

            # If D(it1) < D(it2) i.e. merging of Binomial Tree pointed by it1 & it2 is not
            # possible then move next in heap
            # --Case 1: Orders of x and next-x are not same, we simply move ahead.
            elif _heap[it1].degree < _heap[it2].degree:
                it1 += 1
                it2 += 1
                if it3 < len(_heap):
                    it3 += 1

            # if D(it1),D(it2) & D(it3) are same i.e. degree of three consecutive
            # Binomial Tree are same in heap
            # —–Case 2: If order of next-next-x is also same, move ahead.
            elif it3 < len(_heap) and _heap[it1].degree == _heap[it2].degree and \
                    _heap[it1].degree == _heap[it3].degree:
                it1 += 1
                it2 += 1
                it3 += 1

            # if degree of two Binomial Tree are same in heap
            elif _heap[it1].degree == _heap[it2].degree:
                _heap[it1] = self.merge_binomial_trees(_heap[it1], _heap[it2])
                _heap.remove(_heap[it2])
                if it3 < len(_heap):
                    it3 += 1

        return _heap

    def insert_tree_in_heap(self, _heap: typing.List[int], tree: Node):
        """inserting a Binomial Tree into binomial heap"""
        # creating a new heap i.e temp inserting Binomial Tree into heap
        temp = [tree]

        # perform union operation to finally insert Binomial Tree in original heap
        temp = self.union_bionomial_heap(_heap, temp)
        return self.adjust(temp)

    def remove_min_from_tree_return_bheap(self, tree):
        """
        removing minimum key element from binomial heap this function take Binomial Tree as
        input and return binomial heap after removing head of that tree i.e. minimum element
        """
        _heap = []
        temp = tree.child

        #  making a binomial heap from Binomial Tree
        while temp:
            lo = temp
            temp = temp.sibling
            lo.sibling = None
            _heap.insert(0, lo)

        return _heap

    def insert(self, key):
        """inserting a key into the binomial heap"""
        temp = Node(key)
        self.heap = self.insert_tree_in_heap(self.heap, temp)

    def get_min(self):
        """return pointer of minimum value Node present in the binomial heap"""
        it = 0
        temp = self.heap[it]
        while it < len(self.heap):
            if self.heap[it].key < temp.key:
                temp = self.heap[it]
            it += 1
        return temp

    def extract_min(self):
        new_heap = []

        #  temp contains the pointer of minimum value element in heap
        temp = self.get_min()
        it = 0
        while it < len(self.heap):
            if self.heap[it] != temp:
                # inserting all Binomial Tree into new binomial heap except the Binomial Tree
                # contains minimum element
                new_heap.append(self.heap[it])
            it += 1
        lo = self.remove_min_from_tree_return_bheap(temp)
        new_heap = self.union_bionomial_heap(new_heap, lo)
        new_heap = self.adjust(new_heap)
        self.heap = new_heap

    def print_tree(self, h):
        """print function for Binomial Tree"""
        while h:
            print(h.key, end=" ")
            self.print_tree(h.child)
            h = h.sibling

    def print_heap(self, _heap=None):
        """print function for binomial heap"""
        it = 0
        while it < len(_heap):
            self.print_tree(_heap[it])
            it += 1
        print("")


if __name__ == '__main__':
    _heap = []
    binomial = BinomialHeap(_heap)
    #  Insert data in the heap
    binomial.insert(10)
    binomial.insert(20)
    binomial.insert(30)
    binomial.insert(40)
    binomial.insert(50)
    binomial.insert(60)

    print("\nHeap elements after insertion:")
    binomial.print_heap(binomial.heap)

    temp = binomial.get_min()
    print("Minimum element of heap ", temp.key)

    #  Delete minimum element of heap
    binomial.extract_min()
    print("Heap after deletion of minimum element")
    binomial.print_heap(binomial.heap)
