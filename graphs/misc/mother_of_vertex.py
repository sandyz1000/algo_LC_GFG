"""
What is a Mother Vertex?
A mother vertex in a graph G = (V,E) is a vertex v such that all other vertices in G
can be reached by a path from v.
"""

# program to find a mother vertex in O(V+E) time
from collections import defaultdict


class Graph:
    """
    This class represents a directed graph using adjacency list representation
    Time Complexity : O(V + E)
    """
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary

    def DFSUtil(self, v, visited):
        """
        A recursive function to print DFS starting from v
        :param v:
        :param visited:
        :return:
        """
        # Mark the current node as visited and print it
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def addEdge(self, v, w):
        """
        Add w to the list of v
        :param v:
        :param w:
        :return:
        """
        self.graph[v].append(w)

    def findMother(self):
        """
        Returns a mother vertex if exists. Otherwise returns -1
        :return:
        """
        # visited[] is used for DFS. Initially all are
        # initialized as not visited
        visited = [False] * (self.V)

        # To store last finished vertex (or mother vertex)
        v = 0

        # Do a DFS traversal and find the last finished
        # vertex
        for i in range(self.V):
            if not visited[i]:
                self.DFSUtil(i, visited)
                v = i

        # If there exist mother vertex (or vetices) in given
        # graph, then v must be one (or one of them)

        # Now check if v is actually a mother vertex (or graph
        # has a mother vertex). We basically check if every vertex
        # is reachable from v or not.

        # Reset all values in visited[] as false and do
        # DFS beginning from v to check if all vertices are
        # reachable from it or not.
        visited = [False] * (self.V)
        self.DFSUtil(v, visited)
        if any(not i for i in visited):
            return -1
        else:
            return v


if __name__ == '__main__':
    g = Graph(7)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(4, 1)
    g.addEdge(6, 4)
    g.addEdge(5, 6)
    g.addEdge(5, 2)
    g.addEdge(6, 0)
    print("A mother vertex is ", g.findMother())