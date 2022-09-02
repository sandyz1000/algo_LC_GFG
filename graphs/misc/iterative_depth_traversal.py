"""
Depth First Traversal (or Search) for a graph is similar to Depth First Traversal (DFS) of a
tree. The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same
node again. To avoid processing a node more than once, we use a boolean visited array.

For example, a DFS of below graph is "0 3 4 2 1", other possible DFS is "0 2 1 3 4".

    (1) --> (0) ---> (3)
     A      /  <-\     |
     |     /      \    |
     |    /        \   V
    (2)<-           - (4)

Time complexity of iterative implementation is O(V + E).
"""

from collections import defaultdict


# An Iterative C++ program to do DFS traversal from a given source vertex.
# DFS(int s) traverses vertices

class StackG(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.container = [0] * self.capacity

    def peek(self):
        return self.container[self.top]

    def empty(self):
        return self.top == -1

    def push(self, item):
        if self.top + 1 > self.capacity:
            raise RuntimeError("Index exceed capacity")

        self.top += 1
        self.container[self.top] = item

    def pop(self):
        if self.top < 0:
            raise RuntimeError("No item to pop")

        result = self.container[self.top]
        self.container[self.top] = 0
        self.top -= 1
        return result


class Graph(object):
    """This class represents a directed graph using adjacency list representation"""
    def __init__(self, V):
        self.V = V  # No. of vertices
        self.adj = defaultdict(list)  # adjacency lists

    def addEdge(self, v, w):
        self.adj[v].append(w)  # Add w to v's list.

    def dfs(self, s):
        """prints all not yet visited vertices reachable from s"""
        visited = [False] * self.V  # Initially mark all vertices as not visited
        stack = StackG(100)  # Create a stack for DFS & Push the current source node.
        stack.push(s)

        while not stack.empty():
            # Pop a vertex from stack and print it
            s = stack.pop()

            # Stack may contain same vertex twice. So we need to print the popped item only
            # if it is not visited.
            if not visited[s]:
                print(s, end=" ")
                visited[s] = True

            # Get all adjacent vertices of the popped vertex s If a adjacent has not been visited,
            # then push it to the stack.
            for i in self.adj[s]:
                if not visited[i]:
                    stack.push(i)


if __name__ == '__main__':
    g = Graph(5)  # Total 5 vertices in graph
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 4)

    print("Following is Depth First Traversal")
    g.dfs(0)
