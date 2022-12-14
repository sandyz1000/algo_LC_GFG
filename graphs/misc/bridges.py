"""
https://www.geeksforgeeks.org/bridge-in-a-graph/

Bridges in a graph

An edge in an undirected connected graph is a bridge iff removing it disconnects the graph.
For a disconnected undirected graph, definition is similar, a bridge is an edge removing which
increases number of connected components.

Like Articulation Points,bridges represent vulnerabilities in a connected network and are useful
for designing reliable networks. For example, in a wired computer network, an articulation point
indicates the critical computers and a bridge indicates the critical wires or connections.

    -- REFER -- DIAGRAM --
    http://www.geeksforgeeks.org/bridge-in-a-graph/

How to find all bridges in a given graph?
A simple approach is to one by one remove all edges and see if removal of a edge causes disconnected
graph. Following are steps of simple approach for connected graph.

1) For every edge (u, v), do following
...a) Remove (u, v) from graph
...b) See if the graph remains connected (We can either use BFS or DFS)
...c) Add (u, v) back to the graph.

Time complexity of above method is O(E*(V+E)) for a graph represented using adjacency list.
Can we do better?

A O(V+E) algorithm to find all Bridges
The idea is similar to O(V+E) algorithm for Articulation Points. We do DFS traversal of the given
graph. In DFS tree an edge (u, v) (u is parent of v in DFS tree) is bridge if there does not exit
any other alternative to reach u or an ancestor of u from subtree rooted with v. As discussed in
the previous post, the value low[v] indicates earliest visited vertex reachable from subtree rooted
with v. The condition for an edge (u, v) to be a bridge is, "low[v] > disc[u]"

"""
from __future__ import print_function

# Python program to find bridges in a given undirected graph
# Complexity : O(V+E)

from collections import defaultdict


# This class represents an undirected graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.time = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridge_util(self, u, visited, parent, low, disc):
        """
        A recursive function that finds and prints bridges using DFS traversal
        u --> The vertex to be visited next
        visited[] --> keeps tract of visited vertices
        disc[] --> Stores discovery times of visited vertices
        parent[] --> Stores parent vertices in DFS tree
        :param u:
        :param visited:
        :param parent:
        :param low:
        :param disc:
        :return:
        """
        # Count of children in current node
        children = 0

        # Mark the current node as visited and print it
        visited[u] = True

        # Initialize discovery time and low value
        disc[u] = self.time
        low[u] = self.time
        self.time += 1

        # Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if not visited[v]:
                parent[v] = u
                children += 1
                self.bridge_util(v, visited, parent, low, disc)

                # Check if the subtree rooted with v has a connection to one of the ancestors of u
                low[u] = min(low[u], low[v])

                # If the lowest vertex reachable from subtree under v is below u in DFS tree,
                # then u-v is a bridge
                if low[v] > disc[u]:
                    print("%d %d" % (u, v))

            elif v != parent[u]:  # Update low value of u for parent function calls.
                low[u] = min(low[u], disc[v])

    def bridge(self):
        """DFS based function to find all bridges. It uses recursive function bridgeUtil()"""
        # Mark all the vertices as not visited and Initialize parent and visited,
        # and ap(articulation point) arrays
        visited = [False] * self.V
        disc = [float("Inf")] * self.V
        low = [float("Inf")] * self.V
        parent = [-1] * self.V

        # Call the recursive helper function to find bridges in DFS tree rooted with vertex 'i'
        for i in range(self.V):
            if not visited[i]:
                self.bridge_util(i, visited, parent, low, disc)


if __name__ == '__main__':
    # Time Complexity: The above function is simple DFS with additional arrays.
    # So time complexity is same as DFS which is O(V+E) for adjacency list representation of graph
    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)

    print("Bridges in first graph ")
    g1.bridge()

    g2 = Graph(4)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    print("\nBridges in second graph ")
    g2.bridge()

    g3 = Graph(7)
    g3.addEdge(0, 1)
    g3.addEdge(1, 2)
    g3.addEdge(2, 0)
    g3.addEdge(1, 3)
    g3.addEdge(1, 4)
    g3.addEdge(1, 6)
    g3.addEdge(3, 5)
    g3.addEdge(4, 5)
    print("\nBridges in third graph ")
    g3.bridge()
