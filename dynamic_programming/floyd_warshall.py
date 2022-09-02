"""
https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/

Dynamic Programming | Set 16 (Floyd Warshall Algorithm)

The problem is to find shortest distances between every pair of vertices in a given edge weighted
directed Graph.

Input:
       graph[][] = { {0,   5,  INF, 10},
                    {INF,  0,  3,  INF},
                    {INF, INF, 0,   1},
                    {INF, INF, INF, 0} }
which represents the following graph

             10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3       
Note that the value of graph[i][j] is 0 if i is equal to j 
And graph[i][j] is INF (infinite) if there is no edge from vertex i to j.

Output:
Shortest distance matrix
      0      5      8      9
    INF      0      3      4
    INF    INF      0      1
    INF    INF    INF      0 

            
Floyd Warshall Algorithm
=========================
We initialize the solution matrix same as the input graph matrix as a first step. Then we update
the solution matrix by considering all vertices as an intermediate vertex. The idea is to one by
one pick all vertices and update all shortest paths which include the picked vertex as an
intermediate vertex in the shortest path. When we pick vertex number k as an intermediate vertex,
we already have considered vertices {0, 1, 2, .. k-1} as intermediate vertices. For every pair
(i, j) of source and destination vertices respectively, there are two possible cases.

# REFER IMAGE IN THE LINK ABOVE

1) k is not an intermediate vertex in shortest path from i to j. We keep the value of dist[i][j]
as it is.

2) k is an intermediate vertex in shortest path from i to j. We update the value of dist[i][j]
as dist[i][k] + dist[k][j].

"""
# Python Program for Floyd Warshall Algorithm

# Number of vertices in the graph
V = 4

# Define infinity as the large enough value. This value will be
# used for vertices not connected to each other
INF = float("inf")


# Solves all pair shortest path via Floyd Warshall Algorithm
def floyd_warshall(graph):
    """
    dist[][] will be the output matrix that will finally have the shortest distances between
    every pair of vertices
    """

    # initializing the solution matrix same as input graph matrix OR we can say that the initial
    # values of shortest distances are based on shortest paths considering no intermediate
    # vertices

    # dist = map(lambda i: map(lambda j: j, i), graph)
    dist = [[j for j in i] for i in graph]

    # Add all vertices one by one to the set of intermediate vertices.
    # ---> Before start of a iteration, we have shortest distances between all pairs of vertices
    # such that the shortest distances consider only the vertices in set {0, 1, 2, .. k-1} as
    # intermediate vertices.
    # ---> After the end of a iteration, vertex no. k is added to the set of intermediate
    # vertices and the set becomes {0, 1, 2, .. k}
    for k in range(V):
        # pick all vertices as source one by one
        for i in range(V):
            # Pick all vertices as destination for the above picked source
            for j in range(V):
                # If vertex k is on the shortest path from i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    print_solution(dist)


# A utility function to print the solution
def print_solution(dist):
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("%7s" % "INF", end=" ")
            else:
                print("%7d" % (dist[i][j]), end=" ")
            if j == V - 1:
                print("")


if __name__ == '__main__':
    #       10
    #  (0)------->(3)
    #   |         /|\
    # 5 |          |
    #   |          | 1
    #  \|/         |
    #  (1)------->(2)
    #       3

    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]]
    # Print the solution
    floyd_warshall(graph)
