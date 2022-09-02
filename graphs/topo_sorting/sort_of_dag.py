"""
All Topological Sorts of a Directed Acyclic Graph

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such
that for every directed edge uv, vertex u comes before v in the ordering. Topological Sorting for
a graph is not possible if the graph is not a DAG.

Given a DAG, print all topological sorts of the graph.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
For example, consider the below graph.

    5 ---> 0 <--- 4
    |             |
    |             |
    v             v
    2 ---> 3 ---> 1

All topological sorts of the given graph are:

    4 5 0 2 3 1
    4 5 2 0 3 1
    4 5 2 3 0 1
    4 5 2 3 1 0
    5 2 3 4 0 1
    5 2 3 4 1 0
    5 2 4 0 3 1
    5 2 4 3 0 1
    5 2 4 3 1 0
    5 4 0 2 3 1
    5 4 2 0 3 1
    5 4 2 3 0 1
    5 4 2 3 1 0
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

In a Directed acyclic graph many a times we can have vertices which are unrelated to each other
because of which we can order them in many ways. These various topological sorting is important
in many cases, for example if some relative weight is also available between the vertices,
which is to minimize then we need to take care of relative ordering as well as their relative
weight, which creates the need of checking through all possible topological ordering.

We can go  through all possible ordering via backtracking , the algorithm step are as follows :
1) Initialize all vertices as unvisited.

2) Now choose vertex which is unvisited and has zero indegree and decrease indegree of all those
vertices by 1 (corresponding to removing edges) now add this vertex to result and call the
recursive function again and backtrack.

3) After returning from function reset values of visited, result and indegree for enumeration
of other possibilities.

"""
from __future__ import print_function

# Python program to print all topological sorts of a graph

from collections import defaultdict


class Graph(object):
    def __init__(self, V):
        """
        :param V: int
        """
        self.V = V  # No. of vertices
        self.adj = defaultdict(list)  # Pointer to an array containing adjacency list
        self.indegree = [0] * self.V  # Vector to store indegree of vertices

    def all_topological_sort_util(self, res, visited):
        """
        Main recursive function to print all possible topological sorts
        :param res: List[int]
        :param visited: List[bool]
        :return:
        """
        # To indicate whether all topological are found or not
        flag = False

        for i in range(self.V):
            # If in-degree is 0 and not yet visited then only choose that vertex
            if not self.indegree[i] and not visited[i]:
                # reducing in-degree of adjacent vertices
                for j in self.adj[i]:
                    self.indegree[j] -= 1

                # including in result
                res.append(i)
                visited[i] = True
                self.all_topological_sort_util(res, visited)

                # resetting visited, res and in-degree for backtracking
                visited[i] = False
                del res[len(res) - 1]
                for j in self.adj[i]:
                    self.indegree[j] += 1

                flag = True

        # We reach here if all vertices are visited. So we print the solution here
        if not flag:
            for item in res:
                print(item, end=" ")
            print("")

    def addEdge(self, v, w):
        """
        :param v:
        :param w:
        :return:
        """
        self.adj[v].append(w)
        # increasing inner degree of w by 1
        self.indegree[w] += 1

    def all_topological_sort(self):
        # type: () -> None
        """
        The function does all Topological Sort. It uses recursive all_topological_sort()
        :return:
        """
        # Mark all the vertices as not visited
        visited = [False for count in range(self.V)]
        res = []
        self.all_topological_sort_util(res, visited)


if __name__ == '__main__':
    # Create a graph given in the above diagram
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    print("All Topological sorts\n")
    g.all_topological_sort()