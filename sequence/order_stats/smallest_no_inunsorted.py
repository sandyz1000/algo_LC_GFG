"""
Find the smallest positive number missing from an unsorted array | Set 1
You are given an unsorted array with both positive and negative elements. You have to find the
smallest positive number missing from the array in O(n) time using constant extra space. You can
modify the original array.

------------------------------------------------------
Examples
------------------------------------------------------
Input:  {2, 3, 7, 6, 8, -1, -10, 15}
Output: 1

Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
Output: 4

Input: {1, 1, 0, -1, -2}
Output: 2

A naive method to solve this problem is to search all positive integers, starting from 1 in the
given array. We may have to search at most n+1 numbers in the given array. So this solution
takes O(n^2) in worst case.

We can use sorting to solve it in lesser time complexity. We can sort the array in O(nLogn) time.
Once the array is sorted, then all we need to do is a linear scan of the array. So this approach
takes O(nLogn + n) time which is O(nLogn).

We can also use hashing. We can build a hash table of all positive elements in the given array.
Once the hash table is built. We can look in the hash table for all positive integers,
starting from 1. As soon as we find a number which is not there in hash table, we return it.
This approach may take O(n) time on average, but it requires O(n) extra space.

A O(n) time and O(1) extra space solution:
The idea is similar to this post. We use array elements as index. To mark presence of an element x,
we change the value at the index x to negative. But this approach doesn't work if there are
non-positive (-ve and 0) numbers. So we segregate positive from negative numbers as first step
and then apply the approach.

Following is the two step algorithm:

1) Segregate positive numbers from others i.e., move all non-positive numbers to left side.
In the following code, segregate() function does this part.

2) Now we can ignore negative elements and consider only the part of array which contains all
positive elements. We traverse the array containing all positive numbers and to mark presence
of an element x, we change the sign of value at index x to negative. We traverse the array
again and print the first index which has positive value. In the following code,
findMissingPositive() function does this part. Note that in findMissingPositive, we have
subtracted 1 from the values as indexes start from 0 in C.

"""


# Utility function that puts all non-positive (0 and negative) numbers on left side of arr[]
# and return count of such numbers
def segregate(arr, size):
    j = 0
    for i in range(size):
        if arr[i] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1  # increment count of non-positive integers
    return j


def find_missing_positive(arr, size):
    """
    Find the smallest positive missing number in an array that contains all positive integers
    :param arr:
    :param size:
    :return:
    """
    # Mark arr[i] as visited by making arr[arr[i] - 1] negative. Note that 1 is subtracted
    # because index start from 0 and positive numbers start from 1
    for i in range(size):
        if abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

    # Return the first index value at which is positive
    for i in range(size):
        if arr[i] > 0:
            return i + 1  # 1 is added becuase indexes start from 0

    return size + 1


def find_missing(arr, size):
    """
    Find the smallest positive missing number in an array that contains both positive and
    negative integers
    """
    # First separate positive and negative numbers
    shift = segregate(arr, size)

    # Shift the array and call findMissingPositive for positive part
    return find_missing_positive(arr[shift:size], size - shift)


if __name__ == '__main__':
    # Output: The smallest positive missing number is 1
    arr = [0, 10, 2, -10, -20]
    arr_size = len(arr)
    missing = find_missing(arr, arr_size)
    print("The smallest positive missing number is", missing)
