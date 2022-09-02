# coding=utf-8
"""
Fibonacci Heap | Set 1

https://brilliant.org/wiki/fibonacci-heap/
http://www.geeksforgeeks.org/fibonacci-heap-set-1-introduction/
https://github.com/danielborowski/fibonacci-heap-python

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1) Find Min:      Θ(1)     [Same as both Binary and Binomial]
2) Delete Min:    O(Log n) [Θ(Log n) in both Binary and Binomial]
3) Insert:        Θ(1)     [Θ(Log n) in Binary and Θ(1) in Binomial]
4) Decrease-Key:  Θ(1)     [Θ(Log n) in both Binary and Binomial]
5) Merge:         Θ(1)     [Θ(m Log n) or Θ(m+n) in Binary and Θ(Log n) in Binomial]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Like Binomial Heap, Fibonacci Heap is a collection of trees with min-heap or max-heap property.
In Fibonacci Heap, trees can have any shape even all trees can be single nodes (This is unlike
Binomial Heap where every tree has to be Binomial Tree).

                                         min
                                          |
                                          v
        17 ----- 24 ----- 23 ---- 7 ----- 3
        |       /  |                   /  |  \
        |      26  46                 18  52 41
        30     |                      |       |
               35                     39     44

Fibonacci Heap maintains a pointer to minimum value (which is root of a tree). All tree roots are
connected using circular doubly linked list, so all of them can be accessed using single 'min'
pointer.

The main idea is to execute operations in "lazy" way. For example merge operation simply links
two heaps, insert operation simply adds a new tree with single node. The operation extract
minimum is the most complicated operation. It does delayed work of consolidating trees. This
makes delete also complicated as delete first decreases key to minus infinite, then calls extract
minimum.

------------------------------------------------------------------------
==Below are some interesting facts about Fibonacci Heap==
------------------------------------------------------------------------

1.) The reduced time complexity of Decrease-Key has importance in Dijkstra and Prim algorithms.
With Binary Heap, time complexity of these algorithms is O(VLogV + ELogV). If Fibonacci Heap is
used, then time complexity is improved to O(VLogV + E)

2.) Although Fibonacci Heap looks promising time complexity wise, it has been found slow in
practice as hidden constants are high (Source Wiki).

3.) Fibonacci heap are mainly called so because Fibonacci numbers are used in the running time
analysis. Also, every node in Fibonacci Heap has degree at most O(log n) and the size of a
subtree rooted in a node of degree k is at least Fk+2, where Fk is the kth Fibonacci number.

"""
from __future__ import print_function
from heapq import *
from random import randint


class FibonacciHeap:
    # internal node class
    class Node:
        def __init__(self, data):
            self.data = data
            self.parent = self.child = self.left = self.right = None
            self.degree = 0
            self.mark = False

    # function to iterate through a doubly linked list
    def iterate(self, head):
        node = stop = head
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right

    # pointer to the head and minimum node in the root list
    root_list, min_node = None, None

    # maintain total node count in full fibonacci heap
    total_nodes = 0

    # return min node in O(1) time
    def find_min(self):
        return self.min_node

    def extract_min(self):
        """
        extract (delete) the min node from the heap in O(log n) time amortized cost analysis
        can be found here (http://bit.ly/1ow1Clm)

        """
        z = self.min_node
        if z is not None:
            if z.child is not None:
                # attach child nodes to root list
                children = [x for x in self.iterate(z.child)]
                for i in range(0, len(children)):
                    self.merge_with_root_list(children[i])
                    children[i].parent = None
            self.remove_from_root_list(z)
            # set new min node in heap
            if z == z.right:
                self.min_node = self.root_list = None
            else:
                self.min_node = z.right
                self.consolidate()
            self.total_nodes -= 1
        return z

    def insert(self, data):
        """insert new node into the unordered root list in O(1) time"""
        n = self.Node(data)
        n.left = n.right = n
        self.merge_with_root_list(n)
        if self.min_node is None or n.data < self.min_node.data:
            self.min_node = n
        self.total_nodes += 1

    def decrease_key(self, x, k):
        """modify the data of some node in the heap in O(1) time"""
        if k > x.data:
            return None
        x.data = k
        y = x.parent
        if y is not None and x.data < y.data:
            self.cut(x, y)
            self.cascading_cut(y)
        if x.data < self.min_node.data:
            self.min_node = x

    def merge(self, h2):
        """
        merge two fibonacci heaps in O(1) time by concatenating the root lists the root of
        the new root list becomes equal to the first list and the second list is simply
        appended to the end (then the proper min node is determined)
        """
        H = FibonacciHeap()
        H.root_list, H.min_node = self.root_list, self.min_node
        # fix pointers when merging the two heaps
        last = h2.root_list.left
        h2.root_list.left = H.root_list.left
        H.root_list.left.right = h2.root_list
        H.root_list.left = last
        H.root_list.left.right = H.root_list
        # update min node if needed
        if h2.min_node.data < H.min_node.data:
            H.min_node = h2.min_node
        # update total nodes
        H.total_nodes = self.total_nodes + h2.total_nodes
        return H

    def cut(self, x, y):
        """
        if a child node becomes smaller than its parent node we cut this child node off
        and bring it up to the root list
        """
        self.remove_from_child_list(y, x)
        y.degree -= 1
        self.merge_with_root_list(x)
        x.parent = None
        x.mark = False

    def cascading_cut(self, y):
        """cascading cut of parent node to obtain good time bounds"""
        z = y.parent
        if z is not None:
            if y.mark is False:
                y.mark = True
            else:
                self.cut(y, z)
                self.cascading_cut(z)

    def consolidate(self):
        """
        combine root nodes of equal degree to consolidate the heap by creating a list
        of unordered binomial trees

        :return:
        """
        A = [None] * self.total_nodes
        nodes = [w for w in self.iterate(self.root_list)]
        for w in range(0, len(nodes)):
            x = nodes[w]
            d = x.degree
            while A[d] is not None:
                y = A[d]
                if x.data > y.data:
                    temp = x
                    x, y = y, temp
                self.heap_link(y, x)
                A[d] = None
                d += 1
            A[d] = x

        # find new min node - no need to reconstruct new root list below because root list
        # was iteratively changing as we were moving nodes around in the above loop
        for i in range(0, len(A)):
            if A[i] is not None:
                if A[i].data < self.min_node.data:
                    self.min_node = A[i]

    def heap_link(self, y, x):
        """
        actual linking of one node to another in the root list while also updating
        the child linked list
        """
        self.remove_from_root_list(y)
        y.left = y.right = y
        self.merge_with_child_list(x, y)
        x.degree += 1
        y.parent = x
        y.mark = False

    def merge_with_root_list(self, node):
        """merge a node with the doubly linked root list"""
        if self.root_list is None:
            self.root_list = node
        else:
            node.right = self.root_list.right
            node.left = self.root_list
            self.root_list.right.left = node
            self.root_list.right = node

    def merge_with_child_list(self, parent, node):
        """merge a node with the doubly linked child list of a root node"""
        if parent.child is None:
            parent.child = node
        else:
            node.right = parent.child.right
            node.left = parent.child
            parent.child.right.left = node
            parent.child.right = node

    def remove_from_root_list(self, node):
        """remove a node from the doubly linked root list"""
        if node == self.root_list:
            self.root_list = node.right
        node.left.right = node.right
        node.right.left = node.left

    def remove_from_child_list(self, parent, node):
        """remove a node from the doubly linked child list"""
        if parent.child == parent.child.right:
            parent.child = None
        elif parent.child == node:
            parent.child = node.right
            node.right.parent = parent
        node.left.right = node.right
        node.right.left = node.left


if __name__ == '__main__':
    f = FibonacciHeap()
    f.insert(10)
    f.insert(2)
    f.insert(15)
    f.insert(6)

    m = f.find_min()
    print(m.data)  # 2

    q = f.extract_min()
    print(q.data)  # 2

    # q = f.extract_min()
    # print(q.data)  # 6

    f2 = FibonacciHeap()
    f2.insert(100)
    f2.insert(56)

    f3 = f.merge(f2)
    # x = f3.root_list.right  # pointer to random node
    x = f3.root_list.child
    f3.decrease_key(x, 1)

    # print the root list using the iterate class method
    print([x.data for x in f3.iterate(f3.root_list)])  # [10, 1, 56]

    q = f3.extract_min()
    print(q.data)  # 1
