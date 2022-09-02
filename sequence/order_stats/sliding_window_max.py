"""
Sliding Window Maximum (Maximum of all subarrays of size k)
Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.

------------------------------------------
Examples:
------------------------------------------

Input :
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
Output : 3 3 4 5 5 5 6

Input :
arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13], k = 4
Output : 10 10 10 15 15 90 90

"""
from collections import deque


def print_kmax(arr, n, k):
    """
    Method 3 (A O(n) method: use Dequeue)

    We create a Dequeue, Qi of capacity k, that stores only useful elements of current window of
    k elements. An element is useful if it is in current window and is greater than all other
    elements on left side of it in current window. We process all array elements one by one and
    maintain Qi to contain useful elements of current window and these useful elements are
    maintained in sorted order. The element at front of the Qi is the largest and element at rear
    of Qi is the smallest of current window.

    Time Complexity: O(n).
    It seems more than O(n) at first look. If we take a closer look, we can observe that every
    element of array is added and removed at most once. So there are total 2n operations.

    Auxiliary Space: O(k)

    A Dequeue (Double ended queue) based method for printing maixmum element of
    all subarrays of size k
    :param arr: list(int)
    :param n: int
    :param k: int
    :return:
    """
    # Create a Double Ended Queue, Qi that will store indexes of array elements
    # The queue will store indexes of useful elements in every window and it will
    # maintain decreasing order of values from front to rear in Qi, i.e.,
    # arr[Qi.front[]] to arr[Qi.rear()] are sorted in decreasing order
    # std::deque<int>  Qi(k);
    Qi = deque()
    # Process first k (or first window) elements of array
    i = 0
    while i < k:
        # For very element, the previous smaller elements are useless so remove them from Qi
        while len(Qi) > 0 and arr[i] >= arr[Qi.index(len(Qi) - 1)]:
            Qi.popleft()  # Remove from rear

        # Add new element at rear of queue
        Qi.appendleft(i)
        i += 1

    # Process rest of the elements, i.e., from arr[k] to arr[n-1]
    while i < n:
        # The element at the front of the queue is the largest element of previous window,
        # so print it
        print(arr[Qi[0]], end=" ")
        # Remove the elements which are out of this window
        while len(Qi) > 0 and Qi[0] <= i - k:
            Qi.popleft()  # Remove from front of queue
        # Remove all elements smaller than the currently being added element (remove useless
        # elements)
        while len(Qi) > 0 and arr[i] >= arr[Qi[len(Qi) - 1]]:
            Qi.popleft()
        # Add current element at the rear of Qi
        Qi.append(i)
        i += 1

    # Print the maximum element of last window
    print(arr[Qi[0]], end=" ")


if __name__ == '__main__':
    arr = [12, 1, 78, 90, 57, 89, 56]
    n = len(arr)
    k = 3
    print_kmax(arr, n, k)
