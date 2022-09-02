"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of
S = {S1, S2, .. , Sm} valued coins, how many ways can we make the change?
The order of coins doesn't matter.

For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
So output should be 4. For N = 10 and S = {2, 3, 5, 6}, there are five solutions: {2,2,2,2,2},
{2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.

---------------------
Optimal Substructure:
---------------------
To count total number solutions, we can divide all set solutions in two sets.
1) Solutions that do not contain mth coin (or Sm).
2) Solutions that contain at least one Sm.

Let count(S[], m, n) be the function to count the number of solutions, then it can be written as
sum of count(S[], m-1, n) and count(S[], m, n-Sm).

Therefore, the problem has optimal substructure property as the problem can be solved using
solutions to sub problems.

-------------------------
Overlapping Sub-problems:
-------------------------
The function C({1}, 3) is called two times. If we draw the complete tree, then we can see that
there are many sub problems being called more than once.

C() --> count()
                           C({1,2,3}, 5)
                          /
                         /
             C({1,2,3}, 2)                 C({1,2}, 5)
            /                             /
           /                             /
C({1,2,3}, -1)  C({1,2}, 2)        C({1,2}, 3)    C({1}, 5)
               /                 /                /
              /                 /                /
    C({1,2},0)  C({1},2)   C({1,2},1) C({1},3)  C({1}, 4)  C({}, 5)
                   /       /             /         /
                  /       /             /         /
                .      .  .     .   .     .   C({1}, 3) C({}, 4)
                                               /
                                              /
                                             .      .

Since same sub problems are called again, this problem has Overlapping Sub problems property. So
the Coin Change problem has both properties (see this and this) of a dynamic programming problem.
Like other typical Dynamic Programming(DP) problems, re-computations of same sub-problems can be
avoided by constructing a temporary array table[][] in bottom up manner.

"""
from typing import List


def rec_count(S: List[int], m: int, n: int):
    # If n is 0 then there is 1 solution (do not include any coin)
    if n == 0:
        return 1

    # If n is less than 0 then no solution exists OR If there are no coins and n is greater than
    # 0, then no solution exist
    if n < 0 or (m <= 0 and n >= 1):
        return 0

    # count is sum of solutions
    # (i) including S[m-1]
    # (ii) excluding S[m-1]
    return rec_count(S, m - 1, n) + rec_count(S, m, n - S[m - 1])


def dp_count_1(S: List[int], m: int, total_amount: int):
    """
    Dynamic Programming Python implementation of Coin Change problem
    Time Complexity: O(m*amount)
    Space Complexity: O(m*amount)

    :param S: List[int]
    :param m: int
    :param total_amount: int
    :return:
    """
    # We need amount+1 rows as the table is constructed in bottom up manner using the base
    # case 0 value case (total = 0)
    table = [[0 for x in range(m)] for x in range(total_amount + 1)]

    # Fill the entries for 0 value case (amount = 0)
    for amount in range(m):
        table[0][amount] = 1

    # Fill rest of the table entries in bottom up manner
    for amount in range(1, total_amount + 1):
        for selected_coin in range(m):
            # Count of solutions including S[selected_coin]
            x = 0
            if amount - S[selected_coin] >= 0:
                x = table[amount - S[selected_coin]][selected_coin]

            # Count of solutions excluding S[selected_coin] -> Previous solution
            y = 0
            if selected_coin >= 1:
                y = table[amount][selected_coin - 1]

            # total count
            table[amount][selected_coin] = x + y

    return table[total_amount][m - 1]


def dp_count_2(S: List[int], m: int, total: int):
    """
    Dynamic Programming Python implementation of Coin Change problem
    Time Complexity: O(mn)
    Space Complexity: O(n)
    """
    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0 for k in range(total + 1)]

    # Base case (If given value is 0)
    table[0] = 1

    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0, m):
        for j in range(S[i], total + 1):
            table[j] += table[j - S[i]]

    return table[total]


if __name__ == '__main__':
    arr, n = [1, 2, 3], 4
    # arr, n = [2, 3, 5, 6], 10
    m = len(arr)
    print("Recursive method: %d" % rec_count(arr, m, n))
    print("DP 1 method: %d" % dp_count_1(arr, m, n))
    print("DP 2 method: %d" % dp_count_2(arr, m, n))
