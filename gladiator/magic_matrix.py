
def create_magic_square(matrix):
    pass


def is_magic_square_v2(matrix):
    matrix_size = len(matrix[0])
    sums = set()

    for col in range(matrix_size):
        sums.add(sum(row[col] for row in matrix))

    # Union of row and columns set
    sums |= set([sum(lines) for lines in matrix])

    # Add the sum of the diagonals
    diagonal_sum = 0
    for i in range(0, matrix_size):
        diagonal_sum += matrix[i][i]
    sums.add(diagonal_sum)

    diagonal_sum = 0
    for i in range(matrix_size - 1, -1, -1):
        diagonal_sum += matrix[i][i]
    sums.add(diagonal_sum)

    if len(sums) > 1:
        return False
    else:
        return True


def is_magic_square(matrix):
    i_size = len(matrix[0])
    sum_list = []

    # Vertical:
    for col in range(i_size):
        sum_list.append(sum(row[col] for row in matrix))

    # Horizontal
    sum_list.extend([sum(lines) for lines in matrix])

    # Diagonals
    dl_result = 0
    for i in range(0, i_size):
        dl_result += matrix[i][i]
    sum_list.append(dl_result)

    dr_result = 0
    for i in range(i_size - 1, -1, -1):
        dr_result += matrix[i][i]
    sum_list.append(dr_result)

    if len(set(sum_list)) > 1:
        return False
    return True


if __name__ == "__main__":
    print(is_magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(is_magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
    print(is_magic_square([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
    print(is_magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
    print(is_magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))

    # Validate is magic square ver-2
    print(is_magic_square_v2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(is_magic_square_v2([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
    print(is_magic_square_v2([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
    print(is_magic_square_v2([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
    print(is_magic_square_v2([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
