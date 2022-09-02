"""
Find k numbers with most occurrences in the given array
Given an array of n numbers and a positive integer k. The problem is to find k numbers with most
occurrences, i.e., the top k numbers having the maximum frequency. If two numbers have same
frequency then the larger number should be given preference. The numbers should be displayed in
decreasing order of their frequencies. It is assumed that the array consists of k numbers with most
occurrences.

Examples:
--------
Input : arr = [3, 1, 4, 4, 5, 2, 6, 1], k = 2
Output : 4 1
Frequency of 4 = 2
Frequency of 1 = 2
These two have the maximum frequency and 4 is larger than 1.
--------------------------------------------------------
Input : arr = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], k = 4
Output : 5 11 7 10

"""

# Python implementation to find k numbers with most occurrences in the given array
from collections import defaultdict
from functools import cmp_to_key


class Pair(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def n_mostFrequentNumber(arr, n, k):
    """
    Method 1:

    Using hash table, we create a frequency table which stores the frequency of occurrence of
    each number in the given array. In the hash table we define (x, y) tuple, where x is the key(
    number) and y is its frequency in the array. Now we traverse this hash table and create an
    array freq_arr[] which stores these (number, frequency) tuples. Sort this freq_arr[] on the
    basis of the conditions defined in the problem statement. Now, print the first k numbers of
    this freq_arr[].

    function to print the k numbers with most occurrences

    Time Complexity: O(klogd) for sorting, where d is the count of distinct elements in the array.
    Auxiliary Space: O(d), where d is the count of distinct elements in the array.

    :param arr: List[int]
    :param n: int
    :param k: int
    :return:
    """
    # unordered_map 'um' implemented as frequency hash table unordered_map<int, int> um;
    um = defaultdict(int)
    for i in range(n):
        um[arr[i]] += 1

    # store the elements of 'um' in the vector 'freq_arr'
    freq_arr = [Pair(key, value) for key, value in um.items()]

    # sort the vector 'freq_arr' on the basis of the 'compare' function
    # if frequencies of two elements are same then the larger number should come first
    # sort on the basis of decreasing order of frequencies
    freq_arr.sort(key=cmp_to_key(
        lambda p1, p2: p2.first - p1.first if p1.second == p2.second else p2.second - p1.second))

    # display the the top k numbers
    print("%d numbers with most occurrences are:" % k)

    for i in range(k):
        print(freq_arr[i].first, end=" ")


if __name__ == '__main__':
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    n = len(arr)
    k = 2
    n_mostFrequentNumber(arr, n, k)
