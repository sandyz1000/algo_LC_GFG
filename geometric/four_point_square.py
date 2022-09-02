class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_square(p1, p2, p3, p4):
    """
    This function returns true if (p1, p2, p3, p4) form a square, otherwise false
    :param p1: Point
    :param p2: Point
    :param p3: Point
    :param p4: Point
    :return:
    """

    d2 = dist_square(p1, p2)  # from p1 to p2
    d3 = dist_square(p1, p3)  # from p1 to p3
    d4 = dist_square(p1, p4)  # from p1 to p4

    # If lengths if (p1, p2) and (p1, p3) are same, then
    # following conditions must met to form a square.
    # 1) Square of length of (p1, p4) is same as twice the square of (p1, p2)
    # 2) p4 is at same distance from p2 and p3
    if d2 == d3 and 2*d2 == d4:
        d = dist_square(p2, p4)
        return d == dist_square(p3, p4) and d == d2

    # The below two cases are similar to above case
    if d3 == d4 and 2*d3 == d2:
        d = dist_square(p2, p3)
        return d == dist_square(p2, p4) and d == d3

    if d2 == d4 and 2*d2 == d3:
        d = dist_square(p2, p3)
        return d == dist_square(p3, p4) and d == d2

    return False


def dist_square(p, q):
    """
    Euclidean distance
    A utility function to find square of distance from point 'p' to point 'q'
    :param p: Point
    :param q: Point
    :return:
    """
    return (p.x - q.x)**2 + (p.y - q.y)**2


if __name__ == '__main__':
    p1 = Point(20, 10)
    p2 = Point(10, 20)
    p3 = Point(20, 20)
    p4 = Point(10, 10)

    # p1 ---d2---- p2
    # | \           |
    # d3    d4      |
    # |         \   |
    # p3 --------- p4

    print("Yes" if is_square(p1, p2, p3, p4) else "No")
