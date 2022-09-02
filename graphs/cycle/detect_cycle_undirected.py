"""
Detect cycle in an undirected graph using BFS

https://www.geeksforgeeks.org/detect-cycle-in-an-undirected-graph-using-bfs/

Given an undirected graph, how to check if there is a cycle in the graph?
For example, the following graph has a cycle 1-0-2-1.

        1 --- 0 --- 3
        |    /      |
        |   /       |
        2 -/        4

Explanation:
------------
We have discussed cycle detection for directed graph. We have also discussed a union-find
algorithm for cycle detection in undirected graphs. The time complexity of the union-find
algorithm is O(ELogV). Like directed graphs, we can use DFS to detect cycle in an undirected
graph in O(V+E) time. We do a DFS traversal of the given graph. For every visited vertex 'v',
if there is an adjacent 'u' such that u is already visited and u is not parent of v, then there
is a cycle in graph. If we don't find such an adjacent for any vertex, we say that there is no
cycle. The assumption of this approach is that there are no parallel edges between any two
vertices.

Time Complexity: The program does a simple DFS Traversal of graph and graph is represented
using adjacency list. So the time complexity is O(V+E)

"""
import typing
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        """
        This class represents a undirected graph using adjacency list representation
        :param vertices:
        """
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    def add_edge(self, v, w):
        self.graph[v].append(w)  # Add w to v_s list
        self.graph[w].append(v)  # Add v to w_s list

    def is_cyclic_util(self, v: int, visited: typing.List[bool], parent: int):
        """
        A recursive function that uses visited[] and parent to detect
        cycle in subgraph reachable from vertex v.
        :return:
        """
        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            # If the node is not visited then recurse on it
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v):
                    return True
            # If an adjacent vertex is visited and not parent of current vertex,
            # then there is a cycle
            elif parent != i:
                return True

        return False

    def is_cyclic(self):
        """
        Returns true if the graph contains a cycle, else false.
        :return:
        """
        # Mark all the vertices as not visited
        visited = [False] * self.V
        # Call the recursive helper function to detect cycle in different
        # DFS trees
        for i in range(self.V):
            if not visited[i]:  # Don't recur for u if it is already visited
                if self.is_cyclic_util(i, visited, -1):
                    return True

        return False


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 0)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    if g.is_cyclic():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle ")
    g1 = Graph(3)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)

    if g1.is_cyclic():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle ")
