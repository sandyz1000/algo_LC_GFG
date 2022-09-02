"""
Greedy Algorithms | Set 6 (Prim's MST for Adjacency List Representation)

http://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-mst-for-adjacency-list-representation/

1. Greedy Algorithms | Set 5 (Prim's Minimum Spanning Tree (MST))
2. Graph and its representations

We have discussed Prim's algorithm and its implementation for adjacency matrix representation of
graphs. The time complexity for the matrix representation is O(V^2). In this post, O(ELogV)
algorithm for adjacency list representation is discussed.

As discussed in the previous post, in Prim's algorithm, two sets are maintained, one set contains
list of vertices already included in MST, other set contains vertices not yet included. With
adjacency list representation, all vertices of a graph can be traversed in O(V+E) time using BFS.
The idea is to traverse all vertices of graph using BFS and use a Min Heap to store the vertices
not yet included in MST. Min Heap is used as a priority queue to get the minimum weight edge from
the cut. Min Heap is used as time complexity of operations like extracting minimum element and
decreasing key value is O(LogV) in Min Heap.

---------------------------------------------------
Explanation:
---------------------------------------------------
Following are the detailed steps.
1) Create a Min Heap of size V where V is the number of vertices in the given graph. Every node
of min heap contains vertex number and key value of the vertex.

2) Initialize Min Heap with first vertex as root (the key value assigned to first vertex is 0).
The key value assigned to all other vertices is INF (infinite).

3) While Min Heap is not empty, do following
    a) Extract the min value node from Min Heap. Let the extracted vertex be u.
    b) For every adjacent vertex v of u, check if v is in Min Heap (not yet included in MST).
    If v is in Min Heap and its key value is more than weight of u-v, then update the key value
    of v as weight of u-v.

---------------------------------------------------
Analysis:
---------------------------------------------------

Time Complexity: The time complexity of the above code/algorithm looks O(V^2) as there are two
nested while loops. If we take a closer look, we can observe that the statements in inner loop
are executed O(V+E) times (similar to BFS). The inner loop has decreaseKey() operation which
takes O(LogV) time. So overall time complexity is O(E+V)*O(LogV) which is
O((E+V)*LogV) = O(ELogV) (For a connected graph, V = O(E))
"""

from collections import defaultdict
import heapq


class Graph(object):
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, src, dest, weight):
        """Adds an edge to an undirected graph"""
        # Add an edge from src to dest. A new node is added to the adjacency list of src. The
        # node is added at the beginning. The first element of the node has the destination and
        # the second elements has the weight
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)

        # Since graph is undirected, add an edge from dest to src also
        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)

def prim_mst(graph: Graph):
    ans, n = 0, len(p)
    seen = set()
    vertices = [(0, (0, 0))]
    
    while len(seen) < n:
        # print(vertices, seen)
        w, (u, v) = heapq.heappop(vertices)            
        if v in seen: continue
        ans += w
        seen.add(v)
        for j in range(n):
            if j not in seen and j!=v:
                heapq.heappush(vertices, (manhattan(p[j], p[v]), (v, j)))

if __name__ == '__main__':
    # Output:
    # 0 - 1
    # 5 - 2
    # 2 - 3
    # 3 - 4
    # 6 - 5
    # 7 - 6
    # 0 - 7
    # 2 - 8

    graph = Graph(9)
    graph.addEdge(0, 1, 4)
    graph.addEdge(0, 7, 8)
    graph.addEdge(1, 2, 8)
    graph.addEdge(1, 7, 11)
    graph.addEdge(2, 3, 7)
    graph.addEdge(2, 8, 2)
    graph.addEdge(2, 5, 4)
    graph.addEdge(3, 4, 9)
    graph.addEdge(3, 5, 14)
    graph.addEdge(4, 5, 10)
    graph.addEdge(5, 6, 2)
    graph.addEdge(6, 7, 1)
    graph.addEdge(6, 8, 6)
    graph.addEdge(7, 8, 7)
    prim_mst(graph)
