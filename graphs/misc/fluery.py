"""
Fleury's Algorithm for printing Eulerian Path or Circuit

http://www.geeksforgeeks.org/fleurys-algorithm-for-printing-eulerian-path/

Eulerian Path is a path in graph that visits every edge exactly once. Eulerian Circuit is an
Eulerian Path which starts and ends on the same vertex.

Following is Fleury's Algorithm for printing Eulerian trail or cycle (Source Ref1).
1. Make sure the graph has either 0 or 2 odd vertices.

2. If there are 0 odd vertices, start anywhere. If there are 2 odd vertices, start at one of them.

3. Follow edges one at a time. If you have a choice between a bridge and a non-bridge, always choose
the non-bridge.

4. Stop when you run out of edges.

------------------------------------------------
Explanation:
------------------------------------------------

The idea is, "don't burn bridges" so that we can come back to a vertex and traverse remaining
edges. For example let us consider the following graph.

        0 ----- 2
        |     / |
        |    /  |
        |   /   |
        1 -     3

There are two vertices with odd degree, '2' and '3', we can start path from any of them.
Let us start tour from vertex '2'.

        0 -----(2)
        |     / |
        |    /  |
        |   /   |
        1 -     3

There are three edges going out from vertex '2', which one to pick? We don't pick the edge '2-3'
because that is a bridge (we won't be able to come back to '3'). We can pick any of the remaining
two edge. Let us say we pick '2-0'. We remove this edge and move to vertex '0'.

       (0)     (2)
        |     / |
        |    /  |
        |   /   |
        1 -     3

There is only one edge from vertex '0', so we pick it, remove it and move to vertex '1'. Euler
tour becomes '2-0 0-1'.

        (0)     (2)
               / |
              /  |
             /   |
        (1) -    3

There is only one edge from vertex '1', so we pick it, remove it and move to vertex '2'. Euler
tour becomes '2-0 0-1 1-2'

        (0)    ((2))
                 |
                 |
                 |
        (1)      3

Again there is only one edge from vertex 2, so we pick it, remove it and move to vertex 3. Euler
tour becomes '2-0 0-1 1-2 2-3'

        (0)    ((2))



        (1)     (3)

There are no more edges left, so we stop here. Final tour is '2-0 0-1 1-2 2-3'.

See this for and this fore more examples.

Following is Python implementation of above algorithm. In the following code, it is assumed that
the given graph has an Eulerian trail or Circuit. The main focus is to print an Eulerian trail or
circuit. We can use isEulerian() to first check whether there is an Eulerian Trail or Circuit in
the given graph.

We first find the starting point which must be an odd vertex (if there are odd vertices) and
store it in variable 'u'. If there are zero odd vertices, we start from vertex '0'. We call
printEulerUtil() to print Euler tour starting with u. We traverse all adjacent vertices of u,
if there is only one adjacent vertex, we immediately consider it. If there are more than one
adjacent vertices, we consider an adjacent v only if edge u-v is not a bridge. How to find if a
given edge is bridge? We count number of vertices reachable from u. We remove edge u-v and
again count number of reachable vertices from u. If number of reachable vertices are reduced,
then edge u-v is a bridge. To count reachable vertices, we can either use BFS or DFS,
we have used DFS in the above code. The function DFSCount(u) returns number of vertices reachable
from u.

Once an edge is processed (included in Euler tour), we remove it from the graph. To remove the
edge, we replace the vertex entry with -1 in adjacency list. Note that simply deleting the node
may not work as the code is recursive and a parent call may be in middle of adjacency list.

Time Complexity: Time complexity of the above implementation is O ((V+E)2). The function
printEulerUtil() is like DFS and it calls isValidNextEdge() which also does DFS two times. Time
complexity of DFS for adjacency list representation is O(V+E). Therefore overall time complexity
is O((V+E)*(V+E)) which can be written as O(E2) for a connected graph.

There are better algorithms to print Euler tour, Hierholzer's Algorithm finds in O(V+E) time.

"""

from __future__ import print_function

# Python program print Eulerian Trail in a given Eulerian or Semi-Eulerian Graph

# Time Complexity: Time complexity of the above implementation is O ((V+E)2). The function
# printEulerUtil() is like DFS and it calls isValidNextEdge() which also does DFS two times. Time
#  complexity of DFS for adjacency list representation is O(V+E). Therefore overall time
# complexity is O((V+E)*(V+E)) which can be written as O(E2) for a connected graph.
from collections import defaultdict


# This class represents an undirected graph using adjacency list representation
class Graph(object):
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.Time = 0

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def rmv_edge(self, u, v):
        """This function removes edge u-v from graph"""
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)

    def dfs_count(self, v, visited):
        """A DFS based function to count reachable vertices from v"""
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                count = count + self.dfs_count(i, visited)
        return count

    def is_valid_next_edge(self, u, v):
        """
        The function to check if edge u-v can be considered as next edge in Euler Tour
        :return:
        """
        # The edge u-v is valid in one of the following two cases:
        #  1) If v is the only adjacent vertex of u
        if len(self.graph[u]) == 1:
            return True
        else:
            # 2) If there are multiple adjacent, then u-v is not a bridge Do following steps to
            # check if u-v is a bridge
            # 2.a) count of vertices reachable from u
            visited = [False] * self.V
            count1 = self.dfs_count(u, visited)

            # 2.b) Remove edge (u, v) and after removing the edge, count vertices reachable from u
            self.rmv_edge(u, v)
            visited = [False] * self.V
            count2 = self.dfs_count(u, visited)

            # 2.c) Add the edge back to the graph
            self.add_edge(u, v)

            # 2.d) If count1 is greater, then edge (u, v) is a bridge
            return False if count1 > count2 else True

    def print_euler_util(self, u):
        """Print Euler tour starting from vertex u"""
        # Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            # If edge u-v is not removed and it's a a valid next edge
            if self.is_valid_next_edge(u, v):
                print("%d-%d " % (u, v), end=" "),
                self.rmv_edge(u, v)
                self.print_euler_util(v)

    def print_euler_tour(self):
        """
        The main function that print Eulerian Trail. It first finds an odd degree vertex
        (if there is any) and then calls printEulerUtil() to print the path

        :return:
        """
        # Find a vertex with odd degree
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                u = i
                break
        # Print tour starting from odd vertex
        print("")
        self.print_euler_util(u)


if __name__ == '__main__':
    # Output:
    # 2-0  0-1  1-2  2-3
    # 0-1  1-2  2-0
    # 0-1  1-2  2-0  0-3  3-4  4-2  2-3  3-1

    g1 = Graph(4)
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.print_euler_tour()

    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 0)
    g2.print_euler_tour()

    g3 = Graph(5)
    g3.add_edge(1, 0)
    g3.add_edge(0, 2)
    g3.add_edge(2, 1)
    g3.add_edge(0, 3)
    g3.add_edge(3, 4)
    g3.add_edge(3, 2)
    g3.add_edge(3, 1)
    g3.add_edge(2, 4)
    g3.print_euler_tour()