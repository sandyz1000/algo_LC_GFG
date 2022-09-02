"""
Bucket Sort
Bucket sort is mainly useful when input is uniformly distributed over a range.

------------------------------------------------
Example:
------------------------------------------------
Consider the following problem.
Sort a large set of floating point numbers which are in range from 0.0 to 1.0 and are uniformly
distributed across the range. How do we sort the numbers efficiently?

A simple way is to apply a comparison based sorting algorithm. The lower bound for Comparison
based sorting algorithm (Merge Sort, Heap Sort, Quick-Sort .. etc) is Omega(n Log n), i.e., they
cannot do better than nLogn.
Can we sort the array in linear time? Counting sort can not be applied here as we use keys as
index in counting sort. Here keys are floating point numbers.

------------------------------------------------
Algorithm:
------------------------------------------------

The idea is to use bucket sort. Following is bucket algorithm.

bucketSort(arr[], n)
1) Create n empty buckets (Or lists).
2) Do following for every array element arr[i].
    a) Insert arr[i] into bucket[n*array[i]]
3) Sort individual buckets using insertion sort.
4) Concatenate all sorted buckets.

------------------------------------------------
Time Complexity:
------------------------------------------------
If we assume that insertion in a bucket takes O(1) time then steps 1 and 2 of the above algorithm
clearly take O(n) time. The O(1) is easily possible if we use a linked list to represent a bucket
(In the following code, Python vector is used for simplicity). Step 4 also takes O(n) time as there
will be n items in all buckets.
The main step to analyze is step 3. This step also takes O(n) time on average if all numbers are
uniformly distributed (please refer CLRS book for more details)

"""
from collections import defaultdict


# Python program to sort an array using bucket sort
def bucket_sort(arr, n):
    """
    Function to sort arr[] of size n using bucket sort
    :type arr: List[int]
    :type n: int
    :rtype: None
    """
    # 1) Create n empty buckets
    b = defaultdict(list)

    # 2) Put array elements in different buckets
    for i in range(n):
        bi = int(n * arr[i])  # Index in bucket
        b[bi].append(arr[i])

    # 3) Sort individual buckets
    for i in range(n):
        b[i].sort()

    # 4) Concatenate all buckets into arr[]
    index = 0
    for i in range(n):
        for j in range(len(b[i])):
            arr[index] = b[i][j]
            index += 1


if __name__ == '__main__':
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    n = len(arr)
    bucket_sort(arr, n)
    print("Sorted array is \n", arr)
