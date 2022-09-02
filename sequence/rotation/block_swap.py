""" Block swap algorithm for array rotation

Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
[1, 2, 3, 4, 5, 6, 7 ]

Rotation of the above array by 2 will make array
[3, 4, 5, 6, 7, 1, 2]  """
from __future__ import print_function


class BlockSwap(object):
    def left_rotate_rec(self, arr, d, n, start=0):
        """
        Initialize A = arr[0..d-1] and B = arr[d..n-1]

        1) Do following until size of A is equal to size of B
            a) If A is shorter, divide B into Bl and Br such that Br is of same length as A.
            Swap A and Br to change ABlBr into BrBlA. Now A is at its final place, so recur on
            pieces of B.
            b) If A is longer, divide A into Al and Ar such that Al is of same length as B Swap Al
            and B to
            change AlArB into BArAl. Now B is at its final place, so recur on pieces of A.
        2)  Finally when A and B are of equal size, block swap them

        Time Complexity: O(n)

        """
        # Return If number of elements to be rotated is zero or equal to array size
        if d == 0 or d == n:
            return None

        # If number of elements to be rotated is exactly half of array size
        if n - d == d:
            self.swap(arr, start, n - d, d)
            return

        # If A is shorter
        if d < n - d:
            self.swap(arr, start, n - d, d)
            self.left_rotate_rec(arr, d, n - d, start)

        # If B is shorter
        else:
            self.swap(arr, start, d, n - d)
            self.left_rotate_rec(arr, 2 * d - n, d, start + n - d)  # This is tricky

    def swap(self, arr, fi, si, d):
        """
        :param arr: List[int]
        :param fi: int
        :param si: int
        :param d: int
        :return:
        """
        for i in range(d):
            temp = arr[fi + i]
            arr[fi + i] = arr[si + i]
            arr[si + i] = temp

    def left_rotate_iter(self, arr, d, n):
        """
        Initialize A = arr[0..d-1] and B = arr[d..n-1]

        1) Do following until size of A is equal to size of B
            a) If A is shorter, divide B into Bl and Br such that Br is of same length as A.
                Swap A and Br to change ABlBr into BrBlA. Now A is at its final place, so recur on
                pieces of B.
            b) If A is longer, divide A into Al and Ar such that Al is of same length as B Swap Al
                and B to change AlArB into BArAl. Now B is at its final place, so recur on pieces
                of A.
        2)  Finally when A and B are of equal size, block swap them

        Time Complexity: O(n)

        """
        if d == 0 or d == n:
            return
        i = d
        j = n - d
        while i != j:
            if i < j:  # A is shorter
                self.swap(arr, d - i, d + j - i, i)
                j -= i
            else:  # B is shorter
                self.swap(arr, d - i, d, j)
                i -= j

        # Finally, block swap A and B
        self.swap(arr, d - i, d, i)


if __name__ == '__main__':
    # Output:  [3, 4, 5, 6, 7, 1, 2]

    block_swap = BlockSwap()
    arr = [1, 2, 3, 4, 5, 6, 7]
    arr1 = arr[:]
    arr2 = arr[:]
    block_swap.left_rotate_iter(arr2, 2, 7)
    print("\nIterative method to swap block", arr2)

    block_swap.left_rotate_rec(arr1, 2, 7)
    print("\nRecursive method to swap block", arr1)
