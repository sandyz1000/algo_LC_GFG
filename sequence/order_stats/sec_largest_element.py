"""
Find Second largest element in an array
Given an array of integers, our task is to write a program that efficiently finds the second largest
element present in the array.

Example:

Input : arr[] = {12, 35, 1, 10, 34, 1}
Output : The second largest element is 34.

Input : arr[] = {10, 5, 10}
Output : The second largest element is 5.

Input : arr[] = {10, 10, 10}
Output : The second largest does not exist.

"""
INT_MIN = -9999999


# C program to find second largest element in an array
# Time complexity: O(n)
# Space Complexity: O(n)

# Function to print the second largest elements
def print2largest(arr, arr_size):
    # There should be atleast two elements
    if arr_size < 2:
        print(" Invalid Input ")
        return

    first = second = INT_MIN
    for i in range(arr_size):
        # If current element is smaller than first then update both first and second
        if arr[i] > first:
            second = first
            first = arr[i]

        # If arr[i] is in between first and second then update second
        elif arr[i] > second and arr[i] != first:
            second = arr[i]

    if second == INT_MIN:
        print("There is no second largest elementn")
    else:
        print("The second largest element is %d n" % second)


if __name__ == '__main__':
    arr = [12, 35, 1, 10, 34, 1]
    n = len(arr)
    print2largest(arr, n)
