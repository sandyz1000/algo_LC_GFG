"""
Backtracking | Set 6 (Hamiltonian Cycle)

Hamiltonian Path in an undirected graph is a path that visits each vertex exactly once. A
Hamiltonian cycle (or Hamiltonian circuit) is a Hamiltonian Path such that there is an edge (in
graph) from the last vertex to the first vertex of the Hamiltonian Path. Determine whether a
given graph contains Hamiltonian Cycle or not. If it contains, then print the path. Following are
the input and output of the required function.

--------------------------------
Example:
--------------------------------
Input:
A 2D array graph[V][V] where V is the number of vertices in graph and graph[V][V] is adjacency
matrix representation of the graph. A value graph[i][j] is 1 if there is a direct edge from i to
j, otherwise graph[i][j] is 0.

Output:
An array path[V] that should contain the Hamiltonian Path. path[i] should represent the ith
vertex in the Hamiltonian Path. The code should also return false if there is no Hamiltonian
Cycle in the graph.

For example, a Hamiltonian Cycle in the following graph is {0, 1, 2, 4, 3, 0}. There are more
Hamiltonian Cycles in the graph like {0, 3, 4, 2, 1, 0}

(0)--(1)--(2)
 |   / \   |
 |  /   \  |
 | /     \ |
(3)-------(4)
And the following graph doesn't contain any Hamiltonian Cycle.

(0)--(1)--(2)
 |   / \   |
 |  /   \  |
 | /     \ |
(3)      (4)

--------------------------------
Naive Algorithm
--------------------------------
Generate all possible configurations of vertices and print a configuration that satisfies the
given constraints. There will be n! (n factorial) configurations.

while (there are untried configurations):
   generate the next configuration
   if ( there are edges between two consecutive vertices of this
        configuration and there is an edge from the last vertex to
        the first ):
        print this configuration;
        break;

--------------------------------
Backtracking Algorithm:
--------------------------------
Create an empty path array and add vertex 0 to it. Add other vertices, starting from the vertex
1. Before adding a vertex, check for whether it is adjacent to the previously added vertex and
not already added. If we find such a vertex, we add the vertex as part of the solution. If we do
not find a vertex then we return false.

Note that the above code always prints cycle starting from 0. Starting point should not matter as
cycle can be started from any point. If you want to change the starting point, you should make
two changes to above code.

Change "path[0] = 0;" to "path[0] = s;" where s is your new starting point. Also change loop "for
(int v = 1; v < V; v++)" in hamCycleUtil() to "for (int v = 0; v < V; v++)".

"""
from typing import List

VERTEX = 5


def is_safe(v, graph: List[List[int]], path: List[int], pos: List[int]):
    """
    A utility function to check if the vertex v can be added at index 'pos' in the
    Hamiltonian Cycle constructed so far (stored in 'path[]')
    """
    # Check if this vertex is an adjacent vertex of the previously added vertex.
    if graph[path[pos - 1]][v] == 0:
        return False

    # Check if the vertex has already been included. This step can be optimized by creating
    # an arr of size V
    for i in range(pos):
        if path[i] == v:
            return False
    return True


def hamilton_cycle(graph):
    """
    This function solves the Hamiltonian Cycle problem using Backtracking. It mainly uses
    ham_cycle_util() to solve the problem. It returns false if there is no Hamiltonian Cycle
    possible, otherwise return true and prints the path. Please note that there may be more
    than one solutions, this function prints one of the feasible solutions.
    :param graph: 
    :return: 
    """

    path = [-1 for i in range(VERTEX)]

    # Let us put vertex 0 as the first vertex in the path. If there is a Hamiltonian Cycle,
    # then the path can be started from any point of the cycle as the graph is undirected
    path[0] = 0
    if not ham_cycle_util(graph, path, 1):
        return False

    print_solution(path)
    return True


def ham_cycle_util(graph, path, pos):
    """
    An utility function to solve hamilton path
    :param graph: 2d matrix
    :param path: list
    :param pos: int
    :return: 
    """
    # base case: If all vertices are included in Hamiltonian Cycle
    if pos == VERTEX:
        # And if there is an edge from the last included vertex to the first vertex
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    # Try different vertices as a next candidate in Hamiltonian Cycle. We don't try for 0
    # as we included 0 as starting point in in hamCycle()
    for v in range(1, VERTEX):
        # Check if this vertex can be added to Hamiltonian Cycle
        if is_safe(v, graph, path, pos):
            path[pos] = v
            # recur to construct rest of the path
            if ham_cycle_util(graph, path, pos + 1):
                return True
            # If adding vertex v doesn't lead to a solution, then remove it (BACKTRACK)
            path[pos] = -1

    # If no vertex can be added to Hamiltonian Cycle constructed so far, then return false
    return False


def print_solution(path):
    """
    :return: void
    """
    # Let us print the first vertex again to show the complete cycle
    print("Solution Exists: Following is one Hamiltonian Cycle")
    for vertex in path:
        print(vertex, end=" ")
    print(path[0], "\n")


if __name__ == "__main__":
    # (0)--(1)--(2)
    # |    / \   |
    # |   /   \  |
    # |  /     \ |
    # (3)-------(4)
    graph1 = [[0, 1, 0, 1, 0],
              [1, 0, 1, 1, 1],
              [0, 1, 0, 0, 1],
              [1, 1, 0, 0, 1],
              [0, 1, 1, 1, 0]]

    hamilton_cycle(graph1)

    # (0)--(1)--(2)
    # |    / \    |
    # |   /   \   |
    # |  /     \  |
    # (3)       (4)
    graph2 = [[0, 1, 0, 1, 0],
              [1, 0, 1, 1, 1],
              [0, 1, 0, 0, 1],
              [1, 1, 0, 0, 0],
              [0, 1, 1, 0, 0]]

    hamilton_cycle(graph2)