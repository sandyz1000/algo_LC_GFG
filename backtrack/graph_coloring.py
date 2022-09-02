"""
Backtracking | Set 5 (m Coloring Problem)

Given an undirected graph and a number m, determine if the graph can be colored with at most m
colors such that no two adjacent vertices of the graph are colored with same color. Here coloring
of a graph means assignment of colors to all vertices.

Input:
1) A 2D array graph[V][V] where V is the number of vertices in graph and graph[V][V] is adjacency
matrix representation of the graph. A value graph[i][j] is 1 if there is a direct edge from i to
j, otherwise graph[i][j] is 0.
2) An integer m which is maximum number of colors that can be used.

Output:

An array color[V] that should have numbers from 1 to m. color[i] should represent the color
assigned to the ith vertex. The code should also return false if the graph cannot be colored with
m colors.

--------------------------------------------------
Naive Algorithm
--------------------------------------------------

Generate all possible configurations of colors and print a configuration that satisfies the
given constraints.

while (there are untried configurations):
    # generate the next configuration
    if (no adjacent vertices are colored with same color):
        print this configuration;

There will be V^m configurations of colors.

--------------------------------------------------
Backtracking Algorithm
--------------------------------------------------
The idea is to assign colors one by one to different vertices, starting from the vertex 0. Before
assigning a color, we check for safety by considering already assigned colors to the adjacent
vertices. If we find a color assignment which is safe, we mark the color assignment as part of
solution. If we do not a find color due to clashes then we backtrack and return false.

--------------------------------------------------
Application:
--------------------------------------------------
Graph coloring problem is to assign colors to certain elements of a graph subject to certain constraints.

Vertex coloring is the most common graph coloring problem. The problem is, given m colors,
find a way of coloring the vertices of a graph such that no two adjacent vertices are colored
using same color. The other graph coloring problems like Edge Coloring (No vertex is incident to
two edges of same color) and Face Coloring (Geographical Map Coloring) can be transformed into
vertex coloring.

We introduced graph coloring and applications in previous post. As discussed in the previous
post, graph coloring is widely used. Unfortunately, there is no efficient algorithm available for
coloring a graph with minimum number of colors as the problem is a known NP Complete problem.
There are approximate algorithms to solve the problem though. Following is the basic Greedy
Algorithm to assign colors. It doesn't guarantee to use minimum colors, but it guarantees an
upper bound on the number of colors. The basic algorithm never uses more than d+1 colors where d
is the maximum degree of a vertex in the given graph

The graph coloring problem has huge number of applications.

1) Making Schedule or Time Table: Suppose we want to make am exam schedule for a university. We
have list of different subjects and students enrolled in every subject. Many subjects would have
common students (of same batch, some backlog students, etc). How do we schedule the exam so that
no two exams with a common student are scheduled at same time? How many minimum time slots are
needed to schedule all exams? This problem can be represented as a graph where every vertex is a
subject and an edge between two vertices mean there is a common student. So this is a graph
coloring problem where minimum number of time slots is equal to the chromatic number of the graph.

2) Mobile Radio Frequency Assignment: When frequencies are assigned to towers, frequencies
assigned to all towers at the same location must be different. How to assign frequencies with
this constraint? What is the minimum number of frequencies needed? This problem is also an
instance of graph coloring problem where every tower represents a vertex and an edge between two
towers represents that they are in range of each other.

3) Sudoku: Sudoku is also a variation of Graph coloring problem where every cell represents a
vertex. There is an edge between two vertices if they are in same row or same column or same block.

4) Register Allocation: In compiler optimization, register allocation is the process of assigning
a large number of target program variables onto a small number of CPU registers. This problem is
also a graph coloring problem.

5) Bipartite Graphs: We can check if a graph is Bipartite or not by coloring the graph using two
colors. If a given graph is 2-colorable, then it is Bipartite, otherwise not. See this for more
details.

6) Map Coloring: Geographical maps of countries or states where no two adjacent cities cannot be
assigned same color. Four colors are sufficient to color any map (See Four Color Theorem)

There can be many more applications: For example the below reference video lecture has a case
study at 1:18. Akamai runs a network of thousands of servers and the servers are used to
distribute content on Internet. They install a new software or update existing softwares pretty
much every week. The update cannot be deployed on every server at the same time, because the
server may have to be taken down for the install. Also, the update should not be done one at a
time, because it will take a lot of time. There are sets of servers that cannot be taken down
together, because they have certain critical functions. This is a typical scheduling application
of graph coloring problem. It turned out that 8 colors were good enough to color the graph of
75000 nodes. So they could install updates in 8 passes.

"""
from typing import List
VERTEX = 4


class Graph:
    # Utility function to check the current color assignment is safe
    def is_safe(self, v: int, graph: List[List[bool]], color: List[int], c: int):
        for i in range(VERTEX):
            if graph[v][i] == 1 and c == color[i]:
                return False
        return True

    def graph_coloring_utls(self, graph: List[List[bool]], m: int, color: List[int], v: int):
        # base case: If all vertices are assigned a color then return true
        if v == VERTEX:
            return True

        # Consider this vertex v and try different colors
        for c in range(1, m + 1):
            if self.is_safe(v, graph, color, c):
                color[v] = c
                # recur to assign colors to rest of the vertices
                if self.graph_coloring_utls(graph, m, color, v + 1):
                    return True
                # If assigning color c doesn't lead to a solution then remove it (BACKTRACK)
                color[v] = 0

        return False

    def graph_coloring(self, graph: List[List[bool]], m: int):
        """
        This function solves the m Coloring problem using Backtracking. It mainly uses
        graph_coloring_utls() to solve the problem. It returns false if the m colors cannot be
        assigned, otherwise return true and prints assignments of colors to all vertices. Please
        note that there may be more than one solutions, this function prints one of the feasible
        solutions.
        """
        # Initialize all color values as 0. This initialization is needed correct functioning of
        # isSafe()
        color = [0] * VERTEX

        if not self.graph_coloring_utls(graph, m, color, 0):
            return False

        print("Solution Exists: Following are the assigned colors \n", color)


if __name__ == "__main__":
    #   (3)---(2)
    #    |   / |
    #    |  /  |
    #    | /   |
    #   (0)---(1)

    graph = [[0, 1, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 0]]
    m = 3
    test = Graph()
    test.graph_coloring(graph, m)
