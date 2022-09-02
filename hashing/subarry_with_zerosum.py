"""

Print all subarrays with 0 sum
Given an array, print all subarrays in the array which has sum 0.

------------------------------------------------------------
Examples:
------------------------------------------------------------

Input:  arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]

Output:
Subarray found from Index 2 to 4
Subarray found from Index 2 to 6
Subarray found from Index 5 to 6
Subarray found from Index 6 to 9
Subarray found from Index 0 to 10

-------------------------------------------------------------

Find subarray with given sum | Set 1 (Nonnegative Numbers)
Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given
number.

Examples:

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Ouptut: Sum found between indexes 1 and 4

Input: arr[] = {1, 4}, sum = 0
Output: No subarray found
-------------------------------------------------------------

Find subarray with given sum | Set 2 (Handles Negative Numbers)

Given an unsorted array of integers, find a subarray which adds to a given number. If there are
more than one subarrays with sum as the given number, print any of them.

Examples:

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4

Input: arr[] = {10, 2, -2, -20, 10}, sum = -10
Ouptut: Sum found between indexes 0 to 3

Input: arr[] = {-10, 0, 2, -2, -20, 10}, sum = 20
Ouptut: No subarray with given sum exists

"""
from collections import namedtuple, defaultdict

# Python program to print all subarrays in the array which has sum 0

Pair = namedtuple('Pair', ('first', 'second',))


class SubArrayZeroSum:
    def find_sub_arrays(self, arr, n):
        """
        Explanation:-

        A simple solution is to consider all subarrays one by one and check if sum of every
        subarray is equal to 0 or not. The complexity of this solution would be O(n^2).

        A better approach is to use Hashing.

        Do following for each element in the array:
        1.  Maintain sum of elements encountered so far in a variable (say summation).
        2.  If current sum is 0, we found a subarray starting from index 0 and ending at index
            current_index
        3.  Check if current sum exists in the hash table or not.
        4.  If current sum exists in the hash table, that means we have subarray(s) present with
            0 sum that ends at current_index.
        5.  Insert current sum into the hash table

        Function to print all subarrays in the array which has sum 0
        """
        # create an empty map
        hmap = defaultdict(list)
        # create an empty vector of pairs to store subarray starting and ending index
        out = []
        summation = 0  # Maintains sum of elements so far
        for i in range(n):
            summation += arr[i]  # add current element to sum

            # if sum is 0, we found a subarray starting from index 0 and ending at index i
            if summation == 0:
                out.append(Pair(0, i))

            # If sum already exists in the map there exists at-least one subarray ending at
            # index i with 0 sum
            if summation in hmap:
                vc = hmap[summation]  # map[sum] stores starting index of all subarrays
                for it in vc:
                    out.append(Pair(it + 1, i))

            hmap[summation].append(i)  # Important - no else

        return out  # return output vector

    def printer(self, out):
        """
        Utility function to print all subarrays with sum 0
        :param out:
        :return:
        """
        for it in out:
            print("Subarray found from Index %d to %d" % (it.first, it.second))


class SubArrayGivenSumm:
    """Find subarray with given sum | Set 1 (Non-negative Numbers)

    Method 1 (Simple)
    A simple solution is to consider all subarrays one by one and check the sum of every subarray.
    Following program implements the simple solution. We run two loops: the outer loop picks a
    starting point i and the inner loop tries all subarrays starting from i.

    # Time Complexity: O(n^2) in worst case.
    """

    def sub_array_sum_method(self, arr, n, summation):
        """Returns true if the there is a subarray of arr[] with sum equal to 'sum'
            otherwise returns false.  Also, prints the result
        """
        # Pick a starting point
        for i in range(n):
            curr_sum = arr[i]
            # try all subarrays starting with 'i'
            for j in range(i + 1, n + 1):
                if curr_sum == summation:
                    p = j - 1
                    print("Sum found between indexes %d and %d" % (i, p))
                    return 1

                if curr_sum > summation or j == n:
                    break
                curr_sum = curr_sum + arr[j]

        print("No subarray found")
        return 0


class SubArrayGivenSummEffi:
    """Find subarray with given sum | Set 1 (Non-negative Numbers)

    Method 2 (Efficient) Initialize a variable curr_sum as first element. curr_sum indicates the
    sum of current subarray. Start from the second element and add all elements one by one to the
    curr_sum. If curr_sum becomes equal to sum, then print the solution. If curr_sum exceeds the
    sum, then remove trailing elements while curr_sum is greater than sum.

    Time complexity of method 2 looks more than O(n), but if we take a closer look at the
    program, then we can figure out the time complexity is O(n). We can prove it by counting
    the number of operations performed on every element of arr[] in worst case. There are at
    most 2 operations performed on every element: (a) the element is added to the curr_sum (b)
    the element is subtracted from curr_sum. So the upper bound on number of operations is 2n
    which is O(n).
    """

    def sub_array_sum_method(self, arr, n, summation):
        """Returns true if the there is a subarray of arr[] with sum equal to 'sum' otherwise
        returns false.  Also, prints the result"""
        curr_sum = arr[0]
        start = 0

        for i in range(1, n + 1):
            # If curr_sum exceeds the sum, then remove the starting elements
            while curr_sum > summation and start < i - 1:
                curr_sum = curr_sum - arr[start]
                start += 1

            # If curr_sum becomes equal to sum, then return true
            if curr_sum == summation:
                p = i - 1
                print("Sum found between indexes %d and %d" % (start, p))
                return 1

            if i < n:  # Add this element to curr_sum
                curr_sum = curr_sum + arr[i]

        print("No subarray found")
        return 0


class SubArrayGivenSumNegative:
    """
    Method-3
    Find subarray with given sum | Set 2 (Handles Negative Numbers)

    A simple solution is to consider all subarrays one by one and check if sum of every subarray is
    equal to given sum or not. The complexity of this solution would be O(n^2).

    An efficient way is to use a map. The idea is to maintain sum of elements encountered so far in
    a variable (say curr_sum). Let the given number is sum. Now for each element, we check if
    curr_sum - sum exists in the map or not. If we found it in the map that means, we have a
    subarray present with given sum, else we insert curr_sum into the map and proceed to next
    element. If all elements of the array are processed and we didn't find any subarray with given
    sum, then subarray doesn't exists.

    Time complexity of above solution is O(n) as we are doing only one traversal of the array.
    Auxiliary space used by the program is O(n).
    """

    # Python program to print subarray with sum as given sum

    def sub_array_sum_method(self, arr, n, summation):
        """Function to print subarray with sum as given sum"""
        # create an empty map
        hmap = {}
        # Maintains sum of elements so far
        curr_sum = 0

        for i in range(n):
            # add current element to curr_sum
            curr_sum = curr_sum + arr[i]

            # if curr_sum is equal to target sum we found a subarray starting from index 0
            # and ending at index i
            if curr_sum == summation:
                print("Sum found between indexes 0 to %s " % i)
                return
            # If curr_sum - sum already exists in map we have found a subarray with target sum
            if (curr_sum - summation) in hmap:
                print("Sum found between indexes %s to %s ", (hmap[curr_sum - summation] + 1, i))
                return
            hmap[curr_sum] = i

        # If we reach here, then no subarray exists
        print("No subarray with given sum exists")


if __name__ == '__main__':
    # Output:
    # Subarray found from Index 2 to 4
    # Subarray found from Index 2 to 6
    # Subarray found from Index 5 to 6
    # Subarray found from Index 6 to 9
    # Subarray found from Index 0 to 10

    print("\n ----- Method-0 ------ ")
    summ = SubArrayZeroSum()
    arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
    n = len(arr)
    out = summ.find_sub_arrays(arr, n)

    # if we didn't find any subarray with 0 sum, then subarray doesn't exists
    if len(out) == 0:
        print("No sub-array exists")
    else:
        print(summ.printer(out))

    print("\n -----Method-1 ------ ")
    # Output: Sum found between indexes 1 and 4
    summ = SubArrayGivenSumm()
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    n = len(arr)
    summation = 23
    summ.sub_array_sum_method(arr, n, summation)

    print("\n ------ Method-2 ------")
    # Output: Sum found between indexes 1 and 4
    summ = SubArrayGivenSummEffi()
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    n = len(arr)
    summation = 23
    summ.sub_array_sum_method(arr, n, summation)

    print("\n ------- Method-3 ------")
    # Output: Sum found between indexes 0 to 3
    summ = SubArrayGivenSumNegative()
    arr = [10, 2, -2, -20, 10]
    n = len(arr)
    summation = -10
    summ.sub_array_sum_method(arr, n, summation)
