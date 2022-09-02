"""
* 456
 *
 * ======
 *
 * Task.
 
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] 
and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise return false.


Example 1:
---------
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
---------
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
---------
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

One of the ways to go about applying MQ here is to use MQ for '13' out of '132' pattern, which means
having a decreasing MQ, going from right to left. Now, let’s look at the first slide - in this case
our '1' is 1, '3' is 5 and '2' is 4. We know that the '2' should be between '1' and ‘3’, and the definite
‘2’ (most likely to be the answer) will be the biggest ‘2’ we can find, and the biggest ‘2’ is the
last ‘2’ we can remove with ‘3’ from the queue. Then our task is just to find if we have the ‘1’ which
is smaller then the ‘2’ we already got.


Constraints:
------------
n == nums.length
1 <= n <= 3 * 104
-109 <= nums[i] <= 109

 * ======
 *
 * Source: Leetcode

"""
import sys
from collections import deque
from typing import List


def find132pattern(a: List[int]):
    class MQ:
        def __init__(self):
            self.queue = deque()
            self.prev = -sys.maxsize

        def push(self, cur: int):
            if (self.prev > cur):
                return True

            while (len(self.queue) != 0 and self.queue[len(self.queue) - 1] < cur):
                self.prev = self.queue[len(self.queue) - 1]
                self.queue.pop()

            self.queue.append(cur)
            return False

    queue = MQ()
    for i in range(len(a) - 1, -1, -1):
        if (queue.push(a[i])):
            return True
    return False


if __name__ == "__main__":
    # nums = [1, 2, 3, 4]  # False
    nums = [-1, 3, 2, 0]  # True
    print("Found pattern: ", find132pattern(nums))
