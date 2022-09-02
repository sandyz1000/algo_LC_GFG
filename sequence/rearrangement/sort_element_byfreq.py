"""
Sort elements by frequency | Set 2
Given an array of integers, sort the array according to frequency of elements.

------------------------------------
Example:
------------------------------------
if the input array is {2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12}, then modify the array
to {3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}.

------------------------------------
Algorithm:
------------------------------------
Following is detailed algorithm.
1) Create a BST and while creating BST maintain the count i,e frequency of each coming element in
same BST. This step may take O(nLogn) time if a self balancing BST is used.

2) Do Inorder traversal of BST and store every element and count of each element in an auxiliary
array. Let us call the auxiliary array as 'count[]'. Note that every element of this array is
element and frequency pair. This step takes O(n) time.

3) Sort 'count[]' according to frequency of the elements. This step takes O(nLohn) time if a
O(nLogn) sorting algorithm is used.

4) Traverse through the sorted array 'count[]'. For each element x, print it 'freq' times where
'freq' is frequency of x. This step takes O(n) time.

------------------------------------
Complexity:
------------------------------------
Overall time complexity of the algorithm can be minimum O(nLogn) if we use a O(nLogn) sorting
algorithm and use a self balancing BST with O(Logn) insert operation.

"""
from functools import cmp_to_key


class DataFreq:
    """A structure to store data and its frequency"""
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq


class BSTNode(object):
    def __init__(self, data, freq=1, left=None, right=None):
        self.data = data
        self.freq = freq
        self.left = left
        self.right = right


class BST:
    index = 0

    def compare(self, a, b):
        """
        Function for qsort() implementation. Compare frequencies to
        sort the array according to decreasing order of frequency
        :param a: DataFreq
        :param b: DataFreq
        :return:
        """
        return b.freq - a.freq

    def insert(self, root, data):
        """
        :param root: BSTNode
        :param data:
        :return:
        """
        if root is None:
            return BSTNode(data)

        if data == root.data:  # If already present
            root.freq += 1
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def store(self, root, count):
        """Function to copy elements and their frequencies to count[]."""
        # Base Case
        if root is None:
            return

        # Recur for left substree
        self.store(root.left, count)

        # Store item from root and increment index
        count[self.index] = DataFreq(root.data, root.freq)
        self.index += 1

        # Recur for right subtree
        self.store(root.right, count)

    def sort_by_frequency(self, arr, n):
        """
        The main function that takes an input array as an argument and sorts the array
        items according to frequency
        :param arr: list(int)
        :param n: int
        :return:
        """
        root = None
        # Create an empty BST and insert all array items in BST struct BSTNode *root = None
        for i in range(n):
            root = self.insert(root, arr[i])

        # Create an auxiliary array 'count[]' to store data and frequency pairs.
        # The maximum size of this array would be n when all elements are different
        count = [DataFreq(None, 0)] * n
        self.store(root, count)

        # Sort the count[] array according to frequency (or count)
        # qsort(count, index, sizeof(count[0]), compare)
        count.sort(key=cmp_to_key(self.compare))

        # Finally, traverse the sorted count[] array and copy the i'th item 'freq'
        # times to original array 'arr[]'
        j = 0
        for i in range(self.index):
            for freq in range(count[i].freq, 0, -1):
                arr[j] = count[i].data
                j += 1


if __name__ == '__main__':
    # Output: 3 3 3 3 2 2 2 12 12 5 4
    bst = BST()
    arr = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
    n = len(arr)
    bst.sort_by_frequency(arr, n)
    print(arr)
