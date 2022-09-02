"""
https://www.geeksforgeeks.org/union-find/

Disjoint Set (Or Union-Find) | Set 1 (Detect Cycle in an Undirected Graph)

A disjoint-set data structure is a data structure that keeps track of a set of elements
partitioned into a number of disjoint (non-overlapping) subsets. A union-find algorithm is an
algorithm that performs two useful operations on such a data structure:

Find: Determine which subset a particular element is in. This can be used for determining if two
elements are in the same subset.

Union: Join two subsets into a single subset.

In this post, we will discuss an application of Disjoint Set Data Structure. The application is
to check whether a given graph contains a cycle or not.

Union-Find Algorithm can be used to check whether an undirected graph contains cycle or not. Note
that we have discussed an algorithm to detect cycle. This is another method based on Union-Find.
This method assumes that graph doesn't contain any self-loops. We can keeps track of the subsets
in a 1D array, lets call it parent[].

            0
            |  \
            |    \
            2 --- 1

For each edge, make subsets using both the vertices of the edge. If both the vertices are in the
same subset, a cycle is found.

Initially, all slots of parent array are initialized to -1 (means there is only one item in
every subset).

- - - - - - - - - - - - - - - - - - - - - - - -
0   1   2
-1 -1  -1
- - - - - - - - - - - - - - - - - - - - - - - -

Now process all edges one by one.

Edge 0-1: Find the subsets in which vertices 0 and 1 are. Since they are in different subsets, we
take the union of them. For taking the union, either make node 0 as parent of node 1 or vice-versa.

- - - - - - - - - - - - - - - - - - - - - - - -
0   1   2    <----- 1 is made parent of 0 (1 is now representative of subset {0, 1})
1  -1  -1
- - - - - - - - - - - - - - - - - - - - - - - -

Edge 1-2: 1 is in subset 1 and 2 is in subset 2. So, take union.

- - - - - - - - - - - - - - - - - - - - - - - -
0   1   2    <----- 2 is made parent of 1 (2 is now representative of subset {0, 1, 2})
1   2  -1
- - - - - - - - - - - - - - - - - - - - - - - -

Edge 2-0: 0 is in subset 2 and 2 is also in subset 2. Hence, including this edge forms a cycle.

How subset of 0 is same as 2?
0->1->2 # 1 is parent of 0 and 2 is parent of 1

Note that the implementation of union() and find() is naive and takes O(n) time in worst case.
These methods can be improved to O(Logn) using Union by Rank or Height. We will soon be discussing
Union by Rank in a separate post.

"""
from typing import Dict, List
from collections import defaultdict


# This class represents a undirected graph using adjacency list representation
class Graph(object):
    def __init__(self, vertices: int):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A utility function to find the subset of an element i
    def find_parent(self, parents: List[int], i: int):
        if parents[i] == -1:
            return i
        if parents[i] != -1:
            return self.find_parent(parents, parents[i])

    # A utility function to do union of two subsets
    def union(self, parent: List[int], x: int, y: int):
        x = self.find_parent(parent, x)
        y = self.find_parent(parent, y)
        parent[x] = y

    # The main function to check whether a given graph contains cycle or not
    def is_cyclic(self):

        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sets
        parent = [-1] * self.V

        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)


if __name__ == '__main__':
    # Output: Graph contains cycle
    # Create a graph given in the above diagram
    g = Graph(3)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 0)

    if g.is_cyclic():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle")
