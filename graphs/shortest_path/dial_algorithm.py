"""Dial’s Algorithm (Optimized Dijkstra for small range weights)

http://www.geeksforgeeks.org/dials-algorithm-optimized-dijkstra-for-small-range-weights/

Dial's Algorithm (Optimized Dijkstra for small range weights)
Dijkstra's shortest path algorithm runs in O(Elog V) time when implemented with adjacency list
representation

Can we optimize Dijkstra's shortest path algorithm to work better than O(E log V) if maximum
weight is small (or range of edge weights is small)?

For example:
In the above diagram, maximum weight is 14. Many a times the range of weights on
edges in is in small range (i.e. all edge weight can be mapped to 0, 1, 2.. w where w is a small
number). In that case, Dijkstra's algorithm can be modified by using different data structure,
buckets, which is called dial implementation of dijkstra's algorithm.
time complexity is O(E + WV) where W is maximum weight on any edge of graph, so we can see that,
if W is small then this implementation runs much faster than traditional algorithm.

Following are important observations.
1) Maximum distance between any two node can be at max w(V - 1) (w is maximum edge weight and we
can have at max V-1 edges between two vertices).

2) In Dijkstra algorithm, distances are finalized in non-decreasing, i.e., distance of the closer
(to given source) vertices is finalized before the distant vertices.

---------------------------------------------
Algorithm
---------------------------------------------

-> Maintains some buckets, numbered 0, 1, 2,..... ,wV.
-> Bucket k contains all temporarily labeled nodes with distance equal to k.
-> Nodes in each bucket are represented by list of vertices.
-> Buckets 0, 1, 2,..wV are checked sequentially until the first non-empty bucket is found. Each
node contained in the first non-empty bucket has the minimum distance label by definition.
-> One by one, these nodes with minimum distance label are permanently labeled and deleted from the
bucket during the scanning process.
-> Thus operations involving vertex include:
    a. Checking if a bucket is empty
    b. Adding a vertex to a bucket
    c. Deleting a vertex from a bucket.
-> The position of a temporarily labeled vertex in the buckets is updated accordingly when the
distance label of a vertex changes.
-> Process repeated until all vertices are permanently labeled (or distances of all vertices are
finalized). """

# Python Program for Dijkstra's dial implementation
from collections import defaultdict

INF = 0x3f3f3f3f


class Pair:
    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second


# This class represents a directed graph using adjacency list representation
class Graph(object):
    def __init__(self, V):
        self.V = V
        # In a weighted graph, we need to store vertex and weight pair for every edge
        self.adj = defaultdict(list)

    # adds edge between u and v of weight w
    def add_edge(self, u, v, w):
        self.adj[u].append(Pair(v, w))
        self.adj[v].append(Pair(u, w))

    # Prints shortest paths from src to all other vertices.
    # W is the maximum weight of an edge
    def shortestPath(self, src, W):
        # With each distance, iterator to that vertex in its bucket is stored so that vertex can
        # be deleted in O(1) at time of updation. So dist[i].first = distance of ith vertex from
        # src vertex dits[i].second = iterator to vertex i in bucket number

        # Initialize all distances as infinite (INF)
        dist = [Pair(INF, 0) for i in range(self.V)]

        # Create buckets B[]. B[i] keep vertex of distance label i
        B = defaultdict(list)
        B[0].append(src)
        dist[src].first = 0

        idx = 0
        while True:
            # Go sequentially through buckets till one non-empty bucket is found
            while len(B[idx]) == 0 and idx < W * V:
                idx += 1

            # If all buckets are empty, we are done.
            if idx == W * V:
                break

            # Take top vertex from bucket and pop it
            u = B[idx].pop(0)

            # Process all adjacent of extracted vertex 'u' and
            # update their distanced if required.
            for i in self.adj[u]:
                v = i.first
                weight = i.second

                du = dist[u].first
                dv = dist[v].first

                if dv > du + weight:  # If there is shorted path to v through u.
                    # If dv is not INF then it must be in B[dv]
                    # bucket, so erase its entry using iterator in O(1)
                    if dv != INF:
                        B[dv].remove(dist[v].second)

                    # updating the distance
                    dist[v].first = du + weight
                    dv = dist[v].first

                    # pushing vertex v into updated distance's bucket
                    B[dv].push(0, v)

                    # storing updated iterator in dist[v].second
                    dist[v].second = B[dv][0]

        # Print shortest distances stored in dist[]
        print("Vertex   Distance from Source\n")
        for i in range(self.V):
            print("%d\t%d" %(i, dist[i].first))


if __name__ == '__main__':
    # create the graph given in above fugure
    V = 9
    g = Graph(V)
    # making above shown graph
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)

    # maximum weighted edge - 14
    g.shortestPath(0, 14)
