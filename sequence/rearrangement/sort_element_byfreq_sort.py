"""
Sort elements by frequency | Set 1
Print the elements of an array in the decreasing frequency if 2 numbers have same frequency then
print the one which came first.

Examples:

Input:  arr[] = {2, 5, 2, 8, 5, 6, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6}

Input: arr[] = {2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999}

-------------------------------------------------------
Explanations:
-------------------------------------------------------

METHOD 1 (Use Sorting)

1) Use a sorting algorithm to sort the elements O(nlogn)
2) Scan the sorted array and construct a 2D array of element and count O(n).
3) Sort the 2D array according to count O(nlogn).

Example:

Input 2 5 2 8 5 6 8 8

After sorting we get 2 2 5 5 6 8 8 8

Now construct the 2D array as
2, 2
5, 2
6, 1
8, 3

Sort by count
8, 3
2, 2
5, 2
6, 1

How to maintain order of elements if frequency is same?
The above approach doesn't make sure order of elements if frequency is same. To handle this, we
should use indexes in step 3, if two counts are same then we should first process(or print) the
element with lower index. In step 1, we should store the indexes instead of elements.

Input 5  2  2  8  5  6  8  8

After sorting we get
Element 2 2 5 5 6 8 8 8
Index   1 2 0 4 5 3 6 7

Now construct the 2D array as
Index, Count
1,      2
0,      2
5,      1
3,      3

Sort by count (consider indexes in case of tie)
3, 3
0, 2
1, 2
5, 1

Print the elements using indexes in the above 2D array.
"""
import typing
from functools import cmp_to_key


# Sort elements by frequency. If two elements have same count, then put the elements that appears first

# Used for sorting
class Element:
    def __init__(self, count=0, index=0, val=0):
        self.count = count
        self.index = index
        self.val = val


def mycomp(a, b):
    return a.value - b.value


def mycomp2(a, b):
    """Used for sorting by frequency. And if frequency is same, then by appearance"""
    return a.count - b.count if a.count != b.count else a.index - b.index


def sortByFrequency(arr: typing.List[int], n: int):
    element = [Element(0, i, arr[i]) for i in range(n)]

    # Sort the structure elements according to value, we used stable sort so relative order
    # is maintained.
    element.sort(key=cmp_to_key(mycomp))

    # initialize count of first element as 1
    element[0].count = 1

    # Count occurrences of remaining elements
    for i in range(1, n):
        if element[i].val == element[i - 1].val:
            element[i].count += element[i - 1].count + 1

            # Set count of previous element as -1 , we are doing this because we'll again sort on
            # the basis of counts (if counts are equal than on the basis of index)
            element[i - 1].count = -1

            # Retain the first index (Remember first index is always present in the first duplicate
            # we used stable sort.
            element[i].index = element[i - 1].index
        else:  # Else If previous element is not equal to current so set the count to 1
            element[i].count = 1

    # Now we have counts and first index for each element so now sort on the basis of count and
    # in case of tie use index to sort.
    element.sort(key=cmp_to_key(mycomp2))
    index = 0
    for i in range(n - 1, -1, -1):
        if element[i].count != -1:
            for j in range(element[i].count):
                arr[index] = element[i].val
                index += 1


if __name__ == '__main__':
    # Output: 8 8 8 2 2 5 5 6 -1 9999999
    arr = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
    n = len(arr)

    sortByFrequency(arr, n)
    print(arr)
