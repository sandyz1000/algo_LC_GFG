"""Print all paths from a given source to a destination
Given a directed graph, a source vertex 's' and a destination vertex 'd', print all paths from
given 's' to 'd'.

    0 ----> 3
    ^ \     ^
    |   \   |
    v     \ |
    2 ----> 1

"""

from __future__ import print_function
# Python program to print all paths from a source to destination.
from collections import defaultdict


# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsUtil(self, u, d, visited, path):
        """
        A recursive function to print all paths from 'u' to 'd'. visited[] keeps track of
        vertices in current path. path[] stores actual vertices and path_index is current index
        in path[]
        :param u:
        :param d:
        :param visited:
        :param path:
        :return:
        """
        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if not visited[i]:
                    self.printAllPathsUtil(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    def print_all_paths(self, s, d):
        """Prints all paths from 's' to 'd'"""
        # Mark all the vertices as not visited
        visited = [False] * self.V

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)
    s, d = 2, 3
    print("Following are all different paths from %d to %d :" % (s, d))
    g.print_all_paths(s, d)
