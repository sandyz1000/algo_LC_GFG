"""
Check whether a given graph is Bipartite or not
http://www.geeksforgeeks.org/bipartite-graph/


A Bipartite Graph is a graph whose vertices can be divided into two independent sets, U and V such
that every edge (u, v) either connects a vertex from U to V or a vertex from V to U. In other words,
for every edge (u, v), either u belongs to U and v to V, or u belongs to V and v to U. We can also
say that there is no edge that connects vertices of same set.

----------------------------------
Explanation:
----------------------------------

    --- DIAGRAM GOES HERE ---

A bipartite graph is possible if the graph coloring is possible using two colors such that
vertices in a set are colored with the same color. Note that it is possible to color a cycle
graph with even cycle using two colors. For example, see the following graph.

    --- DIAGRAM GOES HERE ---

It is not possible to color a cycle graph with odd cycle using two colors.

    --- DIAGRAM GOES HERE ---

Algorithm to check if a graph is Bipartite:
One approach is to check whether the graph is 2-colorable or not using backtracking algorithm m
coloring problem.

Following is a simple algorithm to find out whether a given graph is Birpartite or not using
Breadth First Search (BFS).
1.	Assign RED color to the source vertex (putting into set U).
2.	Color all the neighbors with BLUE color (putting into set V).
3.	Color all neighbor’s neighbor with RED color (putting into set U).
4.	This way, assign color to all vertices such that it satisfies all the constraints of m way
    coloring problem where m = 2.
5.  While assigning colors, if we find a neighbor which is colored with same color as current
    vertex, then the graph cannot be colored with 2 vertices (or graph is not Bipartite)

Time Complexity of the above approach is same as that Breadth First Search. In above
implementation is O(V^2) where V is number of vertices. If graph is represented using adjacency
list, then the complexity becomes O(V+E).

"""

from __future__ import print_function
from collections import deque


# Python program to find out whether a given graph is Bipartite or not
class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in range(V)] for row in range(V)]

    def is_bipartite(self, src):
        """This function returns true if graph G[V][V] is Bipartite, else false"""
        # Create a color array to store colors assigned to all vertices. Vertex number is used as
        # index in this array. The value '-1' of  color_arr[i] is used to indicate that no color
        # is assigned to vertex 'i'. The value 1 is used to indicate first color is assigned and
        # value 0 indicates second color is assigned.
        color_arr = [-1] * self.V

        # Assign first color to source
        color_arr[src] = 1

        # Create a queue (FIFO) of vertex numbers and enqueue source vertex for BFS traversal
        queue = [src]

        # Run while there are vertices in queue (Similar to BFS)
        while queue:
            u = queue.pop()
            # Return false if there is a self - loop
            if self.graph[u][u] == 1:
                return False

            for v in range(self.V):
                # An edge from u to v exists and destination v is not colored
                if self.graph[u][v] == 1 and color_arr[v] == -1:
                    # Assign alternate color to this adjacent v of u
                    color_arr[v] = 1 - color_arr[u]
                    queue.append(v)

                # An edge from u to v exists and destination v is colored with same color as u
                elif self.graph[u][v] == 1 and color_arr[v] == color_arr[u]:
                    return False

        # If we reach here, then all adjacent vertices can be colored with alternate color
        return True


class Graph2:
    """
    The above algorithm works only if the graph is strongly connected. In above code, we always
    start with source 0 and assume that vertices are visited from it. One important observation
    is a graph with no edges is also Bipiartite. Note that the Bipartite condition says all
    edges should be from one set to another.

    We can extend the above code to handle cases when a graph is not connected. The idea is
    repeatedly call above method for all not yet visited vertices.

    Python program to find out whether a given graph is Bipartite or not. It works for
    disconnected graph also."""

    VERTEX = 4

    def is_bipartite_util(self, G, src, colorArr):
        """This function returns true if graph G[V][V] is Bipartite, else false"""
        colorArr[src] = 1

        # Create a queue (FIFO) of vertex numbers and enqueue source vertex for BFS traversal
        que = deque()
        que.append(src)

        # Run while there are vertices in queue (Similar to BFS)
        while que:
            # Dequeue a vertex from queue ( Refer http://goo.gl/35oz8 )
            u = que.popleft()

            # Return false if there is a self-loop
            if G[u][u] == 1:
                return False

                # Find all non-colored adjacent vertices
            for v in range(self.VERTEX):
                # An edge from u to v exists and destination v is not colored
                if G[u][v] and colorArr[v] == -1:
                    # Assign alternate color to this adjacent v of u
                    colorArr[v] = 1 - colorArr[u]
                    que.append(v)

                # An edge from u to v exists and destination v is colored with same color as u
                elif G[u][v] and colorArr[v] == colorArr[u]:
                    return False

        # If we reach here, then all adjacent vertices can be colored with alternate color
        return True

    def is_bipartite(self, G):
        """Returns true if G[][] is Bipartite, else false"""
        # Create a color array to store colors assigned to all verities. Vertex/ number is used
        # as index in this array. The value '-1' of  colorArr[i] is used to indicate that no
        # color is assigned to vertex 'i' The value 1 is used to indicate first color is assigned
        # and value 0 indicates second color is assigned.
        colorArr = [-1 for i in range(self.VERTEX)]

        # This code is to handle disconnected graph
        for i in range(self.VERTEX):
            if colorArr[i] == -1:
                if not self.is_bipartite_util(G, i, colorArr):
                    return False
        return True


if __name__ == '__main__':
    print("\n ------------ Method -1 ---------- \n")
    # Output: Yes
    g = Graph(4)
    g.graph = [[0, 1, 0, 1],
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [1, 0, 1, 0]]

    print("Yes" if g.is_bipartite(0) else "No")

    print("\n ------------ Method -2 ---------- \n")
    # Output: Yes
    # Time Complexity of the above approach is same as that Breadth First Search. In above
    # implementation is O(V^2) where V is number of vertices. If graph is represented using
    # adjacency list, then the complexity becomes O(V+E).

    gr = Graph2()
    graph = [[0, 1, 0, 1],
             [1, 0, 1, 0],
             [0, 1, 0, 1],
             [1, 0, 1, 0]]

    print("Yes" if gr.is_bipartite(graph) else "No")
