"""
Given a value V, if we want to make change for V cents, and we have infinite supply of each of
C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change?

Examples:

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents

This problem is a variation of the problem discussed Coin Change Problem. Here instead of finding
total number of possible solutions, we need to find the solution with minimum number of coins.

The minimum number of coins for a value V can be computed using below recursive formula.
-----------------------------------------------------------------------------------------
If V == 0, then 0 coins required.
If V > 0
   minCoin(coins[0..m-1], V) = min {1 + minCoins(V-coin[i])}
                               where i varies from 0 to m-1
                               and coin[i] <= V
------------------------------------------------------------------------------------------

The time complexity of above solution is exponential. If we draw the complete recursion tree,
we can observer that many subproblems are solved again and again. For example, when we start from
V = 11, we can reach 6 by subtracting one 5 times and by subtracting 5 one times. So the
subproblem for 6 is called twice.
Since same suproblems are called again, this problem has Overlapping Subprolems property. So the
min coins problem has both properties (see this and this) of a dynamic programming problem. Like
other typical Dynamic Programming(DP) problems, recomputations of same subproblems can be avoided
by constructing a temporary array table[][] in bottom up manner. Below is Dynamic Programming
based solution.

Dynamic Programming time complexity:
Time complexity of the above solution is O(mV).
"""

INT_MAX = 10000000


def min_coins_rec(coins, m, amount):
    """
    # find minimum of coins to make a given change V
    # m is size of coins arr (number of different coins)
    :type coins:
    :type m:
    :type amount:
    :rtype:
    """
    if amount == 0:
        return 0  # Base case
    res = INT_MAX  # Initialize result

    # Try every coin that has smaller value than V
    for i in range(m):
        if coins[i] <= amount:
            sub_res = min_coins_rec(coins, m, amount - coins[i])
            # if sub_res < INT_MAX:
            #     res = min(sub_res + 1 , res)
            
            # Check for INT_MAX to avoid overflow and see if result can minimized
            if sub_res != INT_MAX and sub_res + 1 < res:
                res = sub_res + 1

    return res


def min_coins_dp(coins, total_coins, amount):
    """
    # m is size of coins arr (number of different coins)
    # table[value] will be storing the minimum number of coins
    # required for value value.  So table[V] will have result
    :type coins:
    :type total_coins:
    :type amount:
    :rtype:
    """
    table = [0] * (amount + 1)
    table[0] = 0  # Base case (If given value V is 0)

    # Initialize all table values as Infinite
    for value in range(1, amount + 1):
        table[value] = INT_MAX

    # Compute minimum coins required for all values from 1 to amount
    for value in range(1, amount + 1):
        # Go through all coins smaller than value
        for j in range(total_coins):
            if coins[j] <= value:
                sub_res = table[value - coins[j]]
                if sub_res != INT_MAX and sub_res + 1 < table[value]:
                    table[value] = sub_res + 1
    return table[amount]


if __name__ == '__main__':
    coins = [9, 6, 5, 1]
    m = len(coins)
    amount = 11
    print("Minimum coins required is %d" % min_coins_rec(coins, m, amount))
    print("Minimum coins required is %d" % min_coins_dp(coins, m, amount))
