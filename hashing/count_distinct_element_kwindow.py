"""
Count distinct elements in every window of size k
Given an array of size n and an integer k, return the of count of distinct numbers in all windows
of size k.

==Example:==

- - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - +
Input:  arr = {1, 2, 1, 3, 4, 2, 3}, k = 4
Output:
3
4
4
3

==Explanation:==

First window is {1, 2, 1, 3}, count of distinct numbers is 3
Second window is {2, 1, 3, 4} count of distinct numbers is 4
Third window is {1, 3, 4, 2} count of distinct numbers is 4
Fourth window is {3, 4, 2, 3} count of distinct numbers is 3
- - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - +
"""


class CountDistinct:
    """
    Simple Python program to count distinct elements in every window of size k

    A Simple Solution is to traverse the given array, consider every window in it and count
    distinct elements in the window. Below is implementation of simple solution

    Time complexity of the above solution is O(nk^2). We can improve time complexity to O(nkLogk) by
    modifying countWindowDistinct() to use sorting. The function can further be optimized to
    use hashing to find distinct elements in a window. With hashing the time complexity becomes
    O(nk). Below is a different approach that works in O(n) time.

    """

    def count_window_distinct(self, win, k):
        """
        Counts distinct elements in window of size k
        :param win: list(int)
        :param k: int
        :return:
        """
        dist_count = 0

        # Traverse the window
        for i in range(k):
            # Check if element arr[i] exists in arr[0..i-1]
            j = 0
            while j < i:
                if win[i] == win[j]:
                    break
                j += 1
            if j == i:
                dist_count += 1
        return dist_count

    def count_distinct(self, arr, n, k):
        """Counts distinct elements in all windows of size k"""
        # Traverse through every window
        for i in range(n - k + 1):
            print(self.count_window_distinct(arr[i:n], k))


class CountDistinct2:
    """
    An Efficient Solution is to use the count of previous window, while sliding the window. The
    idea is to create a hash map that stores elements of current widow. When we slide the window,
    we remove an element from hash and add an element. We also keep track of distinct elements.

    Below is algorithm.
    1) Create an empty hash map. Let hash map be hM
    2) Initialize distinct element count 'dist_count' as 0.
    3) Traverse through first window and insert elements of first window to hM. The elements are
    used as key and their counts as value in hM. Also keep updating ‘dist_count’
    4) Print 'dist_count' for first window.
    5) Traverse through remaining array (or other windows).
      a) Remove the first element of previous window.
      If the removed element appeared only once remove it from hM and do "dist_count–"
      Else (appeared multiple times in hM) decrement its count in hM

      b) Add the current element (last element of new window)
      If the added element is not present in hM add it to hM and do "dist_count++"
      Else (the added element appeared multiple times) increment its count in hM

    Time complexity of the above solution is O(n).
    """
    @staticmethod
    def count_distinct(arr, n, k):
        # Creates an empty hashmap hm
        hm = {}

        # initialize distinct element count for current window
        dist_count = 0

        # Traverse the first window and store count of every element in hash map
        for i in range(k):
            if arr[i] not in hm:
                hm[arr[i]] = 1
                dist_count += 1
            else:
                hm[arr[i]] += 1

        # Print count of first window
        print(dist_count)

        # Traverse through the remaining array
        for i in range(k, n):
            # Remove first element of previous window
            # If there was only one occurrence, then reduce distinct count.
            if hm[arr[i - k]] == 1:
                del hm[arr[i - k]]
                dist_count -= 1
            else:  # reduce count of the removed element
                hm[arr[i - k]] -= 1

            # Add new element of current window If this element appears first time, increment
            # distinct element count
            if arr[i] not in hm:
                hm[arr[i]] = 1
                dist_count += 1
            else:  # Increment distinct element count
                hm[arr[i]] += 1
            print(dist_count)  # Print count of current window


if __name__ == '__main__':
    arr = [1, 2, 1, 3, 4, 2, 3]
    k = 4
    n = len(arr)
    print("Method-1: Count distinct elements in every window of size k")
    test = CountDistinct()
    test.count_distinct(arr, n, k)

    print("\nMethod-2: Count distinct elements in every window of size k")
    test = CountDistinct2()
    test.count_distinct(arr, n, k)
