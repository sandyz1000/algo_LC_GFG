"""
Find the largest subarray with 0 sum
Given an array of integers, find length of the largest subarray with sum equals to 0.

Examples:

Input: arr = [15, -2, 2, -8, 1, 7, 10, 23];
Output: 5
The largest subarray with 0 sum is -2, 2, -8, 1, 7

Input: arr = [1, 2, 3]
Output: 0
There is no subarray with 0 sum

Input: arr = [1, 0, 3]
Output: 1


Method-1:
---------
A simple solution is to consider all subarrays one by one and check the sum of every subarray.
We can run two loops: the outer loop picks a starting point i and the inner loop tries all
subarrays starting from i. Time complexity of this method is O(n^2).


---------------------------------------------------
Method-2 Explanation:
---------------------------------------------------

We can Use Hashing to solve this problem in O(n) time. The idea is to iterate through the
array and for every element arr[i], calculate sum of elements form 0 to i (this can simply be
done as sum += arr[i]). If the current sum has been seen before, then there is a zero sum
array. Hashing is used to store the sum values, so that we can quickly store sum and find
out whether the current sum is seen before or not.

Time Complexity of this solution can be considered as O(n) under the assumption that we have
good hashing function that allows insertion and retrieval operations in O(1) time.

"""
import typing


# A python program to find maximum length subarray with 0 sum in o(n) time
def maxLen(arr: typing.List[int]):
    # Method -1

    max_len = 0  # initialize result
    for i in range(len(arr)):
        # initialize sum for every starting point
        curr_sum = 0
        # try all subarrays starting with 'i'
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            # if curr_sum becomes 0, then update max_len
            if curr_sum == 0:
                max_len = max(max_len, j - i + 1)

    return max_len


def maxlen_hashing(arr: typing.List[int]):
    """ Returns the maximum length
    """
    # NOTE: Dictionary in python in implemented as Hash Maps
    # Create an empty hash map (dictionary)
    hash_map = {}
    max_len = 0  # Initialize result
    curr_sum = 0  # Initialize sum of elements
    # Traverse through the given array
    for i in range(len(arr)):
        # Add the current element to the sum
        curr_sum += arr[i]
        if arr[i] == 0 and max_len == 0:
            max_len = 1
        if curr_sum == 0:
            max_len = i + 1

        # NOTE: 'in' operation in dictionary to search key takes O(1)
        # Look if current sum is seen before
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:
            # else put this sum in dictionary
            hash_map[curr_sum] = i

    return max_len


if __name__ == '__main__':
    # Length of the longest 0 sum subarray is 5
    arr = [15, -2, 2, -8, 1, 7, 10, 13]
    # arr = [0, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 0, 1, 1, 1, 1, 1, 1]

    print("Length of the longest 0 sum subarray is %d" % maxLen(arr))
    print("Length of the longest 0 sum subarray (hashing) is %d" % maxlen_hashing(arr))
