"""
Ford-Fulkerson Algorithm for Maximum Flow Problem
Given a graph which represents a flow network where every edge has a capacity. Also given two
vertices source 's' and sink 't' in the graph, find the maximum possible flow from s to t with
following constraints:

a) Flow on an edge doesn't exceed the given capacity of the edge.

b) Incoming flow is equal to outgoing flow for every vertex except s and t.

For example, consider the following graph from CLRS book

    -- DIAGRAM GOES HERE ---

The maximum possible flow in the above graph is 23.

    -- DIAGRAM GOES HERE ---


Ford-Fulkerson Algorithm
- - - - - - - - - - - - - - - - - - - - -

    The following is simple idea of Ford-Fulkerson algorithm:
    1) Start with initial flow as 0.
    2) While there is a augmenting path from source to sink.
               Add this path-flow to flow.
    3) Return flow.

- - - - - - - - - - - - - -- - - - - - -- - - - - - -

Time Complexity: Time complexity of the above algorithm is O(max_flow * E). We run a loop while
there is an augmenting path. In worst case, we may add 1 unit flow in every iteration. Therefore
the time complexity becomes O(max_flow * E).

How to implement the above simple algorithm?
Let us first define the concept of Residual Graph which is needed for understanding the
implementation.

Residual Graph of a flow network is a graph which indicates additional possible flow. If there is
a path from source to sink in residual graph, then it is possible to add flow. Every edge of a
residual graph has a value called residual capacity which is equal to original capacity of the
edge minus current flow. Residual capacity is basically the current capacity of the edge.

Let us now talk about implementation details. Residual capacity is 0 if there is no edge between
two vertices of residual graph. We can initialize the residual graph as original graph as there
is no initial flow and initially residual capacity is equal to original capacity. To find an
augmenting path, we can either do a BFS or DFS of the residual graph. We have used BFS in below
implementation. Using BFS, we can find out if there is a path from source to sink. BFS also
builds parent[] array. Using the parent[] array, we traverse through the found path and find
possible flow through this path by finding minimum residual capacity along the path. We later add
the found path flow to overall flow.

The important thing is, we need to update residual capacities in the residual graph. We subtract
path flow from all edges along the path and we add path flow along the reverse edges We need to
add path flow along reverse edges because may later need to send flow in reverse direction (See
following link for example). """

# Python program for implementation of Ford Fulkerson algorithm

from collections import defaultdict


# This class represents a directed graph using adjacency matrix representation
class Graph:
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)
        # self.COL = len(gr[0])

    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''

    def bfs(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)

        # Create a queue for BFS
        # Mark the source node as visited and enqueue it
        queue = [s]
        visited[s] = True
        # Standard BFS Loop
        while queue:
            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False

    # Returns tne maximum flow from s to t in the given graph
    def ford_fulkerson(self, source, sink):
        # This array is filled by BFS and to store path
        parent = [-1] * self.ROW

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.bfs(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


if __name__ == '__main__':
    # Output: The maximum possible flow is 23
    graph = [[0, 16, 13, 0, 0, 0],
             [0, 0, 10, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]]

    g = Graph(graph)
    source = 0
    sink = 5
    print("The maximum possible flow is %d " % g.ford_fulkerson(source, sink))