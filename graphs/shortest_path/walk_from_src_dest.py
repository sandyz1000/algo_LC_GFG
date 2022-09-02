"""Count all possible walks from a source to a destination with exactly k edges

Given a directed graph and two vertices 'u' and 'v' in it, count all possible walks from 'u' to 'v'
with exactly k edges on the walk.

The graph is given as adjacency matrix representation where value of graph[i][j] as 1 indicates
that there is an edge from vertex i to vertex j and a value 0 indicates no edge from i to j.

For example:
Consider the following graph. Let source 'u' be vertex 0, destination 'v' be 3 and k be 2.
The output should be 2 as there are two walk from 0 to 3 with exactly 2 edges.
The walks are {0, 2, 3} and {0, 1, 3}

"""

# Python program to count walks from u to v with exactly k edges
# Number of vertices in the graph
V = 4


def count_walks(graph, u, v, k):
    """A naive recursive function to count walks from u to v with k edges
    The worst case time complexity of the above function is O(Vk) where V is the number
    of vertices in the given graph

    Discussion:

    The worst case time complexity of the above function is O(Vk) where V is the number of
    vertices in the given graph. We can simply analyze the time complexity by drawing recursion
    tree. The worst occurs for a complete graph. In worst case, every internal node of recursion
    tree would have exactly n children.

    We can optimize the above solution using Dynamic Programming. The idea is to build a 3D table
    where first dimension is source, second dimension is destination, third dimension is number
    of edges from source to destination, and the value is count of walks. Like other Dynamic
    Programming problems, we fill the 3D table in bottom up manner. """

    if k == 0 and u == v:  # Base cases
        return 1
    if k == 1 and graph[u][v]:
        return 1
    if k <= 0:
        return 0

    count = 0  # Initialize result

    # Go to all adjacents of u and recur
    for i in range(V):
        if graph[u][i] == 1:  # Check if is adjacent of u
            count += count_walks(graph, i, v, k - 1)
    return count


def count_walks_dp(graph, u, v, k):
    """
    A Dynamic programming based function to count walks from u to v with k edges
    Time complexity of the above DP based solution is O(V3K) which is much better than the naive
    solution.

    Time complexity of the above DP based solution is O(V3K) which is much better than the naive
    solution.
    We can also use Divide and Conquer to solve the above problem in O(V3Logk) time. The count of
    walks of length k from u to v is the [u][v]’th entry in (graph[V][V])k. We can calculate
    power of by doing O(Logk) multiplication by using the divide and conquer technique to
    calculate power. A multiplication between two matrices of size V x V takes O(V3) time.
    Therefore overall time complexity of this method is O(V3Logk). """

    # Table to be filled up using DP. The value count[i][j][e] will
    # store count of possible walks from i to j with exactly k edges
    count = [[[0 for e in range(k+1)] for j in range(V)] for j in range(V)]

    # Loop for number of edges from 0 to k
    for e in range(k + 1):
        for i in range(V):  # for source
            for j in range(V):  # for destination
                count[i][j][e] = 0  # initialize value
                if e == 0 and i == j:  # from base cases
                    count[i][j][e] = 1

                if e == 1 and graph[i][j]:
                    count[i][j][e] = 1

                # go to adjacent only when number of edges is more than 1
                if e > 1:
                    for a in range(V):  # adjacent of source i
                        if graph[i][a]:
                            count[i][j][e] += count[a][j][e - 1]

    return count[u][v][k]


if __name__ == '__main__':
    # Let us create the graph shown in above diagram
    graph = [[0, 1, 1, 1],
             [0, 0, 0, 1],
             [0, 0, 0, 1],
             [0, 0, 0, 0]]
    u, v, k = 0, 3, 2

    print("Method-1 Count all possible walks from a source to a destination with exactly k edges",
          count_walks(graph, u, v, k))

    print("Method-2 Count all possible walks from a source to a destination with exactly k edges",
          count_walks_dp(graph, u, v, k))
