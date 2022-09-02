"""
Number of Triangles in Directed and Undirected Graphs
Given a Graph, count number of triangles in it. The graph is can be directed or undirected.

------------------
Example:
------------------

Input: digraph = [[0, 0, 1, 0],
                [1, 0, 0, 1],
                [0, 1, 0, 0],
                [0, 0, 1, 0]]
Output: 2

Two traingle: (0, 2, 1) and (1, 3, 2)

    0 <-- 1 --> 3
     \    ^    /
       \  |  /
          2

Explanation:

We have discussed a method based on graph trace that works for undirected graphs. In this post a
new method is discussed with that is simpler and works for both directed and undirected graphs.

The idea is to use three nested loops to consider every triplet (i, j, k) and check for the above
condition (there is an edge from i to j, j to k and k to i)
However in an undirected graph, the triplet (i, j, k) can be permuted to give six combination
(See previous post for details). Hence we divide the total count by 6 to get the actual number of
triangles.
In case of directed graph, the number of permutation would be 3 (as order of nodes becomes
relevant). Hence in this case the total number of triangles will be obtained by dividing total count
by 3. For example consider the directed graph given below """


# Python program to count triangles in a graph.  The program is
# for adjacency matrix representation of the graph.


# function to calculate the number of triangles in a simple
# directed/undirected graph.
# isDirected is true if the graph is directed, its false otherwise
def countTriangle(g, isDirected):
    nodes = len(g)
    count_Triangle = 0  # Initialize result
    # Consider every possible triplet of edges in graph
    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):
                # check the triplet if it satisfies the condition
                if (i != j and i != k and j != k and
                        g[i][j] and g[j][k] and g[k][i]):
                    count_Triangle += 1
    # if graph is directed , division is done by 3
    # else division by 6 is done
    return count_Triangle / 3 if isDirected else count_Triangle / 6


if __name__ == '__main__':
    # The Number of triangles in undirected graph : 2
    # The Number of triangles in directed graph : 2

    graph = [[0, 1, 1, 0],
             [1, 0, 1, 1],
             [1, 1, 0, 1],
             [0, 1, 1, 0]]
    # Create adjacency matrix of a directed graph
    digraph = [[0, 0, 1, 0],
               [1, 0, 0, 1],
               [0, 1, 0, 0],
               [0, 0, 1, 0]]

    print("The Number of triangles in undirected graph : %d" % countTriangle(graph, False))
    print("The Number of triangles in directed graph : %d" % countTriangle(digraph, True))
