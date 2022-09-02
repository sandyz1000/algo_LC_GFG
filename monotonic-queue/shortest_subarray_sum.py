"""
 * 862

======
Task.

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
If there is no non-empty subarray with sum at least K, return -1.

Example 1:
----------
Input: A = [1], K = 1
Output: 1

Example 2:
----------
Input: A = [1,2], K = 4
Output: -1

Example 3:
----------
Input: A = [2,-1,2], K = 3
Output: 3
 

Note:
=====
1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9


Source: Leetcode

"""
from collections import deque
from typing import List
import sys


class Item:
    def __init__(self, value: int, index: int):
        self.value = value
        self.index = index


def shortestSubarray(A: List[int], K: int):
    class IMQ:
        def __init__(self, K):
            self.q = deque()
            self.min = sys.maxsize
            self.K = K

        def push(self, newItem):
            while (len(self.q) != 0 and newItem.value < self.q[len(self.q) - 1].value):
                self.q.pop()

            # sliding window (minimum) part - bigger subarray satisfies our condition
            # that's why we can short it (move left pointer)
            # => prefixSum[j] - prefixSum[i] >= K
            # => prefixSum[i] <= prefixSum[j] - K
            # while pre[r] - pre[l] >= k
            while len(self.q) != 0 and newItem.value - self.q[0].value >= K:
                self.min = min(self.min, newItem.index - self.q[0].index)
                self.q.popleft()

            self.q.append(newItem)

    q = IMQ(K)
    q.push(Item(0, -1))
    for i in range(len(A)):
        # rewriting array with prefix sums
        A[i] = A[i] + A[i - 1] if i > 0 else A[0]
        q.push(Item(A[i], i))

    return q.min if q.min != sys.maxsize else -1


if __name__ == "__main__":
    A = [2, -1, 2]
    K = 3
    # A = [1,2]
    # K = 4
    # A = [1]
    # K = 1
    print("Shortest sum sub-array :", shortestSubarray(A, K))
