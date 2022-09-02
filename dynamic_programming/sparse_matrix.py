"""Sparse Matrix and its representations | Set 1 (Using Arrays and Linked Lists)

A matrix is a two-dimensional data object made of m rows and n columns, therefore having total
m x n values. If most of the elements of the matrix have 0 value, then it is called a sparse
matrix.

Why to use Sparse Matrix instead of simple matrix ?

Storage: There are lesser non-zero elements than zeros and thus lesser memory can be used to store
only those elements.
Computing time: Computing time can be saved by logically designing a data structure traversing
only non-zero elements..

Example:

0 0 3 0 4
0 0 5 7 0
0 0 0 0 0
0 2 6 0 0

Representing a sparse matrix by a 2D array leads to wastage of lots of memory as zeroes in the
matrix are of no use in most of the cases. So, instead of storing zeroes with non-zero elements,
we only store non-zero elements. This means storing non-zero elements with triples- (Row, Column,
value).

Sparse Matrix Representations can be done in many ways following are two common representations:
1.  Array representation
2.  Linked list representation

"""


def sparse_matrix(matrix):
    # Assume 4x5 sparse matrix
    size = sum([matrix[i][j] for i in range(4) for j in range(5) if matrix[i][j] != 0])

    # number of columns in compactMatrix (size) must be equal to number of non - zero elements in
    #  matrix

    compact_matrix = [[0] * size for i in range(3)]

    # Making of new matrix
    k = 0
    for i in range(4):
        for j in range(5):
            if matrix[i][j] != 0:
                compact_matrix[0][k] = i
                compact_matrix[1][k] = j
                compact_matrix[2][k] = matrix[i][j]
                k += 1

    for i in range(3):
        output = []
        for j in range(size):
            output.append("%d " % compact_matrix[i][j])
        print(output)


class Node(object):
    """C program for Sparse Matrix Representation using Linked Lists
    Node to represent sparse matrix"""
    def __init__(self, value, row_position, column_position, next_node=None):
        """
        :param value: int
        :param row_position: int
        :param column_position: int
        :param next_node: None
        """
        self.value = value
        self.row_position = row_position
        self.column_position = column_position
        self.next_node = next_node


class SparseMatrix(object):
    def __init__(self, start):
        self.start = start

    def create_new_node(self, non_zero_element, row_index, column_index):
        """
        Function to create new node
        :param start: Node
        :param non_zero_element: int
        :param row_index: int
        :param column_index: int
        :return:
        """
        temp = self.start
        if temp is None:
            # Create new node dynamically
            temp = Node(non_zero_element, row_index, column_index, None)
            self.start = temp
        else:
            while temp.next_node is not None:
                temp = temp.next_node

            # Create new node dynamically
            r = Node(non_zero_element, row_index, column_index, None)
            temp.next_node = r

    def print_list(self):
        """
        This function prints contents of linked list starting from start
        :param start: Node
        :return:
        """
        temp = r = s = self.start

        print("row_position: ")
        output = []
        while temp is not None:
            output.append("%d " % temp.row_position)
            temp = temp.next_node

        print("\n", output, "\n")
        print("column_position: ")

        output = []
        while r is not None:
            output.append("%d " % r.column_position)
            r = r.next_node
        print("\n", output, "\n")

        print("Value: ")
        output = []
        while s is not None:
            output.append("%d " % s.value)
            s = s.next_node
        print("\n", output, "\n")


if __name__ == '__main__':
    print("Linked list based implementation")
    matrix = [[0, 0, 3, 0, 4],
              [0, 0, 5, 7, 0],
              [0, 0, 0, 0, 0],
              [0, 2, 6, 0, 0]]

    sm = SparseMatrix(Node(0, 0, 0, None))
    for i in range(4):
        for j in range(5):
            # Pass only those values which are non - zero
            if matrix[i][j] != 0:
                sm.create_new_node(matrix[i][j], i, j)

    sm.print_list()

    print("Array based implementation")
    sparse_matrix(matrix)
