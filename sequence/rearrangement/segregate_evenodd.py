"""
Segregate Even and Odd numbers
Given an array A[], write a function that segregates even and odd numbers. The functions should put
all even numbers first, and then odd numbers.

------------------------------------
Example
------------------------------------
Input  = {12, 34, 45, 9, 8, 90, 3}
Output = {12, 34, 8, 90, 45, 9, 3}
In the output, order of numbers can be changed, i.e., in the above example 34 can come before 12
and 3 can come before 9.

Time Complexity: O(n)
"""
import typing


def segregate_even_odd(arr: typing.List[int]):
    """Python program to segregate even and odd elements of array"""
    # Initialize left and right indexes
    left, right = 0, len(arr) - 1

    while left < right:
        # Increment left index while we see 0 at left
        while arr[left] % 2 == 0 and left < right:
            left += 1
        # Decrement right index while we see 1 at right
        while arr[right] % 2 == 1 and left < right:
            right -= 1
        if left < right:
            # Swap arr[left] and arr[right]*/
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right = right - 1


if __name__ == '__main__':
    arr = [12, 34, 45, 9, 8, 90, 3]
    segregate_even_odd(arr)
    print("Array after segregation: \n\n", arr)
