"""
Transitive closure of a graph
http://www.geeksforgeeks.org/transitive-closure-of-a-graph-using-dfs/

- - - - - - - - - - - - - - - - - - - - - - - - -
For example, consider below graph

        0 -------> 1
        ^         /
        |        /
        |       /
        v  <-- /
        2 -------> 3

Transitive closure of above graphs is
     1 1 1 1
     1 1 1 1
     1 1 1 1
     0 0 0 1

- - - - - - - - - - - - - - - - - - - - - - - - -

Using DFS:
Given a directed graph, find out if a vertex v is reachable from another vertex u for all
vertex pairs (u, v) in the given graph. Here reachable mean that there is a path from vertex u to
v. The reach-ability matrix is called transitive closure of a graph.

------------------------------------------------
Algorithm:
------------------------------------------------
1. Create a matrix tc[V][V] that would finally have transitive closure of given graph.
Initialize all entries of tc[][] as 0.

2. Call DFS for every node of graph to mark reachable vertices in tc[][]. In recursive calls to DFS,
we don't call DFS for an adjacent vertex if it is already marked as reachable in tc[][].

Time Complexity: O(V^2)

------------------------------------------------
Using Floyd Warshall Algorithm:
http://www.geeksforgeeks.org/transitive-closure-of-a-graph/

Given a directed graph, find out if a vertex j is reachable from another vertex i for all vertex
pairs (i, j) in the given graph. Here reachable mean that there is a path from vertex i to j. The
reach-ability matrix is called transitive closure of a graph.

The graph is given in the form of adjacency matrix say 'graph[V][V]' where graph[i][j] is 1 if
there is an edge from vertex i to vertex j or i is equal to j, otherwise graph[i][j] is 0.
Floyd Warshall Algorithm can be used, we can calculate the distance matrix dist[V][V] using Floyd
Warshall, if dist[i][j] is infinite, then j is not reachable from i, otherwise j is reachable and
value of dist[i][j] will be less than V.

Instead of directly using Floyd Warshall, we can optimize it in terms of space and time,
for this particular problem. Following are the optimizations:

1) Instead of integer resultant matrix (dist[V][V] in floyd warshall), we can create a boolean
reach-ability matrix reach[V][V] (we save space). The value reach[i][j] will be 1 if j is
reachable from i, otherwise 0.

2) Instead of using arithmetic operations, we can use logical operations. For arithmetic
operation '+', logical and '&&' is used, and for min, logical or '||' is used. (We save time by a
constant factor. Time complexity is same though)

Time Complexity: O(V^3) where V is number of vertices in the given graph.

"""
from __future__ import print_function
# Python program to print transitive closure of a graph
from collections import defaultdict


class Graph(object):
    """
    Using DFS:
    This class represents a directed graph using adjacency list representation
    """

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # To store transitive closure
        self.tc = [[0 for j in range(self.V)] for i in range(self.V)]

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, s, v):
        """A recursive DFS traversal function that finds all reachable vertices for s"""
        # Mark reach-ability from s to v as true.
        self.tc[s][v] = 1

        # Find all the vertices reachable through v
        for i in self.graph[v]:
            if self.tc[s][i] == 0:
                self.dfs_util(s, i)

    # The function to find transitive closure. It uses recursive dfs_util()
    def transitive_closure(self):
        # Call the recursive helper function to print DFS traversal starting from
        # all vertices one by one
        for i in range(self.V):
            self.dfs_util(i, i)
        print(self.tc)


# Class to represent a graph
class GraphX(object):
    """Using Floyd Warshall Algorithm:"""
    def __init__(self, vertices):
        self.V = vertices

    # A utility function to print the solution
    def print_solution(self, reach):
        print("Following matrix transitive closure of the given graph ")
        for i in range(self.V):
            for j in range(self.V):
                print("%7d\t" % (reach[i][j]), end=" ")
            print("")

    # Prints transitive closure of graph[][] using Floyd Warshall algorithm
    def transitive_closure(self, graph):
        """
        reach[][] will be the output matrix that will finally have reach-ability values.
        Initialize the solution matrix same as input graph matrix
        """
        reach = [i[:] for i in graph]
        # Add all vertices one by one to the set of intermediate vertices.
        # ---> Before start of a iteration, we have reach-ability value for all pairs of vertices
        # such that the reach-ability values consider only the vertices in set
        # {0, 1, 2, .. k-1} as intermediate vertices.
        # ---> After the end of an iteration, vertex no. k is added to the set of intermediate
        # vertices and the set becomes {0, 1, 2, .. k}

        for k in range(self.V):
            # Pick all vertices as source one by one
            for i in range(self.V):
                # Pick all vertices as destination for the above picked source
                for j in range(self.V):
                    # If vertex k is on a path from i to j, then make sure that the value
                    # of reach[i][j] is 1
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

        self.print_solution(reach)


if __name__ == '__main__':
    print("\nUsing DFS Algorithm\n")
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Transitive closure matrix is")
    g.transitive_closure()

    print("\nUsing Floyd Warshall Algorithm\n")
    g = GraphX(4)
    graph = [[1, 1, 0, 1],
             [0, 1, 1, 0],
             [0, 0, 1, 1],
             [0, 0, 0, 1]]

    # Print the solution
    g.transitive_closure(graph)
