"""
Count smaller elements on right side

Write a function to count number of smaller elements on right of each element in an array.
Given an unsorted array arr[] of distinct integers, construct another array count_smaller[] such
that count_smaller[i] contains count of smaller elements on right side of each element arr[i] in
array.

Examples:

Input:   arr = [12, 1, 2, 3, 0, 11, 4]
Output:  count_smaller  = [6, 1, 1, 1, 0, 1, 0]
----------------------------------
(Corner Cases)
Input:   arr = [5, 4, 3, 2, 1]
Output:  count_smaller = [4, 3, 2, 1, 0]
----------------------------------
Input:   arr = [1, 2, 3, 4, 5]
Output:  count_smaller = [0, 0, 0, 0, 0]
----------------------------------

"""


# Method 1 (Simple)

# Use two loops. The outer loop picks all elements from left to right. The inner loop iterates
# through all the elements on right side of the picked element and updates countSmaller[].

# Time Complexity: O(n^2)
# Auxiliary Space: O(1)


def static_vars(**kwargs):
    def decorate(func):
        for k, v in kwargs.items():
            setattr(func, k, v)
        return func

    return decorate


class CountSmaller(object):
    @staticmethod
    def construct_lower_array(arr, count_smaller, n):
        """
        :param arr: list(int)
        :param count_smaller: list(int)
        :param n: list(int)
        :return:
        """
        # initialize all the counts in countSmaller array as 0
        for i in range(n):
            count_smaller[i] = 0

        for i in range(n):
            for j in range(i + 1, n):
                if arr[j] < arr[i]:
                    count_smaller[i] += 1


class Node(object):
    def __init__(self, key, height=1, size=1, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = height
        self.size = size  # size of the tree rooted with this node


class BalanceBST(object):
    """
    Method 2 (Use Self Balancing BST)
    An AVL tree node

    A Self Balancing Binary Search Tree (AVL, Red Black,.. etc) can be used to get the solution
    in O(nLogn) time complexity. We can augment these trees so that every node N contains size
    the subtree rooted with N. We have used AVL tree in the following implementation.

    We traverse the array from right to left and insert all elements one by one in an AVL tree.
    While inserting a new key in an AVL tree, we first compare the key with root. If key is
    greater than root, then it is greater than all the nodes in left subtree of root. So we add
    the size of left subtree to the count of smaller element for the key being inserted. We
    recursively follow the same approach for all nodes down the root.

    """

    count = 0

    def height(self, N):
        """A utility function to get height of the tree rooted with N"""
        return 0 if N is None else N.height

    def size(self, N):
        """A utility function to size of the tree of rooted with N"""
        return 0 if N is None else N.size

    def right_rotate(self, y):
        """A utility function to right rotate subtree rooted with y"""
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        # Update sizes
        y.size = self.size(y.left) + self.size(y.right) + 1
        x.size = self.size(x.left) + self.size(x.right) + 1

        # Return new root
        return x

    def left_rotate(self, x):
        """A utility function to left rotate subtree rooted with x"""
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        #  Update heights
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        # Update sizes
        x.size = self.size(x.left) + self.size(x.right) + 1
        y.size = self.size(y.left) + self.size(y.right) + 1

        # Return new root
        return y

    def get_balance(self, N):
        """Get Balance factor of node N"""
        return 0 if N is None else self.height(N.left) - self.height(N.right)

    def insert(self, node, key):
        """
        Inserts a new key to the tree rotted with node. Also, updates *count
        to contain count of smaller elements for the new key
        """
        # 1.  Perform the normal BST rotation
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
            # UPDATE COUNT OF SMALLER ELEMENTS FOR KEY
            self.count += self.size(node.left) + 1

        # 2. Update height and size of this ancestor node
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        node.size = self.size(node.left) + self.size(node.right) + 1

        # 3. Get the balance factor of this ancestor node to check whether
        # this node became unbalanced
        balance = self.get_balance(node)

        # If this node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node  # return the (unchanged) node pointer

    def construct_lower_array(self, arr, count_smaller, n):
        """
        The following function updates the count_smaller array to contain count of smaller
        elements on right side.

        :param arr: List[int]
        :param count_smaller: List[int]
        :param n: int
        :return:
        """
        root = None
        # Starting from rightmost element, insert all elements one by one in an AVL tree and get
        # the count of smaller elements
        for i in range(n - 1, -1, -1):
            self.count = 0
            root = self.insert(root, arr[i])
            count_smaller[i] = self.count


if __name__ == '__main__':
    print("\n----------Method-1---------\n")
    small = CountSmaller()
    arr = [12, 10, 5, 4, 2, 20, 6, 1, 0, 2]
    n = len(arr)
    low = [0] * n
    small.construct_lower_array(arr, low, n)
    print(arr)

    print("\n----------Method-2---------\n")
    # Output: Following is the constructed smaller count array 3 1 2 2 2 0 0

    bst = BalanceBST()
    arr = [10, 6, 15, 20, 30, 5, 7]
    arr = [12, 1, 2, 3, 0, 11, 4]
    n = len(arr)

    # initialize all the counts in low array as 0
    low = [0 for i in range(n)]
    bst.construct_lower_array(arr, low, n)
    print("Following is the constructed smaller count array\n", low)
