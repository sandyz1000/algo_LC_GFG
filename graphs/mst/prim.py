"""
https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/

Prim's algorithm is also a Greedy algorithm. It starts with an empty spanning tree. The idea
is to maintain two sets of vertices. The first set contains the vertices already included in the
MST, the other set contains the vertices not yet included. At every step, it considers all the
edges that connect the two sets, and picks the minimum weight edge from these edges. After
picking the edge, it moves the other endpoint of the edge to the set containing MST.

A group of edges that connects two set of vertices in a graph is called cut in graph theory. So, at
every step of Prim's algorithm, we find a cut (of two sets, one contains the vertices already
included in MST and other contains rest of the vertices), pick the minimum weight edge from the cut
and include this vertex to MST Set (the set that contains already included vertices).

How does Prim's Algorithm Work? The idea behind Prim's algorithm is simple, a spanning tree means
all vertices must be connected. So the two disjoint subsets (discussed above) of vertices must be
connected to make a Spanning Tree. And they must be connected with the minimum weight edge to
make it a Minimum Spanning Tree.

----------------------------------------
Algorithm
----------------------------------------
1) Create a set mst_set that keeps track of vertices already included in MST.

2) Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE.
Assign key value as 0 for the first vertex so that it is picked first.

3) While mstSet doesn't include all vertices
    a) Pick a vertex u which is not there in mstSet and has minimum key value.
    b) Include u to mstSet.
    c) Update key value of all adjacent vertices of u. To update the key values, iterate through
    all adjacent vertices. For every adjacent vertex v, if weight of edge u-v is less than the
    previous key value of v, update the key value as weight of u-v

The idea of using key values is to pick the minimum weight edge from cut. The key values are used
only for vertices which are not yet included in MST, the key value for these vertices indicate
the minimum weight edges connecting them to the set of vertices included in MST.

Time Complexity of the above program is O(V^2). If the input graph is represented using adjacency
list, then the time complexity of Prim's algorithm can be reduced to O(E log V) with the help of
binary heap.

"""

# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph
from __future__ import print_function
import sys


class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def print_mst(self, parent):
        """A utility function to print the constructed MST stored in parent[]"""
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def min_key(self, key, mst_set):
        """
        A utility function to find the vertex with minimum distance value, from the set of
        vertices not yet included in shortest path tree
        :type key:
        :type mst_set:
        :rtype:
        """

        # Initialize minimum value
        minimum = sys.maxsize
        min_index = sys.maxsize

        for v in range(self.V):
            if key[v] < minimum and not mst_set[v]:
                minimum = key[v]
                min_index = v

        return min_index

    def prim_mst(self):
        """
        Function to construct and print MST for a graph represented using adjacency
        matrix representation"""

        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        # Array to store constructed MST
        parent = [None] * self.V
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mst_set = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for _ in range(self.V):
            # Pick the minimum distance vertex from the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.min_key(key, mst_set)

            # Put the minimum distance vertex in the shortest path tree
            mst_set[u] = True

            # Update dist value of the adjacent vertices of the picked vertex only if the current
            # distance is greater than new distance and the vertex in not in the shortest path tree
            for v in range(self.V):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mst_set[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if 0 < self.graph[u][v] < key[v] and not mst_set[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)


if __name__ == '__main__':
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]

    g.prim_mst()
