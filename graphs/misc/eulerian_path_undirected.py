"""
Eulerian path and circuit for undirected graph

Eulerian Path is a path in graph that visits every edge exactly once. Eulerian Circuit is an
Eulerian Path which starts and ends on the same vertex.

    ---- REFER -- DIAGRAM --
    http://www.geeksforgeeks.org/eulerian-path-and-circuit/

How to find whether a given graph is Eulerian or not?
The problem is same as following question. "Is it possible to draw a given graph without lifting
pencil from the paper and without tracing any of the edges more than once".

A graph is called Eulerian if it has an Eulerian Cycle and called Semi-Eulerian if it has an
Eulerian Path. The problem seems similar to Hamiltonian Path which is NP complete problem for a
general graph. Fortunately, we can find whether a given graph has a Eulerian Path or not in
polynomial time. In fact, we can find it in O(V+E) time.

Following are some interesting properties of undirected graphs with an Eulerian path and cycle.
We can use these properties to find whether a graph is Eulerian or not.

Eulerian Cycle
An undirected graph has Eulerian cycle if following two conditions are true.
a)  All vertices with non-zero degree are connected. We don't care about vertices with zero degree
    because they don't belong to Eulerian Cycle or Path (we only consider all edges).
b)  All vertices have even degree.

Eulerian Path
An undirected graph has Eulerian Path if following two conditions are true.
a)  Same as condition (a) for Eulerian Cycle
b)  If zero or two vertices have odd degree and all other vertices have even degree. Note that only
    one vertex with odd degree is not possible in an undirected graph (sum of all degrees is always
    even in an undirected graph)

Note that a graph with no edges is considered Eulerian because there are no edges to traverse.

How does this work?
In Eulerian path, each time we visit a vertex v, we walk through two unvisited edges with one end
point as v. Therefore, all middle vertices in Eulerian Path must have even degree. For Eulerian
Cycle, any vertex can be middle vertex, therefore all vertices must have even degree.

"""

# Python program to check if a given graph is Eulerian or not
# Time Complexity : O(V+E)

from collections import defaultdict


# This class represents a undirected graph using adjacency list representation
class Graph(object):
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # A function used by isConnected
    def DFSUtil(self, v, visited):
        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def isConnected(self):
        """
        Method to check if all non-zero degree vertices are connected.
        It mainly does DFS traversal starting from node with non-zero degree
        """
        # Mark all the vertices as not visited
        visited = [False] * self.V
        i = 0
        #  Find a vertex with non-zero degree
        for i in range(self.V):
            if len(self.graph[i]) > 1:
                break

        # If there are no edges in the graph, return true
        if i == self.V - 1:
            return True

        # Start DFS traversal from a vertex with non-zero degree
        self.DFSUtil(i, visited)

        # Check if all non-zero degree vertices are visited
        for i in range(self.V):
            if not visited[i] and len(self.graph[i]) > 0:
                return False

        return True

    def isEulerian(self):
        """
        The function returns one of the following values
        0 --> If graph is not Eulerian
        1 --> If graph has an Euler path (Semi-Eulerian)
        2 --> If graph has an Euler Circuit (Eulerian)
        :return: None
        """
        # Check if all non-zero degree vertices are connected
        if not self.isConnected():
            return 0
        else:
            # Count vertices with odd degree
            odd = 0
            for i in range(self.V):
                if len(self.graph[i]) % 2 != 0:
                    odd += 1

            # If odd count is 2, then semi-eulerian.
            # If odd count is 0, then eulerian
            # If count is more than 2, then graph is not Eulerian
            # Note that odd count can never be 1 for undirected graph
            if odd == 0:
                return 2
            elif odd == 2:
                return 1
            elif odd > 2:
                return 0

    # Function to run test cases
    def test(self):
        res = self.isEulerian()
        if res == 2:
            print("graph has a Euler cycle")
        elif res == 1:
            print("graph has a Euler path")
        else:
            print("graph is not Eulerian")


if __name__ == '__main__':
    # Time Complexity: O(V+E)
    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)
    g1.test()

    g2 = Graph(5)
    g2.addEdge(1, 0)
    g2.addEdge(0, 2)
    g2.addEdge(2, 1)
    g2.addEdge(0, 3)
    g2.addEdge(3, 4)
    g2.addEdge(4, 0)
    g2.test()

    g3 = Graph(5)
    g3.addEdge(1, 0)
    g3.addEdge(0, 2)
    g3.addEdge(2, 1)
    g3.addEdge(0, 3)
    g3.addEdge(3, 4)
    g3.addEdge(1, 3)
    g3.test()

    # Let us create a graph with 3 vertices
    # connected in the form of cycle
    g4 = Graph(3)
    g4.addEdge(0, 1)
    g4.addEdge(1, 2)
    g4.addEdge(2, 0)
    g4.test()

    # Let us create a graph with all veritces
    # with zero degree
    g5 = Graph(3)
    g5.test()
