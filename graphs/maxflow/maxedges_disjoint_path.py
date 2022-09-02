"""
Find maximum number of edge disjoint paths between two vertices
Given a directed graph and two vertices in it, source 's' and destination 't', find out the maximum
number of edge disjoint paths from s to t. Two paths are said edge disjoint if they don't share any
edge.

    ----  DIAGRAM GOES HERE -----

There can be maximum two edge disjoint paths from source 0 to destination 7 in the above graph.
Two edge disjoint paths are highlighted below in red and blue colors are 0-2-6-7 and 0-3-6-5-7.

    ----  DIAGRAM GOES HERE -----

Note that the paths may be different, but the maximum number is same. For example, in the above
diagram, another possible set of paths is 0-1-2-6-7 and 0-3-6-5-7 respectively.

This problem can be solved by reducing it to maximum flow problem. Following are steps.
1)  Consider the given source and destination as source and sink in flow network. Assign unit
    capacity to each edge.
2)  Run Ford-Fulkerson algorithm to find the maximum flow from source to sink.
3)  The maximum flow is equal to the maximum number of edge-disjoint paths.

When we run Ford-Fulkerson, we reduce the capacity by a unit. Therefore, the edge can not be used
again. So the maximum flow is equal to the maximum number of edge-disjoint paths."""

from __future__ import print_function

# Python program to find maximum number of edge disjoint paths
# Complexity : (E*(V^3))
# Total augmenting path = VE
# and BFS with adj matrix takes :V^2 times

from collections import defaultdict


# This class represents a directed graph using
# adjacency matrix representation
class Graph:
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)

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

    # Returns tne maximum number of edge-disjoint paths from
    # s to t in the given graph
    def find_disjoint_paths(self, source, sink):

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

            # update residual capacities of the edges and reverse edges along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


if __name__ == '__main__':
    # There can be maximum 2 edge-disjoint paths from 0 to 7
    graph = [[0, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 1, 0, 0, 0, 0, 1],
             [0, 1, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 1, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0]]

    g = Graph(graph)

    source = 0
    sink = 7

    print("There can be maximum %d edge-disjoint paths from %d to %d" %
          (g.find_disjoint_paths(source, sink), source, sink))
