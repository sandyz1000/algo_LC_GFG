"""
* 739
 *
 * ======
 *
 * Task.
 *
 * Given a list of daily temperatures T, return a list such that, for each day
 * in the input, tells you how many days you would have to wait until a warmer
 * temperature. If there is no future day for which this is possible, put 0
 * instead.
 *
 * For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
 * your output should be [1, 1, 4, 2, 1, 1, 0, 0].
 * ======
 *
 * Source: Leetcode
 

"""
import numpy as np
from collections import deque
from typing import List

def dailyTemperatures1(T: List[int]):
    class Item:
        def __init__(self, value: int, index: int):
            self.value = value
            self.index = index

    class DMQ:
        def __init__(self, size: int, defaultValue: int):
            self.q = deque()
            self.nearest_values = [0] * size
            self.default_value = defaultValue

        def push(self, currentItem: Item):
            while (len(self.q) != 0 and currentItem.value >= self.q[len(self.q) - 1].value):
                self.q.pop()

            self.set_nearest_value(currentItem.index)
            self.q.append(currentItem)

        def set_nearest_value(self, current_item_index: int):
            self.nearest_values[current_item_index] = self.default_value
            if (len(self.q) != 0):
                self.nearest_values[current_item_index] = self.q[len(self.q) - 1].index - current_item_index

        def getNearestValues(self) -> List[int]:
            return self.nearest_values

    size = len(T)
    q = DMQ(size, 0)
    for i in range(size - 1, -1, -1):
        q.push(Item(T[i], i))

    return q.getNearestValues()


def dailyTemperatures2(T: List[int]):
    n = len(T)
    nearest = [0] * n  # nearest biggest indexes from right to left
    result = [0] * n

    for i in range(n - 1, -1, -1):
        j = i + 1
        while (j < n and T[j] <= T[i]):
            j = nearest[j]
        nearest[i] = j
        result[i] = 0 if nearest[i] == n else nearest[i] - i

    return result


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    # check if current element is greater than st[-1] if yes st.pop()
    # st.append(index)
    # result.append(current_idx - st[-1])
    st = []
    L = len(temperatures)
    result = np.zeros((L,), int)
    for i in range(L-1, -1, -1):
        while st and temperatures[st[-1]] <= temperatures[i]:
            st.pop()
        if len(st) > 0:
            result[i] = st[-1] - i
        st.append(i)
    return result

if __name__ == "__main__":
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    # print("Daily temperature method-1: ", dailyTemperatures1(T))

    # print("Daily temperature method-2: ", dailyTemperatures2(T))

    print("Daily temperature method-3: ", dailyTemperatures(T))
