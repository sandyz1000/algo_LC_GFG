"""
Number of cells a queen can move with obstacles on the chessboard
http://www.geeksforgeeks.org/number-cells-queen-can-move-obstacles-chessborad/

Consider a N X N chessboard with a Queen and K obstacles. The Queen cannot pass through obstacles.
Given the position (x, y) of Queen, the task is to find the number of cells the queen can move

"""
from collections import namedtuple

Pair = namedtuple('Pair', ('first', 'second', ))


class QueenMove(object):
    """
    Method 1:

    The idea is to iterate over the cells the queen can attack and stop until there is an
    obstacle or end of the board. To do that, we need to iterate horizontally, vertically and
    diagonally.
    The moves from position (x, y) can be:
    (x+1, y): one step horizontal move to the right.
    (x-1, y): one step horizontal move to the left.
    (x+1, y+1): one step diagonal move up-right.
    (x-1, y-1): one step diagonal move down-left.
    (x-1, y+1): one step diagonal move left-up.
    (x+1, y-1): one step diagonal move right-down.
    (x, y+1): one step upward.
    (x, y-1): one step downward.

    Below is Python implementation of this approach:
    Python program to find number of cells a queen can move with obstacles on the chessboard"""

    def check(self, n, x, y, xx, yy, mp):
        # Return if position is valid on chessboard
        ranged = (lambda n, x, y: n >= x > 0 and n >= y > 0)
        ans = 0
        # Checking valid move of Queen in a direction.
        while ranged(n, x, y) and Pair(x, y) not in mp:
            x += xx
            y += yy
            ans += 1

        return ans

    def numberof_position_method(self, n, k, x, y, obst_posx, obst_posy):
        """Return the number of position a Queen can move."""
        x1, y1, ans = 0, 0, 0
        mp = {}

        # Mapping each obstacle's position
        while k:
            k -= 1
            x1 = obst_posx[k]
            y1 = obst_posy[k]
            mp[Pair(x1, y1)] = 1

        # Fetching number of position a queen can move in each direction.
        ans += self.check(n, x + 1, y, 1, 0, mp)
        ans += self.check(n, x - 1, y, -1, 0, mp)
        ans += self.check(n, x, y + 1, 0, 1, mp)
        ans += self.check(n, x, y - 1, 0, -1, mp)
        ans += self.check(n, x + 1, y + 1, 1, 1, mp)
        ans += self.check(n, x + 1, y - 1, 1, -1, mp)
        ans += self.check(n, x - 1, y + 1, -1, 1, mp)
        ans += self.check(n, x - 1, y - 1, -1, -1, mp)

        return ans


class QueenMove2(object):
    """
    Method 2:
    The idea is to iterate over the obstacles and for those who are in the queen's path,
    we calculate the free cells upto that obstacle. If there is no obstacle in the path we have to
    calculate the number of free cells upto end of board in that direction.

    For any (x1, y1) and (x2, y2):
    If they are horizontally at same level: abs(x1 - x2 - 1)
    If they are vertically at same level: abs(y1 - y2 - 1) is the number of free cells between.
    If they are diagonal: both abs(x1 - x2 - 1) or abs(y1 - y2 - 1) is the number of free cells
    between.

    Python program to find number of cells a queen can move with obstacles on the chessboard"""

    @staticmethod
    def numberof_position_method(n, k, x, y, obst_posx, obst_posy):
        """
        Return the number of position a Queen can move.
        :param n: int
        :param k: int
        :param x: int
        :param y: int
        :param obst_posx: list(int)
        :param obst_posy: list(int)
        :return:
        """
        # d11, d12, d21, d22 are for diagonal distances.
        # r1, r2 are for vertical distance.
        # c1, c2 are for horizontal distance.

        d11 = min(x - 1, y - 1)
        d12 = min(n - x, n - y)
        d21 = min(n - x, y - 1)
        d22 = min(x - 1, n - y)

        r1 = y - 1
        r2 = n - y
        c1 = x - 1
        c2 = n - x

        # For each obstacle find the minimum distance. If obstacle is present in any direction,
        # distance will be updated.
        for i in range(k):
            if x > obst_posx[i] and y > obst_posy[i] and x - obst_posx[i] == y - obst_posy[i]:
                d11 = min(d11, x - obst_posx[i] - 1)

            if obst_posx[i] > x and obst_posy[i] > y and obst_posx[i] - x == obst_posy[i] - y:
                d12 = min(d12, obst_posx[i] - x - 1)

            if obst_posx[i] > x and y > obst_posy[i] and obst_posx[i] - x == y - obst_posy[i]:
                d21 = min(d21, obst_posx[i] - x - 1)

            if x > obst_posx[i] and obst_posy[i] > y and x - obst_posx[i] == obst_posy[i] - y:
                d22 = min(d22, x - obst_posx[i] - 1)

            if x == obst_posx[i] and obst_posy[i] < y:
                r1 = min(r1, y - obst_posy[i] - 1)

            if x == obst_posx[i] and obst_posy[i] > y:
                r2 = min(r2, obst_posy[i] - y - 1)

            if y == obst_posy[i] and obst_posx[i] < x:
                c1 = min(c1, x - obst_posx[i] - 1)

            if y == obst_posy[i] and obst_posx[i] > x:
                c2 = min(c2, obst_posx[i] - x - 1)

        return d11 + d12 + d21 + d22 + r1 + r2 + c1 + c2


if __name__ == '__main__':
    test1 = QueenMove()
    test2 = QueenMove2()
    n = 8  # Chessboard size
    k = 1  # Number of obstacles
    qposx = 4  # Queen x position
    qposy = 4  # Queen y position
    obst_posx = [3]  # x position of obstacles
    obst_posy = [5]  # y position of obstacles

    print("\n---- Method-1------")
    print(test1.numberof_position_method(n, k, qposx, qposy, obst_posx, obst_posy))

    print("\n---- Method-2------")
    print(test2.numberof_position_method(n, k, qposx, qposy, obst_posx, obst_posy))
