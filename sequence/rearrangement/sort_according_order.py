"""
Sort an array according to the order defined by another array
Given two arrays A1[] and A2[], sort A1 in such a way that the relative order among the elements
will be same as those are in A2. For the elements not present in A2, append them at last in sorted
order.

Input: A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
       A2[] = {2, 1, 8, 3}
Output: A1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}

The code should handle all cases like number of elements in A2[] may be more or less
compared to A1[]. A2[] may have some elements which may not be there in A1[] and vice versa is
also possible.

"""
from functools import cmp_to_key


class SortWithBinarySearch:
    """
    ---------------------------------------------
    Method 1 (Using Sorting and Binary Search)
    ---------------------------------------------
    Let size of A1[] be m and size of A2[] be n.
    1) Create a temporary array temp of size m and copy contents of A1[] to it.
    2) Create another array visited[] and initialize all entries in it as false. visited[] is
        used to mark those elements in temp[] which are copied to A1[].
    3) Sort temp[]
    4) Initialize the output index ind as 0.
    5) Do following for every element of A2[i] in A2[]
       a) Binary search for all occurrences of A2[i] in temp[], if present then copy all occurrences
          to A1[ind] and increment ind. Also mark the copied elements visited[]
    6) Copy all unvisited elements from temp[] to A1[].

    Time complexity: The steps 1 and 2 require O(m) time. Step 3 requires O(mLogm) time. Step 5
    requires O(nLogm) time. Therefore overall time complexity is O(m + nLogm).

    Python program to sort an array according to the order defined by another array
    """

    def first(self, arr, low, high, x, n):
        """
        A Binary Search based function to find index of FIRST occurrence of x in arr[].
        If x is not present, then it returns -1
        """
        if high >= low:
            mid = low + (high - low) // 2  # (low + high)/2
            if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
                return mid

            if x > arr[mid]:
                return self.first(arr, (mid + 1), high, x, n)
            else:
                return self.first(arr, low, (mid - 1), x, n)
        return -1

    def sort_according(self, A1, A2, m, n):
        """
        Sort A1[0..m-1] according to the order defined by A2[0..n-1].

        :type A1: List(int)
        :type A2: List(int)
        :type m: int
        :type n: int
        :rtype:
        """
        # The temp array is used to store a copy of A1[] and visited[] is used mark the visited
        # elements in temp[].
        temp, visited = [A1[i] for i in range(m)], [0] * m

        # temp[:m] = sorted(temp[:m])
        temp.sort()  # Sort elements in temp

        ind = 0  # for index of output which is sorted A1[]

        # Consider all elements of A2[], find them in temp[] and copy to A1[] in order.
        for i in range(n):
            # Find index of the first occurrence of A2[i] in temp
            f = self.first(temp, 0, m - 1, A2[i], m)

            # If not present, no need to proceed
            if f == -1:
                continue

            j = f  # Copy all occurrences of A2[i] to A1[]
            while j < m and temp[j] == A2[i]:
                A1[ind] = temp[j]
                visited[j] = 1
                ind += 1
                j += 1

        # Now copy all items of temp[] which are not present in A2[]
        for i in range(m):
            if visited[i] == 0:
                A1[ind] = temp[i]
                ind += 1


class SortWithSelfBalancingTree:
    """
    ---------------------------------------------
    Method 2 (Using Self-Balancing Binary Search Tree)
    ---------------------------------------------
    We can also use a self balancing BST like AVL Tree, Red Black Tree, etc. Following are detailed
    steps.

    1) Create a self balancing BST of all elements in A1[]. In every node of BST, also keep track of
    count of occurrences of the key and a bool field visited which is initialized as false for all
    nodes.
    2) Initialize the output index ind as 0.
    3) Do following for every element of A2[i] in A2[]
      a) Search for A2[i] in the BST, if present then copy all occurrences to A1[ind] and increment
      ind. Also mark the copied elements visited in the BST node.
    4) Do an inorder traversal of BST and copy all unvisited keys to A1[].

    Time Complexity of this method is same as the previous method. Note that in a self balancing
    Binary Search Tree, all operations require logm time.

    """


class SortWithHashing:
    """
    ---------------------------------------------
    Method 3 (Use Hashing)
    ---------------------------------------------
    1. Loop through A1[], store the count of every number in a HashMap (key: number, value: count
    of number) .
    2. Loop through A2[], check if it is present in HashMap, if so, put in output array that many
    times and remove the number from HashMap.
    3. Sort the rest of the numbers present in HashMap and put in output array.

    Time Complexity: The steps 1 and 2 on average take O(m+n) time under the assumption that we
    have a good hashing function that takes O(1) time for insertion and search on average. The
    third step takes O(pLogp) time where p is the number of elements remained after considering
    elements of A2[].

    """


class SortWithCustomizedCompare:
    """
    ---------------------------------------------
    Method 4 (By Writing a Customized Compare Method)
    ---------------------------------------------
    We can also customize compare method of a sorting algorithm to solve the above problem.
    For example qsort() in C allows us to pass our own customized compare method.
    1. If num1 and num2 both are in A2 then number with lower index in A2 will be treated smaller
    than other.
    2. If only one of num1 or num2 present in A2, then that number will be treated smaller than the
    other which doesn't present in A2.
    3. If both are not in A2, then natural ordering will be taken.

    Time complexity of this method is O(mnLogm) if we use a O(nLogn) time complexity sorting
    algorithm. We can improve time complexity to O(mLogm) by using a Hashing instead of doing
    linear search.

    A Python program to sort an array according to the order defined by another array

    A2 is made global here so that it can be accessed by compareByA2(). The syntax of qsort()
    allows only two parameters to compareByA2()
    """
    def __init__(self, A2, size2):
        self.A2 = A2
        self.size2 = size2

    def search(self, key):
        for i in range(self.size2):
            if self.A2[i] == key:
                return i
        return -1

    def compare_by_a2(self, a, b):
        """
        A custom compare method to compare elements of A1[] according to the order
        defined by A2[].
        """
        idx1 = self.search(a)
        idx2 = self.search(b)
        if idx1 != -1 and idx2 != -1:
            return idx1 - idx2
        elif idx1 != -1:
            return -1
        elif idx2 != -1:
            return 1
        else:
            return a - b

    def sort_a1_by_a2(self, A1):
        """This method mainly uses qsort to sort A1[] according to A2[]"""
        A1.sort(key=cmp_to_key(self.compare_by_a2))


if __name__ == '__main__':
    A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
    A2 = [2, 1, 8, 3]
    test = SortWithBinarySearch()
    m = len(A1)
    n = len(A2)
    test.sort_according(A1, A2, m, n)
    print("Sorted array is \n", A1)

    # A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8, 7, 5, 6, 9, 7, 5]
    # A2 = [2, 1, 8, 3, 4]
    A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
    A2 = [2, 1, 8, 3]
    test = SortWithCustomizedCompare(A2, len(A2))
    test.sort_a1_by_a2(A1)
    print("Sorted Array is \n", A1)
