"""
Weighted Job Scheduling

Given N jobs where every job is represented by following three elements of it.

Start Time
Finish Time
Profit or Value Associated (>= 0)
Find the maximum profit subset of jobs such that no two jobs in the subset overlap.

Example:
========
Input: Number of Jobs n = 4
    Job Details {Start Time, Finish Time, Profit}
    Job 1:  {1, 2, 50}
    Job 2:  {3, 5, 20}
    Job 3:  {6, 19, 100}
    Job 4:  {2, 100, 200}
Output: The maximum profit is 250.
We can get the maximum profit by scheduling jobs 1 and 4.
Note that there is longer schedules possible Jobs 1, 2 and 3
but the profit with this schedule is 20+50+100 which is less than 250.

The above solution may contain many overlapping subproblems. For example if lastNonConflicting()
always returns previous job, then findMaxProfitRec(arr, n-1) is called twice and the time complexity
becomes O(n*2n). As another example when lastNonConflicting() returns previous to previous job,
there are two recursive calls, for n-2 and n-1. In this example case, recursion becomes same as Fibonacci Numbers.

So this problem has both properties of Dynamic Programming,
-> Optimal Substructure and
-> Overlapping Subproblems.
Like other Dynamic Programming Problems, we can solve this problem by
making a table that stores solution of subproblems.
"""
from dataclasses import dataclass
from typing import List
# Python program for weighted job scheduling using Dynamic Programming.


@dataclass(init=True, frozen=False)
class Job:
    """A job has start time, finish time and profit.
    """
    start: int
    finish: int
    profit: int


class findMaxProfit:
    def __init__(self, arr: List[Job], n: int) -> None:
        self.arr = arr
        self.n = n

    def latestNonConflict(self, arr: List[Job], i: int):
        """
        Find the latest job (in sorted array) that doesn't conflict with the job[i]
        """
        for j in range(i - 1, -1, -1):
            if (arr[j].finish <= arr[i].start):
                return j

        return -1

    def __call__(self):
        # The main function that returns the maximum possible profit from given array of jobs
        # Sort jobs according to finish time
        sorted(self.arr, self.arr + self.n, key=lambda s1, s2: s1.finish < s2.finish)

        # Create an array to store solutions of subproblems. table[i]
        # stores the profit for jobs till arr[i](including arr[i])
        table = [0] * self.n
        table[0] = self.arr[0].profit

        # Fill entries in M[] using recursive property
        for i in range(1, self.n):
            # Find profit including the current job
            inclProf = self.arr[i].profit
            l = self.latestNonConflict(self.arr, i)
            if (l != -1):
                inclProf += table[l]

            # Store maximum of including and excluding
            table[i] = max(inclProf, table[i - 1])

        # Store result and free dynamic memory allocated for table[]
        result = table[self.n - 1]
        del table

        return result


if __name__ == "__main__":
    arr = [Job(3, 10, 20), Job(1, 2, 50), Job(6, 19, 100), Job(2, 100, 200)]
    print("The optimal profit is ", findMaxProfit(arr, len(arr))())
    
