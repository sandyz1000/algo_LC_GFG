"""
Depth First Traversal or DFS for a Graph

http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/

Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree.
The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node
again. To avoid processing a node more than once, we use a boolean visited array.

For example, in the following graph, we start traversal from vertex 2. When we come to vertex 0,
we look for all adjacent vertices of it. 2 is also an adjacent vertex of 0. If we don't mark
visited vertices, then 2 will be processed again and it will become a non-terminating process. A
Depth First Traversal of the following graph is 2, 0, 1, 3.

            0 -------> 1
            A       /
            |      /
            |     /
            V <--/
   start--> 2 -------> 3 <- self loop

Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in
the graph
"""
from __future__ import print_function
# Python program to print DFS traversal for complete graph
from collections import defaultdict


# This class represents a directed graph using adjacency list representation
class Graph(object):
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def dfs_util(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True
        print(v, end=" ")

        # Recur for all the vertices adjacent to
        # this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, src=0):
        """The function to do DFS traversal. It uses recursive DFSUtil()"""
        # total vertices
        V = len(self.graph)

        # Mark all the vertices as not visited
        visited = [False] * V

        self.dfs_util(src, visited)

        # Call the recursive helper function to print DFS traversal starting from all vertices one
        # by one
        for i in range(V):
            if not visited[i]:
                self.dfs_util(i, visited)


if __name__ == '__main__':
    # Output: 0, 1, 2, 3
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Depth First Traversal")
    g.dfs(2)
