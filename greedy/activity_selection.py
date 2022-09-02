"""
The following implementation assumes that the activities are already sorted according to their
finish time.

Prints a maximum set of activities that can be done by a single person, one at a time
# n --> Total number of activities
# s[]--> An array that contains start time of all activities
# f[] --> An array that contains finish time of all activities

"""
from __future__ import print_function


def print_max_activities(s, f):
    n = len(f)
    print("The following activities are selected")

    # The first activity is always selected
    i = 0
    print(i, end=" ")

    # Consider rest of the activities
    for j in range(1, n):
        # If this activity has start time greater than or equal to the finish time of previously
        # selected activity, then select it
        if s[j] >= f[i]:
            print(j, end=" ")
            i = j


if __name__ == "__main__":
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    print_max_activities(s, f)
