"""
Find if there is a path of more than k length from a source

- - - - - - - - - - - - - -
REFER DIAGRAM
http:www.geeksforgeeks.org/find-if-there-is-a-path-of-more-than-k-length-from-a-source/

Input  : Source s = 0, k = 58
Output : True
There exists a simple path 0 -> 7 -> 1 -> 2 -> 8 -> 6 -> 5 -> 3 -> 4

Which has a total distance of 60 km which is more than 58.

Input  : Source s = 0, k = 62
Output : False

In the above graph, the longest simple path has distance 61 (0 -> 7 -> 1-> 2 -> 3 -> 4 -> 5
-> 6 -> 8, so output  should be false for any input greater  than 61.
- - - - - - - - - - - - - -

One important thing to note is, simply doing BFS or DFS and picking the longest edge at every
step would not work. The reason is, a shorter edge can produce longer path due to higher weight
edges connected through it.

The idea is to use Backtracking. We start from given source, explore all paths from current
vertex. We keep track of current distance from source. If distance becomes more than k, we return
true. If a path doesn't produces more than k distance, we backtrack.

How do we make sure that the path is simple and we don't loop in a cycle? The idea is to keep
track of current path vertices in an array. Whenever we add a vertex to path, we check if it
already exists or not in current path. If it exists, we ignore the edge.


---------------------------------------
Explanation:
---------------------------------------
Time Complexity: O(n!)

From the source node, we one-by-one visit all the paths and check if the total weight is greater
than k for each path. So, the worst case will be when the number of possible paths is maximum.
This is the case when every node is connected to every other node.
Beginning from the source node we have n-1 adjacent nodes. The time needed for a path to connect
any two nodes is 2. One for joining the source and the next adjacent vertex. One for breaking the
connection between the source and the old adjacent vertex.
After selecting a node out of n-1 adjacent nodes, we are left with n-2 adjacent nodes (as the
source node is already included in the path) and so on at every step of selecting a node our
problem reduces by 1 node.

We can write this in the form of a recurrence relation as: F(n) = n*(2+F(n-1))
This expands to: 2n + 2n*(n-1) + 2n*(n-1)*(n-2) + .... + 2n(n-1)(n-2)(n-3) .....1
As n times 2n(n-1)(n-2)(n-3)....1 is greater than the given expression so we can safely say time
complexity is: n*2*n!

Here in the question the first node is defined so time complexity becomes
F(n-1) = 2(n-1)*(n-1)! = 2*n*(n-1)! - 2*1*(n-1)! = 2*n!-2*(n-1)! = O(n!)


"""
from __future__ import print_function
from collections import defaultdict


# Program to find if there is a simple path with weight more than k

#  iPair ==>  Integer Pair
class IPair(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


class Graph(object):
    """
    This class represents a dipathted graph using adjacency list representation
    """

    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)

    def addEdge(self, u, v, w):
        self.adj[u].append(IPair(v, w))
        self.adj[v].append(IPair(u, w))

    def pathMoreThanK(self, src, k):
        """Returns true if graph has path more than k length"""
        # # Create a path array with nothing included in path
        path = [False] * self.V

        # Add source vertex to path
        path[src] = True
        return self.pathMoreThanKUtil(src, k, path)

    def pathMoreThanKUtil(self, src, k, path):
        """
        Prints shortest paths from src to all other vertices
        :param src: int
        :param k: int
        :param path: List[bool]
        :return:
        """
        # If k is 0 or negative, return true
        if k <= 0:
            return True

        # Get all adjacent vertices of source vertex src and recursively explore all paths
        # from src.
        for i in self.adj[src]:
            # Get adjacent vertex and weight of edge
            v = i.first
            w = i.second

            # If vertex v is already there in path, then there is a cycle (we ignore this edge)
            if path[v]:
                continue

            #  If weight of is more than k, return true
            if w >= k:
                return True

            #  Else add this vertex to path
            path[v] = True

            # If this adjacent can provide a path longer than k, return true.
            if self.pathMoreThanKUtil(v, k - w, path):
                return True

            # Backtrack
            path[v] = False

        # If no adjacent could produce longer path, return false
        return False


if __name__ == '__main__':
    # Output
    # No
    # Yes

    # create the graph given in above fugure
    V = 9
    g = Graph(V)

    # making above shown graph
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)

    src = 0
    k = 62
    print("Yes" if g.pathMoreThanK(src, k) else "No")

    k = 60
    print("Yes" if g.pathMoreThanK(src, k) else "No")
