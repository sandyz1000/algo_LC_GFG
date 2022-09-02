"""
Implement a jigsaw puzzle. Design the data structures and explain an algorithm to solve the
puzzle. You can assume that you have a fitsWith method which, when passed two puzzle pieces,
returns true if the two pieces belong together.


We will assume that we have a traditional, simple jigsaw puzzle. The puzzle is grid-like,
with rows and columns. Each piece is located in a single row and column and has four edges. Each
edge comes in one of three types: inner, outer, and flat. A corner piece, for example, will have
two flat edges and two other edges, which could be inner or outer.

As we solve the jigsaw puzzle (manually or algorithmically), we'll need to store the position of
each piece. We could think about the position as absolute or relative:
1. Absolute Position: "This piece is located at position (12, 23)." Absolute position would belong
to the Piece class itself and would include an orientation as well.

2. Relative Position: “I don’t know where this piece is actually located, but I know that it is
next to this other piece.” The relative position would belong to the Edge class.

==Algorithm to Solve the Puzzle==
We will sketch this algorithm using a mix of pseudocode and real code.

Just as a kid might in solving a puzzle, we'll start with the easiest pieces first: the corners
and edges. We can easily search through all the pieces to find just the edges. While we're at
it though, it probably makes sense to group all the pieces by their edge types.


We now have a quicker way to zero in on potential matches for any given edge. We then go through
the puzzle, line by line, to match pieces.

The solve method, implemented below, operates by picking an arbitrary start with. It then finds an
open edge on the corner and tries to match it to an open piece. When it finds a match, it does the
following:
1. Attaches the edge.
2. Removes the edge from the list of open edges.
3. Finds the next open edge.

The next open edge is defined to be the one directly opposite the current edge, if it is
available. If it is not available, then the next edge can be any other edge. This will cause the
puzzle to be solved in a spiral-like fashion, from the outside to the inside.

The spiral comes from the fact that the algorithm always moves in a straight line, whenever
possible. When we reach the end of the first edge, the algorithm moves to the only available edge
on that corner piece—a 90-degree turn. It continues to take 90-degree turns at the end of each
side until the entire outer edge of the puzzle is completed. When that last edge piece is in
place, that piece only has one exposed edge remaining, which is again a 90-degree turn. The
algorithm repeats itself for subsequent rings around the puzzle, until finally all the pieces are
in place.

For simplicity, we’re represented inners and outers as an Edge array. This is actually not a
great choice, since we need to add and removed elements from it frequently. If we were writing a
real code, we would probably want to implement these variables as linked lists.

"""


class Type:
    inner = 0
    outer = 0
    flat = 0


class Edge:
    def __init__(self, parent, _type, index, attached_to):
        self.parent = parent
        self._type = _type
        self.index = index  # Index into Piece.edges
        self.attached_to = attached_to  # Relative position

    # See Algorithm section. Returns true if the two pieces should be attached to each other.
    def fitswith(self, edge):
        pass


class Piece:
    def __init__(self):
        self.edges = []
        self.is_corner = False


class Puzzle:
    def __init__(self):
        self.pieces = []  # Remaining pieces left to put away.
        self.solution = []
        # See algorithm section.
        self.inners = []
        self.outers = []
        self.flats = []
        self.corners = []

    # See Algorithm section.
    def sort(self):
        for peice in self.pieces:
            if True:  # P has two flat edges then add p to corners
                pass

            for edge in p.edges:
                if True:  # edge is inner then add to inners
                    pass

                if True:  # edge is outer then add to outers
                    pass

    def solve(self):
        # Pick any corner to start with
        current_edge = self.getExposedEdge(self.corner[0])

        # Loop will iterate in a spiral like fashion until the puzzle is full.
        while current_edge is not None:
            # Match with opposite edges. Inners with outers, etc.
            opposites = self.outers if current_edge.type == self.inner else self.inners

            for fittingEdge in opposites:
                if current_edge.fitsWith(fittingEdge):
                    self.attachEdges(current_edge, fittingEdge)  # attach edge
                    self.removeFromlist(current_edge)
                    self.removeFromList(fittingEdge)

                    # get next edge
                    current_edge = self.nextExposedEdge(fittingEdge)
                    break  # Break out of inner loop. Continue in outer.

    def removeFromList(self, edge):
        if edge.type == self.flat:
            return

        arr = self.inners if self.current_edge.type == self.inner else self.outers
        arr.remove(edge)

    # Return the opposite edge if possible. Else, return any exposed edge.
    def nextExposedEdge(self, edge):
        next_index = (edge.index + 2) % 4  # Opposite edge
        next_edge = edge.parent.edges[next_index]
        if self.isExposed(next_edge):
            return next_edge

        return self.getExposedEdge(edge.parent)

    def attachEdges(self, e1, e2):
        e1.attached_to = e2
        e2.attached_to = e1

    def isExposed(self, edge):
        return edge.type != self.flat and edge.attached_to is None

    def getExposedEdge(self, p):
        for edge in p.edges:
            if self.isExposed(edge):
                return edge

        return None


if __name__ == '__main__':
    pass
