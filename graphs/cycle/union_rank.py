"""
Union-Find Algorithm | Set 2 (Union By Rank and Path Compression)
In the previous post, we introduced union find algorithm and used it to detect cycle in a graph.
We used following union() and find() operations for subsets.

# Naive implementation of find()
def find(parent: List[int], i: int):
    if (parent[i] == -1):
        return i
    return find(parent, parent[i])

# Naive implementation of union()
def union(parent: List, x: int, y: int):
    xset = find(parent, x)
    yset = find(parent, y)
    parent[xset] = yset

The above union() and find() are naive and the worst case time complexity is linear. The trees created to represent
subsets can be skewed and can become like a linked list. Following is an example worst case scenario.

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
The above operations can be optimized to O(Log n) in worst case. The idea is to always attach smaller depth tree
under the root of the deeper tree. This technique is called union by rank. The term rank is preferred instead of
height because if path compression technique (we have discussed it below) is used, then rank is not always equal
to height. Also, size (in place of height) of trees can also be used as rank. Using size as rank also yields worst
case time complexity as O(Logn) (See this for proof)

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

The second optimization to naive method is Path Compression. The idea is to flatten the tree when find() is called.
When find() is called for an element x, root of the tree is returned. The find() operation traverses up from x to
find root. The idea of path compression is to make the found root as parent of x so that we don’t have to traverse
all intermediate nodes again. If x is root of a subtree, then path (to root) from all nodes under x also compresses.

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

The two techniques complement each other. The time complexity of each operation becomes even smaller than O(Logn). 
In fact, amortized time complexity effectively becomes small constant.

"""

# A union by rank and path compression based program to detect cycle in a graph
from collections import defaultdict
from dataclasses import dataclass
# a structure to represent a graph


class Graph:
    def __init__(self, num_of_v):
        self.num_of_v = num_of_v
        self.edges = defaultdict(list)

    # graph is represented as an array of edges
    def add_edge(self, u, v):
        self.edges[u].append(v)


@dataclass(init=True, frozen=False)
class Subset:
    parent: int
    rank: int

# A utility function to find set of an element node(uses path compression technique)


def find(subsets, node):
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets, subsets[node].parent)
    return subsets[node].parent

# A function that does union of two sets of u and v(uses union by rank)


def union(subsets, u, v):
    # Attach smaller rank tree under root of high rank tree(Union by Rank)
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
    elif subsets[v].rank > subsets[u].rank:
        subsets[u].parent = v
    # If ranks are same, then make one as root and increment its rank by one
    else:
        subsets[v].parent = u
        subsets[u].rank += 1


def isCycle(graph: Graph):
    # The main function to check whether a given graph contains cycle or not
    # Allocate memory for creating sets
    subsets = []

    for u in range(graph.num_of_v):
        subsets.append(Subset(u, 0))

    # Iterate through all edges of graph, find sets of both vertices of every edge, if sets are same, then there
    # is cycle in graph.
    for u in graph.edges:
        for v in graph.edges[u]:
            u_rep = find(subsets, u)

            v_rep = find(subsets, v)
            if u_rep == v_rep:
                return True
            union(subsets, u_rep, v_rep)


if __name__ == "__main__":
    g = Graph(3)
    # add edge 0-1
    g.add_edge(0, 1)
    # add edge 1-2
    g.add_edge(1, 2)
    # add edge 0-2
    g.add_edge(0, 2)

    print('Graph contains cycle') if isCycle(g) else print('Graph does not contain cycle')
