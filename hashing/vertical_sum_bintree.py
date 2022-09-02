"""
Vertical Sum in a given Binary Tree | Set 1
https://www.geeksforgeeks.org/vertical-sum-in-binary-tree-set-space-optimized/

Given a Binary Tree, find vertical sum of the nodes that are in same vertical line.
Print all sums through different vertical lines.

------------------------------------------------------------
Examples:
------------------------------------------------------------

      1
    /   \
  2      3
 / \    / \
4   5  6   7

The tree has 5 vertical lines

Vertical-Line-1 has only one node 4 => vertical sum is 4
Vertical-Line-2: has only one node 2=> vertical sum is 2
Vertical-Line-3: has three nodes: 1,5,6 => vertical sum is 1+5+6 = 12
Vertical-Line-4: has only one node 3 => vertical sum is 3
Vertical-Line-5: has only one node 7 => vertical sum is 7

So expected output is 4, 2, 12, 3 and 7

------------------------------------------------------------
Explanation:
------------------------------------------------------------

We need to check the Horizontal Distances from root for all nodes. If two nodes have the same
Horizontal Distance (HD), then they are on same vertical line. The idea of HD is simple. HD for
root is 0, a right edge (edge connecting to right subtree) is considered as +1 horizontal
distance and a left edge is considered as -1 horizontal distance. For example, in the above tree,
HD for Node 4 is at -2, HD for Node 2 is -1, HD for 5 and 6 is 0 and HD for node 7 is +2.
We can do inorder traversal of the given Binary Tree. While traversing the tree,
we can recursively calculate HDs. We initially pass the horizontal distance as 0 for root. For
left subtree, we pass the Horizontal Distance as Horizontal distance of root minus 1. For right
subtree, we pass the Horizontal Distance as Horizontal Distance of root plus 1.

------------------------------------------------------------
------------------------------------------------------------

"""


class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.data = key
        self.left = left
        self.right = right


class LLNode:
    def __init__(self, key, next_node=None, prev_node=None):
        self.data = key
        self.next = next_node
        self.prev = prev_node


class Tree:
    """Class for a Binary Tree"""

    def __init__(self, root):
        self.root = root

    def vertical_sum(self, root):
        """A wrapper over VerticalSumUtil()"""
        if root is None:  # base case
            return
        hM = {}  # Creates an empty hashMap hM
        # Calls the vertical_sum_util() to store the vertical sum values in hM
        self.vertical_sum_util(root, 0, hM)
        # Prints the values stored by vertical_sum_util()
        print(hM.values())

    def vertical_sum_util(self, root, hD, hM):
        """
        Traverses the tree in Inoorder form and builds a hashMap hM that contains
        the vertical sum
        """
        if root is None:  # base case
            return

        # Store the values in hM for left subtree
        self.vertical_sum_util(root.left, hD - 1, hM)

        # Update vertical sum for hD of this node
        # prevSum = 0 if hD not in hM else hM[hD]
        hM[hD] = hM.get(hD, 0) + root.data

        #  Store the values in hM for right subtree
        self.vertical_sum_util(root.right, hD + 1, hM)


class VerticalSumBinaryTree(object):
    """
    Method-2
    Python implementation of space optimized solution to find vertical sum.

    Vertical Sum in Binary Tree | Set 2 (Space Optimized)
    Given a Binary Tree, find vertical sum of the nodes that are in same vertical line. Print all sums
    through different vertical lines.

    Examples:

          1
        /   \
      2      3
     / \    / \
    4   5  6   7
    The tree has 5 vertical lines

    Vertical-Line-1 has only one node 4 => vertical sum is 4
    Vertical-Line-2: has only one node 2=> vertical sum is 2
    Vertical-Line-3: has three nodes: 1,5,6 => vertical sum is 1+5+6 = 12
    Vertical-Line-4: has only one node 3 => vertical sum is 3
    Vertical-Line-5: has only one node 7 => vertical sum is 7

    So expected output is 4, 2, 12, 3 and 7

    In this post, Doubly Linked List based solution is discussed. The solution discussed
    here requires only n nodes of linked list where n is total number of vertical lines in
    binary tree. 
    
    Below is algorithm.
    -------------------
    verticalSumDLL(root)
    1)  Create a node of doubly linked list node with value 0. Let the node be llnode.
    2)  verticalSumDLL(root, llnode)

    verticalSumDLL(tnode, llnode)
    1) Add current node's data to its vertical line
        llnode.data = llnode.data + tnode.data
    2) Recursively process left subtree
    # If left child is not empty
    if (tnode.left is not None):
        if (llnode.prev is None):
            llnode.prev = LLNode(0);
            llnode.prev.next = llnode;
        
        verticalSumDLLUtil(tnode.left, llnode.prev)
    
    3)  Recursively process right subtree
    if (tnode.right is not None):
        if (llnode.next is None):
            llnode.next = LLNode(0)
            llnode.next.prev = llnode
        
        verticalSumDLLUtil(tnode.right, llnode.next);
    

    """
    def __init__(self, root):
        self.root = root

    def vertical_sum_dll(self, root):
        """
        Prints vertical sum of different vertical lines in tree.
        This method mainly uses vertical_sum_dll_util().
        """
        # Create a doubly linked list node to store sum of lines going through root.
        # Vertical sum is initialized as 0.
        llnode = LLNode(0)

        # Compute vertical sum of different lines
        self.vertical_sum_dll_util(root, llnode)

        # llnode refers to sum of vertical line going through root. Move llnode
        # to the leftmost line.
        while llnode.prev is not None:
            llnode = llnode.prev

        # Prints vertical sum of all lines starting from leftmost vertical line
        while llnode is not None:
            print(llnode.data, end=" ")
            llnode = llnode.next

    def vertical_sum_dll_util(self, tree_node, llnode):
        """Constructs linked list"""
        # Add current node's data to its vertical line (in-order traversal)
        llnode.data = llnode.data + tree_node.data

        #  Recursively process left subtree
        if tree_node.left is not None:
            if llnode.prev is None:
                llnode.prev = LLNode(0)
                llnode.prev.next = llnode
            self.vertical_sum_dll_util(tree_node.left, llnode.prev)

        # Process right subtree
        if tree_node.right is not None:
            if llnode.next is None:
                llnode.next = LLNode(0)
                llnode.next.prev = llnode
            self.vertical_sum_dll_util(tree_node.right, llnode.next)


if __name__ == '__main__':
    print("\nMethod-1")
    # Create following Binary Tree
    #       1
    #     /    \
    #   2        3
    #  / \      / \
    # 4   5    6   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = (TreeNode(3))
    root.left.left = (TreeNode(4))
    root.left.right = (TreeNode(5))
    root.right.left = (TreeNode(6))
    root.right.right = (TreeNode(7))
    t = Tree(root)

    print("Following are the values of vertical sums with the positions of the columns with "
          "respect to root")
    t.vertical_sum(root)

    print("\nMethod-2")
    # Output : Vertical Sums are 4 2 12 3 7
    # Time Complexity: O(n)

    # Let us construct the tree shown above
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Vertical Sums are")
    vsbt = VerticalSumBinaryTree(root)
    vsbt.vertical_sum_dll(root)
