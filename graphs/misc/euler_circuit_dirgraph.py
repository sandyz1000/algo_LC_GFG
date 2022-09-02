"""
Euler Circuit in a Directed Graph
Eulerian Path is a path in graph that visits every edge exactly once. Eulerian Circuit is an
Eulerian Path which starts and ends on the same vertex.

A graph is said to be eulerian if it has eulerian cycle. We have discussed eulerian circuit for an
undirected graph. In this post, same is discussed for a directed graph.

For example, the following graph has eulerian cycle as {1, 0, 3, 4, 0, 2, 1} SCC

        1 ---> 0 <--- 3
        |    /    \   |
        |   /      \  |
        2 -         - 4


How to check if a directed graph is eulerian?
A directed graph has an eulerian cycle if following conditions are true
1) All vertices with nonzero degree belong to a single strongly connected component.
2) In degree and out degree of every vertex is same.

We can detect singly connected component using Kosaraju's DFS based simple algorithm.
To compare in degree and out degree, we need to store in degree an out degree of every vertex.
Out degree can be obtained by size of adjacency list. In degree can be stored by creating an array
of size equal to number of vertices.

Time complexity of the above implementation is O(V + E) as Kosaraju's algorithm takes O(V + E)
time. After running Kosaraju's algorithm we traverse all vertices and compare in degree with out
degree which takes O(V) time

"""

# A Python program to check if a given directed graph is Eulerian or not

from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.IN = [0] * vertices

    def addEdge(self, v, u):

        self.graph[v].append(u)
        self.IN[u] += 1

    def DFSUtil(self, v, visited):
        visited[v] = True
        for node in self.graph[v]:
            if not visited[node]:
                self.DFSUtil(node, visited)

    def getTranspose(self):
        gr = Graph(self.V)

        for node in range(self.V):
            for child in self.graph[node]:
                gr.addEdge(child, node)

        return gr

    def isSCC(self):
        visited = [False] * self.V
        v = 0
        for v in range(self.V):
            if len(self.graph[v]) > 0:
                break

        self.DFSUtil(v, visited)
        # If DFS traversal doesn't visit all vertices, then return false.
        for i in range(self.V):
            if not visited[i]:
                return False

        gr = self.getTranspose()
        visited = [False] * self.V
        gr.DFSUtil(v, visited)

        for i in range(self.V):
            if not visited[i]:
                return False

        return True

    def isEulerianCycle(self):
        # Check if all non-zero degree vertices are connected
        if not self.isSCC():
            return False

        # Check if in degree and out degree of every vertex is same
        for v in range(self.V):
            if len(self.graph[v]) != self.IN[v]:
                return False

        return True


if __name__ == '__main__':
    # Output: Given directed graph is eulerian
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 0)
    if g.isEulerianCycle():
        print("Given directed graph is eulerian")
    else:
        print("Given directed graph is NOT eulerian")
