"""Shortest path with exactly k edges in a directed and weighted graph
http://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph/

Given a directed and two vertices 'u' and 'v' in it, find shortest path from 'u' to 'v' with
exactly k edges on the path.

The graph is given as adjacency matrix representation where value of graph[i][j] indicates the
weight of an edge from vertex i to vertex j and a value INF(infinite) indicates no edge from i to j.

For example consider the following graph.

    (0) ----> (1)
    |  \
    |    \
    |       \
    (3) ----> (2)

Let source 'u' be vertex 0, destination 'v' be 3 and k
be 2. There are two walks of length 2, the walks are {0, 2, 3} and {0, 1, 3}.
The shortest among the two is {0, 2, 3} and weight of path is 3+6 = 9.

The idea is to browse through all paths of length k from u to v using the approach discussed in the
previous post and return weight of the shortest path. A simple solution is to start from u, go to
all adjacent vertices and recur for adjacent vertices with k as k-1, source as adjacent vertex and
destination as v."""

# Python program to find shortest path with exactly k edges
import sys

V = 4  # Define number of vertices in the graph and inifinite value
INT_MAX = sys.maxsize


class ShortestPath:
    def shortest_path(self, graph, u, v, k):
        """
        A naive recursive function to count walks from u to v with k edges
        The worst case time complexity of the above function is O(Vk) where V is the number of
        vertices in the given graph.

        The worst case time complexity of the above function is O(Vk) where V is the number of
        vertices in the given graph. We can simply analyze the time complexity by drawing recursion
        tree. The worst occurs for a complete graph. In worst case, every internal node of recursion
        tree would have exactly V children.

        We can optimize the above solution using Dynamic Programming. The idea is to build a 3D table
        where first dimension is source, second dimension is destination, third dimension is number
        of edges from source to destination, and the value is count of walks. Like other Dynamic
        Programming problems, we fill the 3D table in bottom up manner.

        :param graph:
        :param u:
        :param v:
        :param k:
        :return:
        """
        if k == 0 and u == v:  # Base cases
            return 0
        if k == 1 and graph[u][v] != INT_MAX:
            return graph[u][v]
        if k <= 0:
            return INT_MAX

        res = INT_MAX  # Initialize result

        # Go to all adjacent of u and recur
        for i in range(V):
            if graph[u][i] != INT_MAX and u != i and v != i:
                rec_res = self.shortest_path(graph, i, v, k - 1)
                if rec_res != INT_MAX:
                    res = min(res, graph[u][i] + rec_res)

        return res


class ShortestPathDP:
    """Dynamic Programming based C++ program to find shortest path with exactly k edges"""

    def shortest_path(self, graph, u, v, k):
        """
        A Dynamic programming based function to find the shortest path from u to v
        with exactly k edges.
        Time complexity of the above DP based solution is O(V3K) which is much better than the
        naive solution.
        :param graph:
        :param u:
        :param v:
        :param k:
        :return:
        """
        # Table to be filled up using DP. The value sp[i][j][e] will store
        # weight of the shortest path from i to j with exactly k edges
        sp = [[[0 for j in range(k+1)] for i in range(V)] for r in range(V)]

        # Loop for number of edges from 0 to k
        for e in range(k + 1):
            for i in range(V):  # for source
                for j in range(V):  # for destination
                    sp[i][j][e] = INT_MAX  # initialize value

                    if e == 0 and i == j:  # from base cases
                        sp[i][j][e] = 0
                    if e == 1 and graph[i][j] != INT_MAX:
                        sp[i][j][e] = graph[i][j]

                    # go to adjacent only when number of edges is more than 1
                    if e > 1:
                        for a in range(V):
                            # There should be an edge from i to a and a should not be same
                            # as either i or j
                            if graph[i][a] != INT_MAX and i != a and \
                                            j != a and sp[a][j][e - 1] != INT_MAX:
                                sp[i][j][e] = min(sp[i][j][e], graph[i][a] + sp[a][j][e - 1])

        return sp[u][v][k]


if __name__ == '__main__':
    # Output: Weight of the shortest path is 9

    test1 = ShortestPath()
    test2 = ShortestPathDP()

    graph = [[0, 10, 3, 2],
             [INT_MAX, 0, INT_MAX, 7],
             [INT_MAX, INT_MAX, 0, 6],
             [INT_MAX, INT_MAX, INT_MAX, 0]]

    u = 0
    v = 3
    k = 2

    print("Recursive: Weight of the shortest path is ", test1.shortest_path(graph, u, v, k))
    print("DP: Weight of the shortest path is ", test2.shortest_path(graph, u, v, k))
