"""
1. Color first vertex with first color.
2. Consider the currently picked vertex and color it with the lowest numbered color that has not
been used on any previously colored vertices adjacent to it. If all previously used colors
appear on vertices adjacent to v, assign a new color to it.
Time Complexity: O(V^2 + E) in worst case.
"""

from collections import defaultdict


class Graph(object):
    def __init__(self, VERTEX):
        self.VERTEX = VERTEX
        self.adjacency = defaultdict(list)

    def add_edge(self, v: int, w: int):
        # Since graph is undirected
        self.adjacency[v].append(w)
        self.adjacency[w].append(v)

    def greedy_coloring(self):
        # Initialize no color to all vertices
        result = [-1] * self.VERTEX

        # Assign the first color to first vertex
        result[0] = 0

        # A temporary arr to store the available colors. True value of available[cr] would mean
        # that the color cr is assigned to one of its adjacent vertices
        available = [False] * self.VERTEX

        for u in range(1, self.VERTEX):
            # Process all adjacent vertices and flag their colors as unavailable
            for conn in self.adjacency[u]:
                if result[conn] != -1:
                    available[result[conn]] = True

            cr = 0
            for cr in range(self.VERTEX):
                if not available[cr]:
                    break

            result[u] = cr

            # Reset the values back to false for the next iteration
            for conn in self.adjacency[u]:
                if result[conn] != -1:
                    available[result[conn]] = False

        return result


if __name__ == '__main__':
    # Output: [0, 1, 2, 0, 1]
    g1 = Graph(5)
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(2, 3)
    g1.add_edge(3, 4)
    print("Coloring of graph-1 \n", g1.greedy_coloring())

    # Output: [0, 1, 2, 0, 3]
    g2 = Graph(5)
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(1, 2)
    g2.add_edge(1, 4)
    g2.add_edge(2, 4)
    g2.add_edge(4, 3)
    print("\nColoring of graph-2 \n", g2.greedy_coloring())
