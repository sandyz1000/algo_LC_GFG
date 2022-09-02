"""Find the number of islands | Set 1 (Using DFS)

Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island.

Example:
the below matrix contains 5 islands
Input : mat= {{1, 1, 0, 0, 0},
               {0, 1, 0, 0, 1},
               {1, 0, 0, 1, 1},
               {0, 0, 0, 0, 0},
               {1, 0, 1, 0, 1}
Output : 5
------------------------------------------
Discussion:
This is an variation of the standard problem:
Counting number of connected components in a undirected graph.

Before we go to the problem, let us understand what is a connected component. A connected component
of an undirected graph is a subgraph in which every two vertices are connected to each other by a
path(s), and which is connected to no other vertices outside the subgraph.

A graph where all vertices are connected with each other, has exactly one connected component,
consisting of the whole graph. Such graph with only one connected component is called as Strongly
Connected Graph.

The problem can be easily solved by applying DFS() on each component. In each DFS() call, a
component or a sub-graph is visited. We will call DFS on the next un-visited component.
The number of calls to DFS() gives the number of connected components. BFS can also be used.

What is an island?
A group of connected 1s forms an island. For example, the below matrix contains 5 islands
{1, 1, 0, 0, 0},
{0, 1, 0, 0, 1},
{1, 0, 0, 1, 1},
{0, 0, 0, 0, 0},
{1, 0, 1, 0, 1}

"""
from __future__ import print_function


# Time complexity: O(ROW x COL)
# Program to count islands in boolean 2D matrix
class Graph:
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    # A function to check if a given cell
    # (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1
        # and not yet visited
        return 0 <= i < self.ROW and 0 <= j < self.COL \
               and not visited[i][j] and self.graph[i][j]

    def DFS(self, i, j, visited):
        """
        A utility function to do DFS for a 2D boolean matrix. It only considers the 8
        neighbours as adjacent vertices
        :param i:
        :param j:
        :param visited:
        :return:
        """
        # These arrays are used to get row and column numbers of 8 neighbours of a given cell
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

        # Mark this cell as visited
        visited[i][j] = True

        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)

    def count_islands(self):
        """The main function that returns count of islands in a given boolean 2D matrix"""
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        # Initialize count as 0 and travese
        # through the all cells of
        # given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # Visit all cells in this island
                    # and increment island count
                    self.DFS(i, j, visited)
                    count += 1

        return count


if __name__ == '__main__':
    # Output: Number of islands is : 5
    graph = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]]

    row = len(graph)
    col = len(graph[0])

    g = Graph(row, col, graph)

    print("Number of islands is :")
    print(g.count_islands())
