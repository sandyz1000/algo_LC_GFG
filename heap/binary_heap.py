# coding=utf-8

"""
https://www.geeksforgeeks.org/binary-heap/

Binary Heap
A Binary Heap is a Binary Tree with following properties.

1) It's a complete tree (All levels are completely filled except possibly the last level and the
last level has all keys as left as possible). This property of Binary Heap makes them suitable to
be stored in an array.

2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at root must be
minimum among all keys present in Binary Heap. The same property must be recursively true for all
nodes in Binary Tree. Max Binary Heap is similar to Min Heap.

Examples of Min Heap:

            10                      10
         /      \               /       \
       20        100          15         30
      /                      /  \        /  \
    30                     40    50    100   40

How is Binary Heap represented?

A Binary Heap is a Complete Binary Tree. A binary heap is typically represented as array.
1. The root element will be at Arr[0].
2. Below table shows indexes of other nodes for the ith node, i.e., Arr[i]:
    Arr[(i-1)/2]	Returns the parent node
    Arr[(2*i)+1]	Returns the left child node
    Arr[(2*i)+2]	Returns the right child node

            1
         /      \
        3        6
      /   \    / 
     5    9   8

    [1, 3, 6, 5, 9, 8]

--------------------------------------------------------------------------------------------
Array Representation Of Binary Heap

Applications of Heaps:
1) Heap Sort: Heap Sort uses Binary Heap to sort an array in O(nLogn) time.

2) Priority Queue: Priority queues can be efficiently implemented using Binary Heap because it
supports insert(), delete() and extractmax(), decreaseKey() operations in O(logn) time. Binomoial
Heap and Fibonacci Heap are variations of Binary Heap. These variations perform union also
efficiently.

3) Graph Algorithms: The priority queues are especially used in Graph Algorithms like Dijkstra's
Shortest Path and Prim's Minimum Spanning Tree.

4) Many problems can be efficiently solved using Heaps. See following for example.
    a) K'th Largest Element in an array.
    b) Sort an almost sorted array/
    c) Merge K Sorted Arrays.


The traversal method use to achieve Array representation is Level Order
==Operations on Min Heap:==

1) getMini(): It returns the root element of Min Heap. Time Complexity of this operation is O(1).

2) extractMin(): Removes the minimum element from Min Heap. Time Complexity of this Operation is
O(Logn) as this operation needs to maintain the heap property (by calling heapify()) after
removing root.

3) decreaseKey(): Decreases value of key. Time complexity of this operation is O(Logn). If the
decreases key value of a node is greater than parent of the node, then we don't need to do
anything. Otherwise, we need to traverse up to fix the violated heap property.

4) insert(): Inserting a new key takes O(Logn) time. We add a new key at the end of the tree. IF
new key is greater than its parent, then we don't need to do anything. Otherwise, we need to
traverse up to fix the violated heap property.

5) delete(): Deleting a key also takes O(Logn) time. We replace the key to be deleted with minimum
infinite by calling decreaseKey(). After decreaseKey(), the minus infinite value must reach root,
so we call extractMin() to remove key.

-----------------------------------------------------------------------
==Applications of Heap Data Structure==
-----------------------------------------------------------------------
http://www.geeksforgeeks.org/applications-of-heap-data-structure/

Heap Data Structure is generally taught with Heapsort. Heapsort algorithm has limited uses
because Quicksort is better in practice. Nevertheless, the Heap data structure itself is
enormously used. Following are some uses other than Heapsort.

==Priority Queues:==
Priority queues can be efficiently implemented using Binary Heap because it supports insert(),
delete() and extractmax(), decreaseKey() operations in O(logn) time. Binomial Heap and Fibonacci
Heap are variations of Binary Heap. These variations perform union also in O(logn) time which is
a O(n) operation in Binary Heap. Heap Implemented priority queues are used in Graph algorithms
like Prim's Algorithm and Dijkstra's algorithm.

==Order statistics:==
The Heap data structure can be used to efficiently find the kth smallest (or largest) element
in an array

-----------------------------------------------------------------------
==Why is Binary Heap Preferred over BST for Priority Queue?==
-----------------------------------------------------------------------
http://www.geeksforgeeks.org/why-is-binary-heap-preferred-over-bst-for-priority-queue/

A typical Priority Queue requires following operations to be efficient.

    1. Get Top Priority Element (Get minimum or maximum)
    2. Insert an element
    3. Remove top priority element
    4. Decrease Key

A Binary Heap supports above operations with following time complexities:

    1. O(1)
    2. O(Logn)
    3. O(Logn)
    4. O(Logn)

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        Min Heap           Binary Search Tree

            8                   30
          /   \               /    \
        15    12             12    90
       /  \                 /  \
      90  30               8   15

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

A Self Balancing Binary Search Tree like AVL Tree, Red-Black Tree, etc can also support above
operations with same time complexities.

1.  Finding minimum and maximum are not naturally O(1), but can be easily implemented in O(1) by
    keeping an extra pointer to minimum or maximum and updating the pointer with insertion and
    deletion if required. With deletion we can update by finding inorder predecessor or successor.

2.  Inserting an element is naturally O(Logn)

3.  Removing maximum or minimum are also O(Logn)

4.  Decrease key can be done in O(Logn) by doing a deletion followed by insertion. See this for
    details.

==So why is Binary Heap Preferred for Priority Queue?==

1.  Since Binary Heap is implemented using arrays, there is always better locality of reference
    and operations are more cache friendly.
2.  Although operations are of same time complexity, constants in Binary Search Tree are higher.
3.  We can build a Binary Heap in O(n) time. Self Balancing BSTs require O(nLogn) time to construct.
4.  Binary Heap doesn't require extra space for pointers.
5.  Binary Heap is easier to implement.
6.  There are variations of Binary Heap like Fibonacci Heap that can support insert and
    decrease-key in Θ(1) time

==Is Binary Heap always better?==

Although Binary Heap is for Priority Queue, BSTs have their own advantages and the list of
advantages is in-fact bigger compared to binary heap.

1.  Searching an element in self-balancing BST is O(Logn) which is O(n) in Binary Heap.
2.  We can print all elements of BST in sorted order in O(n) time, but Binary Heap requires
    O(nLogn) time.
3.  Floor and ceil can be found in O(Logn) time.
4.  K'th largest/smallest element be found in O(Logn) time by augmenting tree with an additional
    field.

-----------------------------------------------------------------------
==Time Complexity of building a heap==
-----------------------------------------------------------------------
http://www.geeksforgeeks.org/time-complexity-of-building-a-heap/

Consider the following algorithm for building a Heap of an input array A.

- - - - - - - - - - - - - - - - - - - - - - - - +
BUILD-HEAP(A)                                   |
    heapsize := size(A);                        |
    for i := floor(heapsize/2) downto 1         |
        do HEAPIFY(A, i);                       |
    end for                                     |
END                                             |
- - - - - - - - - - - - - - - - - - - - - - - - +

A quick look over the above algorithm suggests that the running time is O(nlg(n)), since each call
to Heapify costs O(lg(n)) and Build-Heap makes O(n) such calls.

This upper bound, though correct, is not asymptotically tight.

We can derive a tighter bound by observing that the running time of Heapify depends on the height
of the tree 'h' (which is equal to lg(n), where n is number of nodes) and the heights of most
sub-trees are small.
The height 'h' increases as we move upwards along the tree. Line-3 of Build-Heap runs a loop from
the index of the last internal node (heapsize/2) with height=1, to the index of root(1) with
height = lg(n). Hence, Heapify takes different time for each node, which is O(h).

For finding the Time Complexity of building a heap, we must know the number of nodes having
height h.
For this we use the fact that, A heap of size n has at most n/2^(h+1) nodes with height h.

Now to derive the time complexity, we express the total cost of Build-Heap as-

(1) T(n) = \sum_{h = 0}^{lg(n)}\left \lceil \frac{n}{2^{h+1}} \right \rceil * O(h)\\ &= O(n *
\sum_{h = 0}^{lg(n)}\frac{h}{2^{h}})\\ &= O(n * \sum_{h = 0}^{\infty}\frac{h}{2^{h}})\\ \end{flalign*}

Step 2 uses the properties of the Big-Oh notation to ignore the ceiling function and the constant
2(2^{h+1} = 2.2^h). Similarly in Step three, the upper limit of the summation can be increased to
infinity since we are using Big-Oh notation.

Sum of infinite G.P. (x < 1)

(2)    \begin{align*} \sum_{n = 0}^{\infty}{x}^{n} = \frac{1}{1-x} \end{align*}

On differentiating both sides and multiplying by x, we get

(3)    \begin{align*} \sum_{n = 0}^{\infty}n{x}^{n} = \frac{x}{(1-x)^{2}} \end{align*}

Putting the result obtained in (3) back in our derivation (1), we get

(4)     = O(n * (1/2) / (1 - (1/2)^2) = O(n * 2)
        = O(n)

Hence Proved that the Time complexity for Building a Binary Heap is O(n).

"""

# Import the heap functions from python library
from heapq import heappush, heappop, heapify


class MinHeap:
    """
    heappop - pop and return the smallest element from heap
    heappush - push the value item onto the heap, maintaining heap invariant
    heapify - transform list into heap, in place, in linear time
    """
    # Constructor to initialize a heap
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insert_key(self, k):
        """ Inserts a new key 'k' """
        heappush(self.heap, k)

    def decrease_key(self, i, new_val):
        """
        Decrease value of key at index 'i' to new_val

        It is assumed that new_val is smaller than heap[i]
        """
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

    # Method to remove minimum element from min heap
    def extract_min(self):
        return heappop(self.heap)

    def delete_key(self, i):
        """
        This function deletes key at index i. It first reduces value to minus infinite and
        then calls extractMin()
        """
        self.decrease_key(i, float("-inf"))
        self.extract_min()

    # Get the minimum element from the heap
    def get_min(self):
        return self.heap[0]


if __name__ == '__main__':
    heapObj = MinHeap()
    heapObj.insert_key(3)
    heapObj.insert_key(2)
    heapObj.delete_key(1)
    heapObj.insert_key(15)
    heapObj.insert_key(5)
    heapObj.insert_key(4)
    heapObj.insert_key(45)

    print("Extract min:", heapObj.extract_min())
    print("Get min:", heapObj.get_min())
    heapObj.decrease_key(2, 1)
    print("Get min:", heapObj.get_min())