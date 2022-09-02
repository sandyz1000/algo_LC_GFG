"""
Print all combinations of points that can compose a given number
You can win three kinds of basketball points, 1 point, 2 points, and 3 points.
Given a total score n, print out all the combination to compose n.

Examples:
- - - - - - - - - - - - - - - - - - - - - - - - - - - +
    For n = 1, the program should print following:
    1

    For n = 2, the program should print following:
    1 1
    2

    For n = 3, the program should print following:
    1 1 1
    1 2
    2 1
    3

    For n = 4, the program should print following:
    1 1 1 1
    1 1 2
    1 2 1
    1 3
    2 1 1
    2 2
    3 1

    and so on ...

- - - - - - - - - - - - - - - - - - - - - - - - - - - +
"""


# Python program to Print all combinations of points that can compose a given number

class GFG:
    """
    Algorithm:

    1. At first position we can have three numbers 1 or 2 or 3.
    2. First put 1 at first position and recursively call for n-1.
    3. Then put 2 at first position and recursively call for n-2.
    4. Then put 3 at first position and recursively call for n-3.
    5. If n becomes 0 then we have formed a combination that compose n, so print the current
    combination.

    Below is a generalized implementation. In the below implementation, we can change MAX_POINT if
    there are higher points (more than 3) in the basketball game.
    """

    def print_compositions(self, arr, n, i):
        """
        Function prints all combinations of numbers 1, 2, ...MAX_POINT that sum up to n.
        i is used in recursion keep track of index in arr[] where next element is to be added.
        Initial value of i must be passed as 0
        """
        MAX_POINT = 3
        if n == 0:
            print(arr[:i])

        elif n > 0:
            for k in range(1, MAX_POINT + 1):
                arr[i] = k
                self.print_compositions(arr, n - k, i + 1)


if __name__ == '__main__':
    test = GFG()
    n = 5
    size = 100
    arr = [0] * size
    print("Different compositions formed by 1, 2 and 3 of %d are " % n,
          test.print_compositions(arr, n, 0))
