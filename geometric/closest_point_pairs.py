"""
https://www.geeksforgeeks.org/closest-pair-of-points-onlogn-implementation/

We are given an array of n points in the plane, and the problem is to find out the closest pair
of points in the array. This problem arises in a number of applications. For example,
in air-traffic control, you may want to monitor planes that come too close together, since this
may indicate a possible collision. Recall the following formula for distance between two points p
and q.

|pq| = math.sqrt((px -qx)**2 + (py - qy)**2)

We have discussed a divide and conquer solution for this problem. The time complexity of the
implementation provided in the previous post is O(n (Logn)^2). In this post, we discuss an
implementation with time complexity as O(nLogn).

Following is a recap of the algorithm discussed in the previous post.
1) We sort all points according to x coordinates.
2) Divide all points in two halves.
3) Recursively find the smallest distances in both sub arrays.
4) Take the minimum of two smallest distances. Let the minimum be d.
5) Create an array strip[] that stores all points which are at most d distance away from the middle
line dividing the two sets.
6) Find the smallest distance in strip[].
7) Return the minimum of d and the smallest distance calculated in above step 6.

The great thing about the above approach is, if the array strip[] is sorted according to y
coordinate, then we can find the smallest distance in strip[] in O(n) time. In the implementation
discussed in previous post, strip[] was explicitly sorted in every recursive call that made the
time complexity O(n (Logn)^2), assuming that the sorting step takes O(nLogn) time.

In this post, we discuss an implementation where the time complexity is O(nLogn). The idea is to
presort all points according to y coordinates. Let the sorted array be Py[]. When we make
recursive calls, we need to divide points of Py[] also according to the vertical line. We can do
that by simply processing every point and comparing its x coordinate with x coordinate of middle
line.

Time Complexity:Let Time complexity of above algorithm be T(n). Let us assume that we use a
O(nLogn) sorting algorithm. The above algorithm divides all points in two sets and recursively
calls for two sets. After dividing, it finds the strip in O(n) time. Also, it takes O(n) time to
divide the Py array around the mid vertical line. Finally finds the closest points in strip in O(n)
time.
So T(n) can expressed as follows
T(n) = 2T(n/2) + O(n) + O(n) + O(n)
T(n) = 2T(n/2) + O(n)
T(n) = T(nLogn)

---------------------------------------------------------------------------- """
from __future__ import print_function, absolute_import

import sys
import math
import functools


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class ClosestPairs(object):
    def __init__(self, points=[]):
        self.points = points
        self.size = len(points)

    def closest(self):
        """
        The main function that finds the smallest distance. This method mainly uses utils
        :return:
        """
        points, n = self.points, self.size

        px = [points[i] for i in range(n)]
        py = [points[i] for i in range(n)]
        px.sort(key=functools.cmp_to_key(lambda a, b: a.x - b.x))
        py.sort(key=functools.cmp_to_key(lambda a, b: a.y - b.y))

        return self.utils(px, py, n)

    def utils(self, px, py, n):
        """
        A recursive function to find the smallest distance. The arr Px contains all points
        sorted according to x coordinates and Py contains all points sorted according to y
        coordinates
        :param px: list
        :param py: list
        :param n: int
        :return:
        """
        # If there are 2 or 3 points, then use brute force
        if n <= 3:
            return self.brute_force(px, n)

        mid = n // 2  # Find the middle point
        mid_point = px[mid]
        # Divide points in y sorted arr around the vertical line. Assumption: All x
        # coordinates are distinct.
        pyl = []  # y sorted points on left of vertical line
        pyr = []  # y sorted points on right of vertical line
        for i in range(n):
            if py[i].x < mid_point.x:
                pyl.append(py[i])
            else:
                pyr.append(py[i])

        # Consider the vertical line passing through the middle point calculate the smallest
        # distance dl on left of middle point and dr on right side
        dl = self.utils(px[:mid], pyl, mid)
        dr = self.utils(px[mid:], pyr, n - mid)

        d = min(dl, dr)  # Find the smaller of two distances

        # Build an arr strip[] that contains points close (closer than d)
        # to the line passing through the middle point
        strip = [py[i] for i in range(n) if abs(py[i].x - mid_point.x) < d]
        # Find the closest points in strip. Return the minimum of d and closest distance
        # is strip[]
        return min(d, self.strip_closest(strip, len(strip), d))

    def strip_closest(self, strip, size, d):
        """
        A utility function to find the distance between the closest points of strip of given size.
        All points in strip[] are sorted according to y coordinate. They all have an upper bound
        on minimum distance as d.
        Note that this method seems to be a O(n^2) method, but it's a O(n) method as the inner
        loop runs at most 6 times.
        :param strip: list[Point]
        :param size: int
        :param d: float
        :return:
        """
        minimum = d
        for i in range(size):
            j = i + 1
            while j < size and strip[j].y - strip[i].y < minimum:
                distance = self.dist(strip[i], strip[j])
                if distance < minimum:
                    minimum = distance
                j += 1
        return minimum

    def dist(self, p1, p2):
        """
        :param p1: Point
        :param p2: Point
        :return:
        """
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def brute_force(self, px, n):
        """
        Needed to sort arr of points according to X coordinate
        :return:
        """
        minimum = sys.maxsize
        for i in range(n):
            for j in range(i + 1, n):
                distance = self.dist(px[i], px[j])
                if distance < minimum:
                    minimum = distance
        return minimum


if __name__ == '__main__':
    closest_pairs = ClosestPairs([Point(2, 3), Point(12, 30), Point(40, 50), Point(5, 1),
                                  Point(12, 10), Point(3, 4)])
    print("The smallest distance is ", closest_pairs.closest())
