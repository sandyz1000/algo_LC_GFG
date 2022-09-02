"""
/**
 * 84
 *
 * ======
 *
 * Task.
 *
 * Given n non-negative integers representing the histogram's bar height where
 * the width of each bar is 1, find the area of largest rectangle in the
 * histogram.

Explanation:
The largest area’s height will be the highest bar of the selected bars or the smaller bar that
will cut along other bars that are bigger. We can cut along bigger bars with smaller bar and we can’t
cut along smaller bars with the bigger one. Thus the width would be spanning between smaller bars -
from the smaller bar on the left to the smaller bar on the right from the current bar.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

-- REFER: largest_rectangle.png ---

The largest rectangle is shown in the shaded area, which has area = 10 unit.


Input: [2,1,5,6,2,3]
Output: 10
 * ======
 *
 * Source: Leetcode
 */

"""
# %%
from collections import deque
from typing import List


class Item:
    def __init__(self, value: int, index: int):
        self.value = value
        self.index = index


# %%
# NOTE: remove all the element which is greater than current element in both side
def largestRectangleArea(heights: List[int]):
    class MQ:
        def __init__(self, default_nearest: int, n: int):
            self.queue = deque()
            self.nearest = [0] * n
            self.defaultNearest = default_nearest

        def push(self, newItem: Item):
            while (len(self.queue) > 0 and newItem.value <= self.queue[len(self.queue) - 1].value):
                self.queue.pop()

            if (len(self.queue) == 0):
                self.nearest[newItem.index] = self.defaultNearest
            else:
                self.nearest[newItem.index] = self.queue[len(self.queue) - 1].index

            self.queue.append(newItem)

    n = len(heights)

    # default nearest value for increasing mq from left to right is -1
    leftRight = MQ(-1, n)
    for i in range(n):
        leftRight.push(Item(heights[i], i))

    # default nearest value for increasing mq from right to left is n
    rightLeft = MQ(n, n)
    for i in range(n - 1, -1, -1):
        rightLeft.push(Item(heights[i], i))

    maxArea = 0
    for i in range(n):
        width = rightLeft.nearest[i] - leftRight.nearest[i] - 1
        current_area = width * heights[i]
        maxArea = max(maxArea, current_area)

    return maxArea


heights = [2, 1, 5, 6, 2, 3]
# Output: 10
print("Largest rectangle area: ", largestRectangleArea(heights))


# %%
"""
Using 1 mq. The biggest area involving a height at i is between nearest
smallest value on the left, and nearest smallest value on the right.
"""


def largestRectangleArea(heights: List[int]):
    class MQ:
        def __init__(self):
            self.queue = deque()
            self.maxArea = 0

        def push(self, newItem):
            # Increasing mono queue
            while (len(self.queue) > 0 and newItem.value < self.queue[len(self.queue) - 1].value):
                upperBoundary = self.queue.pop()
                leftBoundaryIndex = self.queue[len(self.queue) - 1].index if len(self.queue) != 0 else -1
                width = newItem.index - leftBoundaryIndex - 1
                currentArea = width * upperBoundary.value
                self.maxArea = max(self.maxArea, currentArea)
            self.queue.append(newItem)

    q = MQ()
    for i in range(0, len(heights) + 1):
        currentValue = heights[i] if i < len(heights) else 0
        q.push(Item(currentValue, i))
    return q.maxArea


height = [2, 1, 5, 6, 2, 3]
print("Largest rectangle area: ", largestRectangleArea(height))


# %%
"""
Using arrays of nearest smaller values. The biggest area involving a
height at i is between nearest smallest value on the left, and * nearest
smallest value on the right.
"""


def largestRectangleArea(heights: List[int]):
    n = len(heights)
    leftToRightNearestValuesLessThan = [0] * n

    for i in range(n):
        j = i - 1
        while (j >= 0 and heights[i] <= heights[j]):
            j = leftToRightNearestValuesLessThan[j]
        leftToRightNearestValuesLessThan[i] = j

    rightToLeftNearestValuesLessThan = [0] * n
    for i in range(n - 1, -1, -1):
        j = i + 1
        while (j < n and heights[i] <= heights[j]):
            j = rightToLeftNearestValuesLessThan[j]
        rightToLeftNearestValuesLessThan[i] = j

    result = 0

    for i in range(n):
        area = heights[i] * (rightToLeftNearestValuesLessThan[i] - leftToRightNearestValuesLessThan[i] - 1)
        result = max(result, area)

    return result


height = [2, 1, 5, 6, 2, 3]
print("Largest rectangle area: ", largestRectangleArea(height))

# %%
