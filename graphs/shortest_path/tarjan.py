"""Tarjan's Algorithm to find Strongly Connected Components
http://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/

A directed graph is strongly connected if there is a path between all pairs of vertices.
A strongly connected component (SCC) of a directed graph is a maximal strongly connected subgraph.
For example, there are 3 SCCs in the following graph.

        (1) --- > (0) --- > (3)
        |       /           |
        |     /             |
        |   /               |
        (2)                 (4)

Tarjan Algorithm is based on following facts:
1. DFS search produces a DFS tree/forest
2. Strongly Connected Components form subtrees of the DFS tree.
3. If we can find head of such subtrees, we can print/store all the nodes in that subtree
(including head) and that will be one SCC.
4. There is no back edge from one SCC to another (There can be cross edges, but cross edges will
not be used while processing the graph).

To find head of a SCC, we calculate desc and low array (as done for articulation point, bridge,
biconnected component). As discussed in the previous posts, low[u] indicates earliest visited
vertex (the vertex with minimum discovery time) that can be reached from subtree rooted with u.
A node u is head if disc[u] = low[u].


"""

# Python program to find strongly connected components in a given
# directed graph using Tarjan's algorithm (single DFS)
# Time Complexity : O(V+E)

from collections import defaultdict


# This class represents an directed graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        self.Time = 0

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def SCCUtil(self, u, low, disc, stack_member, st):
        """
        A recursive function that find finds and prints strongly connected components using DFS
        traversal
        u --> The vertex to be visited next
        disc[] --> Stores discovery times of visited vertices
        low[] -- >> earliest visited vertex (the vertex with minimum discovery time) that can
        be reached from subtree rooted with current vertex
        st -- >> To store all the connected ancestors (could be part of SCC)
        stack_member[] --> bit/index array for faster check whether a node is in stack

        :param u:
        :param low:
        :param disc:
        :param stack_member:
        :param st:
        :return:
        """
        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stack_member[u] = True
        st.append(u)

        # Go through all vertices adjacent to this
        for v in self.graph[u]:

            # If v is not visited yet, then recur for it
            if disc[v] == -1:

                self.SCCUtil(v, low, disc, stack_member, st)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                # Case 1 (per above discussion on Disc and Low value)
                low[u] = min(low[u], low[v])

            elif stack_member[v]:
                # Update low value of 'u' only if 'v' is still in stack (i.e. it's a back edge,
                # not cross edge).
                # Case 2 (per above discussion on Disc and Low value)
                low[u] = min(low[u], disc[v])

        # head node found, pop the stack and print an SCC
        w = -1  # To store stack extracted vertices
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                print (w)
                stack_member[w] = False

            print("")

    def SCC(self):
        """The function to do DFS traversal. It uses recursive SCCUtil()"""
        # Mark all the vertices as not visited and Initialize parent and visited,
        # and ap(articulation point) arrays
        disc = [-1] * (self.V)
        low = [-1] * (self.V)
        stackMember = [False] * (self.V)
        st = []

        # Call the recursive helper function to find articulation points in DFS tree
        # rooted with vertex 'i'
        for i in range(self.V):
            if disc[i] == -1:
                self.SCCUtil(i, low, disc, stackMember, st)


if __name__ == '__main__':

    g1 = Graph(5)
    g1.add_edge(1, 0)
    g1.add_edge(0, 2)
    g1.add_edge(2, 1)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)
    print("SSC in first graph ")
    g1.SCC()

    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    print("nSSC in second graph ")
    g2.SCC()

    g3 = Graph(7)
    g3.add_edge(0, 1)
    g3.add_edge(1, 2)
    g3.add_edge(2, 0)
    g3.add_edge(1, 3)
    g3.add_edge(1, 4)
    g3.add_edge(1, 6)
    g3.add_edge(3, 5)
    g3.add_edge(4, 5)
    print("nSSC in third graph ")
    g3.SCC()

    g4 = Graph(11)
    g4.add_edge(0, 1)
    g4.add_edge(0, 3)
    g4.add_edge(1, 2)
    g4.add_edge(1, 4)
    g4.add_edge(2, 0)
    g4.add_edge(2, 6)
    g4.add_edge(3, 2)
    g4.add_edge(4, 5)
    g4.add_edge(4, 6)
    g4.add_edge(5, 6)
    g4.add_edge(5, 7)
    g4.add_edge(5, 8)
    g4.add_edge(5, 9)
    g4.add_edge(6, 4)
    g4.add_edge(7, 9)
    g4.add_edge(8, 9)
    g4.add_edge(9, 8)
    print("nSSC in fourth graph ")
    g4.SCC()

    g5 = Graph(5)
    g5.add_edge(0, 1)
    g5.add_edge(1, 2)
    g5.add_edge(2, 3)
    g5.add_edge(2, 4)
    g5.add_edge(3, 0)
    g5.add_edge(4, 2)
    print("nSSC in fifth graph ")
    g5.SCC()