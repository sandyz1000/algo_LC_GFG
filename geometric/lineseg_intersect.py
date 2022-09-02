"""
https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/

Given two line segments (p1, q1) and (p2, q2), find if the given line segments intersect with
each other. Let us define notion of orientation.
Orientation of an  ordered triplet of points in the plane can be
- counterclockwise
- clockwise
- collinear
"""


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class LineSegIntersect(object):
    def __init__(self, points=[]):
        self.p1 = points[0]
        self.q1 = points[1]
        self.p2 = points[2]
        self.q2 = points[3]

    def on_segment(self, p, q, r):
        """
        Given three co-linear points p, q, r, the function checks if point q lies on line
        segment 'pr'
        :type p: Point
        :type q: Point
        :type r: Point
        :return:
        """
        if max(p.x, r.x) >= q.x >= min(p.x, r.x) and max(p.y, r.y) >= q.y >= min(p.y, r.y):
            return True
        return False

    def orientation(self, p, q, r):
        """
        To find orientation of ordered triplet (p, q, r). The function returns following values
        0 --> p, q and r are collinear
        1 --> Clockwise
        2 --> Counterclockwise
        :type p: Point
        :type q: Point
        :type r: Point
        :return:
        """
        # See http://www.geeksforgeeks.org/orientation-3-ordered-points/
        # for details of below formula.
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0  # collinear

        return 1 if val > 0 else 2  # clock or counter clock wise

    def do_intersect(self):
        """
        The main function that returns True if line segment 'p1q1' and 'p2q2' intersect.
        :return:
        """
        p1, q1, p2, q2 = self.p1, self.q1, self.p2, self.q2
        # Find the four orientations needed for general and special cases
        o1 = self.orientation(p1, q1, p2)
        o2 = self.orientation(p1, q1, q2)
        o3 = self.orientation(p2, q2, p1)
        o4 = self.orientation(p2, q2, q1)

        # General case
        if o1 != o2 and o3 != o4:
            return True

        # Special Cases
        # p1, q1 and p2 are collinear and p2 lies on segment p1q1
        if o1 == 0 and self.on_segment(p1, p2, q1):
            return True

        # p1, q1 and p2 are collinear and q2 lies on segment p1q1
        if o2 == 0 and self.on_segment(p1, q2, q1):
            return True

        # p2, q2 and p1 are collinear and p1 lies on segment p2q2
        if o3 == 0 and self.on_segment(p2, p1, q2):
            return True

        # p2, q2 and q1 are collinear and q1 lies on segment p2q2
        if o4 == 0 and self.on_segment(p2, q1, q2):
            return True

        return False  # Doesn't fall in any of the above cases


if __name__ == '__main__':
    lsi = LineSegIntersect([Point(1, 1), Point(10, 1), Point(1, 2), Point(10, 2)])
    result = lsi.do_intersect()
    print("Points Intersect" if result else "Points do not intersect")
    print("------------------------")

    lsi = LineSegIntersect([Point(10, 0), Point(0, 10), Point(0, 0), Point(10, 10)])
    result = lsi.do_intersect()
    print("Points Intersect" if result else "Points do not intersect")
    print("------------------------")

    lsi = LineSegIntersect([Point(-5, -5), Point(0, 0), Point(1, 1), Point(10, 10)])
    result = lsi.do_intersect()
    print("Points Intersect" if result else "Points do not intersect")
