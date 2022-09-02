""" Minimum time required to rot all oranges

Given a matrix of dimension m*n where each cell in the matrix can have values 0, 1 or 2 which has
the following meaning:

0: Empty cell
1: Cells have fresh oranges
2: Cells have rotten oranges

So we have to determine what is the minimum time required so that all the oranges become rotten. A
rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1],
[i,j+1] (up, down, left and right). If it is impossible to rot every orange then simply return -1.

Examples:

Input:  arr = [{2, 1, 0, 2, 1},
                {1, 0, 1, 2, 1},
                {1, 0, 0, 2, 1}]
Output:
All oranges can become rotten in 2 time frames.


Input:  arr = [{2, 1, 0, 2, 1},
                {0, 0, 1, 2, 1},
                {1, 0, 0, 2, 1}]

Output: All oranges cannot be rotten."""

from __future__ import print_function
from collections import deque


# Python program to find minimum time required to make all oranges rotten
class Ele:
    """structure for storing coordinates of the cell"""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class RotOrange:
    R = 3
    C = 5

    @staticmethod
    def is_valid(i, j):
        """function to check whether a cell is valid / invalid"""
        return 0 <= i < RotOrange.R and RotOrange.R > 0 <= j < RotOrange.C

    @staticmethod
    def is_delim(temp):
        """Function to check whether the cell is delimiter which is (-1, -1)"""
        return temp.x == -1 and temp.y == -1

    @staticmethod
    def check_all(arr):
        """Function to check whether there is still a fresh orange remaining"""
        for i in range(RotOrange.R):
            for j in range(RotOrange.C):
                if arr[i][j] == 1:
                    return True
        return False

    @staticmethod
    def rot_oranges(arr):
        """This function finds if it is possible to rot all oranges or not. If possible, then
        it returns minimum time required to rot all, otherwise returns -1"""
        # Create a queue of cells
        Q = deque()
        # temp = Ele
        ans = 0
        # Store all the cells having rotten orange in first time frame
        for i in range(RotOrange.R):
            for j in range(RotOrange.C):
                if arr[i][j] == 2:
                    Q.append(Ele(i, j))

        # Separate these rotten oranges from the oranges which will rotten due the oranges in
        # first time frame using delimiter which is (-1, -1)
        Q.append(Ele(-1, -1))

        # Process the grid while there are rotten oranges in the Queue
        while Q:
            # This flag is used to determine whether even a single fresh orange gets rotten due
            # to rotten oranges in current time frame so we can increase the count of the
            # required time.
            flag = False

            # Process all the rotten oranges in current time frame.
            while not RotOrange.is_delim(Q[0]):
                temp = Q[0]

                # Check right adjacent cell that if it can be rotten
                if RotOrange.is_valid(temp.x + 1, temp.y + 1) and arr[temp.x + 1][temp.y] == 1:
                    if not flag:
                        # if this is the first orange to get rotten, increase count and
                        # set the flag.
                        ans += 1
                        flag = True
                    # Make the orange rotten
                    arr[temp.x + 1][temp.y] = 2

                    # push the adjacent orange to Queue
                    temp.x += 1
                    Q.append(Ele(temp.x, temp.y))

                    # Move back to current cell
                    temp.x -= 1

                # Check left adjacent cell that if it can be rotten
                if RotOrange.is_valid(temp.x - 1, temp.y) and arr[temp.x - 1][temp.y] == 1:
                    if not flag:
                        ans += 1
                        flag = True
                    arr[temp.x - 1][temp.y] = 2
                    temp.x -= 1
                    Q.append(Ele(temp.x, temp.y))  # push this cell to Queue
                    temp.x += 1

                # Check top adjacent cell that if it can be rotten
                if RotOrange.is_valid(temp.x, temp.y + 1) and arr[temp.x][temp.y + 1] == 1:
                    if not flag:
                        ans += 1
                        flag = True
                    arr[temp.x][temp.y + 1] = 2
                    temp.y += 1
                    Q.append(Ele(temp.x, temp.y))  # Push this cell to Queue
                    temp.y -= 1

                # Check bottom adjacent cell if it can be rotten
                if RotOrange.is_valid(temp.x, temp.y - 1) and arr[temp.x][temp.y - 1] == 1:
                    if not flag:
                        ans += 1
                        flag = True
                    arr[temp.x][temp.y - 1] = 2
                    temp.y -= 1
                    Q.append(Ele(temp.x, temp.y))  # push this cell to Queue
                Q.popleft()

            # Pop the delimiter
            Q.popleft()

            # If oranges were rotten in current frame than separate the rotten oranges using
            # delimiter for the next frame for processing.
            if Q:
                Q.append(Ele(-1, -1))
            # If Queue was empty than no rotten oranges left to process so exit

        # Return -1 if all arranges could not rot, otherwise -1.s
        return -1 if (RotOrange.check_all(arr)) else ans


if __name__ == '__main__':
    # Output: Time required for all oranges to rot = 2
    test = RotOrange()
    arr = [[2, 1, 0, 2, 1],
           [1, 0, 1, 2, 1],
           [1, 0, 0, 2, 1]]
    ans = test.rot_oranges(arr)
    if ans == -1:
        print("All oranges cannot rot")
    else:
        print("Time required for all oranges to rot = %d " % ans)
