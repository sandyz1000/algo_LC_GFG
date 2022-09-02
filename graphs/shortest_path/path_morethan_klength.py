"""
Find if there is a path of more than k length from a source

Given a graph, a source vertex in the graph and a number k, find if there is a simple path (
without any cycle) starting from given source and ending at any other vertex.

------------------------------------------------
Example:
------------------------------------------------

Input  : Source s = 0, k = 58
Output : True
Explanation: There exists a simple path 0 -> 7 -> 1 -> 2 -> 8 -> 6 -> 5 -> 3 -> 4
Which has a total distance of 60 km which is more than 58.
------------------------
Input  : Source s = 0, k = 62
Output : False
Explanation: In the above graph, the longest simple path has distance 61
(0 -> 7 -> 1-> 2 -> 3 -> 4 -> 5-> 6 -> 8, so output should be false for any input greater than 61.
------------------------

Time Complexity: O(n!)

------------------------------------------------
Explanation:
------------------------------------------------

From the source node, we one-by-one visit all the paths and check if the total weight is greater
than k for each path. So, the worst case will be when the number of possible paths is maximum. This
is the case when every node is connected to every other node.

Beginning from the source node we have n-1 adjacent nodes. The time needed for a path to connect any
two nodes is 2. One for joining the source and the next adjacent vertex. One for breaking the
connection between the source and the old adjacent vertex.
After selecting a node out of n-1 adjacent nodes, we are left with n-2 adjacent nodes (as the source
node is already included in the path) and so on at every step of selecting a node our problem
reduces by 1 node.

We can write this in the form of a recurrence relation as: F(n) = n*(2+F(n-1))
This expands to: 2n + 2n*(n-1) + 2n*(n-1)*(n-2) + ... + 2n(n-1)(n-2)(n-3)...1
As n times 2n(n-1)(n-2)(n-3)...1 is greater than the given expression so we can safely say time
complexity is: n*2*n!

Here in the question the first node is defined so time complexity becomes
F(n-1) = 2(n-1)*(n-1)! = 2*n*(n-1)! - 2*1*(n-1)! = 2*n!-2*(n-1)! = O(n!)"""

from __future__ import print_function
from collections import defaultdict


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


# Program to find if there is a simple path with weight more than k
# This class represents a dir path graph using adjacency list representation
class Graph(object):
    def __init__(self, V):
        self.V = V
        # In a weighted graph, we need to store vertex
        # and weight pair for every edge
        self.adj = defaultdict(list)

    def path_more_than_k(self, src, k):
        """

        :param src:
        :param k:
        :return:
        """
        # Create a path array with nothing included in path
        path = [0] * self.V
        path[src] = True  # Add source vertex to path

        return self.path_more_than_k_util(src, k, path)

    # Prints shortest paths from src to all other vertices
    def path_more_than_k_util(self, src, k, path):
        # If k is 0 or negative, return true;
        if k <= 0:
            return True

        # Get all adjacent vertices of source vertex src and
        # recursively explore all paths from src.
        for i in self.adj[src]:
            v = i.first
            w = i.second

            # Get adjacent vertex and weight of edge
            # If vertex v is already there in path, then there is a cycle (we ignore this edge)
            if path[v]:
                continue

            if w >= k:  # If weight of is more than k, return true
                return True

            path[v] = True  # Else add this vertex to path

            # If this adjacent can provide a path longer than k, return true.
            if self.path_more_than_k_util(v, k - w, path):
                return True
            path[v] = False  # Backtrack

        # If no adjacent could produce longer path, return false
        return False

    # Utility function to an edge (u, v) of weight w
    def add_edge(self, u, v, w):
        self.adj[u].append(Pair(v, w))
        self.adj[v].append(Pair(u, w))


if __name__ == '__main__':
    # Output:
    # No, Yes
    V = 9  # create the graph given in above fugure
    g = Graph(V)

    # making above shown graph
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)
    src = 0
    k = 62
    print("Yes" if g.path_more_than_k(src, k) else "No")

    k = 60
    print("Yes" if g.path_more_than_k(src, k) else "No")
