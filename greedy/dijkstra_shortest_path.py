"""
Greedy Algorithms | Set 7 (Dijkstra's shortest path algorithm)

REFER DIAGRAM

http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/

Given a graph and a source vertex in graph, find shortest paths from source to all vertices in
the given graph.

Dijkstra's algorithm is very similar to Prim's algorithm for minimum spanning tree. Like Prim's
MST, we generate a SPT (shortest path tree) with given source as root. We maintain two sets,
one set contains vertices included in shortest path tree, other set includes vertices not yet
included in shortest path tree. At every step of the algorithm, we find a vertex which is in the
other set (set of not yet included) and has minimum distance from source.

Below are the detailed steps used in Dijkstra's algorithm to find the shortest path from a single
source vertex to all other vertices in the given graph.

------------------------------------
Algorithm
------------------------------------

1) Create a set sptSet (shortest path tree set) that keeps track of vertices included in shortest
path tree, i.e., whose minimum distance from source is calculated and finalized. Initially,
this set is empty.

2) Assign a distance value to all vertices in the input graph. Initialize all distance values as
INFINITE. Assign distance value as 0 for the source vertex so that it is picked first.

3) While sptSet doesn't include all vertices
    a) Pick a vertex u which is not there in sptSet and has minimum distance value.
    b) Include u to sptSet.
    c) Update distance value of all adjacent vertices of u. To update the distance values,
    iterate through all adjacent vertices. For every adjacent vertex v, if sum of distance value
    of u (from source) and weight of edge u-v, is less than the distance value of v, then update
    the distance value of v. """

from __future__ import print_function
# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
import sys
from typing import List, Optional


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def min_distance(self, dist, spt_set):
        """A utility function to find the vertex with minimum distance value, from the set of
        vertices not yet included in shortest path tree

        Arguments:
            dist {[type]} -- [description]
            spt_set {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        # Initialize minimum distance for next node
        minimum = sys.maxsize
        min_index = sys.maxsize
        # Search not nearest vertex not in the shortest path tree
        for v in range(self.V):
            if dist[v] < minimum and not spt_set[v]:
                minimum = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        """Function that implements Dijkstra's single source shortest path algorithm for a graph
        represented using adjacency matrix representation


        Arguments:
            src {[type]} -- [description]
        """
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        spt_set = [False] * self.V

        for _ in range(self.V):
            # Pick the minimum distance vertex from the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.min_distance(dist, spt_set)

            # Put the minimum distance vertex in the shortest path tree
            spt_set[u] = True

            # Update dist value of the adjacent vertices of the picked vertex only if the current
            # distance is greater than new distance and the vertex in not in the shortest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and not spt_set[v] and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)


if __name__ == '__main__':
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]]

    g.dijkstra(0)
