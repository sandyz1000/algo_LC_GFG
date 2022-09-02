"""
Given a polygon and a point 'p', find if 'p' lies inside the polygon or not. The points lying on
the border are considered inside

Following is a simple idea to check whether a point is inside or outside:
1) Draw a horizontal line to the right of each point and extend it to infinity
1) Count the number of times the line intersects with polygon edges.
2) A point is inside the polygon if either count of intersections is odd or
   point lies on an edge of polygon.  If none of the conditions is true, then
   point lies outside.

Time Complexity: O(n) where n is the number of vertices in the given polygon.
"""

INF = 10000


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)


class PointLieInsidePolygon(object):
    def __init__(self, points, n):
        self.points = points
        self.n = n

    def on_segment(self, p, q, r):
        """
        Given three collinear points p, q, r, the function checks if point q lies on line
        segment 'pr'
        :return:
        """
        if max(p.x, r.x) >= q.x >= min(p.x, r.x) and max(p.y, r.y) >= q.y >= min(p.y, r.y):
            return True
        return False

    def is_inside(self, point):
        """
        :param polygon: list(Point)
        :param n: int
        :param point: Point
        :return:
        """
        polygon = self.points
        n = self.n

        # There must be at least 3 vertices in polygon[]
        if n < 3:
            return False

        # Create a point for line segment from p to infinite
        extreme = Point(INF, point.y)

        # Count intersections of the above line with sides of polygon
        i, count = 0, 0
        while True:
            next_point = (i + 1) % n
            # Check if the line segment from 'point' to 'extreme' intersects
            # with the line segment from 'polygon[i]' to 'polygon[next_point]'
            if self.do_intersect(polygon[i], polygon[next_point], point, extreme):
                # If the point 'p' is collinear with line segment 'i-next_point',
                # then check if it lies on segment. If it lies, return true, otherwise false
                if self.orientation(polygon[i], point, polygon[next_point]) == 0:
                    return self.on_segment(polygon[i], point, polygon[next_point])

                count += 1
            i = next_point

            if i == 0: break

        # Return true if count is odd, false otherwise
        return count & 1  # Same as (count%2 == 1)

    def orientation(self, p, q, r):
        """
        To find orientation of ordered triplet (p, q, r). The function returns following values
        0 --> p, q and r are colinear
        1 --> Clockwise
        2 --> Counterclockwise
        :param p: Point
        :param q: Point
        :param r: Point
        :return:
        """
        value = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if value == 0:
            return 0  # colinear
        return 1 if (value > 0) else 2  # clock or counterclock wise

    def do_intersect(self, p1, q1, p2, q2):
        """
        The function that returns true if line segment 'p1q1' and 'p2q2' intersect.
        :return:
        """
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
    polygon1 = [Point(0, 0), Point(10, 0), Point(10, 10), Point(0, 10)]
    assertion = PointLieInsidePolygon(polygon1, len(polygon1))

    point = Point(20, 20)
    result = "Yes" if assertion.is_inside(point) else "No"
    print("%s for points %s" % (result, point))

    point = Point(5, 5)
    result = "Yes" if assertion.is_inside(point) else "No"
    print("%s for points %s" % (result, point))

    polygon2 = [Point(0, 0), Point(10, 0), Point(10, 10), Point(0, 10)]
    assertion = PointLieInsidePolygon(polygon2, len(polygon2))

    point = Point(3, 3)
    result = "Yes" if assertion.is_inside(point) else "No"
    print("%s for points %s" % (result, point))

    point = Point(5, 1)
    result = "Yes" if assertion.is_inside(point) else "No"
    print("%s for points %s" % (result, point))

    point = Point(8, 1)
    result = "Yes" if assertion.is_inside(point) else "No"
    print("%s for points %s" % (result, point))

    polygon3 = [Point(0, 0), Point(10, 0), Point(10, 10), Point(0, 10)]
    assertion = PointLieInsidePolygon(polygon3, len(polygon3))

    point = Point(-1, 10)
    result = "Yes" if assertion.is_inside(point) else "No"
    print("%s for points %s" % (result, point))

    print ("-------------------------------")
