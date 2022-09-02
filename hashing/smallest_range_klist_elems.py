"""
Find smallest range containing elements from k lists
Given k sorted lists of integers of size n each, find the smallest range that includes at least
element from each of the k lists. If more than one smallest ranges are found, print any one of them.

------------------------------------------------------
Example :
------------------------------------------------------
Input:
K = 3
arr1[] : [4, 7, 9, 12, 15]
arr2[] : [0, 8, 10, 14, 20]
arr3[] : [6, 12, 16, 30, 50]
Output:
The smallest range is [6 8]
Explanation: Smallest range is formed by
number 7 from first list, 8 from second
list and 6 from third list.


Input:
k = 3
arr1[] : [4, 7]
arr2[] : [1, 2]
arr3[] : [20, 40]
The smallest range is [2 20]

----------------------------------------------------------------------------------------------------
Naive Approach: Given K sorted list, find a range where there is at least one element from every list.
The idea to solve the problem is very simple, keep k pointers which will constitute the elements in the
range, by taking the min and max of the k elements the range can be formed. Initially, all the pointers
will point to the start of all the k arrays. Store the range max to min. If the range has to be minimised
then either the minimum value has to be increased or maximum value has to be decreased.
The maximum value cannot be decreased as the array is sorted but the minimum value can be increased. To
continue increasing the minimum value, increase the pointer of the list containing the minimum value and
update the range until one of the lists exhausts.

Algorithm:
1. Create an extra space ptr of length k to store the pointers and a variable minrange initilized to a maximum value.
2. Initially the index of every list is 0, therefore initialize every element of ptr[0..k] to 0, the array ptr will
    store the index of the elements in the range.
3. Repeat the following steps until atleast one list exhausts:
    a. Now find the minimum and maximum value among the current elements of all the list pointed by the ptr[0…k] array.
    b. Now update the minrange if current (max-min) is less than minrange.
    c. increment the pointer pointing to current minimum element.

Time complexity : O(n * k2), to find the maximum and minimum in an array of length k the time required is O(k), 
and to traverse all the k arrays of length n (in worst case), the time complexity is O(n*k), then the total time 
complexity is O(n*k2).

Space complexity: O(k), an extra array is required of length k so the space complexity is O(k)

----------------------------------------------------------------------------------------------------
A Better efficient approach is to use min heap. Below are the steps –

Efficient approach: The approach remains the same but the time complexity can be reduced by using 
min-heap or priority queue. Min heap can be used to find the maximum and minimum value in logarithmic 
time or log k time instead of linear time. Rest of the approach remains the same.

Algorithm:
1. create an Min heap to store k elements, one from each array and a variable minrange initilized to a 
maximum value and also keep a variable max to store the maximum integer.
2. Initially put the first element of each element from each list and store the maximum value in max.
3. Repeat the following steps until atleast one list exhausts :
    a. To find the minimum value or min, use the top or root of the Min heap which is the minimum element.
    b. Now update the minrange if current (max-min) is less than minrange.
    c. remove the top or root element from priority queue and insert the next element from the list which 
    contains the min element and upadate the max with the new element inserted.

Time Complexity: The while loop inside findSmallestRange() function can run maximum n*k
times. In every iteration of loop, we call heapify which takes O(Logk) time. Therefore,
the time complexity is O(nk Logk).

Space complexity: O(k). The priority queue will store k elements so the space complexity os O(k)
"""

N = 5
INT_MAX = 9999999999999
INT_MIN = -INT_MAX

# ------ IMPLEMENTATION 1 ----------
# array for storing the current index of list i
ptr = [0 for i in range(501)]


def findSmallestRange(arr, n, k):
    """
    This function takes an k sorted lists in the form of 2D array as
    an argument. It finds out smallest range that includes elements from
    each of the k lists.
    """
    i, minval, maxval, minrange, minel, maxel, flag, minind = 0, 0, 0, 0, 0, 0, 0, 0

    # initializing to 0 index
    for i in range(k + 1):
        ptr[i] = 0

    minrange = 10**9

    while(1):

        # for mainting the index of list
        # containing the minimum element
        minind = -1
        minval = 10**9
        maxval = -10**9
        flag = 0

        # iterating over all the list
        for i in range(k):

            # if every element of list[i] is
            # traversed then break the loop
            if(ptr[i] == n):
                flag = 1
                break

            # find minimum value among all the list
            # elements pointing by the ptr[] array
            if(ptr[i] < n and arr[i][ptr[i]] < minval):
                minind = i  # update the index of the list
                minval = arr[i][ptr[i]]

            # find maximum value among all the
            # list elements pointing by the ptr[] array
            if(ptr[i] < n and arr[i][ptr[i]] > maxval):
                maxval = arr[i][ptr[i]]

        # if any list exhaust we will
        # not get any better answer,
        # so break the while loop
        if(flag):
            break

        ptr[minind] += 1

        # updating the minrange
        if((maxval - minval) < minrange):
            minel = minval
            maxel = maxval
            minrange = maxel - minel

    print("The smallest range is [", minel, maxel, "]")


# ------ IMPLEMENTATION 2 ---------
class MinHeapNode:
    """A min heap node"""

    def __init__(self, element, i=None, j=None):
        self.element = element  # The element to be stored
        self.i = i  # index of the list from which the element is taken
        self.j = j  # index of the next element to be picked from list


class MinHeap:
    """A class for Min Heap"""

    def __init__(self, harr, heap_size):
        self.harr = harr  # pointer to array of elements in heap
        self.heap_size = heap_size  # size of min heap
        i = (heap_size - 1) // 2
        while i >= 0:
            self.min_heapify(i)
            i -= 1

    def left(self, i):
        """to get index of left child of node at index i"""
        return 2 * i + 1

    def right(self, i):
        """to get index of right child of node at index i"""
        return 2 * i + 2

    def get_min(self):
        return self.harr[0]

    def replace_min(self, x):
        self.harr[0] = x
        self.min_heapify(0)

    def min_heapify(self, i):
        """
        A recursive method to heapify a subtree with root at given index.
        This method assumes that the subtrees are already heapified
        """
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < self.heap_size and self.harr[l].element < self.harr[i].element:
            smallest = l

        if r < self.heap_size and self.harr[r].element < self.harr[smallest].element:
            smallest = r

        if smallest != i:
            self.harr[i], self.harr[smallest] = self.harr[smallest], self.harr[i]
            self.min_heapify(smallest)


def find_smallest_range(arr, k):

    # Create a min heap with k heap nodes. Every heap node has first element of an list
    max_range = INT_MAX
    minimum, maximum = INT_MAX, INT_MIN
    start, end = 0, 0

    harr = []
    for i in range(k):
        harr.append(MinHeapNode(arr[i][0], i, 1))
        # store max element
        if harr[i].element > maximum:
            maximum = harr[i].element

    hp = MinHeap(harr, k)  # Create the heap
    # Now one by one get the minimum element from min heap and replace it with next element
    # of its list
    while True:
        root = hp.get_min()  # Get the minimum element and store it in output
        minimum = hp.get_min().element  # update min
        if max_range > maximum - minimum + 1:
            max_range = maximum - minimum + 1
            start = minimum
            end = maximum

        # Find the next element that will replace current root of heap. The next element belongs
        # to same list as the current root.
        if root.j < N:
            root.element = arr[root.i][root.j]
            root.j += 1
            if root.element > maximum:  # update max element
                maximum = root.element
        if root.j >= N:
            break  # break if we have reached end of any list

        # Replace root with next element of list
        hp.replace_min(root)
    print("The smallest max_range is [ %d %d ]" % (start, end))


if __name__ == '__main__':
    arr = [
        [4, 7, 9, 12, 15],
        [0, 8, 10, 14, 20],
        [6, 12, 16, 30, 50]
    ]
    k = len(arr)
    findSmallestRange(arr, N, k)

    # Output : The smallest range is [6 8]
    arr = [[4, 7, 9, 12, 15],
           [0, 8, 10, 14, 20],
           [6, 12, 16, 30, 50]]
    k = len(arr)
    find_smallest_range(arr, k)
