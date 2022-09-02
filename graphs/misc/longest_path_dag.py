"""Longest Path in a Directed Acyclic Graph"""

from collections import defaultdict
import sys

INF = - sys.maxsize


class AdjListNode(object):
    """
    Graph is represented using adjacency list. Every node of adjacency list
    contains vertex number of the vertex to which edge connects. It also
    contains weight of the edge
    """

    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graph(object):
    """
    Class to represent a graph using adjacency list representation
    Given a Weighted Directed Acyclic Graph (DAG) and a source vertex s in it, find the longest
    distances from s to all other vertices in the given graph.

    The longest path problem for a general graph is not as easy as the shortest path problem because
    the longest path problem doesn't have optimal substructure property. In fact, the Longest Path
    problem is NP-Hard for a general graph. However, the longest path problem has a linear time
    solution for directed acyclic graphs. The idea is similar to linear time solution for shortest
    path in a directed acyclic graph., we use Tological Sorting.

    We initialize distances to all vertices as minus infinite and distance to source as 0,
    then we find a topological sorting of the graph. Topological Sorting of a graph represents a
    linear ordering of the graph (See below, figure (b) is a linear representation of figure (a) ).
    Once we have topological order (or linear representation), we one by one process all vertices in
    topological order. For every vertex being processed, we update distances of its adjacent using
    distance of current vertex.

    Time complexity of topological sorting is O(V+E). After finding topological order, the algorithm
    process all vertices and for every vertex, it runs a loop for all adjacent vertices. Total
    adjacent vertices in a graph is O(E). So the inner loop runs O(V+E) times. Therefore,
    overall time complexity of this algorithm is O(V+E)."""

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def topological_sort_util(self, v, visited, stack):
        """
        A function used by longest_path
        A recursive function used by longestPath. See below link for details
        http://www.geeksforgeeks.org/topological-sorting
        :param visited: list[bool]
        :param stack: list
        :return:
        """
        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        # list<AdjListNode>::iterator i;
        for node in self.graph[v]:
            if not visited[node.vertex]:
                self.topological_sort_util(node.vertex, visited, stack)

        # Push current vertex to stack which stores topological sort
        stack.append(v)

    def add_edge(self, u, v, weight):
        """
        function to add an edge to graph
        :param u:
        :param v:
        :param weight:
        :return:
        """
        self.graph[u].append(AdjListNode(v, weight))

    def longest_path(self, s):
        """
        The function to find longest distances from a given vertex.
        It uses recursive topologicalSortUtil() to get topological sorting.
        Finds longest distances from given source vertex
        :param s: int
        :return:
        """
        stack = []
        dist = [0] * self.V

        # // Mark all the vertices as not visited
        visited = [False] * self.V
        for i in range(self.V):
            visited[i] = False

        # Call the recursive helper function to store Topological Sort
        # starting from all vertices one by one
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        # Initialize distances to all vertices as infinite and distance
        # to source as 0
        for i in range(self.V):
            dist[i] = INF
        dist[s] = 0

        # Process vertices in topological order
        size = len(stack)
        while size > 0:
            # Get the next vertex from topological order
            u = stack[size - 1]
            stack.pop()
            size = size - 1

            # Update distances of all adjacent vertices
            if dist[u] != INF:
                for node in self.graph[u]:
                    if dist[node.vertex] < dist[u] + node.weight:
                        dist[node.vertex] = dist[u] + node.weight

        # Print the calculated longest distances
        for i in range(self.V):
            print("INF" if (dist[i] == INF) else dist[i])


if __name__ == '__main__':
    # Output: INF 0 2 9 8 10
    g = Graph(6)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 3, 6)
    g.add_edge(1, 2, 2)
    g.add_edge(2, 4, 4)
    g.add_edge(2, 5, 2)
    g.add_edge(2, 3, 7)
    g.add_edge(3, 5, 1)
    g.add_edge(3, 4, -1)
    g.add_edge(4, 5, -2)

    s = 1
    print("Following are longest distances from source vertex %d \n" % s)
    g.longest_path(s)
