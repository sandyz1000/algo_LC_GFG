"""
k largest(or smallest) elements in an array | added Min Heap method

Question: Write an efficient program for printing k largest elements in an array. Elements in array
can be in any order.

For example:
If given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements
i.e., k = 3 then your program should print 50, 30 and 23.

Discussion:

==Method 1 (Use Bubble k times)==
1) Modify Bubble Sort to run the outer loop at most k times.
2) Print the last k elements of the array obtained in step 1.

Time Complexity: O(nk)

Like Bubble sort, other sorting algorithms like Selection Sort can also be modified to get the k
largest elements.

==Method 2 (Use temporary array)==
K largest elements from arr[0..n-1]

1) Store the first k elements in a temporary array temp[0..k-1].
2) Find the smallest element in temp[], let the smallest element be min.
3) For each element x in arr[k] to arr[n-1]
If x is greater than the min then remove min from temp[] and insert x.
4) Print final k elements of temp[]

Time Complexity: O((n-k)*k). If we want the output sorted then O((n-k)*k + klogk)

==Method 3(Use Sorting)==
1) Sort the elements in descending order in O(nLogn)
2) Print the first k numbers of the sorted array O(k).

Time complexity: O(nlogn)

==Method 4 (Use Max Heap)==
1) Build a Max Heap tree in O(n)
2) Use Extract Max k times to get k maximum elements from the Max Heap O(klogn)

Time complexity: O(n + klogn)

==Method 5(Use Order Statistics)==
1) Use order statistic algorithm to find the kth largest element. Please see the topic selection in
worst-case linear time O(n)
2) Use QuickSort Partition algorithm to partition around the kth largest number O(n).
3) Sort the k-1 elements (elements greater than the kth largest element) O(kLogk). This step is
needed only if sorted output is required.

Time complexity: O(n) if we don't need the sorted output, otherwise O(n+kLogk)

==Method 6 (Use Min Heap)==
This method is mainly an optimization of method 1. Instead of using temp[] array, use Min Heap.

1) Build a Min Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array. O(k)

2) For each element, after the kth element (arr[k] to arr[n-1]), compare it with root of MH.
...a) If the element is greater than the root then make it root and call heapify for MH
...b) Else ignore it.
#  The step 2 is O((n-k)*logk)

3) Finally, MH has k largest elements and root of the MH is the kth largest element.

Time Complexity: O(k + (n-k)Logk) without sorted output. If sorted output is needed then
O(k + (n-k)Logk + kLogk)

All of the above methods can also be used to find the kth largest (or smallest) element.

"""
from heapq import heappush, heappop, heapify
import typing


def kLargest(arr: typing.List[int], k: int):
    # Sort the given array arr in reverse order This method doesn't work with primitive data
    # types. So, instead of int, Integer type array will be used
    arr.sort(reverse=True)

    # Print the first kth largest elements
    for i in range(k):
        print(arr[i], end=" ")


class MinHeap:
    """
    heappop - pop and return the smallest element from heap
    heappush - push the value item onto the heap, maintaining heap invariant
    heapify - transform list into heap, in place, in linear time
    """
    # Constructor to initialize a heap

    def __init__(self, arr: typing.List[int], k: int):
        self.heap = []
        for i in range(k):
            self.heap.append(arr[i])
        heapify(self.heap)

    def parent(self, i):
        return (i - 1) // 2

    def insert_key(self, k):
        """ Inserts a new key 'k' """
        heappush(self.heap, k)

    def decrease_key(self, i, new_val):
        """
        Decrease value of key at index 'i' to new_val

        It is assumed that new_val is smaller than heap[i]
        """
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

    # Method to remove minimum element from min heap
    def extract_min(self):
        return heappop(self.heap)

    def delete_key(self, i):
        """
        This function deletes key at index i. It first reduces value to minus infinite and
        then calls extractMin()
        """
        self.decrease_key(i, float("-inf"))
        self.extract_min()

    # Get the minimum element from the heap
    def get_min(self):
        return self.heap[0]


def first_K_elements(arr: typing.List[int], size: int, k: int):
    # Creating Min Heap for given array with only k elements
    min_heap = MinHeap(arr, k)

    # Loop For each element in array after the kth element
    for i in range(k, size):
        # if current element is smaller than minimum element, do nothing and
        # continue to next element
        if (min_heap.heap[0] > arr[i]):
            continue

        # Otherwise Change minimum element to current element, and call heapify to
        # restore the heap property
        else:
            min_heap.heap[0] = arr[i]
            heapify(min_heap.heap)

    # Now min heap contains k maximum elements, Iterate and print
    for i in range(k):
        print(min_heap.extract_min(), end=" ")
    print("----")


if __name__ == '__main__':
    arr = [1, 23, 12, 9, 30, 2, 50]
    # arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
    k = 3
    size = len(arr)
    # kLargest(arr, k)

    first_K_elements(arr, size, k)
