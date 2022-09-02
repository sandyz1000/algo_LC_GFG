"""
Find all possible binary trees with given Inorder Traversal
Last Updated: 06-12-2018
Given an array that represents Inorder Traversal, find all possible Binary Trees with the given Inorder
traversal and print their preorder traversals.

Examples:
-------------------------------------------------------------------
Input:   in[] = {3, 2};
Output:  Preorder traversals of different possible Binary Trees are:
         3 2
         2 3
Below are different possible binary trees
    3        2
     \      /
      2    3

Input:   in[] = {4, 5, 7};
Output:  Preorder traversals of different possible Binary Trees are:
          4 5 7
          4 7 5
          5 4 7
          7 4 5
          7 5 4
Below are different possible binary trees
  4         4           5         7       7
   \          \       /   \      /       /
    5          7     4     7    4       5
     \        /                  \     /
      7      5                    5   4
-------------------------------------------------------------------

Let given inorder traversal be in[]. In the given traversal, all nodes in left subtree of in[i] must
appear before it and in right subtree must appear after it. So when we consider in[i] as root, all elements
from in[0] to in[i-1] will be in left subtree and in[i+1] to n-1 will be in right subtree.
If in[0] to in[i-1] can form x different trees and in[i+1] to in[n-1] can from y different trees then
we will have x*y total trees when in[i] as root. So we simply iterate from 0 to n-1 for root. For every
node in[i], recursively find different left and right subtrees. If we take a closer look, we can notice
that the count is basically n’th Catalan number. We have discussed different approaches to find n’th Catalan
number here.

The idea is to maintain a list of roots of all Binary Trees. Recursively construct all possible left and
right subtrees. Create a tree for every pair of left and right subtree and add the tree to list.

Below is detailed algorithm.
----------------------------
1) Initialize list of Binary Trees as empty.
2) For every element in[i] where i varies from 0 to n-1,
    do following
......a)  Create a new node with key as 'arr[i]',
          let this node be 'node'
......b)  Recursively construct list of all left subtrees.
......c)  Recursively construct list of all right subtrees.
3) Iterate for all left subtrees
   a) For current leftsubtree, iterate for all right subtrees
        Add current left and right subtrees to 'node' and add
        'node' to list.

"""
from typing import List


class Node:
    # Utility to create a new node
    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None

# A utility function to do preorder traversal of BST


def preorder(root: Node) -> None:
    if root is not None:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)


def getTrees(arr: List[int], start: int, end: int) -> List:
    """
    Function for constructing all possible trees with given inorder traversal stored in an array from
    arr[start] to arr[end]. This function returns a vector of trees.

    Arguments:
        arr {[List]} -- [description]
        start {[int]} -- [description]
        end {[int]} -- [description]

    Returns:
        [List] -- [description]
    """    
    # List to store all possible trees
    trees = []

    # if start > end then subtree will be empty so returning NULL in the list
    if start > end:
        trees.append(None)
        return trees

    # Iterating through all values from start to end for constructing left and right subtree recursively
    for i in range(start, end + 1):

        # Constructing left subtree
        ltrees = getTrees(arr, start, i - 1)

        # Constructing right subtree
        rtrees = getTrees(arr, i + 1, end)

        # Looping through all left and right subtrees and connecting to ith root below
        for j in ltrees:
            for k in rtrees:

                # Making arr[i] as root
                node = Node(arr[i])

                # Connecting left subtree
                node.left = j

                # Connecting right subtree
                node.right = k

                # Adding this tree to list
                trees.append(node)
    return trees


if __name__ == "__main__":
    inp = [4, 5, 7]
    n = len(inp)

    trees = getTrees(inp, 0, n - 1)

    print("Preorder traversals of different possible Binary Trees are ")
    for i in trees:
        preorder(i)
        print("----")
