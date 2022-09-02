# coding=utf-8

"""
Hopcroft–Karp Algorithm for Maximum Matching | Set 1 (Introduction)

http://www.geeksforgeeks.org/hopcroft-karp-algorithm-for-maximum-matching-set-1-introduction/

A matching in a Bipartite Graph is a set of the edges chosen in such a way that no two edges
share an endpoint. A maximum matching is a matching of maximum size (maximum number of edges). In
a maximum matching, if any edge is added to it, it is no longer a matching. There can be more
than one maximum matching for a given Bipartite Graph.

We have discussed importance of maximum matching and Ford Fulkerson Based approach for maximal
Bipartite Matching in previous post. Time complexity of the Ford Fulkerson based algorithm is O(V
x E).

Hopcroft Karp algorithm is an improvement that runs in O(math.sqrt(V) x E) time. Let us define
few terms before we discuss the algorithm

Free Node or Vertex: Given a matching M, a node that is not part of matching is called free node.
Initially all vertices as free (See first graph of below diagram). In second graph, u2 and v2 are
free. In third graph, no vertex is free.

Matching and Not-Matching edges: Given a matching M, edges that are part of matching are called
Matching edges and edges that are not part of M (or connect free nodes) are called Not-Matching
edges. In first graph, all edges are non-matching. In second graph, (u0, v1), (u1, v0) and (u3,
v3) are matching and others not-matching.

Alternating Paths: Given a matching M, an alternating path is a path in which the edges belong
alternatively to the matching and not matching. All single edges paths are alternating paths.
Examples of alternating paths in middle graph are u0-v1-u2 and u2-v1-u0-v2.

Augmenting path: Given a matching M, an augmenting path is an alternating path that starts from
and ends on free vertices. All single edge paths that start and end with free vertices are
augmenting paths. In below diagram, augmenting paths are highlighted with blue color. Note that
the augmenting path always has one extra matching edge.

The Hopcroft Karp algorithm is based on below concept.

A matching M is not maximum if there exists an augmenting path. It is also true other way, i.e,
a matching is maximum if no augmenting path exists

So the idea is to one by one look for augmenting paths. And add the found paths to current matching.

---------------------------------
Hopcroft Karp Algorithm
---------------------------------

1) Initialize Maximal Matching M as empty.
2) While there exists an Augmenting Path p
     Remove matching edges of p from M and add not-matching edges of p to M
     (This increases size of M by 1 as p starts and ends with a free vertex)
3) Return M.

In the initial graph all single edges are augmenting paths and we can pick in any order. In the
middle stage, there is only one augmenting path. We remove matching edges of this path from M and
add not-matching edges. In final matching, there are no augmenting paths so the matching is
maximum.

There are few important things to note before we start implementation.

We need to find an augmenting path (A path that alternates between matching and not matching
edges, and has free vertices as starting and ending points).

Once we find alternating path, we need to add the found path to existing Matching. Here adding
path means, making previous matching edges on this path as not-matching and previous not-matching
edges as matching.

The idea is to use BFS (Breadth First Search) to find augmenting paths. Since BFS traverses level
by level, it is used to divide the graph in layers of matching and not matching edges. A dummy
vertex NIL is added that is connected to all vertices on left side and all vertices on right
side. Following arrays are used to find augmenting path. Distance to NIL is initialized as INF (
infinite). If we start from dummy vertex and come back to it using alternating path of distinct
vertices, then there is an augmenting path.

pairU[]: An array of size m+1 where m is number of vertices on left side of Bipartite Graph.
pairU[u] stores pair of u on right side if u is matched and NIL otherwise.

pairV[]: An array of size n+1 where n is number of vertices on right side of Bipartite Graph.
pairU[v] stores pair of v on left side if v is matched and NIL otherwise.

dist[]: An array of size m+1 where m is number of vertices on left side of Bipartite Graph. dist[
u] is initialized as 0 if u is not matching and INF (infinite) otherwise. dist[] of NIL is also
initialized as INF

Once an augmenting path is found, DFS (Depth First Search) is used to add augmenting paths to
current matching. DFS simply follows the distance array setup by BFS. It fills values in pairU[u]
and pairV[v] if v is next to u in BFS.
"""

from __future__ import print_function
from collections import deque, defaultdict

# Python implementation of Hopcroft Karp algorithm for maximum matching

NIL, INF = 0, 99999999999


class BipGraph:
    """A class to represent Bipartite graph for Hopcroft Karp implementation"""

    def __init__(self, m, n):
        """m and n are number of vertices on left and right sides of Bipartite Graph"""
        self.m = m
        self.n = n
        # adj[u] stores adjacents of left side vertex 'u'. The value of u ranges from 1 to m.
        # 0 is used for dummy vertex
        self.adj = defaultdict(list)  # self.m + 1

        # These are basically pointers to arrays needed for hopcroftKarp()
        self.pairU, self.pairV, self.dist = None, None, None

    def hopcroft_karp(self):
        """Returns size of maximum matching"""
        # pairU[u] stores pair of u in matching where u is a vertex on left side of Bipartite Graph.
        # If u doesn't have any pair, then pairU[u] is NIL
        self.pairU = [0] * (self.m + 1)

        # pairV[v] stores pair of v in matching. If v doesn't have any pair, then pairU[v] is NIL
        self.pairV = [0] * (self.n + 1)

        # dist[u] stores distance of left side vertices dist[u] is one more than dist[u'] if u
        # is next to u'in augmenting path
        self.dist = [0] * (self.m + 1)

        # Initialize NIL as pair of all vertices
        for u in range(self.m):
            self.pairU[u] = NIL
        for v in range(self.n):
            self.pairV[v] = NIL

        result = 0  # Initialize result

        # Keep updating the result while there is an augmenting path.
        while self.bfs():
            # Find a free vertex
            for i in range(1, self.m + 1):
                # If current vertex is free and there is an augmenting path from current vertex
                if self.pairU[u] == NIL and self.dfs(u):
                    result += 1
        return result

    def bfs(self):
        """Returns true if there is an augmenting path, else returns false"""
        Q = deque()  # an integer queue

        # First layer of vertices (set distance as 0)
        for u in range(1, self.m + 1):
            # If this is a free vertex, add it to queue
            if self.pairU[u] == NIL:
                # u is not matched
                self.dist[u] = 0
                Q.append(u)

            # Else set distance as infinite so that this vertex is considered next time
            else:
                self.dist[u] = INF

        # Initialize distance to NIL as infinite
        self.dist[NIL] = INF

        # Q is going to contain vertices of left side only.
        while len(Q) != 0:
            # Dequeue a vertex
            u = Q.popleft()

            # If this node is not NIL and can provide a shorter path to NIL
            if self.dist[u] < self.dist[NIL]:
                # Get all adjacent vertices of the dequeued vertex u
                # list<int>::iterator i;
                for i in self.adj[u]:
                    v = i
                    # If pair of v is not considered so far (v, pairV[V]) is not yet explored edge.
                    if self.dist[self.pairV[v]] == INF:
                        # Consider the pair and add it to queue
                        self.dist[self.pairV[v]] = self.dist[u] + 1;
                        Q.append(self.pairV[v])

        # If we could come back to NIL using alternating path of distinct vertices then there is
        # an augmenting path
        return self.dist[NIL] != INF

    def dfs(self, u):
        """Returns true if there is an augmenting path beginning with free vertex u"""
        if u != NIL:
            for i in self.adj[u]:
                # Adjacent to u
                v = i

                # Follow the distances set by BFS
                if self.dist[self.pairV[v]] == self.dist[u] + 1:
                    # If dfs for pair of v also returns true
                    if self.dfs(self.pairV[v]):
                        self.pairV[v] = u
                        self.pairU[u] = v
                        return True

            # If there is no augmenting path beginning with u.
            self.dist[u] = INF
            return False
        return True

    def addEdge(self, u, v):
        self.adj[u].push_back(v)  # Add u to v’s list.
        self.adj[v].push_back(u)  # Add u to v’s list.


if __name__ == '__main__':
    # Output: Size of maximum matching is 4
    g = BipGraph(4, 4)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 1)
    g.addEdge(3, 2)
    g.addEdge(4, 2)
    g.addEdge(4, 4)

    print("Size of maximum matching is ", g.hopcroft_karp())
