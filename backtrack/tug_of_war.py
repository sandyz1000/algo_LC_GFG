# Tug of War
# ===========
# Given a set of n integers, divide the set in two subsets of n/2 sizes each such that the
# difference of the sum of two subsets is as minimum as possible. If n is even, then sizes of two
# subsets must be strictly n/2 and if n is odd, then size of one subset must be (n-1)/2 and size of
# other subset must be (n+1)/2.

# For example, let given set be {3, 4, 5, -3, 100, 1, 89, 54, 23, 20}, the size of set is 10.
# Output for this set should be {4, 100, 1, 23, 20} and {3, 5, -3, 89, 54}. Both output subsets are
# of size 5 and sum of elements in both subsets is same (148 and 148). Let us consider another
# example where n is odd. Let given set be {23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4}. The output
# subsets should be {45, -34, 12, 98, -1} and {23, 0, -99, 4, 189, 4}. The sums of elements in two
# subsets are 120 and 121 respectively.

# The following solution tries every possible subset of half size. If one subset of half size is
# formed, the remaining elements form the other subset. We initialize current set as empty and one
# by one build it. There are two possibilities for every element, either it is part of current set,
# or it is part of the remaining elements (other subset). We consider both possibilities for every
# element. When the size of current set becomes n/2, we check whether this solutions is better than
# the best solution available so far. If it is, then we update the best solution.


import sys

INT_MAX = sys.maxsize


class TugOfWar(object):
    min_diff = INT_MAX

    def print_solution(self, arr, soln, n):
        print("The first subset is: ")
        for i in range(n):
            if soln[i]:
                print(arr[i] + " ")

        print("\nThe second subset is: ")
        for i in range(n):
            if not soln[i]:
                print(arr[i] + " ")

    def tow_utils(self, arr, n, curr_elements, no_of_selected_elements, soln, summation,
                  curr_sum, curr_position):
        """
        :param arr: List[int]
        :param n: int
        :param curr_elements: List[bool]
        :param no_of_selected_elements: int
        :param soln: List[bool]
        :param summation: int
        :param curr_sum: int
        :param curr_position: int
        :return:
        """
        # checks whether the it is going out of bound
        if curr_position == n:
            return

        # checks that the numbers of elements left are not less than the number of elements
        # required to form the solution
        if (n // 2 - no_of_selected_elements) > (n - curr_position):
            return

        # consider the cases when current element is not included in the solution
        self.tow_utils(arr, n, curr_elements, no_of_selected_elements, soln,
                       summation, curr_sum, curr_position + 1)

        # add the current element to the solution
        no_of_selected_elements += 1
        curr_sum = curr_sum + arr[curr_position]
        curr_elements[curr_position] = True

        if no_of_selected_elements == n // 2:
            # Check if solution is formed, checks if the solution formed is better than the best
            # solution so far
            if abs(summation / 2 - curr_sum) < self.min_diff:
                self.min_diff = abs(summation / 2 - curr_sum)
                for i in range(n):
                    soln[i] = curr_elements[i]
        else:
            # consider the cases where current element is included in the solution
            self.tow_utils(arr, n, curr_elements, no_of_selected_elements, soln,
                           summation, curr_sum, curr_position + 1)

        # removes current element before returning to the caller of this function (BACKTRACK)
        curr_elements[curr_position] = False

    def tug_of_war(self, arr, n):
        """
        :param arr: list
        :param n: int
        :return:
        """
        # the boolean array that contains the inclusion and exclusion of an element in current set.
        # The number excluded automatically form the other set
        curr_elements = [False] * n

        # The inclusion/exclusion arr for final solution
        soln = [False] * n
        summation = sum(arr)
        self.tow_utils(arr, n, curr_elements, 0, soln, summation, 0, 0)
        print("The first subset is:", [arr[i] for i in range(n) if soln[i]])
        print("The second subset is:", [arr[i] for i in range(n) if not soln[i]])


if __name__ == "__main__":
    test = TugOfWar()
    # The first subset is: 45 -34 12 98 -1
    # The second subset is: 23 0 -99 4 189 4
    arr = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
    n = len(arr)
    test.tug_of_war(arr, n)
