"""
Segregate 0s and 1s in an array
You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side
of the array. Traverse array only once.

------------------------------------
Example:
------------------------------------
Input array = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
Output array = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

------------------------------------
Explanation:
------------------------------------
Method 2 (Use two indexes to traverse)
Maintain two indexes. Initialize first index left as 0 and second index right as n-1.

Do following while left < right
a) Keep incrementing index left while there are 0s at it
b) Keep decrementing index right while there are 1s at it
c) If left < right then exchange arr[left] and arr[right]

Time Complexity: O(n)
"""
import typing


# Python program to sort a binary array in one pass

def segregate0and1(arr: typing.List[int], size: int):
    """Function to put all 0s on left and all 1s on right
    """
    # Initialize left and right indexes
    left, right = 0, size - 1

    while left < right:
        # Increment left index while we see 0 at left
        while arr[left] == 0 and left < right:
            left += 1

        # Decrement right index while we see 1 at right
        while arr[right] == 1 and left < right:
            right -= 1

        # If left is smaller than right then there is a 1 at left
        # and a 0 at right. Exchange arr[left] and arr[right]
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr


if __name__ == '__main__':
    # Output: [0, 0, 1, 1, 1, 1]
    arr = [0, 1, 0, 1, 1, 1]
    arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    arr_size = len(arr)
    print("Array after segregation")
    print(segregate0and1(arr, arr_size))
