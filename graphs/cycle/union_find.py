"""
https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/

Union-Find Algorithm | Set 2 (Union By Rank and Path Compression)

The above union() and find() are naive and the worst case time complexity is linear. The trees
created to represent subsets can be skewed and can become like a linked list. Following is an
example worst case scenario.

Let there be 4 elements 0, 1, 2, 3

Initially, all elements are single element subsets.
0 1 2 3

Do Union(0, 1)
   1   2   3
  /
 0

Do Union(1, 2)
     2   3
    /
   1
 /
0

Do Union(2, 3)
         3
        /
      2
     /
   1
 /
0

The above operations can be optimized to O(Log n) in worst case. The idea is to always attach
smaller depth tree under the root of the deeper tree. This technique is called union by rank. The
term rank is preferred instead of height because if path compression technique (we have discussed
it below) is used, then rank is not always equal to height. Also, size (in place of height) of
trees can also be used as rank. Using size as rank also yields worst case time complexity as 
O(Logn) (See this for proof)



Let us see the above example with union by rank
Initially, all elements are single element subsets.
0 1 2 3

Do Union(0, 1)
   1   2   3
  /
 0

Do Union(1, 2)
   1    3
 /  \
0    2

Do Union(2, 3)
    1
 /  |  \
0   2   3

The second optimization to naive method is Path Compression. The idea is to flatten the tree when
find() is called. When find() is called for an element x, root of the tree is returned. The find()
operation traverses up from x to find root. The idea of path compression is to make the found root
as parent of x so that we don't have to traverse all intermediate nodes again. If x is root
of a subtree, then path (to root) from all nodes under x also compresses.


Let the subset {0, 1, .. 9} be represented as below and find() is called
for element 3.
              9
         /    |    \
        4     5      6
     /     \        /  \
    0        3     7    8
            /  \
           1    2

When find() is called for 3, we traverse up and find 9 as representative
of this subset. With path compression, we also make 3 as the child of 9 so
that when find() is called next time for 1, 2 or 3, the path to root is reduced.

               9
         /    /  \    \
        4    5    6     3
     /           /  \   /  \
    0           7    8  1   2

The two techniques complement each other. The time complexity of each operation becomes even
smaller than O(Logn). In fact, amortized time complexity effectively becomes small constant.

"""
# Python Program for union-find algorithm to detect cycle in a undirected graph
# we have one egde for any two vertex i.e 1-2 is either 1-2 or 2-1 but not both

from collections import defaultdict

# This class represents a undirected graph using adjacency list representation


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A utility function to find the subset of an element i
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        elif parent[i] != -1:
            return self.find_parent(parent, parent[i])

    # A utility function to do union of two subsets
    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set

    # The main function to check whether a given graph contains cycle or not
    def isCyclic(self):
        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sets
        parent = [-1] * (self.V)

        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)


if __name__ == '__main__':
    #     /* Let us create the following graph
    #          0
    #         |  \
    #         |    \
    #         1-----2 */
    #
    # Create a graph given in the above diagram
    g = Graph(3)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 0)

    if g.isCyclic():
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")
