"""
LRU Cache Implementation

How to implement LRU caching scheme? What data structures should be used? We are given
total possible page numbers that can be referred. We are also given cache (or memory)
size (Number of page frames that cache can hold at a time). The LRU caching scheme is
to remove the least recently used frame when the cache is full and a new page is
referenced which is not there in cache.

We use two data structures to implement an LRU Cache.

1. Queue which is implemented using a doubly linked list. The maximum size of the queue
will be equal to the total number of frames available (cache size).The most recently
used pages will be near front end and least recently pages will be near rear end.

2. A Hash with page number as key and address of the corresponding queue node as value.

When a page is referenced, the required page may be in the memory. If it is in the
memory, we need to detach the node of the list and bring it to the front of the queue.
If the required page is not in the memory, we bring that in memory. In simple words,
we add a new node to the front of the queue and update the corresponding node address
in the hash. If the queue is full, i.e. all the frames are full, we remove a node from
the rear of queue, and add the new node to the front of queue.

Example - Consider the following reference string :

1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 Find the number of page faults using least recently
used (LRU) page replacement algorithm with 3 page frames.

---------------------------------------------
Explanation -
---------------------------------------------

REFER-DIAGRAM
http://www.geeksforgeeks.org/lru-cache-implementation/

"""
from __future__ import print_function


# Python program to show implementation of LRU cache

# A Queue Node (Queue is implemented using Doubly Linked List)
class QNode:
    def __init__(self, page_number, prev_node=None, next_node=None):
        self.pageNumber = page_number  # the page number stored in this QNode
        self.prev = prev_node
        self.next = next_node


# A Queue (A FIFO collection of Queue Nodes)
class Queue:
    def __init__(self, number_of_frames, front=None, rear=None):
        self.count = 0  # Number of filled frames
        self.numberOfFrames = number_of_frames  # total number of frames
        self.front = front
        self.rear = rear


# A hash (Collection of pointers to Queue Nodes)
class Hash:
    def __init__(self, capacity):
        self.capacity = capacity  # how many pages can be there
        self.arr = [None for i in range(self.capacity)]  # an array of queue nodes


class LRUCache(object):
    def __init__(self, hash, q):
        self.hash = hash
        self.queue = q

    @staticmethod
    def _are_all_frames_full(queue):
        """A function to check if there is slot available in memory
        """
        return queue.count == queue.numberOfFrames

    @staticmethod
    def _is_queue_empty(queue):
        """A utility function to check if queue is empty
        """
        return queue.rear is None

    def dequeue(self):
        """A utility function to delete a frame from queue
        """
        if self._is_queue_empty(self.queue):
            return

        # If this is the only node in list, then change front
        if self.queue.front == self.queue.rear:
            self.queue.front = None

        # Change rear and remove the previous rear
        self.queue.rear = self.queue.rear.prev

        if self.queue.rear:
            self.queue.rear.next = None

        # decrement the number of full frames by 1
        self.queue.count -= 1

    def enqueue(self, pageNumber):
        """A function to add a page with given 'pageNumber' to both queue and hash
        """
        # If all frames are full, remove the page at the rear
        if self._are_all_frames_full(self.queue):
            # remove page from hash
            hash.arr[self.queue.rear.pageNumber] = None
            self.dequeue()

        # Create a new node with given page number, And add the new node to the front
        # of queue
        temp = QNode(pageNumber)
        temp.next = self.queue.front

        # If queue is empty, change both front and rear pointers
        if self._is_queue_empty(self.queue):
            self.queue.rear = self.queue.front = temp
        else:
            # Else change the front
            self.queue.front.prev = temp
            self.queue.front = temp

        # Add page entry to hash also
        hash.arr[pageNumber] = temp

        # increment number of full frames
        self.queue.count += 1

    def reference_page(self, page_number):
        """ This function is called when a page with given 'page_number' is referenced
        from cache (or memory). There are two cases:

        1. Frame is not there in memory, we bring it in memory and add to the front of
        queue
        2. Frame is there in memory, we move the frame to front of queue
        """
        req_page = self.hash.arr[page_number]

        # the page is not in cache, bring it
        if req_page is None:
            self.enqueue(page_number)

        # page is there and not at front, change pointer
        elif req_page != self.queue.front:
            # Unlink requested page from its current location in queue.
            req_page.prev.next = req_page.next
            if req_page.next:
                req_page.next.prev = req_page.prev

            # If the requested page is rear, then change rear as this node will be moved
            # to front
            if req_page == self.queue.rear:
                self.queue.rear = req_page.prev
                self.queue.rear.next = None

            # Put the requested page before current front
            req_page.next = self.queue.front
            req_page.prev = None

            # Change prev of current front
            req_page.next.prev = req_page

            # Change front to the requested page
            self.queue.front = req_page


if __name__ == '__main__':
    # 5 4 1 3
    # Let cache can hold 4 pages

    q = Queue(4)

    # Let 10 different pages can be requested (pages to be referenced are numbered from
    # 0 to 9
    hash = Hash(10)

    test = LRUCache(hash, q)
    # Let us refer pages 1, 2, 3, 1, 4, 5
    test.reference_page(1)
    test.reference_page(2)
    test.reference_page(3)
    test.reference_page(1)
    test.reference_page(4)
    test.reference_page(5)

    # Let us print cache frames after the above referenced pages
    print("%d" % q.front.pageNumber, end=" ")
    print("%d" % q.front.next.pageNumber, end=" ")
    print("%d" % q.front.next.next.pageNumber, end=" ")
    print("%d" % q.front.next.next.next.pageNumber, end=" ")
