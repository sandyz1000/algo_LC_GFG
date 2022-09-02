"""
We have discussed Backtracking and Knight's tour problem in Set 1. Let us discuss Rat in a
Maze as another example problem that can be solved using Backtracking.

A Maze is given as N*N binary matrix of blocks where source block is the upper left most block
i.e., maze[0][0] and destination block is lower rightmost block i.e., maze[N-1][N-1]. A rat
starts from source and has to reach destination. The rat can move only in two directions: forward
and down.

In the maze matrix, 0 means the block is dead end and 1 means the block can be used in the path
from source to destination. Note that this is a simple version of the typical Maze problem. For
example, a more complex version can be that the rat can move in 4 directions and a more complex
version can be with limited number of moves.

Gray blocks are dead ends (value = 0).

                {1, 0, 0, 0}
                {1, 1, 0, 1}
                {0, 1, 0, 0}
                {1, 1, 1, 1}

All enteries in solution path are marked as 1.

                {1, 0, 0, 0}
                {1, 1, 0, 0}
                {0, 1, 0, 0}
                {0, 1, 1, 1}

"""

# Python program to solve Rat in a Maze problem using backtracking

N = 4


class RatInMaze(object):

    def is_safe(self, maze, x, y):
        """
        A utility function to check if x,y is valid index for N*N maze
        :param maze:
        :param x:
        :param y:
        :return:
        """
        return 0 <= x < N and 0 <= y < N and maze[x][y] == 1

    def solve_maze(self, maze):
        """
        This function solves the Maze problem using Backtracking. It mainly uses solveMazeUtil()
        to solve the problem. It returns false if no path is possible, otherwise return true and
        prints the path in the form of 1s. Please note that there may be more than one solutions,
        this function prints one of the feasible solutions

        :param maze: List[List[int]]
        :return:
        """
        sol = [[0 for i in range(4)] for j in range(4)]
        if not self.solve_maze_util(maze, 0, 0, sol):
            return None
        return sol

    def solve_maze_util(self, maze, x, y, sol):
        """
        A recursive utility function to solve Maze problem
        """
        if x == N - 1 and y == N - 1:
            sol[x][y] = 1
            return True

        # Check if maze[x][y] is valid
        if self.is_safe(maze, x, y):
            # mark x,y as part of solution path
            sol[x][y] = 1

            # Move forward in x direction
            if self.solve_maze_util(maze, x + 1, y, sol):
                return True

            # If moving in x direction doesn't give solution then Move down in y direction
            if self.solve_maze_util(maze, x, y + 1, sol):
                return True

            # If none of the above movements work then BACKTRACK: unmark x,y as part of solution
            # path
            sol[x][y] = 0
            return False

        return False


if __name__ == '__main__':
    rim = RatInMaze()
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]

    solution = rim.solve_maze(maze)
    if solution:
        for index, row in enumerate(solution):
            for item in row:
                print(item, end=" ")
            print("")
