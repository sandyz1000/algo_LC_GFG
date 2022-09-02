"""
Find the largest three elements in an array
Given an array with all distinct elements, find the largest three elements.
Expected time complexity is O(n) and extra space is O(1).

Examples:

Input: arr = [10, 4, 3, 50, 23, 90]
Output: 90, 50, 23

"""
INT_MIN = -9999999


# Function to print three largest elements
def print2largest(arr, arr_size):
    # There should be at-least two elements
    if arr_size < 3:
        print(" Invalid Input ")

    third = first = second = INT_MIN
    for i in range(arr_size):
        # If current element is smaller than first
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]

        # If arr[i] is in between first and second then update second
        elif arr[i] > second:
            third = second
            second = arr[i]

        elif arr[i] > third:
            third = arr[i]

    print("Three largest elements are %d %d %d\n" % (first, second, third))


if __name__ == '__main__':
    arr = [12, 13, 1, 10, 34, 1]
    n = len(arr)
    print2largest(arr, n)
