"""
Breadth First Traversal or BFS for a Graph
http://www.geeksforgeeks.org/breadth-first-traversal-for-a-graph/

Breadth First Traversal (or Search) for a graph is similar to Breadth First Traversal of a
tree (See method 2 of this post). The only catch here is, unlike trees, graphs may contain
cycles, so we may come to the same node again. To avoid processing a node more than once,
we use a boolean visited array. For simplicity, it is assumed that all vertices are reachable
from the starting vertex.

For example, in the following graph, we start traversal from vertex 2. When we come to vertex 0,
we look for all adjacent vertices of it. 2 is also an adjacent vertex of 0. If we don't mark
visited vertices, then 2 will be processed again and it will become a non-terminating process. A
Breadth First Traversal of the following graph is 2, 0, 3, 1.

            0 -------> 1
            A       /
            |      /
            |     /
            V <--/
  start-->  2 -------> 3 <- self loop

Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in
the graph.
"""
from __future__ import print_function
from collections import defaultdict


# This class represents a directed graph using adjacency list representation
class Graph(object):
    """
    Program to print BFS traversal from a given source vertex. BFS(int s) traverses vertices
    reachable from s.
    """

    def __init__(self):
        """default dictionary to store graph"""
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        function to add an edge to graph
        :param u:
        :param v:
        :return:
        """
        self.graph[u].append(v)

    def bfs(self, s):
        """
        Function to print a BFS of graph
        :param s:
        :return:
        """
        # Mark all the vertices as not visited
        size = len(self.graph)
        visited = [False] * size

        # Create a queue for BFS Mark the source node as visited and enqueue it
        queue = [s]
        visited[s] = True

        while queue:
            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the dequeued vertex s. If a adjacent has not
            # been visited, then mark it visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is Breadth First Traversal (starting from vertex 2)\n")
    g.bfs(2)
