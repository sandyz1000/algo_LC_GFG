"""
Program to find largest element in an array
Given an array, find the largest element in it.

Input : arr = [10, 20, 4]
Output : 20

Input : arr = [20, 10, 20, 4, 100]
Output : 100

"""


# Time Complexity: O(n)
# C function to find maximum in arr[] of size n

def largest(arr, n):
    maximum = arr[0]  # Initialize maximum element
    # Traverse array elements from second and compare every element with current max
    for i in range(1, n):
        if arr[i] > maximum:
            maximum = arr[i]

    return maximum


if __name__ == '__main__':
    arr = [10, 324, 45, 90, 9808]
    n = len(arr)
    print("Largest in given array is %d" % largest(arr, n))
