"""Given a graph G and an integer K, K-cores of the graph are connected components that are left
after all vertices of degree less than k have been removed

Input : Adjacency list representation of graph shown
        on left side of below diagram
Output: K-Cores :
[2] -> 3 -> 4 -> 6
[3] -> 2 -> 4 -> 6 -> 7
[4] -> 2 -> 3 -> 6 -> 7
[6] -> 2 -> 3 -> 4 -> 7
[7] -> 3 -> 4 -> 6

The standard algorithm to find a k-core graph is to remove all the vertices that have degree less
than- 'K' from the input graph. We must be careful that removing a vertex reduces the degree of
all the vertices adjacent to it, hence the degree of adjacent vertices can also drop below-'K'.
And thus, we may have to remove those vertices also. This process may/may not go until there are
no vertices left in the graph.

To implement above algorithm, we do a modified DFS on the input graph and delete all the vertices
having degree less than 'K', then update degrees of all the adjacent vertices, and if their
degree falls below 'K' we will delete them too.

Time complexity of the above solution is O(V + E) where V is number of vertices and E is
number of edges."""

# program to find K-Cores of a graph
from collections import defaultdict


# This class represents a undirected graph using adjacency
# list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to undirected graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self, v, visited, vDegree, k):
        """
        A recursive function to call DFS starting from v.
        It returns true if vDegree of v after processing is less than k else false
        It also updates vDegree of adjacent if vDegree of v is less than k.
        And if vDegree of a processed adjacent becomes less than k, then it reduces of
        vDegree of v also,
        :param v:
        :param visited:
        :param vDegree:
        :param k:
        :return:
        """

        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:

            # vDegree of v is less than k, then vDegree of
            # adjacent must be reduced
            if vDegree[v] < k:
                vDegree[i] = vDegree[i] - 1

            # If adjacent is not processed, process it
            if not visited[i]:

                # If vDegree of adjacent after processing becomes
                # less than k, then reduce vDegree of v also
                if self.DFSUtil(i, visited, vDegree, k):
                    vDegree[v] -= 1

        # Return true if vDegree of v is less than k
        return vDegree[v] < k

    # Prints k cores of an undirected graph
    def printKCores(self, k):

        # INITIALIZATION
        # Mark all the vertices as not visited
        visited = [False] * self.V

        # Store vDegrees of all vertices
        vDegree = [0] * self.V
        for i in self.graph:
            vDegree[i] = len(self.graph[i])

        # choose any vertex as starting vertex
        self.DFSUtil(0, visited, vDegree, k)

        # DFS traversal to update vDegrees of all vertices,in case they are unconnected
        for i in range(self.V):
            if not visited[i]:
                self.DFSUtil(i, k, vDegree, visited)

        # PRINTING K CORES
        print("\n K-cores: ")
        for v in range(self.V):

            # Only considering those vertices which have vDegree >= K after DFS
            if vDegree[v] >= k:
                print(str("\n [ ") + str(v) + str(" ]"))

                # Traverse adjacency list of v and print only those adjacent which
                # have vvDegree >= k after DFS
                for i in self.graph[v]:
                    if vDegree[i] >= k:
                        print("-> ", str(i))


if __name__ == '__main__':
    k = 3
    g1 = Graph(9)
    g1.addEdge(0, 1)
    g1.addEdge(0, 2)
    g1.addEdge(1, 2)
    g1.addEdge(1, 5)
    g1.addEdge(2, 3)
    g1.addEdge(2, 4)
    g1.addEdge(2, 5)
    g1.addEdge(2, 6)
    g1.addEdge(3, 4)
    g1.addEdge(3, 6)
    g1.addEdge(3, 7)
    g1.addEdge(4, 6)
    g1.addEdge(4, 7)
    g1.addEdge(5, 6)
    g1.addEdge(5, 8)
    g1.addEdge(6, 7)
    g1.addEdge(6, 8)
    g1.printKCores(k)

    g2 = Graph(13)
    g2.addEdge(0, 1)
    g2.addEdge(0, 2)
    g2.addEdge(0, 3)
    g2.addEdge(1, 4)
    g2.addEdge(1, 5)
    g2.addEdge(1, 6)
    g2.addEdge(2, 7)
    g2.addEdge(2, 8)
    g2.addEdge(2, 9)
    g2.addEdge(3, 10)
    g2.addEdge(3, 11)
    g2.addEdge(3, 12)
    g2.printKCores(k)
