"""
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest
subsequence of a given sequence such that all elements of the subsequence are sorted in
increasing order. For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and
LIS is {10, 22, 33, 50, 60, 80}.

Examples:
Input  : arr[] = {3, 10, 2, 1, 20}
Output : Length of LIS = 3
The longest increasing subsequence is 3, 10, 20

Input  : arr[] = {3, 2}
Output : Length of LIS = 1
The longest increasing subsequences are {3} and {2}

Input : arr[] = {50, 3, 10, 7, 40, 80}
Output : Length of LIS = 4
The longest increasing subsequence is {3, 7, 40, 80}

----------------------------------
Explanation:
----------------------------------
To make use of recursive calls, this function must return two things:
1) Length of LIS ending with element arr[n-1]. We use max_ending_here for this purpose
2) Overall maximum, as the LIS may end with an element before arr[n-1] is used as *maximum*
for this purpose. The value of LIS of full array of size n is stored in variable *maximum*
which is our final result

-----------------------------------
Optimal Substructure:
-----------------------------------
Let arr[0..n-1] be the input array and L(i) be the length of the LIS ending at index i such that
arr[i] is the last element of the LIS.
Then, L(i) can be recursively written as:
L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
L(i) = 1, if no such j exists.

To find the LIS for a given array, we need to return max(L(i)) where 0 < i < n.
Thus, we see the LIS problem satisfies the optimal substructure property as the main problem can be
solved using solutions to subproblems.

------------------------------------
Overlapping Subproblems:
------------------------------------
Considering the above implementation, following is recursion tree for an array of size 4. lis(n)
gives us the length of LIS for arr[].

                lis(4)
            /           \ 
          lis(3)        lis(2) lis(1)
         /              /
       lis(2) lis(1) lis(1)
       /
    lis(1)

We can see that there are many subproblems which are solved again and again. So this problem has
Overlapping Substructure property and re-computation of same subproblems can be avoided by either
using Memoization or Tabulation. Following is a tabulated implementation for the LIS problem.

Note that the time complexity of the above Dynamic Programming (DP) solution is O(n^2) and there
is a O(nLogn) solution for the LIS problem. We have not discussed the O(n Log n) solution here as
the purpose of this post is to explain Dynamic Programming with a simple example.

See below post for O(n Log n) solution.
http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
"""
import sys
from typing import List, Tuple
from functools import lru_cache


def lis(nums: List[int]) -> int:

    @lru_cache(maxsize=None)
    def lengthof_lis_utils(nums: Tuple[int], prev: int, curr: int):
        if curr == len(nums): return 0
        taken = 0
        if nums[curr] > prev:
            taken = 1 + lengthof_lis_utils(nums, nums[curr], curr + 1)
        not_taken = lengthof_lis_utils(nums, prev, curr + 1)
        return max(taken, not_taken)
    
    return lengthof_lis_utils(tuple(nums), -sys.maxsize, 0)

def lis_dp(arr):
    """
    Dynamic programming Python implementation of LIS problem lis returns length of the
    longest increasing subsequence in arr of size n

    :param arr: List[int]
    :return: int
    """
    n = len(arr)
    # Declare the list (arr) for LIS and initialize LIS values for all indexes
    lis = [1] * n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Initialize maximum to 0 to get the maximum of all LIS and Pick maximum of all LIS values
    return max(lis)

def lis_monoqueue(arr: List[int]) -> int:
    st = []
    rt = len(arr) - 1
    lis = 0
    while rt != -1:
        while len(st) != 0 and arr[rt] >= st[-1]:
            lis = max(len(st), lis)
            st.pop()
        
        st.append(arr[rt])
        rt -= 1
    return max(lis, len(st))


if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    # arr = [50, 3, 10, 7, 40, 80]
    # arr = [3, 10, 2, 1, 20]
    # print("Length of lis is", lis_dp(arr))
    print("Length of lis is", lis(arr))
    # print("Length of lis is", lis_monoqueue(arr))
