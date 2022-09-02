"""Shortest Path in a weighted Graph where weight of an edge is 1 or 2
Given a directed graph where every edge has weight as either 1 or 2, find the shortest path from a
given source vertex 's' to a given destination vertex 't'. Expected time complexity is O(V+E).

A Simple Solution is to use Dijkstra's shortest path algorithm, we can get a shortest path in
O(E + VLogV) time.

How to do it in O(V+E) time?
The idea is to use BFS. One important observation about BFS is,
the path used in BFS always has least number of edges between any two vertices. So if all edges
are of same weight, we can use BFS to find the shortest path. For this problem, we can modify the
graph and split all edges of weight 2 into two edges of weight 1 each. In the modified graph,
we can use BFS to find the shortest path.

How many new intermediate vertices are needed?
We need to add a new intermediate vertex for every source vertex. The reason is simple, if we add
a intermediate vertex x between u and v and if we add same vertex between y and z, then new paths
u to z and y to v are added to graph which might have note been there in original graph.
Therefore in a graph with V vertices, we need V extra vertices.

In the below implementation 2*V vertices are created in a graph and for every edge (u, v), we split
it into two edges (u, u+V) and (u+V, w). This way we make sure that a different intermediate vertex
is added for every source vertex.

Asymptotic Analysis:

How is this approach O(V+E)? In worst case, all edges are of weight 2 and we need to do O(E)
operations to split all edges and 2V vertices, so the time complexity becomes O(E) + O(V+E) which
is O(V+E)."""

from __future__ import print_function

# Program to shortest path from a given source vertex s to a given destination vertex t.
# Expected time complexity is O(V+E)

from collections import defaultdict


class Graph:
    """This class represents a directed graph using adjacency list representation"""

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.V_org = vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def add_edge(self, u, v, w):
        if w == 1:
            self.graph[u].append(v)
        else:
            '''split all edges of weight 2 into two
            edges of weight 1 each.  The intermediate
            vertex number is maximum vertex number + 1,
            that is V.'''
            self.graph[u].append(self.V)
            self.graph[self.V].append(v)
            self.V = self.V + 1

    # To print the shortest path stored in parent[]
    def print_path(self, parent, j):
        path_len = 1
        if parent[j] == -1 and j < self.V_org:  # Base Case : If j is source
            print(j)
            return 0  # when parent[-1] then path length = 0
        l = self.print_path(parent, parent[j])

        # incerement path length
        path_len = l + path_len

        # print node only if its less than original node length.
        # i.e do not print any new node that has been added later
        if j < self.V_org:
            print(j)

        return path_len

    def find_shortest_path(self, src, dest):
        """
        This function mainly does BFS and prints the shortest path from src to dest. It is assumed
        that weight of every edge is 1
        :param src:
        :param dest:
        :return:
        """
        # Mark all the vertices as not visited
        # Initialize parent[] and visited[]
        visited = [False] * self.V
        parent = [-1] * self.V

        # Create a queue for BFS
        queue = [src]

        # Mark the source node as visited and enqueue it
        visited[src] = True

        while queue:
            s = queue.pop(0)  # Dequeue a vertex from queue
            if s == dest:  # if s = dest then print the path and return
                return self.print_path(parent, s)

            # Get all adjacent vertices of the dequeued vertex s
            # If a adjacent has not been visited, then mark it visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = s


if __name__ == '__main__':
    # Output: Shortest Path between 0 and 3 is  [0, 1, 3]
    # Shortest Distance between 0 and 3 is 3

    g = Graph(4)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 0, 1)
    g.add_edge(2, 3, 2)
    g.add_edge(3, 3, 2)

    src = 0
    dest = 3
    print("Shortest Path between %d and %d is  " % (src, dest)),
    l = g.find_shortest_path(src, dest)
    print("\nShortest Distance between %d and %d is %d " % (src, dest, l)),
