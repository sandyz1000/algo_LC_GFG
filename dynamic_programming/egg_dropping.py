"""
The following is a description of the instance of this famous puzzle involving n=2 eggs and a
building with k=36 floors.

Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from, and
which will cause the eggs to break on landing. We make a few assumptions:

.... An egg that survives a fall can be used again.
.... A broken egg must be discarded.
.... The effect of a fall is the same for all eggs.
.... If an egg breaks when dropped, then it would break if dropped from a higher floor.
.... If an egg survives a fall then it would survive a shorter fall.
.... It is not ruled out that the first-floor windows break eggs, nor is it ruled out that the
    36th-floor do not cause an egg to break.

If only one egg is available and we wish to be sure of obtaining the right result, the experiment
can be carried out in only one way. Drop the egg from the first-floor window; if it survives, drop
it from the second floor window. Continue upward until it breaks. In the worst case, this method
may require 36 droppings. Suppose 2 eggs are available. What is the least number of egg-droppings
that is guaranteed to work in all cases?

The problem is not actually to find the critical floor, but merely to decide from which floor
eggs should be dropped so that total number of trials are minimized.

In this post, we will discuss solution to a general problem with n eggs and k floors. The solution
is to try dropping an egg from every floor (from 1 to k) and recursively calculate the minimum
number of droppings needed in worst case. The floor which gives the minimum value in worst case is
going to be part of the solution.
In the following solutions, we return the minimum number of trials in worst case; these solutions
can be easily modified to print floor numbers of every trials also.

1) Optimal Substructure:
When we drop an egg from a floor x, there can be two cases
(1) The egg breaks
(2) The egg doesn't break.

1) If the egg breaks after dropping from xth floor, then we only need to check for floors lower
than x with remaining eggs; so the problem reduces to x-1 floors and n-1 eggs

2) If the egg doesn't break after dropping from the xth floor, then we only need to check for
floors higher than x; so the problem reduces to k-x floors and n eggs.

Since we need to minimize the number of trials in worst case, we take the maximum of two cases.
We consider the max of above two cases for every floor and choose the floor which yields minimum
number of trials.

  k ==> Number of floors
  n ==> Number of Eggs
  eggDrop(n, k) ==> Minimum number of trials needed to find the critical
                    floor in worst case.
  eggDrop(n, k) ==> 1 + min{max(eggDrop(n - 1, x - 1), eggDrop(n, k - x)):
                 x in {1, 2, ..., k}}

2) Overlapping Subproblems:
It should be noted that the above function computes the same sub-problems again and again. See the
following partial recursion tree, E(2, 2) is being evaluated twice. There will many repeated
subproblems when you draw the complete recursion tree even for small values of n and k.


                         E(2,4)
                           |
          -------------------------------------
          |             |           |         |
          |             |           |         |
      x=1/\          x=2/\      x=3/ \    x=4/ \
        /  \           /  \       ....      ....
       /    \         /    \
 E(1,0)  E(2,3)     E(1,1)  E(2,2)
          /\  /\...         /  \
      x=1/  \               .....
        /    \
     E(1,0)  E(2,2)
            /   \
            ......

Partial recursion tree for 2 eggs and 4 floors.

Since same sub-problems are called again, this problem has Overlapping Subproblems property. So Egg
Dropping Puzzle has both properties (see this and this) of a dynamic programming problem. Like
other typical Dynamic Programming(DP) problems, re computations of same subproblems can be avoided
by constructing a temporary array eggFloor[][] in bottom up manner.

Time Complexity: O(nk^2)
Auxiliary Space: O(nk)

As an exercise, you may try modifying the above DP solution to print all intermediate floors
(The floors used for minimum trial solution).

"""
INT_MAX = 32767
import numpy as np


def egg_drop_rec(n: int, k: int):
    """
    Function to get minimum number of trials needed in worst case with n eggs and k floors
    """
    # If there are no floors, then no trials needed. OR if there is one floor,
    # one trial needed.
    if k == 1 or k == 0:
        return k

    # We need k trials for one egg and k floors
    if n == 1:
        return k

    minimum = INT_MAX

    # Consider all droppings from 1st floor to kth floor and return the minimum of
    # these values plus 1.
    for x in range(1, k + 1):
        res1 = egg_drop_rec(n - 1, x - 1)  # When egg breaks after dropping from x floor
        res2 = egg_drop_rec(n, k - x)  # When egg doesn't break after dropping from x floor
        minimum = min(max(res1, res2), minimum)

    return minimum + 1


def egg_drop(n: int, k: int):
    """
    Function to get minimum number of trials needed in worst case with n eggs and k floors
    """
    # A 2D table where entry egg_floor[i][j] will represent minimum
    # number of trials needed for i eggs and j floors.
    egg_floor = np.zeros((n + 1, k + 1), dtype=int)

    # We need 1 trial for 1 floor and 0 trials for 0 floors
    for i in range(1, n + 1):
        egg_floor[i, 1] = 1
        egg_floor[i, 0] = 0

    # We always need j trials for one egg and j floors.
    for j in range(1, k + 1):
        egg_floor[1, j] = j

    # Fill rest of the entries in table using optimal substructure property
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            egg_floor[i, j] = INT_MAX
            for x in range(1, j + 1):
                egg_floor[i, j] = min(1 + max(egg_floor[i - 1, x - 1], egg_floor[i, j - x]), egg_floor[i, j])

    # egg_floor[n][k] holds the result
    # print(egg_floor)
    return egg_floor[n, k]


if __name__ == '__main__':
    n, k = 2, 100
    print("DP: Minimum number of trials in worst case with %d eggs and %d floors is %d" %
          (n, k, egg_drop(n, k)))

    # print("Recursion: Minimum number of trials in worst case with %d eggs and %d floors is %d" %
    #       (n, k, egg_drop_rec(n, k)))
