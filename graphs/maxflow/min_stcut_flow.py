"""Find minimum s-t cut in a flow network

In a flow network, an s-t cut is a cut that requires the source ‘s’ and the sink ‘t’ to be in
different subsets, and it consists of edges going from the source’s side to the sink’s side. The
capacity of an s-t cut is defined by the sum of capacity of each edge in the cut-set. (Source:
Wiki)

The problem discussed here is to find minimum capacity s-t cut of the given network. Expected
output is all edges of the minimum cut.

------------------------------------------------------------
Example:
------------------------------------------------------------

In the following flow network, example s-t cuts are {{0 ,1}, {0, 2}}, {{0, 2}, {1,
2}, {1, 3}}, etc. The minimum s-t cut is {{1, 3}, {4, 3}, {4 5}} which has capacity as 12+7+4 =
23.

        --- DIAGRAM GOES HERE ---

------------------------------------------------------------
Explanation:
------------------------------------------------------------

Minimum Cut and Maximum Flow

Like Maximum Bipartite Matching, this is another problem which can solved using Ford-Fulkerson
Algorithm. This is based on max-flow min-cut theorem.

The max-flow min-cut theorem states that in a flow network, the amount of maximum flow is equal
to capacity of the minimum cut. See CLRS book for proof of this theorem.

From Ford-Fulkerson, we get capacity of minimum cut. How to print all edges that form the minimum
cut? The idea is to use residual graph.

Following are steps to print all edges of minimum cut.
1)  Run Ford-Fulkerson algorithm and consider the final residual graph.
2)  Find the set of vertices that are reachable from source in the residual graph.
3)  All edges which are from a reachable vertex to non-reachable vertex are minimum cut edges.
    Print all such edges."""

# Python program for finding min-cut in the given graph
# Complexity : (E*(V^3))
# Total augmenting path = VE and BFS with adj matrix takes :V^2 times

from collections import defaultdict


# This class represents a directed graph using adjacency matrix representation
class Graph:
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.org_graph = [i[:] for i in graph]
        self.ROW = len(graph)
        self.COL = len(graph[0])

    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''

    def bfs(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * self.ROW

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
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False

    # Returns tne min-cut of the given graph
    def min_cut(self, source, sink):
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

        # print the edges which initially had weights
        # but now have 0 weight
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j] == 0 and self.org_graph[i][j] > 0:
                    print(str(i) + " - " + str(j))


if __name__ == '__main__':
    # 1 - 3
    # 4 - 3
    # 4 - 5

    graph = [[0, 16, 13, 0, 0, 0],
             [0, 0, 10, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]]

    g = Graph(graph)
    source = 0
    sink = 5
    g.min_cut(source, sink)