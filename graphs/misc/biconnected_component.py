"""
Biconnected Components

A biconnected component is a maximal biconnected subgraph.

Biconnected Graph is already discussed here. In this article, we will see how to find biconnected
component in a graph using algorithm by John Hopcroft and Robert Tarjan.

In above graph, following are the biconnected components:

-> 4-2 3-4 3-1 2-3 1-2
-> 8-9
-> 8-5 7-8 5-7
-> 6-0 5-6 1-5 0-1
-> 10-11

Algorithm is based on Disc and Low Values discussed in Strongly Connected Components Article.

Idea is to store visited edges in a stack while DFS on a graph and keep looking for Articulation
Points (highlighted in above figure). As soon as an Articulation Point u is found, all edges
visited while DFS from node u onwards will form one biconnected component. When DFS completes for
one connected component, all edges present in stack will form a biconnected component.

If there is no Articulation Point in graph, then graph is biconnected and so there will be one
biconnected component which is the graph itself.

"""

# Python program to find bi-connected components in a given undirected graph
# Complexity : O(V+E)


from collections import defaultdict


# This class represents an directed graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # time is used to find discovery times
        self.time = 0

        # Count is number of biconnected components
        self.count = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bcc_util(self, u, parent, low, disc, st):
        """
        A recursive function that finds and prints strongly connected components using DFS traversal
        u --> The vertex to be visited next
        disc[] --> Stores discovery times of visited vertices
        low[] -- >> earliest visited vertex (the vertex with minimum
                   discovery time) that can be reached from subtree
                   rooted with current vertex
        st -- >> To store visited edges

        :param u:
        :param parent:
        :param low:
        :param disc:
        :param st:
        :return:
        """
        # Count of children in current node
        children = 0

        # Initialize discovery time and low value
        disc[u] = self.time
        low[u] = self.time
        self.time += 1

        # Recur for all the vertices adjacent to this vertex
        for v in self.graph[u]:
            # If v is not visited yet, then make it a child of u in DFS tree and recur for it
            if disc[v] == -1:
                parent[v] = u
                children += 1
                # store the edge in stack
                st.append((u, v))
                self.bcc_util(v, parent, low, disc, st)

                # Check if the subtree rooted with v has a connection to one of the ancestors of u
                # Case 1 -- per Strongly Connected Components Article
                low[u] = min(low[u], low[v])

                # If u is an articulation point,pop all edges from stack till (u, v)
                if parent[u] == -1 and children > 1 or parent[u] != -1 and low[v] >= disc[u]:
                    self.count += 1  # increment count
                    w = -1
                    while w != (u, v):
                        w = st.pop()
                        print(w, end=" ")
                    print("")

            elif v != parent[u] and low[u] > disc[v]:
                # Update low value of 'u' only of 'v' is still in stack (i.e. it's a back edge,
                # not cross edge).
                # Case 2
                # -- per Strongly Connected Components Article

                low[u] = min(low[u], disc[v])

                st.append((u, v))

    def bcc(self):
        """The function to do DFS traversal. It uses recursive BCCUtil()"""
        # Initialize disc and low, and parent arrays
        disc = [-1] * self.V
        low = [-1] * self.V
        parent = [-1] * self.V
        st = []

        # Call the recursive helper function to find articulation points in DFS tree rooted
        # with vertex 'i'
        for i in range(self.V):
            if disc[i] == -1:
                self.bcc_util(i, parent, low, disc, st)

            # If stack is not empty, pop all edges from stack
            if st:
                self.count = self.count + 1

                while st:
                    w = st.pop()
                    print(w, end=" ")
                print("")


# Create a graph given in the above diagram
if __name__ == '__main__':
    g = Graph(12)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.addEdge(1, 5)
    g.addEdge(0, 6)
    g.addEdge(5, 6)
    g.addEdge(5, 7)
    g.addEdge(5, 8)
    g.addEdge(7, 8)
    g.addEdge(8, 9)
    g.addEdge(10, 11)

    g.bcc()
    print("Above are %d biconnected components in graph" % g.count)
