"""
Connect n ropes with minimum cost

There are given n ropes of different lengths, we need to connect these ropes into one rope.
The cost to connect two ropes is equal to sum of their lengths. We need to connect the ropes
with minimum cost.

For example if we are given 4 ropes of lengths 4, 3, 2 and 6. We can connect the ropes in
following ways.
1) First connect ropes of lengths 2 and 3. Now we have three ropes of lengths 4, 6 and 5.
2) Now connect ropes of lengths 4 and 5. Now we have two ropes of lengths 6 and 9.
3) Finally connect the two ropes and all ropes have connected.

Total cost for connecting all ropes is 5 + 9 + 15 = 29. This is the optimized cost for connecting
ropes. Other ways of connecting ropes would always have same or more cost.

Example:
If we connect 4 and 6 first (we get three strings of 3, 2 and 10), then connect 10 and 3 (we get
two strings of 13 and 2). Finally we connect 13 and 2. Total cost in this way is 10 + 13 + 15 = 38.

"""
import typing


class MinHeap:
    """
    If we observe the above problem closely, we can notice that the lengths of the ropes which
    are picked first are included more than once in total cost. Therefore, the idea is to connect
    smallest two ropes first and recur for remaining ropes. This approach is similar to Huffman
    Coding. We put smallest ropes down the tree so that they can be repeated multiple times
    rather than the longer ropes.

    Following is complete algorithm for finding the minimum cost for connecting n ropes.
    Let there be n ropes of lengths stored in an array len[0..n-1]
    1)  Create a min heap and insert all lengths into the min heap.
    2)  Do following while number of elements in min heap is not one.
        a) Extract the minimum and second minimum from min heap
        b) Add the above two extracted values and insert the added value to the min-heap.
    3)  Return the value of only left item in min heap.

    Time Complexity: Time complexity of the algorithm is O(nLogn) assuming that we use a O(nLogn)
    sorting algorithm. Note that heap operations like insert and extract take O(Logn) time.

    Algorithmic Paradigm: Greedy Algorithm
    """
    def __init__(self, capacity):
        self.size = 0  # Current size of min heap
        self.capacity = capacity  # capacity of min heap
        self.harr = [0] * capacity  # Array of minheap nodes

    @staticmethod
    def minHeapify(minHeap, idx):
        """
        The standard minHeapify function. """
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < minHeap.size and minHeap.harr[left] < minHeap.harr[smallest]:
            smallest = left

        if right < minHeap.size and minHeap.harr[right] < minHeap.harr[smallest]:
            smallest = right

        if smallest != idx:
            minHeap.harr[smallest], minHeap.harr[idx] = minHeap.harr[idx], minHeap.harr[smallest]
            MinHeap.minHeapify(minHeap, smallest)

    # A utility function to check if size of heap is 1 or not
    @staticmethod
    def is_size_one(minHeap):
        return minHeap.size == 1

    # A standard function to extract minimum value node from heap
    @staticmethod
    def extract_min(minHeap):
        temp = minHeap.harr[0]
        minHeap.harr[0] = minHeap.harr[minHeap.size - 1]
        minHeap.size -= 1
        MinHeap.minHeapify(minHeap, 0)
        return temp

    @staticmethod
    def insert_min_heap(min_heap, val):
        """
        A utility function to insert a new node to Min Heap
        """
        min_heap.size += 1
        i = min_heap.size - 1
        while i and (val < min_heap.harr[(i - 1) // 2]):
            min_heap.harr[i] = min_heap.harr[(i - 1) // 2]
            i = (i - 1) // 2
        min_heap.harr[i] = val

    @staticmethod
    def build_min_heap(min_heap):
        """
        A standard funvtion to build min heap
        :param min_heap:
        :return:
        """
        n = min_heap.size - 1
        for i in range((n - 1) // 2, -1, -1):
            MinHeap.minHeapify(min_heap, i)

    @staticmethod
    def create_and_build_min_heap(arr, size):
        """
        Creates a min heap of capacity equal to size and inserts all values from len[] in it.
        Initially size of min heap is equal to capacity
        """
        minHeap = MinHeap(size)
        for i in range(size):
            minHeap.harr[i] = arr[i]
        minHeap.size = size
        MinHeap.build_min_heap(minHeap)
        return minHeap

    @staticmethod
    def min_cost(arr: typing.List[int], n: int):
        """
        The main function that returns the minimum cost to connect n ropes of
        lengths stored in len[0..n-1]

        :param arr: list(int)
        :param n: int
        :return:
        """
        cost = 0  # Initialize result

        # Create a min heap of capacity equal to n and put all ropes in it
        min_heap = MinHeap.create_and_build_min_heap(arr, n)

        # Iterate while size of heap doesn't become 1
        while not MinHeap.is_size_one(min_heap):
            # Extract two minimum length ropes from min heap
            minimum = MinHeap.extract_min(min_heap)
            sec_min = MinHeap.extract_min(min_heap)
            cost += (minimum + sec_min)  # Update total cost

            # Insert a new rope in min heap with length equal to sum of two
            # extracted minimum lengths
            MinHeap.insert_min_heap(min_heap, minimum + sec_min)

        # Finally return total minimum cost for connecting all ropes
        return cost


if __name__ == '__main__':
    arr = [4, 3, 2, 6]
    # arr = [5, 7, 4, 2, 1, 3, 6]
    size = len(arr)
    print("Total cost for connecting ropes is %d " % MinHeap.min_cost(arr, size))
