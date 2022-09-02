"""
Number of Triangles in an Undirected Graph
Given an Undirected simple graph, We need to find how many triangles it can have.

For example below graph have 2 triangles in it.

    0 --- 1 --- 3
     \    |    /
       \  |  /
          2

    0 --- 1     1 --- 2
      \   |     |   /
        \ |     |  /
          2     3

Explanation:

Let A[][] be adjacency matrix representation of graph. If we calculate A3, then the number of
triangle in Undirected Graph is equal to trace(A3) / 6. Where trace(A) is the sum of the elements
on the main diagonal of matrix A.

Trace of a graph represented as adjacency matrix A[V][V] is,
trace(A[V][V]) = A[0][0] + A[1][1] + .... + A[V-1][V-1]

Count of triangles = trace(A3) / 6

How does this work?

If we compute An for an adjacency matrix representation of graph, then a value An[i][j]
represents number of distinct walks between vertex i to j in graph. In A3, we get all distinct
paths of length 3 between every pair of vertices.

A triangle is a cyclic path of length three, i.e. begins and ends at same vertex. So A3[i][i]
represents a triangle beginning and ending with vertex i. Since a triangle has three vertices and
it is counted for every vertex, we need to divide result by 3. Furthermore, since the graph is
undirected, every triangle twice as i-p-q-j and i-q-p-j, so we divide by 2 also. Therefore,
number of triangles is trace(A3) / 6.

Time Complexity: The time complexity of above algorithm is O(V3) where V is number of vertices in
the graph, we can improve the performance to O(V2.8074) using Strassen’s matrix multiplication
algorithm."""

from __future__ import print_function


# Python program for finding number of triangles in an Undirected Graph. The program is for
# adjacency matrix representation of the graph

class Graph:
    VERTEX = 4

    def multiply(self, A, B, C):
        """Utility function for matrix multiplication"""
        for i in range(self.VERTEX):
            for j in range(self.VERTEX):
                C[i][j] = 0
                for k in range(self.VERTEX):
                    C[i][j] += A[i][k] * B[k][j]

    def getTrace(self, graph):
        """
        Utility function to calculate trace of a matrix (sum of diagnonal elements)
        :param graph: 2d-array
        :return:
        """
        trace = 0
        for i in range(self.VERTEX):
            trace += graph[i][i]
        return trace

    def triangleInGraph(self, graph):
        """Utility function for calculating number of triangles in graph"""
        aux2 = [[0 for i in range(self.VERTEX)] for j in range(self.VERTEX)]  # To Store graph^2
        aux3 = [[0 for i in range(self.VERTEX)] for j in range(self.VERTEX)]  # To Store graph^3

        # Initialising aux matrices with 0
        for i in range(self.VERTEX):
            for j in range(self.VERTEX):
                aux2[i][j] = aux3[i][j] = 0

        # aux2 is graph^2 now  printMatrix(aux2)
        self.multiply(graph, graph, aux2)

        # after this multiplication aux3 is graph^3 printMatrix(aux3);
        self.multiply(graph, aux2, aux3)

        trace = self.getTrace(aux3)
        return trace // 6


if __name__ == '__main__':
    # Output: Total number of Triangle in Graph : 2
    # Let us create the example graph discussed above
    gfg = Graph()
    graph = [[0, 1, 1, 0],
             [1, 0, 1, 1],
             [1, 1, 0, 1],
             [0, 1, 1, 0]]

    print("Total number of Triangle in Graph : %d\n" % gfg.triangleInGraph(graph))
