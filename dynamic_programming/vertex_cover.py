
# Vertex Cover Problem | Set 1 (Introduction and Approximate Algorithm)

# http://www.geeksforgeeks.org/vertex-cover-problem-set-1-introduction-approximate-algorithm-2/

# A vertex cover of an undirected graph is a subset of its vertices such that for every edge (u,
# v) of the graph, either 'u' or 'v' is in vertex cover. Although the name is Vertex Cover,
# the set covers all edges of the given graph. Given an undirected graph, the vertex cover problem
# is to find minimum size vertex cover.

# Vertex Cover Problem is a known NP Complete problem, i.e., there is no polynomial time solution for
# this unless P = NP. There are approximate polynomial time algorithms to solve the problem though.

# Approximate Algorithm for Vertex Cover:
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 1) Initialize the result as {}
# 2) Consider a set of all edges in given graph.  Let the set be E.
# 3) Do following while E is not empty
#     a) Pick an arbitrary edge (u, v) from set E and add 'u' and 'v' to result
#     b) Remove all edges from E which are either incident on u or v.
# 4) Return result
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                     (0)    (2)                  (0)---(2)
#                         \   |                           \
#                          \  |                      /---/(4)
# (0)   (1)           (1) ---(3)                  (1)   (3)
# No vertex cover     min vertex cover {3}        Min vertex cover {4, 2} or {4, 0}

from collections import defaultdict


# Python Program to print Vertex Cover of a given undirected graph

class Graph:
    """This class represents an undirected graph using adjacency list"""

    def __init__(self, V):
        self.V = V  # No. of vertices
        self.adj = defaultdict(list)

    def add_edge(self, v, w):
        """Function to add an edge into the graph"""
        self.adj[v].append(w)  # Add w to v's list.
        self.adj[w].append(v)  # Graph is undirected

    def print_vertex_cover(self):
        """The function to print vertex cover"""
        # Initialize all vertices as not visited.
        visited = [False] * self.V
        # Consider all edges one by one
        for u in range(self.V):
            # An edge is only picked when both visited[u] and visited[v] are false
            if not visited[u]:
                # Go through all adjacent of u and pick the first not yet visited vertex (We are
                # basically picking an edge (u, v) from remaining edges.
                for v in self.adj[u]:
                    if not visited[v]:
                        # Add the vertices (u, v) to the result set. We make the vertex u and v
                        # visited so that all edges from/to them would be ignored
                        visited[v] = True
                        visited[u] = True
                        break

        # Print the vertex cover
        for j in range(self.V):
            if visited[j]:
                print(j, end=" ")


if __name__ == '__main__':
    # Output: 0 1 3 4 5 6
    # Time Complexity of above algorithm is O(V + E).
    # Create a graph given in the above diagram
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 6)

    g.print_vertex_cover()
