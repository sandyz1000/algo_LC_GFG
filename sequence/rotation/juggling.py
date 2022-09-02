"""
Program for array rotation
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

----------------------------------------
Example:
----------------------------------------
Input: [1, 2, 3, 4, 5, 6, 7]
Output: [3, 4, 5, 6, 7, 1, 2]

"""
import typing


class Rotation:
    """
    Function to left Rotate arr[] of size n by 1
    Time complexity: O(n*d)
    Auxiliary Space: O(1)
    """

    def left_rotate(self, arr: typing.List[int], d: int, n: int):
        """
        Function to left rotate arr[] of size n by d
        :param arr: List[int]
        :param d: int
        :param n: int
        :return:
        """
        for i in range(d):
            self.left_rotateby_one(arr, n)

    def left_rotateby_one(self, arr, n):
        """
        :param n:
        :return:
        """
        i, temp = 0, arr[0]
        while i < n - 1:
            arr[i] = arr[i + 1]
            i += 1
        arr[i] = temp


class JugglingAlgorithm:
    """
    Instead of moving one by one, divide the array in different sets where number of sets is
    equal to GCD of n and d and move the elements within sets. If GCD is 1 as it is for the above
    example array (n = 7 and d =2), then elements will be moved within one set only,
    we just start with temp = arr[0] and keep moving arr[I+d] to arr[I] and finally store temp at
    the right place.

    Here is an example for n =12 and d = 3. GCD is 3 and

    Let arr[] be {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    a)	Elements are first moved in first set arr[]
        after this step --> {4 2 3 7 5 6 10 8 9 1 11 12}

    b)	Then in second set.
        arr[] after this step --> {4 5 3 7 8 6 10 11 9 1 2 12}

    c)	Finally in third set.
        arr[] after this step --> {4 5 6 7 8 9 10 11 12 1 2 3}

    Time complexity: O(n)
    Auxiliary Space: O(1)
    """

    def left_rotate(self, arr: typing.List[int], d: int, n: int):
        """
        Function to left rotate arr[] of siz n by d """
        for i in range(self.gcd(d, n)):
            # move i-th values of blocks
            temp = arr[i]
            j = i
            while True:
                k = j + d
                if k >= n:
                    k = k - n  # Wrap around
                if k == i:
                    break
                arr[j] = arr[k]
                j = k
            arr[j] = temp

    def gcd(self, a: int, b: int):
        """
        Function to get gcd of a and b """
        return a if b == 0 else self.gcd(b, a % b)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("\n Method -1: Rotate one by one: ---")
    test = Rotation()
    test.left_rotate(arr, 2, len(arr))
    print(arr)

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("\n Method -2: Juggling algorithm ---")
    test = JugglingAlgorithm()
    test.left_rotate(arr, 2, len(arr))
    print(arr)
