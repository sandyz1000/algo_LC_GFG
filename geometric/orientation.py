# coding=utf-8
"""
Orientation of an ordered triplet of points in the plane can be
-> counterclockwise
-> clockwise
-> collinear

Algorithm:
Slope of line segment (p1, p2): σ = (y2 - y1)/(x2 - x1)
Slope of line segment (p2, p3): τ = (y3 - y2)/(x3 - x2)

If  σ < τ, the orientation is counterclockwise (left turn)
If  σ = τ, the orientation is collinear
If  σ > τ, the orientation is clockwise (right turn)

Using above values of σ and τ, we can conclude that,
the orientation depends on sign of  below expression:

(y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1)

Above expression is negative when σ < τ, i.e., counterclockwise
Above expression is 0 when σ = τ, i.e., collinear
Above expression is positive when σ > τ, i.e., clockwise

"""


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def orientation(p1, p2, p3):
    """
    To find orientation of ordered triplet (p1, p2, p3).
    The function returns following values
    0 --> p, q and r are collinear
    1 --> Clockwise
    2 --> Counterclockwise
    :param p1:
    :param p2:
    :param p3:
    :return:
    """
    val = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)
    if val == 0:
        return 0  # collinear
    return 1 if (val > 0) else 2  # clock or counter clock wise


if __name__ == '__main__':
    p1, p2, p3 = Point(0, 0), Point(4, 4), Point(1, 2)
    o = orientation(p1, p2, p3)
    if o == 0:
        print("Linear")
    elif o == 1:
        print("Clockwise")
    else:
        print("Counter Clockwise")
