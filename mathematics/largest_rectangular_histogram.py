"""
Largest Rectangular Area in a Histogram | Set 1
Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit.
For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 2, 6}. The largest possible rectangle possible is 12 (see the below figure, the max area rectangle is highlighted in red)
"""
# A Divide and Conquer Program to find maximum rectangular area in a histogram
import sys
import math
INT_MIN = -sys.maxsize


def maxValue(x, y, z):
    """A utility function to find minimum of three integers
    """
    return max(max(x, y), z)


def minVal(hist, i, j):
    """A utility function to get minimum of two numbers in hist[] """
    if (i == -1): 
        return j
    if (j == -1): 
        return i
    return (hist[i] < hist[j]) if i else j


def getMid(s, e):
    """  A utility function to get the middle index from corner indexes. """
    return s + (e -s)/2

def rmq_util(hist, st, ss, se, qs, qe, index):
    """
    A recursive function to get the index of minimum value in a given range of
    indexes. The following are parameters for this function.

    hist   --> Input array for which segment tree is built
    st    --> Pointer to segment tree
    index --> Index of current node in the segment tree. Initially 0 is
    passed as root is always at index 0
    ss & se  --> Starting and ending indexes of the segment represented by
    current node, i.e., st[index]
    qs & qe  --> Starting and ending indexes of query range

    """
    # // If segment of this node is a part of given range, then return the
    # // min of the segment
    if (qs <= ss and qe >= se):
        return st[index]

    # // If segment of this node is outside the given range
    if (se < qs or ss > qe):
        return -1

    # // If a part of this segment overlaps with the given range
    mid = getMid(ss, se)
    return minVal(hist, rmq_util(hist, st, ss, mid, qs, qe, 2*index+1),
            rmq_util(hist, st, mid+1, se, qs, qe, 2*index+2))


def RMQ(hist, st, n, qs, qe):
    """ Return index of minimum element in range from index qs (quey start) to  qe (query end). 
    It mainly uses RMQUtil()
    
    Arguments:
        hist {[type]} -- [description]
        st {[type]} -- [description]
        n {[type]} -- [description]
        qs {[type]} -- [description]
        qe {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    # // Check for erroneous input values
    if (qs < 0 or qe > n-1 or qs > qe):
        print("Invalid Input")
        return -1

    return rmq_util(hist, st, 0, n-1, qs, qe, 0)


def constructSTUtil(hist, ss, se, st, si):
    """ A recursive function that constructs Segment Tree for hist[ss..se].
    si is index of current node in segment tree st
    
    Arguments:
        hist {[type]} -- [description]
        ss {[type]} -- [description]
        se {[type]} -- [description]
        st {[type]} -- [description]
        si {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    #  If there is one element in array, store it in current node of
    # segment tree and return
    if (ss == se): return (st[si] == ss)

    # If there are more than one elements, then recur for left and
    # right subtrees and store the minimum of two values in this node
    mid = getMid(ss, se)
    st[si] =  minVal(hist, constructSTUtil(hist, ss, mid, st, si*2+1),
                constructSTUtil(hist, mid+1, se, st, si*2+2))
    return st[si]


def constructST(hist, n):
    """
    # Function to construct segment tree from given array. This function
    # allocates memory for segment tree and calls constructSTUtil() to
    # fill the allocated memory */
    """
    # // Allocate memory for segment tree
    x = int(math.ceil(math.log2(n))) #Height of segment tree
    max_size = 2* int(math.pow(2, x)) - 1 #Maximum size of segment tree
    st = [i for i in range(max_size)]

    # // Fill the allocated memory st
    constructSTUtil(hist, 0, n-1, st, 0)

    # // Return the constructed segment tree
    return st


def getMaxAreaRec(hist, st, n, l, r):
    """
    A recursive function to find the maximum rectangular area. It uses segment 
    tree 'st' to find the minimum value in hist[l..r]
    """

    # Base cases
    if (l > r):  return INT_MIN
    if (l == r):  return hist[l]

    # // Find index of the minimum value in given rang  This takes O(Logn)time
    m = RMQ(hist, st, n, l, r)

    # /* Return maximum of following three possible cases
    # a) Maximum area in Left of min value (not including the min)
    # a) Maximum area in right of min value (not including the min)
    # c) Maximum area including min */
    return maxValue(getMaxAreaRec(hist, st, n, l, m-1),
            getMaxAreaRec(hist, st, n, m+1, r),
            (r-l+1)*(hist[m]) )

def getMaxArea(hist, n):
    """The main function to find max area
    
    Arguments:
        hist {list} -- [description]
        n {int} -- [description]
    """
    # // Build segment tree from given array. This takes O(n) time
    st = constructST(hist, n)

    # // Use recursive utility function to find the  maximum area
    return getMaxAreaRec(hist, st, n, 0, n-1)


if __name__ == "__main__":
    hist = [6, 1, 5, 4, 5, 2, 6]
    n = len(hist)
    print("Maximum area is ", getMaxArea(hist, n))
    