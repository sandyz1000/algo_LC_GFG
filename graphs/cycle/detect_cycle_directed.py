"""
Detect Cycle in a Directed Graph
https://www.geeksforgeeks.org/detect-cycle-in-a-graph/


Given a directed graph, check whether the graph contains a cycle or not. Your function should
return true if the given graph contains at least one cycle, else return false. For example,
the following graph contains three cycles 0->2->0, 0->1->2->0 and 3->3, so your function must
return true.
        ---- REFER DIAGRAM ----

Depth First Traversal can be used to detect cycle in a Graph. DFS for a connected graph produces
a tree. There is a cycle in a graph only if there is a back edge present in the graph. A back
edge is an edge that is from a node to itself (selfloop) or one of its ancestor in the tree
produced by DFS. In the following graph, there are 3 back edges, marked with cross sign. We can
observe that these 3 back edges indicate 3 cycles present in the graph.

        ---- REFER DIAGRAM - GOES - HERE ----

For a disconnected graph, we get the DFS forrest as output. To detect cycle, we can check for
cycle in individual trees by checking back edges.

To detect a back edge, we can keep track of vertices currently in recursion stack of function for
DFS traversal. If we reach a vertex that is already in the recursion stack, then there is a cycle
in the tree. The edge that connects current vertex to the vertex in the recursion stack is back
edge. We have used recStack[] array to keep track of vertices in the recursion stack.

Time Complexity of this method is same as time complexity of DFS traversal which is O(V+E).
"""
from __future__ import print_function
# Python program to detect cycle in a graph
from collections import defaultdict


class Graph(object):
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, rec_stack):
        # Mark current node as visited and adds to recursion stack
        visited[v] = True
        rec_stack[v] = True

        # Recur for all neighbours if any neighbour is visited and in rec_stack then
        # graph is cyclic
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.is_cyclic_util(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True

        # The node needs to be popped from recursion stack before function ends, i.e. Backtrack
        rec_stack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def is_cyclic(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V
        for node in range(self.V):
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    if g.is_cyclic() == 1:
        print("Graph has a cycle")
    else:
        print("Graph has no cycle")
