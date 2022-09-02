"""
Given a set of points in the plane. the convex hull of the set is the smallest convex polygon that
contains all the points of it.
Using Graham's scan algorithm, we can find Convex Hull in O(nLogn) time.

Let points[0..n-1] be the input array.

1) Find the bottom-most point by comparing y coordinate of all points. If there are two points
with same y value, then the point with smaller x coordinate value is considered. Let the
bottom-most point be P0. Put P0 at first position in output hull.

2) Consider the remaining n-1 points and sort them by polar angle in counterclockwise order
around points[0]. If polar angle of two points is same, then put the nearest point first.

3 After sorting, check if two or more points have same angle. If two more points have same angle,
then remove all same angle points except the point farthest from P0. Let the size of new array be
m.

4) If m is less than 3, return (Convex Hull not possible)

5) Create an empty stack 'S' and push points[0], points[1] and points[2] to S.

6) Process remaining m-3 points one by one. Do following for every point 'points[i]'
    4.1) Keep removing points from stack while orientation of following 3 points is not
    counterclockwise (or they don't make a left turn).
        a) Point next to top in stack b) Point at the top of stack c) points[i]
    4.2) Push points[i] to S

7) Print contents of S

Phase 1 (Sort points):
We first find the bottom-most point. The idea is to pre-process points be
sorting them with respect to the bottom-most point. Once the points are sorted, they form a
simple closed path. What should be the sorting criteria? computation of actual angles would be
inefficient since trigonometric functions are not simple to evaluate. The idea is to use the
orientation to compare angles without actually computing them (See the compare() function below)

Phase 2 (Accept or Reject Points):
Once we have the closed path, the next step is to traverse the
path and remove concave points on this path. How to decide which point to remove and which to
keep? Again, orientation helps here. The first two points in sorted array are always part of
Convex Hull. For remaining points, we keep track of recent three points, and find the angle
formed by them. Let the three points be prev(p), curr(c) and next(n). If orientation of these
points (considering them in same order) is not counterclockwise, we discard c, otherwise we keep it


Time Complexity:
Let n be the number of input points. The algorithm takes O(nLogn) time if we use a O(nLogn)
sorting algorithm.

The first step (finding the bottom-most point) takes O(n) time.
The second step (sorting points) takes O(nLogn) time.
Third step takes O(n) time. In third step, every element is pushed and popped at most one time.
So the sixth step to process points one by one takes O(n) time, assuming that the stack operations
take O(1) time. Overall complexity is O(n) + O(nLogn) + O(n) + O(n) which is O(nLogn)

"""
import functools


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GrahamConvexHull(object):
    def __init__(self, points=[]):
        self.p0 = None
        self.points = points
        self.size = len(points)

    def next_to_top(self, stack):
        """
        A utility function to find next to top in a stack
        :return:
        :type stack: list
        """
        size = len(stack)
        return stack[size - 2]

    def distance_sq(self, p1, p2):
        """
        A utility function to return square of distance between p1 and p2
        :type p1: Point
        :type p2: Point
        :return:
        """
        return (p1.x - p2.x)**2 + (p1.y - p2.y)**2

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
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    def compare(self, vp1, vp2):
        """
        A function used by library function sorted() to sort an arr of points with respect
        to the first point
        :type vp1: Point
        :type vp2: Point
        :return:
        """
        # Find orientation
        o = self.orientation(self.p0, vp1, vp2)
        if o == 0:
            return -1 if self.distance_sq(self.p0, vp2) >= self.distance_sq(self.p0, vp1) else 1

        return -1 if o == 2 else 1

    def convex_hull(self):
        """
        Return convex hull of a set of n points.
        :return:
        """
        points, n = self.points, self.size
        # Find the bottom most point
        ymin, min = points[0].y, 0
        for i in range(n):
            y = points[i].y
            # Pick the bottom-most or chose the left most point in case of tie
            if (y < ymin) or (ymin == y and points[i].x < points[min].x):
                ymin, min = points[i].y, i

        # Place the bottom-most point at first position
        points[0], points[min] = points[min], points[0]

        # Sort n-1 points with respect to the first point. A point p1 comes before p2 in sorted
        # output if p2 has larger polar angle (in counterclockwise direction) than p1
        self.p0 = points[0]
        points = [self.p0] + sorted(points[1:], key=functools.cmp_to_key(self.compare))

        # If two or more points make same angle with p0, Remove all but the one that is farthest
        # from p0. Remember that, in above sorting, our criteria was to keep the farthest point at
        # the end when more than one points have same angle.
        m = 1  # Initialize size of modified arr

        for i in range(1, n):
            # Keep removing i while angle of i and i+1 is same with respect to p0
            while i < n - 1 and self.orientation(self.p0, points[i], points[i + 1]) == 0:
                i += 1

            points[m] = points[i]
            m += 1  # Update size of modified arr

        # If modified arr of points has less than 3 points, convex hull is not possible
        if m < 3:
            return

        # Create an empty stack and push first three points to it.
        stack = [points[0], points[1], points[2]]
        size = len(stack)

        # Process remaining n-3 points
        for i in range(3, m):
            # Keep removing top while the angle formed by points next-to-top, top, and
            # points[i] makes a non-left turn
            while len(stack) >= 2 and self.\
                    orientation(self.next_to_top(stack), stack[len(stack) - 1], points[i]) != 2:
                stack.pop()
                size -= 1
            stack.append(points[i])

        return stack


if __name__ == '__main__':
    points = [Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4), Point(0, 0),
              Point(1, 2), Point(3, 1), Point(3, 3)]
    gch = GrahamConvexHull(points)
    results = gch.convex_hull()
    size = len(results)

    # Now stack has the output points, print contents of stack
    while len(results) is not 0:
        point = results[size - 1]
        print("(%d, %d)" % (point.x, point.y))
        results.pop()
        size -= 1
