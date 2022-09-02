"""Transitive closure of a graph

Given a directed graph, find out if a vertex j is reachable from another vertex i for all vertex
pairs (i, j) in the given graph. Here reachable mean that there is a path from vertex i to j.
The reach-ability matrix is called transitive closure of a graph.

---------------------------------------
Discussion:
---------------------------------------

The graph is given in the form of adjacency matrix say graph[V][V] where graph[i][j] is 1 if there
is an edge from vertex i to vertex j or i is equal to j, otherwise graph[i][j] is 0.

Floyd Warshall Algorithm can be used, we can calculate the distance matrix dist[V][V] using
Floyd Warshall, if dist[i][j] is infinite, then j is not reachable from i, otherwise j is reachable
and value of dist[i][j] will be less than V.

Instead of directly using Floyd Warshall, we can optimize it in terms of space and time, for this
particular problem.

Following are the optimizations:

1)  Instead of integer resultant matrix (dist[V][V] in floyd warshall), we can create a boolean
    reach-ability matrix reach[V][V] (we save space). The value reach[i][j] will be 1 if j is
    reachable from i, otherwise 0.
2)  Instead of using arithmetic operations, we can use logical operations.
    For arithmetic operation '+', logical and '&&' is used, and for min, logical or '||' is used.
    (We save time by a constant factor. Time complexity is same though)

"""

# Python program for transitive closure using Floyd Warshall Algorithm
# Time Complexity : O(V^3)


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices

    # A utility function to print the solution
    def printSolution(self, reach):
        print("Following matrix transitive closure of the given graph ")
        for i in range(self.V):
            for j in range(self.V):
                print("%7d\t" % (reach[i][j]))
            print("")

    # Prints transitive closure of graph[][] using Floyd Warshall algorithm
    def transitiveClosure(self, graph):
        """reach[][] will be the output matrix that will finally have reachability values.
        Initialize the solution matrix same as input graph matrix"""
        reach = [i[:] for i in graph]
        # Add all vertices one by one to the set of intermediate vertices.
        # -> Before start of a iteration, we have reachability value for all pairs of vertices
        # such that the reachability values consider only the vertices in set {0, 1, 2, .. k-1}
        # as intermediate vertices.
        # -> After the end of an iteration, vertex no. k is added to the set of intermediate
        # vertices and the set becomes {0, 1, 2, .. k}
        for k in range(self.V):

            # Pick all vertices as source one by one
            for i in range(self.V):

                # Pick all vertices as destination for the
                # above picked source
                for j in range(self.V):
                    # If vertex k is on a path from i to j,
                    # then make sure that the value of reach[i][j] is 1
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

        self.printSolution(reach)


g = Graph(4)

graph = [[1, 1, 0, 1],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [0, 0, 0, 1]]

# Print the solution
g.transitiveClosure(graph)
