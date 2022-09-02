"""
K'th Smallest/Largest Element in Unsorted Array | Set 1

http://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

Given an array and a number k where k is smaller than size of array, we need to find the k'th
smallest element in the given array. It is given that all array elements are distinct.

Examples:

Input: arr = [7, 10, 4, 3, 20, 15], k = 3
Output: 7

Input: arr = [7, 10, 4, 3, 20, 15], k = 4
Output: 10
"""
import typing
import sys
from heapq import heapify, heappop, heappush
INT_MAX = sys.maxsize


class MaxHeapCustom(object):
    """A class for Max Heap"""

    def __init__(self, a, size):
        self.harr = a  # pointer to array of elements in heap
        self.capacity = 0  # maximum possible size of min heap
        self.heap_size = size  # Current number of elements in min heap

        i = (self.heap_size - 1) // 2
        while i >= 0:
            self.max_heapify(i)
            i -= 1

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def get_max(self):
        return self.harr[0]  # Returns maximum

    def replace_max(self, x):
        """to replace root with new node x and heapify() new root"""
        self.harr[0] = x
        self.max_heapify(0)

    def extract_max(self):
        """Method to remove maximum element (or root) from max heap"""
        if self.heap_size == 0:
            return INT_MAX

        # // Store the maximum value.
        root = self.harr[0]

        # If there are more than 1 items, move the last item to root and call heapify.
        if self.heap_size > 1:
            self.harr[0] = self.harr[self.heap_size - 1]
            self.max_heapify(0)
        self.heap_size -= 1

        return root

    def max_heapify(self, i):
        """A recursive method to heapify a subtree with root at given index. This method
        assumes that the subtrees are already heapified"""
        left = self.left(i)
        right = self.right(i)
        largest = i
        if left < self.heap_size and self.harr[left] > self.harr[i]:
            largest = left
        if right < self.heap_size and self.harr[right] > self.harr[largest]:
            largest = right
        if largest != i:
            self.harr[i], self.harr[largest] = self.harr[largest], self.harr[i]
            self.max_heapify(largest)


class MinHeapCustom(object):
    """A class for Min Heap"""

    def __init__(self, a, size):
        self.harr = a  # pointer to array of elements in heap
        self.capacity = 0  # maximum possible size of min heap
        self.heap_size = size  # Current number of elements in min heap

        i = (self.heap_size - 1) // 2
        while i >= 0:
            self.min_heapify(i)
            i -= 1

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    def getMin(self):
        return self.harr[0]

    def extract_min(self):
        """Method to remove minimum element (or root) from min heap"""
        if self.heap_size == 0:
            return INT_MAX

        root = self.harr[0]  # Store the minimum value.

        # If there are more than 1 items, move the last item to root and call heapify.
        if self.heap_size > 1:
            self.harr[0] = self.harr[self.heap_size - 1]
            self.min_heapify(0)

        self.heap_size -= 1
        return root

    def min_heapify(self, i):
        """
        A recursive method to heapify a subtree with root at given index
        This method assumes that the subtrees are already heapified
        :param i:
        :return:
        """
        l = self.left(i)
        r = self.right(i)
        smallest = i

        if l < self.heap_size and self.harr[l] < self.harr[i]:
            smallest = l

        if r < self.heap_size and self.harr[r] < self.harr[smallest]:
            smallest = r

        if smallest != i:
            self.harr[i], self.harr[smallest] = self.harr[smallest], self.harr[i]
            self.min_heapify(smallest)


# ======== Min and Max heap ========= #
class MaxHeap:
    """
    heappop - pop and return the largest element from heap
    heappush - push the value item onto the heap, maintaining heap invariant
    heapify - transform list into heap, in place, in linear time
    """
    @staticmethod
    def MaxHeapObj():
        class maxheap_struct(object):
            def __init__(self, val): self.val = val
            def __lt__(self, other): return self.val > other.val
            def __eq__(self, other): return self.val == other.val
            def __str__(self): return str(self.val)
        return maxheap_struct
    
    def __init__(self, arr: typing.List[int], k: int) -> None:
        self.heap: typing.List[self.MaxHeapObj] = []
        for i in range(k):
            self.heap.append(self.MaxHeapObj(arr[i]))
        heapify(self.heap)

    def parent(self, i: int):
        return (i - 1) // 2
    
    def insert_key(self, k) -> None:
        heappush(self.heap, self.MaxHeapObj(k))
    
    def increase_key(self, i: int, new_val: int):
        self.heap[i] = self.MaxHeapObj(new_val)
        while i != 0 and self.heap[self.parent(i)].val < self.heap[i].val:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

    def extract_max(self) -> int:
        return heappop(self.heap).val
    
    def delete_key(self, i) -> None:
        self.increase_key(i, float('inf'))
        self.extract_max()


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


# A Python program to find k'th smallest element using min heap
class KSmallestUnsorted(object):
    def kth_smallest_method1(self, arr, n, k):
        """
        Method 1 (Simple Solution)
        A Simple Solution is to sort the given array using a O(nlogn)
        sorting algorithm like Merge Sort, Heap Sort, etc and return the element at index k-1 in
        the sorted array. Time Complexity of this solution is O(nLogn).
        Function to return k'th smallest element in a given array
        :param arr:
        :param n:
        :param k:
        :return:
        """
        arr.sort()  # Sort the given array
        # Return k'th element in the sorted array
        return arr[k - 1]

    def kth_smallest_method2(self, arr, n, k):
        """
        Method 2 (Using Min Heap - HeapSelect)
        We can find k'th smallest element in time complexity better than O(nLogn). A simple
        optimization is to create a Min Heap of the given n elements and call extractMin() k times.
        Time complexity of this solution is O(n + kLogn).

        Function to return k'th smallest element in a given array
        :param arr:
        :param n:
        :param k:
        :return:
        """
        # Build a heap of n elements: O(n) time
        mh = MinHeapCustom(arr, n)

        # Do extract min (k-1) times
        for i in range(k - 1):
            mh.extract_min()
        return mh.getMin()  # Return root

    def kth_smallest_method3(self, arr, n, k):
        """
        Method 3 (Using Max-Heap)
        We can also use Max Heap for finding the k'th smallest element.
        Restrict the size of the heap to k element

        Following is algorithm.
        1) Build a Max-Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array. O(k)
        2) For each element, after the k'th element (arr[k] to arr[n-1]), compare it with root of
        MH.
            a) If the element is less than the root then make it root and call heapify for MH
            b) Else ignore it.
        The step 2 is O((n-k)*logk)
        3) Finally, root of the MH is the kth smallest element.
        Time complexity of this solution is O(k + (n-k)*Logk)

        Function to return k'th largest element in a given array
        :param arr:
        :param n:
        :param k:
        :return:
        """
        # Build a heap of first k elements: O(k) time
        mh = MaxHeapCustom(arr, k)

        # Process remaining n-k elements.  If current element is smaller than root,
        # replace root with current element
        for i in range(k, n):
            if arr[i] < mh.get_max():
                mh.replace_max(arr[i])

        return mh.get_max()  # Return root

    def kth_smallest_method4(self, arr, l, r, k):
        """
        Method 4 (QuickSelect)

        This is an optimization over method 1 if QuickSort is used as a sorting algorithm in
        first step. In QuickSort, we pick a pivot element, then move the pivot element to its
        correct position and partition the array around it. The idea is, not to do complete
        quicksort, but stop at the point where pivot itself is k'th smallest element. Also,
        not to recur for both left and right sides of pivot, but recur for one of them according
        to the position of pivot.

        The worst case time complexity of this method is O(n^2), but it works in O(n) on average.

        This function returns k'th smallest element in arr[l..r] using
        QuickSort based method.  ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT
        :param arr: List[int]
        :param l:
        :param r:
        :param k:
        :return:
        """
        # If k is smaller than number of elements in array
        if 0 < k <= r - l + 1:
            # Partition the array around last element and get position of pivot element
            # in sorted array
            pos = self.partition(arr, l, r)
            if pos - l == k - 1:  # If position is same as k
                return arr[pos]

            # If position is more, recur for left sub-array
            if pos - l > k - 1:
                return self.kth_smallest_method4(arr, l, pos - 1, k)
            # Else recur for right sub-array (k -1) - (pos -1)
            return self.kth_smallest_method4(arr, pos + 1, r, (k - 1) - (pos - l))

        # If k is more than number of elements in array
        return INT_MAX

    def partition(self, arr, left, right):
        """
        Standard partition process of QuickSort(). It considers the last element as pivot
        and moves all smaller element to left of it and greater elements to right

        :param arr: List[int]
        :param left: int
        :param right: int
        :return:
        """
        x, i = arr[right], left
        for j in range(left, right):
            if arr[j] <= x:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[right] = arr[right], arr[i]
        return i


if __name__ == '__main__':
    test = KSmallestUnsorted()
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3
    print("K'th smallest element is %d " % test.kth_smallest_method1(arr, n, k))

    # arr = [12, 3, 5, 7, 19]
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3
    print("K'th smallest element is %d " % test.kth_smallest_method2(arr, n, k))

    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3
    print("K'th smallest element is %d " % test.kth_smallest_method3(arr, n, k))

    arr = [12, 3, 5, 7, 4, 19, 26]
    # arr = [12, 3, 35, 37, 34, 19, 26]
    n = len(arr)
    k = 3
    # k = 5
    print("K'th smallest element is %d " % test.kth_smallest_method4(arr, 0, n - 1, k))
