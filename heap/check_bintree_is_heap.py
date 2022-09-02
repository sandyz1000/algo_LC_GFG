"""
Given a binary tree we need to check it has heap property or not, Binary tree need to fulfill
following two conditions for being a heap:

1)  It should be a complete tree (i.e. all levels except last should be full).
2)  Every node's value should be greater than or equal to its child node (considering max-heap).

For example this tree contains heap property -

                97
              /    \
             46    37
            /  \  / \
           12  3 7  31
          / \
         6  9

While this doesn't -

                 97
               /    \
              46    37
             / \   / \
            12  3 7  31
               / \
              2  4

"""
# Python program to checks if a binary tree is max heap ot not


class Node(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class IsHeap(object):
    """
    We check each of the above condition separately, for checking completeness isComplete and for
    checking heap isHeapUtil function are written.

    Detail about isComplete function can be found here.

    isHeapUtil function is written considering following things -

    1.  Every Node can have 2 children, 0 child (last level nodes) or 1 child (there can be at most
        one such node).
    2.  If Node has No child then it's a leaf node and return true (Base case)
    3.  If Node has one child (it must be left child because it is a complete tree) then we need
        to compare this node with its single child only.
    4.  If Node has both child then check heap property at Node and recur for both subtrees.

    """

    def count_nodes(self, root):
        """
        This function counts the number of nodes in a binary tree
        :param root:
        :return:
        """
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def is_complete_utility(self, root, index, number_nodes):
        """
        This function checks if the binary tree is complete or not
        :param root:
        :param index:
        :param number_nodes:
        :return:
        """
        # An empty tree is complete
        if root is None:
            return True

        # If index assigned to current node is more than
        # number of nodes in tree, then tree is not complete
        if index >= number_nodes:
            return False

        # Recur for left and right subtrees
        return self.is_complete_utility(root.left, 2 * index + 1, number_nodes) and \
            self.is_complete_utility(root.right, 2 * index + 2, number_nodes)

    def is_heap_utility(self, root):
        """
        ### This Function checks the heap property in the tree.
        :param root:
        :return:
        """
        # Base case : single node satisfies property
        if root.left is None and root.right is None:
            return True

        # node will be in second last level
        if root.right is None:
            # check heap property at Node
            # No recursive call , because no need to check last level
            return root.key >= root.left.key

        else:
            # Check heap property at Node and
            # Recursive check heap property at left and right subtree
            if root.key >= root.left.key and root.key >= root.right.key:
                return self.is_heap_utility(root.left) and self.is_heap_utility(root.right)
            else:
                return False

    def is_heap(self, root):
        """
        Function to check binary tree is a Heap or Not.
        :param root:
        :return:
        """
        # These two are used in isCompleteUtil()
        node_count = self.count_nodes(root)
        index = 0

        if self.is_complete_utility(root, index, node_count) and self.is_heap_utility(root):
            return True
        return False


if __name__ == '__main__':
    root = None
    root = Node(10)
    root.left = Node(9)
    root.right = Node(8)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
    root.left.left.left = Node(3)
    root.left.left.right = Node(2)
    root.left.right.left = Node(1)
    test = IsHeap()
    print("Given binary tree is a Heap\n" if test.is_heap(root) else
          "Given binary tree is not a Heap\n")
