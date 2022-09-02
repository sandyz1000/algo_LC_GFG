"""
Greedy Algorithms | Set 6 (Prim's MST for Adjacency List Representation)

REFER-DIAGRAM --
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

# A Python program for Prims's MST for adjacency list representation of graph

from collections import defaultdict
from heapq import heappop, heappush
import sys


class Heap(object):
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    def swapMinHeapNode(self, a, b):
        """
        A utility function to swap two nodes of min heap. Needed for min heapify
        :param a:
        :param b:
        :return:
        """
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    def minHeapify(self, idx):
        """
        A standard function to heapify at given idx
        This function also updates position of nodes when they are swapped.
        Position is needed for decreaseKey()
        :param idx:
        :return:
        """
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self.array[left][1] < \
                self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] < \
                self.array[smallest][1]:
            smallest = right

        # The nodes to be swapped in min heap
        # if idx is not smallest
        if smallest != idx:
            # Swap positions
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest

            # Swap nodes
            self.swapMinHeapNode(smallest, idx)

            self.minHeapify(smallest)

    def extractMin(self):
        """Standard function to extract minimum node from heap"""
        # Return NULL wif heap is empty
        if self.isEmpty():
            return

        # Store the root node
        root = self.array[0]

        # Replace root node with last node
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        # Update position of last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1

        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):
        # Get the index of v in  heap array
        i = self.pos[v]

        # Get the node and update its dist value
        self.array[i][1] = dist

        # Travel up while the complete tree is not heapified. This is a O(Logn) loop
        while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]:
            # Swap this node with its parent
            self.pos[self.array[i][0]] = (i - 1) // 2
            self.pos[self.array[(i - 1) // 2][0]] = i
            self.swapMinHeapNode(i, (i - 1) // 2)

            # move to parent index
            i = (i - 1) // 2

    def isInMinHeap(self, v):
        """
        A utility function to check if a given vertex 'v' is in min heap or not
        :param v:
        :return:
        """
        return True if self.pos[v] < self.size else False


def printArr(parent, n):
    for i in range(1, n):
        print("%d - %d" % (parent[i], i))


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
    """
    The main function that prints the Minimum Spanning Tree(MST) using the Prim's Algorithm.
    :return:
    """
    # Get the number of vertices in graph
    V = graph.V
    graph = graph.graph
    # key values used to pick minimum weight edge in cut
    key = []
    # List to store constructed MST
    parent = []
    # minHeap represents set E
    minHeap = Heap()

    # Initialize min heap with all vertices. Key values of all vertices
    # (except the 0th vertex) is initially infinite
    for v in range(V):
        parent.append(-1)
        key.append(sys.maxsize)
        minHeap.array.append(minHeap.newMinHeapNode(v, key[v]))
        minHeap.pos.append(v)

    # Make key value of 0th vertex as 0 so that it is extracted first
    minHeap.pos[0] = 0
    key[0] = 0
    minHeap.decreaseKey(0, key[0])

    # Initially size of min heap is equal to V
    minHeap.size = V

    # In the following loop, min heap contains all nodes
    # not yet added in the MST.
    while not minHeap.isEmpty():
        # Extract the vertex with minimum distance value
        newHeapNode = minHeap.extractMin()
        u = newHeapNode[0]

        # Traverse through all adjacent vertices of u (the extracted vertex) and update their
        # distance values
        for p_crawl in graph[u]:
            v = p_crawl[0]
            # If shortest distance to v is not finalized yet, and distance to v through u
            # is less than its previously calculated distance
            if minHeap.isInMinHeap(v) and p_crawl[1] < key[v]:
                key[v] = p_crawl[1]
                parent[v] = u
                # update distance value in min heap also
                minHeap.decreaseKey(v, key[v])

    printArr(parent, V)


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
