# coding=utf-8
"""
Graph is a data structure that consists of following two components:
1. A finite set of vertices also called as nodes.

2. A finite set of ordered pair of the form (u, v) called as edge. The pair is ordered because (
u, v) is not same as (v, u) in case of directed graph(di-graph). The pair of form (u,
v) indicates that there is an edge from vertex u to vertex v. The edges may contain
weight/value/cost.

Graphs are used to represent many real life applications: Graphs are used to represent networks.
The networks may include paths in a city or telephone network or circuit network. Graphs are also
used in social networks like linkedIn, facebook. For example, in facebook, each person is
represented with a vertex(or node). Each node is a structure and contains information like person
id, name, gender and locale. See this for more applications of graph.

Following two are the most commonly used representations of graph.
1. Adjacency Matrix
2. Adjacency List

There are other representations also like, Incidence Matrix and Incidence List.
The choice of the graph representation is situation specific. It totally depends on the type of
operations to be performed and ease of use.

Adjacency Matrix: Adjacency Matrix is a 2D arr of size V x V where V is the number of vertices
in a graph. Let the 2D arr be adj[][], a slot adj[i][j] = 1 indicates that there is an edge
from vertex i to vertex j. Adjacency matrix for undirected graph is always symmetric. Adjacency
Matrix is also used to represent weighted graphs. If adj[i][j] = w, then there is an edge from
vertex i to vertex j with weight w.

Adjacency Matrix Representation of Graph

        [[  0.,  15.,   0.,   7.,  10.,   0.],
        [ 15.,   0.,   9.,  11.,   0.,   9.],
        [  0.,   9.,   0.,   0.,  12.,   7.],
        [  7.,  11.,   0.,   0.,   8.,  14.],
        [ 10.,   0.,  12.,   8.,   0.,   8.],
        [  0.,   9.,   7.,  14.,   8.,   0.]]

Pros: Representation is easier to implement and follow. Removing an edge takes O(1) time. Queries
like whether there is an edge from vertex ‘u’ to vertex ‘v’ are efficient and can be done O(1).

Cons: Consumes more space O(V^2). Even if the graph is sparse(contains less number of edges),
it consumes the same space. Adding a vertex is O(V^2) time.

Adjacency List: An arr of linked lists is used. Size of the arr is equal to number of
vertices. Let the arr be arr[]. An entry arr[i] represents the linked list of vertices
adjacent to the ith vertex. This representation can also be used to represent a weighted graph.
The weights of edges can be stored in nodes of linked lists. Following is adjacency list
representation of the above graph.

Adjacency List Representation of Graph

        0 -> [1:4]-> [2:3]
        1 -> [4:7]
        2 -> []
        3 -> []
        4 -> []
        5 -> [3:8]

"""
from collections import defaultdict


class Graph(object):
    """
    A structure to represent a graph. A graph is an arr of adjacency lists.
    Size of arr will be V (number of vertices in graph)
    """

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Add an edge from src to dest.  A new node is added to the adjacency list of src. The
        # node is added at the begining
        self.graph[u].append(v)


class SparseGraph(object):
    """
    Implementation of adjacency matrix sparse graph
    """

    def __init__(self, V):
        self.matrix_size = V ** 2
        self.graph = [[None] * V] * V

    def add_edge(self, u, v, data, directed=False):
        self.graph[u][v] = data


if __name__ == '__main__':
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    print(graph.graph)
