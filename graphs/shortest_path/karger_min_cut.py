"""Karger's algorithm for Minimum Cut | Set 1 (Introduction and Implementation)

http://www.geeksforgeeks.org/kargers-algorithm-for-minimum-cut-set-1-introduction-and-implementation/

Given an undirected and unweighted graph, find the smallest cut (smallest number of edges that
disconnects the graph into two components).

The input graph may have parallel edges.

    (0)-- a --(1)
     |  \       |
     b    c     d
     |       \  |
    (2)-- e --(3)

A Simple Solution use Max-Flow based s-t cut algorithm to find minimum cut. Consider every pair of
vertices as source 's' and sink 't', and call minimum s-t cut algorithm to find the s-t cut. Return
minimum of all s-t cuts. Best possible time complexity of this algorithm is O(V5) for a graph.
[How? there are total possible V2 pairs and s-t cut algorithm for one pair takes O(V*E) time and
E = O(V2)].

Below is simple Karger's Algorithm for this purpose. Below Karger's algorithm can be implemented in
O(E) = O(V2) time.

1)  Initialize contracted graph CG as copy of original graph
2)  While there are more than 2 vertices.
      a) Pick a random edge (u, v) in the contracted graph.
      b) Merge (or contract) u and v into a single vertex (update
         the contracted graph).
      c) Remove self-loops
3) Return cut represented by two vertices."""

from __future__ import print_function

from collections import namedtuple
from random import randint

# Karger's algorithm to find Minimum Cut in an undirected, unweighted and connected graph.

# a structure to represent a unweighted edge in graph
Edge = namedtuple('Edge', ['src', 'dest'])
Edge.__new__.__defaults__ = (None, None,)


# a structure to represent a connected, undirected and unweighted graph as a collection of edges.
class Graph(object):
    def __init__(self, V, E, edge=[]):
        # V-> Number of vertices, E-> Number of edges
        self.V = V
        self.E = E
        # graph is represented as an array of edges. Since the graph is undirected, the edge
        # from src to dest is also edge from dest to src. Both are counted as 1 edge here.
        self.edge = edge

    def kargerMinCut(self):
        """
        # A very basic implementation of Karger's randomized algorithm for finding the minimum cut.
        # Please note that Karger's algorithm is a Monte Carlo Randomized algo and the cut returned
        # by the algorithm may not be minimum always
        :return:
        """
        # Get data of given graph
        V = self.V
        E = self.E
        edge = self.edge

        # Allocate memory for creating V subsets.
        # Create V subsets with single elements
        subsets = [Subset(v, 0) for v in range(V)]
        vertices = V  # Initially there are V vertices in contracted graph
        # Keep contracting vertices until there are 2 vertices.
        while vertices > 2:
            i = randint(0, E)  # Pick a random edge
            # Find vertices (or sets) of two corners of current edge
            subset1 = Subset.find(subsets, edge[i].src)
            subset2 = Subset.find(subsets, edge[i].dest)
            # If two corners belong to same subset, then no point considering this edge
            if subset1 == subset2:
                continue

            else:  # Else contract the edge (or combine the corners of edge into one vertex)
                print("Contracting edge %d-%d\n" % (edge[i].src, edge[i].dest))
                vertices -= 1
                Subset.union(subsets, subset1, subset2)

        # Now we have two vertices (or subsets) left in the contracted graph, so count the
        # edges between two components and return the count.
        cutedges = 0
        for i in range(E):
            subset1 = Subset.find(subsets, edge[i].src)
            subset2 = Subset.find(subsets, edge[i].dest)
            if subset1 != subset2:
                cutedges += 1

        return cutedges


class Subset(object):
    """A structure to represent a subset for union-find"""

    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

    # A utility function to find set of an element i (uses path compression technique)
    @staticmethod
    def find(subsets, i):
        # find root and make root as parent of i (path compression)
        if subsets[i].parent != i:
            subsets[i].parent = Subset.find(subsets, subsets[i].parent)

        return subsets[i].parent

    # A function that does union of two sets of x and y (uses union by rank)
    @staticmethod
    def union(subsets, x, y):
        xroot = Subset.find(subsets, x)
        yroot = Subset.find(subsets, y)

        # Attach smaller rank tree under root of high rank tree (Union by Rank)
        if subsets[xroot].rank < subsets[yroot].rank:
            subsets[xroot].parent = yroot

        elif subsets[xroot].rank > subsets[yroot].rank:
            subsets[yroot].parent = xroot

        # // If ranks are same, then make one as root and increment its rank by one
        else:
            subsets[yroot].parent = xroot
            subsets[xroot].rank += 1


if __name__ == '__main__':
    # Let us create following unweighted graph
    #     0------1
    #     | \    |
    #     |   \  |
    #     |     \|
    #     2------3

    V = 4  # Number of vertices in graph
    E = 5  # Number of edges in graph
    edges = [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3)]

    graph = Graph(V, E, [Edge(edge[0], edge[1]) for edge in edges])
    # Use a different seed value for every run.
    # randint(time())

    print("\nCut found by Karger's randomized algo is %d\n" % graph.kargerMinCut())
