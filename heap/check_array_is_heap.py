"""
How to check if a given array represents a Binary Heap?
Given an array, how to check if the given array represents a Binary Max-Heap.

==Example:==

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Input:  arr[] = {90, 15, 10, 7, 12, 2}
Output: True

The given array represents below tree
       90
     /    \
   15      10
  /  \     /
 7    12  2

The tree follows max-heap property as every node is greater than all of its descendants.

Input:  arr[] = {9, 15, 10, 7, 12, 11}
Output: False

The given array represents below tree
       9
     /   \
   15     10
  /  \    /
 7    12 11

The tree doesn't follows max-heap property 9 is smaller than 15 and 10, and 10 is smaller
than 11.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""


def is_heap_recur(arr, i, n):
    """
    A Simple Solution is to first check root, if it's greater than all of its descendants. Then
    check for children of root. Time complexity of this solution is O(n^2)

    An Efficient Solution is to compare root only with its children (not all descendants),
    if root is greater than its children and same is true for for all nodes, then tree is
    max-heap (This conclusion is based on transitive property of > operator, i.e., if x > y and y
    > z, then x > z).

    The last internal node is present at index (2n-2)/2 assuming that indexing begins with 0.

    Time complexity of this solution is O(n). The solution is similar to preorder traversal
    of Binary Tree.
    -------------------------------------------------------
    Returns true if arr[i..n-1] represents a max-heap
    Time complexity of this solution is O(n).
    The solution is similar to preorder traversal of Binary Tree.

    :param arr:
    :param i:
    :param n:
    :return:
    """
    if i > (n - 2) / 2:  # If a leaf node
        return True

    # If an internal node and is greater than its children, and
    # same is recursively true for the children
    size = len(arr)
    if ((2 * i + 1) < size and arr[i] >= arr[2 * i + 1]) and \
            ((2 * i + 2) < size and arr[i] >= arr[2 * i + 2]) and \
            is_heap_recur(arr, 2 * i + 1, n) and is_heap_recur(arr, 2 * i + 2, n):
        return True

    return False


def is_heap(arr, n):
    """
    An Iterative Solution is to traverse all internal nodes and check id node is greater
    than its children or not."""
    # Start from root and go till the last internal node
    for i in range((n - 2) // 2 + 1):
        # If left child is greater, return false
        if (2 * i + 1) < len(arr) and arr[2 * i + 1] > arr[i]:
            return False

        # If right child is greater, return false
        if (2 * i + 2) < len(arr) and arr[2 * i + 2] > arr[i]:
            return False
    return True


if __name__ == '__main__':
    # Output: Yes
    arr = [90, 15, 10, 7, 12, 2, 7, 3]
    n = len(arr)
    # print("Yes" if is_heap_recur(arr, 0, n) else "No")

    print("\n ---- Iterative method --- \n")
    print("Yes" if is_heap(arr, n) else "No")
