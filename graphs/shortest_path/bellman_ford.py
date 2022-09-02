"""
Dynamic Programming | Set 23 (Bellman-Ford Algorithm)
http://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/

Given a graph and a source vertex src in graph, find shortest paths from src to all vertices in the
given graph. The graph may contain negative weight edges.

We have discussed Dijkstra's algorithm for this problem. Dijkstra's algorithm is a Greedy
algorithm and time complexity is O(VLogV) (with the use of Fibonacci heap). Dijkstra doesn't work
for Graphs with negative weight edges, Bellman-Ford works for such graphs. Bellman-Ford is also
simpler than Dijkstra and suites well for distributed systems. But time complexity of
Bellman-Ford is O(VE), which is more than Dijkstra.

-------------------------------------------------
Algorithm:
-------------------------------------------------
Input: Graph and a source vertex src

Output: Shortest distance to all vertices from src. If there is a negative weight cycle,
then shortest distances are not calculated, negative weight cycle is reported.

1) This step initializes distances from source to all vertices as infinite and distance to source
itself as 0. Create an array dist[] of size |V| with all values as infinite except dist[src]
where src is source vertex.

2) This step calculates shortest distances. Do following |V|-1 times where |V| is the number of
vertices in given graph.
    a) Do following for each edge u-v
        If dist[v] > dist[u] + weight of edge uv, then update dist[v]
            dist[v] = dist[u] + weight of edge uv

3) This step reports if there is a negative weight cycle in graph. Do following for each edge u-v
.... If dist[v] > dist[u] + weight of edge uv, then "Graph contains negative weight cycle"
The idea of step 3 is, step 2 guarantees shortest distances if graph doesn't contain negative
weight cycle. If we iterate through all edges one more time and get a shorter path for any vertex,
then there is a negative weight cycle

How does this work?

Like other Dynamic Programming Problems, the algorithm calculate shortest paths in bottom-up
manner. It first calculates the shortest distances for the shortest paths which have at-most one
edge in the path. Then, it calculates shortest paths with at-most 2 edges, and so on. After the
ith iteration of outer loop, the shortest paths with at most i edges are calculated. There can be
maximum |V| - 1 edges in any simple path, that is why the outer loop runs |v| - 1 times. The idea
is, assuming that there is no negative weight cycle, if we have calculated shortest paths with at
most i edges, then an iteration over all edges guarantees to give shortest path with at-most
(i+1) edges (Proof is simple, you can refer this or MIT Video Lecture)

Proof:
http://courses.csail.mit.edu/6.006/spring11/lectures/lec15.pdf

Refer Diagram:
http://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/

Notes:
1) Negative weights are found in various applications of graphs. For example, instead of
paying cost for a path, we may get some advantage if we follow the path.

2) Bellman-Ford works better (better than Dijksra's) for distributed systems. Unlike Dijksra's
where we need to find minimum value of all vertices, in Bellman-Ford, edges are considered one by
one.

"""
from __future__ import print_function


class Graph(object):
    """
    Python program for Bellman-Ford's single source shortest path algorithm.
    """

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary to store graph

    # function to add an edge to graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # utility function used to print the solution
    def print_arr(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.V):
            print("%d to %d" % (i, dist[i]))

    def bellman_ford(self, src):
        """
        The main function that finds shortest distances from src to all other vertices using
        Bellman-Ford algorithm. The function # also detects negative weight cycle

        :param src:
        :return:
        """
        # Step 1: Initialize distances from src to all other vertices as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest path from src to any other
        # vertex can have at-most |V| - 1 edges
        for i in range(self.V - 1):
            # Update dist value of the picked vertex.
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: check for negative-weight cycles. The above step guarantees shortest distances
        # if graph doesn't contain negative weight cycle. If we get a shorter path, then there
        # is a cycle.
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # print all distance
        self.print_arr(dist)


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    # Print the solution
    g.bellman_ford(0)
