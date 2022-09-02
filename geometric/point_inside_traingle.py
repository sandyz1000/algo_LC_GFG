"""
Given three corner points of a triangle, and one more point P. Write a function to check whether
P lies within the triangle or not.

For example, consider the following program, the function should return true for P(10,
15) and false for P'(30, 15)

              B(10,30)
                / \
               /   \
              /     \
             /   P   \      P'
            /         \
     A(0,0) ----------- C(20,0)

"""


class PointInsideTraingle(object):
    def is_inside(self, x1, y1, x2, y2, x3, y3, x, y):
        """
        A function to check whether point P(x, y) lies inside the triangle
        formed by A(x1, y1), B(x2, y2) and C(x3, y3)
        :type x1: int
        :type x2: int
        :type x3: int
        :type y1: int
        :type y2: int
        :type y3: int
        :type x: int
        :type y: int
        :return:
        """
        # Calculate area of triangle ABC
        A = self.area(x1, y1, x2, y2, x3, y3)
        # Calculate area of triangle PBC
        A1 = self.area(x, y, x2, y2, x3, y3)
        # Calculate area of triangle PAC
        A2 = self.area(x1, y1, x, y, x3, y3)
        # Calculate area of triangle PAB
        A3 = self.area(x1, y1, x2, y2, x, y)

        # Check if sum of A1, A2 and A3 is same as A
        return A == A1 + A2 + A3

    def area(self, x1, y1, x2, y2, x3, y3):
        """
        A utility function to calculate area of triangle formed by (x1, y1),
        (x2, y2) and (x3, y3)
        :param x1: int
        :param y1: int
        :param x2: int
        :param y2: int
        :param x3: int
        :param y3: int
        :return:
        """
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

if __name__ == '__main__':
    # Let us check whether the point P(10, 15) lies inside the triangle
    #   formed by A(0, 0), B(20, 0) and C(10, 30)
    pit = PointInsideTraingle()
    print("Inside" if pit.is_inside(0, 0, 20, 0, 10, 30, 10, 15) else "Not inside")
