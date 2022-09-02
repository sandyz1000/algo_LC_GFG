"""
Replace every element with the greatest element on right side

Given an array of integers, replace every element with the next greatest element
(greatest element on the right side) in the array. Since there is no element next to the last
element, replace it with -1.

Example:
----------------
If the array is [16, 17, 4, 3, 5, 2], then it should be modified to [17, 5, 5, 5, 2, -1].

Explanation:
----------------

A naive method is to run two loops. The outer loop will one by one pick array elements from left
to right. The inner loop will find the greatest element present after the picked element. Finally
the outer loop will replace the picked element with the greatest element found by inner loop. The
time complexity of this method will be O(n*n).
A tricky method is to replace all elements using one traversal of the array. The idea is to start
from the rightmost element, move to the left side one by one, and keep track of the maximum
element. Replace every element with the maximum element. """


# Python Program to replace every element with the greatest element on right side

# Function to replace every element with the next greatest element
def next_greatest(arr):
    size = len(arr)
    # Initialize the next greatest element
    max_from_right = arr[size - 1]
    # The next greatest element for the rightmost element is always -1
    arr[size - 1] = -1
    # Replace all other elements with the next greatest
    for i in range(size - 2, -1, -1):
        # Store the current element (needed later for updating the next greatest element)
        temp = arr[i]
        # Replace current element with the next greatest
        arr[i] = max_from_right
        # Update the greatest element, if needed
        max_from_right = max(temp, max_from_right)


if __name__ == '__main__':
    # Output: [17, 5, 5, 5, 2, -1]
    arr = [16, 17, 4, 3, 5, 2]
    next_greatest(arr)
    print("Modified array is", arr)
