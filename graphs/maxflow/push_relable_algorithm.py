"""Push Relabel Algorithm | Set 1 (Introduction and Illustration)

http://www.geeksforgeeks.org/push-relabel-algorithm-set-1-introduction-and-illustration/
http://www.geeksforgeeks.org/push-relabel-algorithm-set-2-implementation/


Given a graph which represents a flow network where every edge has a capacity. Also given two
vertices source 's' and sink 't' in the graph, find the maximum possible flow from s to t with
following constraints:

a) Flow on an edge doesn’t exceed the given capacity of the edge.

b) Incoming flow is equal to outgoing flow for every vertex except s and t.

------------------------------------------------
Explanation:
------------------------------------------------

--Push-Relabel Algorithm--

Push-Relabel approach is the more efficient than Ford-Fulkerson algorithm. In this post,
Goldberg's "generic" maximum-flow algorithm is discussed that runs in O(V2E) time. This time
complexity is better than O(E2V) which is time complexity of Edmond-Karp algorithm (a BFS based
implementation of Ford-Fulkerson). There exist a push-relabel approach based algorithm that works
in O(V3) which is even better than the one discussed here.

--Similarities with Ford Fulkerson--

Like Ford-Fulkerson, Push-Relabel also works on Residual Graph (Residual Graph of a flow network
is a graph which indicates additional possible flow. If there is a path from source to sink in
residual graph, then it is possible to add flow).

--Differences with Ford Fulkerson--

1.  Push-relabel algorithm works in a more localized. Rather than examining the entire residual
    network to find an augmenting path, push-relabel algorithms work on one vertex at a time (Source
    : CLRS Book).
2.  In Ford-Fulkerson, net difference between total outflow and total inflow for every vertex (
    Except source and sink) is maintained 0. Push-Relabel algorithm allows inflow to exceed the
    outflow before reaching the final flow. In final flow, the net difference is 0 for all except
    source and sink.
3.  Time complexity wise more efficient.

The intuition behind the push-relabel algorithm (considering a fluid flow problem) is that we
consider edges as water pipes and nodes are joints. The source is considered to be at the highest
level and it sends water to all adjacent nodes. Once a node has excess water, it pushes water to
a smaller height node. If water gets locally trapped at a vertex, the vertex is Relabeled which
means its height is increased.

Following are some useful facts to consider before we proceed to algorithm.

1. Each vertex has associated to it a height variable and a Excess Flow. Height is used to determine
whether a vertex can push flow to an adjacent or not (A vertex can push flow only to a smaller
height vertex). Excess flow is the difference of total flow coming into the vertex minus the
total flow going out of the vertex.
    - - -- - - - - -- - --  - - - -
    Excess Flow of u = Total Inflow to u - Total Outflow from u
    - - -- - - - - -- - --  - - - -

2.  Like Ford Fulkerson. each edge has associated to it a flow (which indicates current flow) and a
capacity

--------------------------------------------------
Algorithm:
--------------------------------------------------

Following are abstract steps of complete algorithm.

Push-Relabel Algorithm
1) Initialize PreFlow : Initialize Flows and Heights

2) While it is possible to perform a Push() or Relablel() on a vertex
   # Or while there is a vertex that has excess flow
        Do Push() or Relabel()

# At this point all vertices have Excess Flow as 0 (Except source and sink)
3) Return flow.


There are three main operations in Push-Relabel Algorithm

1. Initialize PreFlow() It initializes heights and flows of all vertices.
- - - - - - - - - - - - - - - - - - - - - - - -
    Preflow()
    1) Initialize height and flow of every vertex as 0.
    2) Initialize height of source vertex equal to total number of vertices in graph.
    3) Initialize flow of every edge as 0.
    4) For all vertices adjacent to source s, flow and excess flow is equal to capacity initially.
- - - - - - - - - - - - - - - - - - - - - - - -

2. Push() is used to make the flow from a node which has excess flow. If a vertex has excess flow
and there is an adjacent with smaller height (in residual graph), we push the flow from the
vertex to the adjacent with lower height. The amount of pushed flow through the pipe (edge) is
equal to the minimum of excess flow and capacity of edge.

3. Relabel() operation is used when a vertex has excess flow and none of its adjacent is at lower
height. We basically increase height of the vertex so that we can perform push(). To increase
height, we pick the minimum height adjacent (in residual graph, i.e., an adjacent to whom we can
add flow) and add 1 to it. """

from __future__ import print_function
import sys

INT_MAX = sys.maxsize


# Python program to implement push-relabel algorithm for getting maximum flow of graph

class Edge:
    # To store current flow and capacity of edge
    def __init__(self, flow, capacity, u, v):
        self.flow = flow
        self.capacity = capacity
        self.u = u
        self.v = v


class Vertex:
    """Represent a Vertex"""

    def __init__(self, h, e_flow):
        self.h = h
        self.e_flow = e_flow


class Graph:
    """To represent a flow network"""

    def __init__(self, V):
        self.V = V
        self.ver = []
        self.edge = []
        # all vertices are initialized with 0 height and 0 excess flow
        for i in range(self.V):
            self.ver.append(Vertex(0, 0))

    def add_edge(self, u, v, capacity):
        # flow is initialized with 0 for all edge
        self.edge.append(Edge(0, capacity, u, v))

    def pre_flow(self, s):
        # Making h of source Vertex equal to no. of vertices Height of other vertices is 0.
        self.ver[s].h = len(self.ver)
        for i in range(len(self.edge)):
            # If current edge goes from source
            if self.edge[i].u == s:
                # Flow is equal to capacity
                self.edge[i].flow = self.edge[i].capacity

                # Initialize excess flow for adjacent v
                self.ver[self.edge[i].v].e_flow += self.edge[i].flow

                # Add an edge from v to s in residual graph with capacity equal to 0
                self.edge.append(Edge(-self.edge[i].flow, 0, self.edge[i].v, s))

    def over_flow_vertex(self, ver):
        """returns index of overflowing Vertex"""
        for i in range(1, len(self.ver) - 1):
            if ver[i].e_flow > 0:
                return i

        # -1 if no overflowing Vertex
        return -1

    def update_reverse_edge_flow(self, i, flow):
        """Update reverse flow for flow added on ith Edge"""
        u, v = self.edge[i].v, self.edge[i].u

        for j in range(len(self.edge)):
            if self.edge[j].v == v and self.edge[j].u == u:
                self.edge[j].flow -= flow
                return

        # adding reverse Edge in residual graph
        e = Edge(0, flow, u, v)
        self.edge.append(e)

    def push(self, u):
        """To push flow from overflowing vertex u"""
        # Traverse through all edges to find an adjacent (of u) to which flow can be pushed
        for i in range(len(self.edge)):
            # Checks u of current edge is same as given overflowing vertex
            if self.edge[i].u == u:
                # if flow is equal to capacity then no push is possible
                if self.edge[i].flow == self.edge[i].capacity:
                    continue

                # Push is only possible if height of adjacent is smaller than height of
                # overflowing vertex
                if self.ver[u].h > self.ver[self.edge[i].v].h:
                    # Flow to be pushed is equal to minimum of remaining flow on edge
                    # and excess flow.
                    flow = min(self.edge[i].capacity - self.edge[i].flow, self.ver[u].e_flow)
                    # Reduce excess flow for overflowing vertex
                    self.ver[u].e_flow -= flow
                    # Increase excess flow for adjacent
                    self.ver[self.edge[i].v].e_flow += flow
                    # Add residual flow (With capacity 0 and negative flow)
                    self.edge[i].flow += flow
                    self.update_reverse_edge_flow(i, flow)
                    return True
        return False

    def relabel(self, u):
        """function to relabel vertex u"""
        # Initialize minimum height of an adjacent
        mh = INT_MAX

        # Find the adjacent with minimum height
        for i in range(len(self.edge)):
            if self.edge[i].u == u:
                # if flow is equal to capacity then no relabeling
                if self.edge[i].flow == self.edge[i].capacity:
                    continue

                # Update minimum height
                if self.ver[self.edge[i].v].h < mh:
                    mh = self.ver[self.edge[i].v].h

                    # updating height of u
                    self.ver[u].h = mh + 1

    def get_max_flow(self, s, t):
        """main function for printing maximum flow of graph"""
        self.pre_flow(s)

        # loop untill none of the Vertex is in overflow
        while self.over_flow_vertex(self.ver) != -1:
            u = self.over_flow_vertex(self.ver)
            if not self.push(u):
                self.relabel(u)

        # ver.back() returns last Vertex, whose e_flow will be final maximum flow
        last_ver = len(self.ver) - 1
        return self.ver[last_ver].e_flow


if __name__ == '__main__':
    # Output: Maximum flow is 23
    V = 6
    g = Graph(V)

    # Creating above shown flow network
    g.add_edge(0, 1, 16)
    g.add_edge(0, 2, 13)
    g.add_edge(1, 2, 10)
    g.add_edge(2, 1, 4)
    g.add_edge(1, 3, 12)
    g.add_edge(2, 4, 14)
    g.add_edge(3, 2, 9)
    g.add_edge(3, 5, 20)
    g.add_edge(4, 3, 7)
    g.add_edge(4, 5, 4)

    # Initialize source and sink
    s, t = 0, 5

    print("Maximum flow is ", g.get_max_flow(s, t))
