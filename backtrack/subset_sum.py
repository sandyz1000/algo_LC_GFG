# coding=utf-8
"""
http://www.geeksforgeeks.org/backttracking-set-4-subset-sum/

Backtracking | Set 4 (Subset Sum)

Subset sum problem is to find subset of elements that are selected from a given set whose sum
adds up to a given number K. We are considering the set contains non-negative values. It is
assumed that the input set is unique (no duplicates are presented).

Exhaustive Search Algorithm for Subset Sum:
------------------------------------------------

One way to find subsets that sum to K is to consider all possible subsets. A power set contains
all those subsets generated from a given set. The size of such a power set is 2N.

Backtracking Algorithm for Subset Sum
------------------------------------------------
Using exhaustive search we consider all subsets irrespective of whether they satisfy given
constraints or not. Backtracking can be used to make a systematic consideration of the elements
to be selected.

Assume given set of 4 elements, say w[1] ... w[4]. Tree diagrams can be used to design backtracking
algorithms. The following tree diagram depicts approach of generating variable sized tuple.

    -----  DIAGRAM GOES HERE ----

In the above tree, a node represents function call and a branch represents candidate element. The
root node contains 4 children. In other words, root considers every element of the set as
different branch. The next level sub-trees correspond to the subsets that includes the parent
node. The branches at each level represent tuple element to be considered. For example, if we are
at level 1, tuple_vector[1] can take any value of four branches generated. If we are at level 2
of left most node, tuple_vector[2] can take any value of three branches generated, and so on…

For example the left most child of root generates all those subsets that include w[1]. Similarly
the second child of root generates all those subsets that includes w[2] and excludes w[1].

As we go down along depth of tree we add elements so far, and if the added sum is satisfying
explicit constraints, we will continue to generate child nodes further. Whenever the constraints
are not met, we stop further generation of sub-trees of that node, and backtrack to previous node
to explore the nodes not yet explored. In many scenarios, it saves considerable amount of
processing time.

The tree should trigger a clue to implement the backtracking algorithm (try yourself). It prints
all those subsets whose sum add up to given number. We need to explore the nodes along the
breadth and depth of the tree. Generating nodes along breadth is controlled by loop and nodes
along the depth are generated using recursion (post order traversal).

Pseudo code given below
    if(subset is satisfying the constraint)
        print the subset
        exclude the current element and consider next element
    else
        generate the nodes of present level along breadth of tree and
        recur for next levels
"""

from __future__ import print_function
from functools import cmp_to_key


class SubsetSum:
    def __init__(self):
        self.total_nodes = 0

    def subset_sum(self, s, t, s_size, t_size, summation, ite, target_sum):
        """
        s            - set vector
        t            - tuple vector
        s_size       - set size
        t_size       - tuple size so far
        summation    - sum so far
        ite          - nodes count
        target_sum   - sum to be found

        :param s: List[int]
        :param t: List[int]
        :param s_size: int
        :param t_size: int
        :param summation: int
        :param ite: int
        :param target_sum: int
        :return:
        """
        self.total_nodes += 1
        if target_sum == summation and ite < s_size:
            # We found subset
            self.print_subset(t, t_size)
            # Exclude previously added item and consider next candidate
            self.subset_sum(s, t, s_size, t_size - 1, summation - s[ite],
                            ite + 1, target_sum)
            return
        else:
            # generate nodes along the breadth
            for i in range(ite, s_size):
                t[t_size] = s[i]
                # consider next level node (along depth)
                self.subset_sum(s, t, s_size, t_size + 1, summation + s[i],
                                i + 1, target_sum)

    def generate_subsets(self, s, size, target_sum):
        """
        Wrapper to print subsets that sum to target_sum input is weights vector and target_sum

        :param s: List[int]
        :param size: int
        :param target_sum: int
        :return:
        """
        tuple_vector = [0] * size
        self.subset_sum(s, tuple_vector, size, 0, 0, 0, target_sum)

    def print_subset(self, arr, size):
        for i in range(size):
            print("%d" % arr[i], end=" ")
        print("")


class SubsetSumX:
    def __init__(self):
        self.total_nodes = 0

    def print_subset(self, arr, size):
        for i in range(size):
            print("%d" % arr[i], end=" ")
        print("")

    def subset_sum(self, s, t, s_size, t_size, summation, ite, target_sum):
        """
        s            - set vector
        t            - tuplet vector
        s_size       - set size
        t_size       - tuple size so far
        summation    - sum so far
        ite          - nodes count
        target_sum   - sum to be found

        :param s: List[int]
        :param t: List[int]
        :param s_size: int
        :param t_size: int
        :param summation: int
        :param ite: int
        :param target_sum: int
        :return:
        """
        self.total_nodes += 1

        if target_sum == summation:
            self.print_subset(t, t_size)

            # constraint check
            if ite + 1 < s_size and summation - s[ite] + s[ite + 1] <= target_sum:
                # Exclude previous added item and consider next candidate
                self.subset_sum(s, t, s_size, t_size - 1, summation - s[ite],
                                ite + 1, target_sum)
            return

        else:
            # constraint check
            if ite < s_size and summation + s[ite] <= target_sum:
                # generate nodes along the breadth
                for i in range(ite, s_size):
                    t[t_size] = s[i]
                    if summation + s[i] <= target_sum:
                        # consider next level node (along depth)
                        self.subset_sum(s, t, s_size, t_size + 1, summation + s[i],
                                        i + 1, target_sum)

    def generate_subsets(self, s, size, target_sum):
        """
        The power of backtracking appears when we combine explicit and implicit constraints,
        and we stop generating nodes when these checks fail. We can improve the above algorithm
        by strengthening the constraint checks and presorting the data. By sorting the initial
        array, we need not to consider rest of the array, once the sum so far is greater than
        target number. We can backtrack and check other possibilities.

        Similarly, assume the array is presorted and we found one subset. We can generate next
        node excluding the present node only when inclusion of next node satisfies the constraints.
        Given below is optimized implementation (it prunes the subtree if it is not satisfying
        constraints).

        Wrapper that prints subsets that sum to target_sum

        """

        tuplet_vector = [0] * size
        total = 0

        # sort the set
        s.sort(key=cmp_to_key(lambda pLhs, pRhs: pLhs - pRhs))
        for i in range(size):
            total += s[i]

        if s[0] <= target_sum <= total:
            self.subset_sum(s, tuplet_vector, size, 0, 0, 0, target_sum)


if __name__ == '__main__':
    print("\nMethod-1 ----- \n")
    subset = SubsetSum()
    weights = [10, 7, 5, 18, 12, 20, 15]
    size = len(weights)
    subset.generate_subsets(weights, size, 35)
    print("Nodes generated %d" % subset.total_nodes)

    print("\nMethod-2 ----- \n")
    subset = SubsetSumX()
    weights = [15, 22, 14, 26, 32, 9, 16, 8]
    target = 53
    size = len(weights)

    subset.generate_subsets(weights, size, target)
    print("Nodes generated %d" % subset.total_nodes)
