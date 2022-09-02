"""
Clone a Binary Tree with Random Pointers
http://www.geeksforgeeks.org/clone-binary-tree-random-pointers/

Given a Binary Tree where every node has following structure.

class Node:
    def __init__(self, key, left=None, right=None, _random=None):
        self.key = key
        self.left = left
        self.right = right
        self.random = _random

The random pointer points to any random node of the binary tree and can even point to None, clone
the given binary tree.


Method 1 (Use Hashing)
The idea is to store mapping from given tree nodes to clone tree nodes in hashtable. Following are detailed steps.

1) Recursively traverse the given Binary and copy key value, left pointer and right pointer to clone tree.
While copying, store the mapping from given tree node to clone tree node in a hashtable. In the following
pseudo code, ‘cloneNode’ is currently visited node of clone tree and ‘treeNode’ is currently visited node of
given tree.

   cloneNode->key  = treeNode->key
   cloneNode->left = treeNode->left
   cloneNode->right = treeNode->right
   map[treeNode] = cloneNode

2) Recursively traverse both trees and set random pointers using entries from hash table.

   cloneNode->random = map[treeNode->random]
"""

from typing import Dict
from collections import defaultdict


class Node:
    """
    A binary tree node has data, pointer to left child, a pointer to right child and
    a pointer to random node"""

    def __init__(self, key=0, left=None, right=None, _random=None):
        self.key = key
        self.left = left
        self.right = right
        self.random = _random


class CloneBinTreeUsingHashing:
    """
    Method 1 (Use Hashing)
    The idea is to store mapping from given tree nodes to clone tree node in hashtable.
    Following are detailed steps.

    1) Recursively traverse the given Binary and copy key value, left pointer and right pointer to
    clone tree. While copying, store the mapping from given tree node to clone tree node in a
    hashtable. In the following pseudo code, 'cloneNode' is currently visited node of clone tree
    and 'treeNode' is currently visited node of given tree.

       cloneNode.key  = treeNode.key
       cloneNode.left = treeNode.left
       cloneNode.right = treeNode.right
       map[treeNode] = cloneNode

    2) Recursively traverse both trees and set random pointers using entries from hash table.

       cloneNode.random = map[treeNode.random]

    Following is Python implementation of above idea.

    Note that map doesn't implement hash table, it actually is based on self-balancing
    binary search tree.

    A hashmap based Python program to clone a binary tree with random pointers
    """

    def print_inorder(self, node: Node):
        """Given a binary tree, print its Nodes in inorder"""
        if node is None:
            return

        self.print_inorder(node.left)  # First recur on left sutree
        # then print data of Node and its random
        print("[ %s ]" % ("{}.{}".format(node.key, "None") if node.random is None else
                          "{}.{}".format(node.key, node.random.key)))
        # now recur on right subtree
        self.print_inorder(node.right)

    def copy_left_right_node(self, tree_node: Node, mymap: Dict[Node, Node]):
        """
        Pre-order traversal of node to hashmap
        :param tree_node: Node
        :param mymap: defaultdict(Node)
        :return:
        """
        if tree_node is None:
            return None
        clone_node = Node(tree_node.key)
        mymap[tree_node] = clone_node
        clone_node.left = self.copy_left_right_node(tree_node.left, mymap)
        clone_node.right = self.copy_left_right_node(tree_node.right, mymap)
        return clone_node

    def copy_random(self, tree_node: Node, clone_tree: Node, mymap: Dict[Node, Node]):
        """
        This function copies random node by using the hashmap built by
        copy_left_right_node()
        """
        if clone_tree is None:
            return
        clone_tree.random = mymap[tree_node.random]
        self.copy_random(tree_node.left, clone_tree.left, mymap)
        self.copy_random(tree_node.right, clone_tree.right, mymap)

    def clone_tree(self, tree: Node):
        """
        This function makes the clone of given tree. 
        It mainly uses copy_left_right_node() and copy_random()
        """
        if tree is None:
            return None

        mymap = defaultdict(Node)
        new_tree = self.copy_left_right_node(tree, mymap)
        self.copy_random(tree, new_tree, mymap)
        return new_tree


class TempModifyBinaryTree:
    """
    Method 2 (Temporarily Modify the Given Binary Tree)

    1. Create new nodes in cloned tree and insert each new node in original tree between the left
    pointer edge of corresponding node in the original tree (See the below image). i.e. if
    current node is A and it's left child is B ( A - >> B ), then new cloned node with key A will
    be created (say cA) and it will be put as A — >> cA — >> B (B can be a None or a non-None
    left child). Right child pointer will be set correctly i.e. if for current node A,
    right child is C in original tree (A — >> C) then corresponding cloned nodes cA and cC will
    like cA —- >> cC

            1                  (1)
          /   \               /   \
         2     3             2    (3)
                            / \  /
                          (2)   2
                          /
                         2

    2. Set random pointer in cloned tree as per original tree
    i.e. if node A's random pointer points to node B, then in cloned tree, cA will point to cB
    (cA and cB are new node in cloned tree corresponding to node A and B in original tree)

    3. Restore left pointers correctly in both original and cloned tree
    """

    def print_inorder(self, node):
        """Given a binary tree, print its Nodes in inorder"""
        if node is None:
            return

        self.print_inorder(node.left)  # First recur on left sutree
        # then print data of Node and its random
        print("[ %s ]" % ("{}.{}".format(node.key, "None") if node.random is None else
                          "{}.{}".format(node.key, node.random.key)), end=" ")
        # now recur on right subtree
        self.print_inorder(node.right)

    def copy_left_right_node(self, tree_node):
        """
        This function creates new nodes cloned tree and puts new cloned node in between current
        node and it's left child

        i.e. if current node is A and it's left child is B ( A --- >> B ),
             then new cloned node with key A wil be created (say cA) and it will be put as
             A --- >> cA --- >> B

        Here B can be a None or a non-None left child Right child pointer will be set correctly
        i.e. if for current node A, right child is C in original tree
        (A --- >> C) then corresponding cloned nodes cA and cC will like
        cA ---- >> cC

        :param tree_node:
        :return:
        """
        if tree_node is None:
            return None

        a_left = tree_node.left
        tree_node.left = Node(tree_node.key)
        tree_node.left.left = a_left
        if a_left is not None:
            a_left.left = self.copy_left_right_node(a_left)

        tree_node.left.right = self.copy_left_right_node(tree_node.right)
        return tree_node.left

    def copy_random_node(self, tree_node, clone_node):
        """
        This function sets random pointer in cloned tree as per original tree i.e. if node A's
        random pointer points to node B, then in cloned tree, cA wil point to cB (cA and cB are
        new node in cloned tree corresponding to node A and B in original tree)

        :param tree_node:
        :param clone_node:
        :return:
        """
        if tree_node is None:
            return None
        if tree_node.random is not None:
            clone_node.random = tree_node.random
        else:
            clone_node.random = None

        if tree_node.left is not None and clone_node.left is not None:
            self.copy_random_node(tree_node.left.left, clone_node.left.left)

        self.copy_random_node(tree_node.right, clone_node.right)

    def restore_tree_left_node(self, tree_node, clone_node):
        """This function will restore left pointers correctly in both original and cloned tree"""
        if tree_node is None:
            return None
        if clone_node.left is not None:
            cloneLeft = clone_node.left.left
            tree_node.left = tree_node.left.left
            clone_node.left = cloneLeft
        else:
            tree_node.left = None

        self.restore_tree_left_node(tree_node.left, clone_node.left)
        self.restore_tree_left_node(tree_node.right, clone_node.right)

    def clone_tree(self, tree_node):
        """This function makes the clone of given tree"""
        if tree_node is None:
            return None

        clone_node = self.copy_left_right_node(tree_node)
        self.copy_random_node(tree_node, clone_node)
        self.restore_tree_left_node(tree_node, clone_node)
        return clone_node


def clone_bintree():
    # Output:
    # Inorder traversal of original binary tree is:
    # [4 1], [2 None], [5 3], [1 5], [3 None],
    #
    # Inorder traversal of cloned binary tree is:
    # [4 1], [2 None], [5 3], [1 5], [3 None],
    print("\n ------- Method-1 ----- ")

    cbt = CloneBinTreeUsingHashing()
    # Test No 1
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.random = tree.left.right
    tree.left.left.random = tree
    tree.left.right.random = tree.right

    # Test No 2
    # tree = None

    # Test No 3
    # tree = Node(1)

    # Test No 4
    # tree = Node(1)
    # tree.left = Node(2)
    # tree.right = Node(3)
    # tree.random = tree.right
    # tree.left.random = tree

    print("Inorder traversal of original binary tree is: \n")
    cbt.print_inorder(tree)

    clone = cbt.clone_tree(tree)

    print("\n\nInorder traversal of cloned binary tree is: \n")
    cbt.print_inorder(clone)


def tempmod_bintree():
    print("\n ------- Method-2 ----- ")
    temp = TempModifyBinaryTree()

    # print("# Test No 1")
    # tree = Node(1)
    # tree.left = Node(2)
    # tree.right = Node(3)
    # tree.left.left = Node(4)
    # tree.left.right = Node(5)
    # tree.random = tree.left.right
    # tree.left.left.random = tree
    # tree.left.right.random = tree.right
    #
    # print("# Test No 2")
    # tree = None
    #
    # print("# Test No 3")
    # tree = Node(1)
    #
    # print("# Test No 4")
    # tree = Node(1)
    # tree.left = Node(2)
    # tree.right = Node(3)
    # tree.random = tree.right
    # tree.left.random = tree
    #
    # print("# Test No 5")
    # tree = Node(1)
    # tree.left = Node(2)
    # tree.right = Node(3)
    # tree.left.left = Node(4)
    # tree.left.right = Node(5)
    # tree.right.left = Node(6)
    # tree.right.right = Node(7)
    # tree.random = tree.left

    # Output:
    # Inorder traversal of original binary tree is:
    # [5 9], [6 7], [7 None], [8 10], [9 7], [10 6], [11 9], [12 8], [13 None],
    # Inorder traversal of cloned binary tree is:
    # [5 9], [6 7], [7 None], [8 10], [9 7], [10 6], [11 9], [12 8], [13 None],

    print("# Test No 6")
    tree = Node(10)
    n2 = Node(6)
    n3 = Node(12)
    n4 = Node(5)
    n5 = Node(8)
    n6 = Node(11)
    n7 = Node(13)
    n8 = Node(7)
    n9 = Node(9)
    tree.left = n2
    tree.right = n3
    tree.random = n2
    n2.left = n4
    n2.right = n5
    n2.random = n8
    n3.left = n6
    n3.right = n7
    n3.random = n5
    n4.random = n9
    n5.left = n8
    n5.right = n9
    n5.random = tree
    n6.random = n9
    n9.random = n8

    # print("# Test No 7")
    # tree = Node(1)
    # tree.left = Node(2)
    # tree.right = Node(3)
    # tree.left.random = tree
    # tree.right.random = tree.left

    print("Inorder traversal of original binary tree is: \n")
    temp.print_inorder(tree)

    clone = temp.clone_tree(tree)

    print("\n\nInorder traversal of cloned binary tree is: \n")
    temp.print_inorder(clone)


if __name__ == '__main__':
    clone_bintree()
    tempmod_bintree()
