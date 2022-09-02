"""
Design a Data Structure for the following operations. The data structure should be efficient
enough to accommodate the operations according to their frequency.

1)  findMin() : Returns the minimum item.
    Frequency: Most frequent

2)  findMax() : Returns the maximum item.
    Frequency: Most frequent

3)  deleteMin() : Delete the minimum item.
    Frequency: Moderate frequent

4)  deleteMax() : Delete the maximum item.
    Frequency: Moderate frequent

5)  Insert() : Inserts an item.
    Frequency: Least frequent

6)  Delete() : Deletes an item.
    Frequency: Least frequent.

Explanation: 
=============================================
A simple solution is to maintain a sorted array where smallest element is at first position
and largest element is at last. The time complexity of findMin(), findMAx() and deleteMax()
is O(1). But time complexities of deleteMin(), insert() and delete() will be O(n).

Can we do the most frequent two operations in O(1) and other operations in O(Logn) time?.

The idea is to use two binary heaps (one max and one min heap). The main challenge is,
while deleting an item, we need to delete from both min-heap and max-heap. So, we need some
kind of mutual data structure. In the following design, we have used doubly linked list as a
mutual data structure. The doubly linked list contains all input items and indexes of
corresponding min and max heap nodes. The nodes of min and max heaps store addresses of nodes
of doubly linked list. The root node of min heap stores the address of minimum item in doubly
linked list. Similarly, root of max heap stores address of maximum item in doubly linked
list. Following are the details of operations.

1) findMax(): We get the address of maximum value node from root of Max Heap. So this is a
O(1) operation.

1) findMin(): We get the address of minimum value node from root of Min Heap. So this is a
O(1) operation.

3) deleteMin(): We get the address of minimum value node from root of Min Heap. We use this
address to find the node in doubly linked list. From the doubly linked list, we get node of
Max Heap. We delete node from all three. We can delete a node from doubly linked list in O(1)
time. delete() operations for max and min heaps take O(Logn) time.

4) deleteMax(): is similar to deleteMin()

5) Insert() We always insert at the beginning of linked list in O(1) time. Inserting the
address in Max and Min Heaps take O(Logn) time. So overall complexity is O(Logn)

6) Delete() We first search the item in Linked List. Once the item is found in O(n) time,
we delete it from linked list. Then using the indexes stored in linked list, we delete it
from Min Heap and Max Heaps in O(Logn) time. So overall complexity of this operation is O(n).
The Delete operation can be optimized to O(Logn) by using a balanced binary search tree
instead of doubly linked list as a mutual data structure. Use of balanced binary search will
not effect time complexity of other operations as it will act as a mutual data structure like
doubly Linked List.
"""

from __future__ import print_function
import sys

INF = sys.maxsize


class LNode(object):
    def __init__(self, data, min_heap_index, max_heap_index, next_node=None, prev_node=None):
        self.data = data
        self.min_heap_index = min_heap_index
        self.max_heap_index = max_heap_index
        self.next_node = next_node
        self.prev_node = prev_node


class List(object):
    """Structure for a doubly linked list"""

    def __init__(self, head=None):
        self.head = head


# Structure for min heap
class MinHeap(object):
    def __init__(self, capacity=0, size=0, m_array=[]):
        self.size = size
        self.capacity = capacity
        self.array = m_array


# Structure for max heap
class MaxHeap(object):
    def __init__(self, capacity=0, size=0, m_array=[]):
        self.size = size
        self.capacity = capacity
        self.array = m_array


# The required data structure
class MyDataStructure(object):

    def __init__(self, capacity):
        self.minHeap = self.create_min_heap(capacity)
        self.maxHeap = self.create_max_heap(capacity)
        self.llist = self.create_list()

    def create_max_heap(self, capacity):
        """Utility function to create a max heap of given capacity"""
        m_array = [LNode(None, None, None)] * capacity
        maxHeap = MaxHeap(capacity, 0, m_array)
        return maxHeap

    def create_min_heap(self, capacity):
        """Utility function to create a min heap of given capacity"""
        m_array = [LNode(None, None, None)] * capacity
        minHeap = MinHeap(capacity, 0, m_array)
        return minHeap

    def create_list(self):
        """Utility function to create a List"""
        return List()

    def new_lnode(self, data):
        """A utility function to create a new List node"""
        node = LNode(data, -1, -1)
        return node

    def is_max_heap_empty(self):
        """Some basic operations for heaps and List"""
        return self.maxHeap.size == 0

    def is_min_heap_empty(self):
        return self.minHeap.size == 0

    def is_max_heap_full(self):
        return self.maxHeap.size == self.maxHeap.capacity

    def is_min_heap_full(self):
        return self.minHeap.size == self.minHeap.capacity

    def is_list_empty(self):
        return not self.llist.head

    def has_only_one_lnode(self):
        return not self.llist.head.next_node and not self.llist.head.prev_node

    def min_heapify(self, index):
        """
        The standard minheapify function.  The only thing it does extra is swapping
        indexes of heaps inside the List

        :param index:
        :return:
        """
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        min_heap = self.minHeap

        if left < min_heap.size and min_heap.array[left] and \
                min_heap.array[left].data < min_heap.array[smallest].data:
            smallest = left

        if right < min_heap.size and min_heap.array[right] and \
                min_heap.array[right].data < min_heap.array[smallest].data:
            smallest = right

        if smallest != index:
            # First swap indexes inside the List using address of List nodes
            min_heap.array[smallest].min_heap_index, min_heap.array[index].min_heap_index = \
                min_heap.array[index].min_heap_index, min_heap.array[smallest].min_heap_index

            # Now swap pointers to List nodes
            min_heap.array[smallest], min_heap.array[index] = \
                min_heap.array[index], min_heap.array[smallest]

            # Fix the heap downward
            self.min_heapify(smallest)

    def max_heapify(self, index):
        """
        The standard maxHeapify function.  The only thing it does extra
        is swapping indexes of heaps inside the List

        :param index:
        :return:
        """
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        max_heap = self.maxHeap

        if left < max_heap.size and max_heap.array[left] and \
                max_heap.array[left].data > max_heap.array[largest].data:
            largest = left

        if right < max_heap.size and max_heap.array[right] and \
                max_heap.array[right].data > max_heap.array[largest].data:
            largest = right

        if largest != index:
            # First swap indexes inside the List using address of List nodes
            max_heap.array[largest].max_heap_index, max_heap.array[index].max_heap_index = \
                max_heap.array[index].max_heap_index, max_heap.array[largest].max_heap_index

            max_heap.array[largest], max_heap.array[index] = \
                max_heap.array[index], max_heap.array[largest]

            # Fix the heap downward
            self.max_heapify(largest)

    def insert_min_heap(self, temp):
        """
        Standard function to insert an item in Min Heap
        :param temp:
        :return:
        """
        if self.is_min_heap_full():
            return

        self.minHeap.size += 1
        i = self.minHeap.size - 1
        while i and temp.data < self.minHeap.array[(i - 1) // 2].data:
            self.minHeap.array[i] = self.minHeap.array[(i - 1) // 2]
            self.minHeap.array[i].min_heap_index = i
            i = (i - 1) // 2

        self.minHeap.array[i] = temp
        self.minHeap.array[i].min_heap_index = i

    def insert_max_heap(self, temp):
        """
        :param temp:
        :return:
        """
        if self.is_max_heap_full():
            return

        self.maxHeap.size += 1
        i = self.maxHeap.size - 1
        while i and temp.data > self.maxHeap.array[(i - 1) // 2].data:
            self.maxHeap.array[i] = self.maxHeap.array[(i - 1) // 2]
            self.maxHeap.array[i].max_heap_index = i
            i = (i - 1) // 2

        self.maxHeap.array[i] = temp
        self.maxHeap.array[i].max_heap_index = i

    def find_min(self):
        """Function to find minimum value stored in the main data structure"""
        if self.is_min_heap_empty():
            return INF

        return self.minHeap.array[0].data

    def find_max(self):
        """Function to find maximum value stored in the main data structure"""
        if self.is_max_heap_empty():
            return INF

        return self.maxHeap.array[0].data

    def remove_lnode(self, temp):
        """
        A utility function to remove an item from linked list
        :param temp:
        :return:
        """
        if self.has_only_one_lnode():
            self.llist.head = None

        elif not temp.prev_node:  # first node
            self.llist.head = temp.next_node
            temp.next_node.prev_node = None

        else:  # any other node including last
            temp.prev_node.next_node = temp.next_node
            if temp.next_node:  # last node
                temp.next_node.prev_node = temp.prev_node

    def delete_max(self):
        """Function to delete maximum value stored in the main data structure"""
        if self.is_max_heap_empty():
            return

        temp = self.maxHeap.array[0]

        # delete the maximum item from maxHeap
        self.maxHeap.array[0] = self.maxHeap.array[self.maxHeap.size - 1]
        self.maxHeap.size -= 1

        self.maxHeap.array[0].max_heap_index = 0
        self.max_heapify(0)

        # remove the item from minHeap
        self.minHeap.array[temp.min_heap_index] = self.minHeap.array[self.minHeap.size - 1]
        self.minHeap.size -= 1

        self.minHeap.array[temp.min_heap_index].min_heap_index = temp.min_heap_index
        self.min_heapify(temp.min_heap_index)

        # remove the node from List
        self.remove_lnode(temp)

    def delete_min(self):
        """Function to delete minimum value stored in the main data structure"""
        if self.is_min_heap_empty():
            return

        temp = self.minHeap.array[0]

        # delete the minimum item from minHeap
        self.minHeap.array[0] = self.minHeap.array[self.minHeap.size - 1]
        self.minHeap.size -= 1
        self.minHeap.array[0].min_heap_index = 0
        self.min_heapify(0)

        # remove the item from maxHeap
        self.maxHeap.array[temp.max_heap_index] = self.maxHeap.array[self.maxHeap.size - 1]
        self.maxHeap.size -= 1
        self.maxHeap.array[temp.max_heap_index].max_heap_index = temp.max_heap_index
        self.max_heapify(temp.max_heap_index)
        self.remove_lnode(temp)  # remove the node from List

    def insert_at_head(self, temp):
        """
        Function to enList an item to List
        :param temp:
        :return:
        """
        if self.is_list_empty():
            self.llist.head = temp
        else:
            temp.next_node = self.llist.head
            self.llist.head.prev_node = temp
            self.llist.head = temp

    def delete(self, item):
        """
        Function to delete an item from List. The function also removes item from
        min and max heaps
        :param my_ds:
        :param item:
        :return:
        """
        minHeap = self.minHeap
        maxHeap = self.maxHeap

        if self.is_list_empty():
            return

        # search the node in List
        temp = self.llist.head
        while temp and temp.data != item:
            temp = temp.next_node

        if not temp or temp and temp.data != item:  # if item not found
            return

        # remove item from min heap
        minHeap.array[temp.min_heap_index] = minHeap.array[minHeap.size - 1]
        minHeap.size -= 1
        minHeap.array[temp.min_heap_index].min_heap_index = temp.min_heap_index
        self.min_heapify(temp.min_heap_index)

        # remove item from max heap
        maxHeap.array[temp.max_heap_index] = maxHeap.array[maxHeap.size - 1]
        maxHeap.size -= 1
        maxHeap.array[temp.max_heap_index].max_heap_index = temp.max_heap_index
        self.max_heapify(temp.max_heap_index)

        self.remove_lnode(temp)  # remove node from List

    def insert(self, data):
        """insert operation for main data structure"""
        temp = self.new_lnode(data)
        self.insert_at_head(temp)  # insert the item in List
        self.insert_min_heap(temp)  # insert the item in min heap
        self.insert_max_heap(temp)  # insert the item in max heap


if __name__ == '__main__':
    datastruct = MyDataStructure(10)
    # Test Case #1
    # myDS.insert(10)
    # myDS.insert(2)
    # myDS.insert(32)
    # myDS.insert(40)
    # myDS.insert(5)

    # Test Case #2
    datastruct.insert(10)
    datastruct.insert(20)
    datastruct.insert(30)
    datastruct.insert(40)
    datastruct.insert(50)

    print("Maximum = %d \n" % datastruct.find_max())
    print("Minimum = %d \n" % datastruct.find_min())

    datastruct.delete_max()  # 50 is deleted
    print("After deleteMax()\n")
    print("Maximum = %d \n" % datastruct.find_max())
    print("Minimum = %d \n" % datastruct.find_min())

    datastruct.delete_min()  # 10 is deleted
    print("After deleteMin()\n")
    print("Maximum = %d \n" % datastruct.find_max())
    print("Minimum = %d \n" % datastruct.find_min())

    datastruct.delete(40)  # 40 is deleted
    print("After Delete()\n")
    print("Maximum = %d \n" % datastruct.find_max())
    print("Minimum = %d \n" % datastruct.find_min())
