"""
Maximum sum such that no two elements are adjacent (Answer the question in most efficient way)

Given an array of positive numbers, find the maximum sum of a sub-sequence with the constraint that
no 2 numbers in the sequence should be adjacent in the array. So 3 2 7 10 should return 13
(sum of 3 and 10) or 3 2 5 10 7 should return 15 (sum of 3, 5 and 7).

--------------------------------------------------------
Examples :
--------------------------------------------------------
Input : [5, 5, 10, 100, 10, 5]
Output : 110

Input : [1, 2, 3]
Output : 4

Input : [1, 20, 3]
Output : 20

"""


def find_max_sum(arr):
    """
    Algorithm:

    Loop for all elements in arr[] and maintain two sums incl and excl where incl = Max sum
    including the previous element and excl = Max sum excluding the previous element.

    Max sum excluding the current element will be max(incl, excl) and max sum including the
    current element will be excl + current element (Note that only excl is considered because
    elements cannot be adjacent).

    At the end of the loop return max of incl and excl.

    Function to return max sum such that no two elements are adjacent
    """
    incl = 0
    excl = 0
    for i in arr:
        maximum = max(incl, excl)
        incl = excl + i  # Current max including i
        excl = maximum

    return excl if excl > incl else incl  # return max of incl and excl


if __name__ == '__main__':
    arr = [5, 5, 10, 100, 10, 5]
    print(find_max_sum(arr))