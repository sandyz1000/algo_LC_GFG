"""
Kruskal Algorithm:

http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/

REFER DIAGRAM

What is Minimum Spanning Tree?

Given a connected and undirected graph, a spanning tree of that graph is a sub-graph that is a
tree and connects all the vertices together. A single graph can have many different spanning
trees. A minimum spanning tree (MST) or minimum weight spanning tree for a weighted, connected
and undirected graph is a spanning tree with weight less than or equal to the weight of every
other spanning tree. The weight of a spanning tree is the sum of weights given to each edge of
the spanning tree.

How many edges does a minimum spanning tree has?
A minimum spanning tree has (V - 1) edges where V is the number of vertices in the given graph.

What are the applications of Minimum Spanning Tree?
See this for applications of MST.

Below are the steps for finding MST using Kruskal's algorithm

1.  Sort all the edges in non-decreasing order of their weight.
2.  Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far.
    If cycle is not formed, include this edge. Else, discard it.
3.  Repeat step#2 until there are (V-1) edges in the spanning tree.

The algorithm is a Greedy Algorithm. The Greedy Choice is to pick the smallest weight edge that
does not cause a cycle in the MST constructed so far. Let us understand it with an example:
Consider the below input graph.
---------------------------------------------------------------

Time Complexity:
O(ElogE) or O(ElogV). Sorting of edges takes O(ELogE) time. After sorting, we iterate through
all edges and apply find-union algorithm. The find and union operations can take at most
O(LogV) time.
So overall complexity is O(ELogE + ELogV) time. The value of E can be at most O(V2), so O(LogV)
are O(LogE) same. Therefore, overall time complexity is O(ElogE) or O(ElogV) """

# Python program for Kruskal's algorithm to find Minimum Spanning Tree
# of a given connected, undirected and weighted graph
from __future__ import print_function


class Graph(object):
    """Class to represent a graph"""
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary to store graph

    def add_edge(self, u, v, w):
        """function to add an edge to graph"""
        self.graph.append([u, v, w])

    def find(self, parent, vertex):
        """A utility function to find set of an element i (uses path compression technique)"""
        if parent[vertex] == vertex:
            return vertex
        return self.find(parent, parent[vertex])

    def union(self, parent, rank, x, y):
        """A function that does union of two sets of x and y (uses union by rank)"""
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        # If ranks are same, then make one as root and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        """The main function to construct MST using Kruskal's algorithm"""
        result = []  # This will store the resultant MST

        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result[]

        # Step 1: Sort all the edges in non-decreasing order of their weight. If we are not
        # allowed to change the given graph, we can create a copy of graph
        self.graph.sort(key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            # Step 2: Pick the smallest edge and increment the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does't cause cycle, include it in result and increment the
            # index of result for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                # Else discard the edge

        # print the contents of result[] to display the built MST
        print("Following are the edges in the constructed MST")
        for u, v, weight in result:
            # print str(u) + " -- " + str(v) + " == " + str(weight)
            print("%d -- %d == %d" % (u, v, weight))


if __name__ == "__main__":
    # Output:
    # Following are the edges in the constructed MST
    # 2 -- 3 == 4
    # 0 -- 3 == 5
    # 0 -- 1 == 10

    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    g.kruskal_mst()
