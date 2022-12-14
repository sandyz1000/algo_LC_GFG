"""
Check for Identical BSTs without building the trees
Given two arrays which represent a sequence of keys. Imagine we make a Binary Search Tree (BST)
from each array. We need to tell whether two BSTs will be identical or not without actually
constructing the tree.

-------------------------------------------
Examples:
-------------------------------------------
the input arrays are {2, 4, 3, 1} and {2, 1, 4, 3} will construct the same tree

Let the input arrays be a[] and b[]

Example 1:
a = [2, 4, 1, 3] will construct following tree.
       2
     /  \
    1    4
        /
        3

b = [2, 4, 3, 1] will also also construct the same tree.
       2
     /  \
    1    4
        /
       3
So the output is "True"

Example 2:

a = {8, 3, 6, 1, 4, 7, 10, 14, 13}
b = {8, 10, 14, 3, 6, 4, 1, 7, 13}

They both construct the same following BST, so output is "True"
           _8_
         /    \
       3      10
     /  \       \
    1     6      14
        /   \    /
       4     7  13

"""
import typing
INT_MIN = -9999999
INT_MAX = 9999999


# A Python program to check for Identical BSTs without building the trees


def is_same_bst_util(a: typing.List, b: typing.List, n: int,
                     i1: int, i2: int, minimum: int, maximum: int) -> bool:
    """
    The main function that checks if two arrays a[] and b[] of size n construct same BST. The two
    values 'min' and 'max' decide whether the call is made for left subtree or right subtree of a
    parent element. The indexes i1 and i2 are the indexes in (a[] and b[]) after which we search
    the left or right child. Initially, the call is made for INT_MIN and INT_MAX as 'min' and
    'max' respectively, because root has no parent. i1 and i2 are just after the indexes of the
    parent element in a[] and b[].    
    """        
    #   Search for a value satisfying the constraints of min and max in a[] and
    #   b[]. If the parent element is a leaf node then there must be some
    #   elements in a[] and b[] satisfying constraint.
    j, k = i1, i2
    while j < n:
        if minimum < a[j] < maximum:
            break
        j += 1

    while k < n:
        if minimum < b[k] < maximum:
            break
        k += 1

    # If the parent element is leaf in both arrays
    if j == n and k == n:
        return True

    # Return false if any of the following is true
    # a) If the parent element is leaf in one array, but non-leaf in other.
    # b) The elements satisfying constraints are not same. We either search for left child or
    # right child of the parent element (decided by min and max values).
    # The child found must be same in both arrays
    if ((j == n) ^ (k == n)) or a[j] != b[k]:
        return False

    # Make the current child as parent and recursively check for left and right
    # subtrees of it. Note that we can also pass a[k] in place of a[j] as they
    # are both are same

    # Right Subtree and Left Subtree
    return is_same_bst_util(a, b, n, j + 1, k + 1, a[j], maximum) and \
        is_same_bst_util(a, b, n, j + 1, k + 1, minimum, a[j])


def is_same_bst(a, b, n):
    return is_same_bst_util(a, b, n, 0, 0, INT_MIN, INT_MAX)


if __name__ == '__main__':
    a = [8, 3, 6, 1, 4, 7, 10, 14, 13]
    b = [8, 10, 14, 3, 6, 4, 1, 7, 13]
    n = len(a)
    print("%s\n" % "BSTs are same" if is_same_bst(a, b, n) else "BSTs not same")
