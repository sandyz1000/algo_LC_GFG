"""
Boruvka's algorithm:

REFER DIAGRAM

http://www.geeksforgeeks.org/greedy-algorithms-set-9-boruvkas-algorithm/

Like Prim's and Kruskal's, Boruvka's algorithm is also a Greedy algorithm.

-----------------------------------------------------
Algorithm:
-----------------------------------------------------
1) Input is a connected, weighted and directed graph.
2) Initialize all vertices as individual components (or sets).
3) Initialize MST as empty.
4) While there are more than one components, do following for each component.
    a) Find the closest weight edge that connects this component to any other component.
    b) Add this closest edge to MST if not already added.
5) Return MST.

Interesting Facts about Boruvka's algorithm:
1) Time Complexity of Boruvka's algorithm is O(E log V) which is same as Kruskal's and Prim's
algorithms.

2) Boruvka's algorithm is used as a step in a faster randomized algorithm that works in linear
time O(E).

3) Boruvka's algorithm is the oldest minimum spanning tree algorithm was discovered by Boruvka's
in 1926, long before computers even existed. The algorithm was published as a method of
constructing an efficient electricity network.

"""
from __future__ import print_function


class Graph(object):
    """
    Boruvka's algorithm to find Minimum Spanning Tree of a given connected, undirected and
    weighted graph
    Class to represent a graph
    """
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        """A utility function to find set of an element i (uses path compression technique)"""
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        """A function that does union of two sets of x and y (uses union by rank)"""
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        # If ranks are same, then make one as root and increment
        # its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def boruvka_mst(self):
        """The main function to construct MST using Kruskal's algorithm"""
        parent = []
        rank = []
        # An array to store index of the cheapest edge of subset. It store [u,v,w] for each
        # component
        cheapest = []

        # Initially there are V different trees. Finally there will be one tree that will be MST
        num_trees = self.V
        mst_weight = 0

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            cheapest = [-1] * self.V

        # Keep combining components (or sets) until all components are not combined into single MST
        while num_trees > 1:
            # Traverse through all edges and update cheapest of every component
            for i in range(len(self.graph)):

                # Find components (or sets) of two corners of current edge
                u, v, w = self.graph[i]
                set1 = self.find(parent, u)
                set2 = self.find(parent, v)

                # If two corners of current edge belong to same set, ignore current edge. Else
                # check if current edge is closer to previous cheapest edges of set1 and set2
                if set1 != set2:
                    if cheapest[set1] == -1 or cheapest[set1][2] > w:
                        cheapest[set1] = [u, v, w]
                    if cheapest[set2] == -1 or cheapest[set2][2] > w:
                        cheapest[set2] = [u, v, w]

            # Consider the above picked cheapest edges and add them to MST
            for node in range(self.V):
                # Check if cheapest for current set exists
                if cheapest[node] != -1:
                    u, v, w = cheapest[node]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)

                    if set1 != set2:
                        mst_weight += w
                        self.union(parent, rank, set1, set2)
                        print("Edge %d-%d with weight %d included in MST" % (u, v, w))
                        num_trees = num_trees - 1

            # reset cheapest array
            cheapest = [-1] * self.V

        print("Weight of MST is %d" % mst_weight)


if __name__ == '__main__':
    # Output:
    # Edge 0-3 included in MST
    # Edge 0-1 included in MST
    # Edge 2-3 included in MST
    # Weight of MST is 19

    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    g.boruvka_mst()
