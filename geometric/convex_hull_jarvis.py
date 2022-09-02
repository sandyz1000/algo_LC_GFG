"""
https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/

The idea of Jarvis's Algorithm is simple, we start from the leftmost point (or point with
minimum x coordinate value) and we keep wrapping points in counterclockwise direction.
The big question is, given a point p as current point, how to find the next point in output?
- The idea is to use orientation() here. Next point is selected as the point that beats all other
points at counterclockwise orientation, i.e., next point is q if for any other point r, we have
"orientation(p, r, q) = counterclockwise". Following is the detailed algorithm.

1) Initialize p as leftmost point.
2) Do following while we don't come back to the first (or leftmost) point.
    a) The next point q is the point such that the triplet (p, q, r) is counterclockwise for any
    other point r.
    b) next[p] = q (Store q as next of p in the output convex hull).
    c) p = q (Set p as q for next iteration).

Time Complexity:
For every point on the hull we examine all the other points to determine the
next point. Time complexity is (m * n) where n is number of input points and m is number of
output or hull points (m <= n). In worst case, time complexity is O(n^2). The worst case occurs
when all the points are on the hull (m = n)
"""


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)


class JarvisConvexHull(object):
    def __init__(self, points=[]):
        self.points = points
        self.size = len(points)

    def orientation(self, p, q, r):
        """
        To find orientation of ordered triplet (p, q, r). The function returns following values
        0 --> p, q and r are collinear
        1 --> Clockwise
        2 --> Counter clockwise
        :type p: Point
        :type q: Point
        :type r: Point
        :return:
        """
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0  # co-linear
        return 1 if val > 0 else 2  # clock or counter clock wise

    def find_extreme_point(self, hull, p, n):
        hull.append(self.points[p])  # Add current point to result
        # Search for a point 'q' such that orientation(p, x, q) is counterclockwise for all
        # points 'x'. The idea is to keep track of last visited most counter clock- wise point
        # in q. If any point 'i' is more counter clock-wise than q, then update q.
        q = (p + 1) % n
        for i in range(n):
            # If i is more counterclockwise than current q, then update q
            if self.orientation(self.points[p], self.points[i], self.points[q]) == 2:
                q = i

        # Now q is the most counterclockwise with respect to p Set p as q for next iteration,
        # so that q is added to result 'hull'
        p = q
        return p

    def convex_hull(self):
        """
        Prints convex hull of a set of n points.
        :return:
        """
        points, n = self.points, self.size
        # There must be at least 3 points
        if n < 3:
            return None

        hull = []  # Initialize Result
        l = 0  # Find the leftmost point
        for i in range(1, n):
            if points[i].x < points[l].x:
                l = i

        # Start from leftmost point, keep moving counterclockwise until reach the start point
        # again.  This loop runs O(h) times where h is number of points in result or output.
        p = self.find_extreme_point(hull, l, n)
        while p != l:
            p = self.find_extreme_point(hull, p, n)

        return hull


if __name__ == '__main__':
    points = [Point(0, 3), Point(2, 2), Point(1, 1), Point(2, 1), Point(3, 0),
              Point(0, 0), Point(3, 3)]
    jch = JarvisConvexHull(points)
    results = jch.convex_hull()
    if results and len(results) > 0:
        print("The results are:")
        for res in results:
            print(res)
    else:
        print("Enter minimum sets of points")
