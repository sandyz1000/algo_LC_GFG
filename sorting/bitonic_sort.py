# coding=utf-8
"""
Bitonic Sort
http://www.geeksforgeeks.org/bitonic-sort/

------------------------------------------
==Background==
------------------------------------------

Bitonic Sort is a classic parallel algorithm for sorting.

Bitonic sort does O(n Log^2n) comparisons.
The number of comparisons done by Bitonic sort are more than popular sorting algorithms like
Merge Sort [ does O(nLogn) comparisons], but Bitonice sort is better for parallel implementation
because we always compare elements in predefined sequence and the sequence of comparison doesn't
depend on data. Therefore it is suitable for implementation in hardware and parallel processor
array.
To understand Bitonic Sort, we must first understand what is Bitonic Sequence and how to make a
given sequence Bitonic.

----------------------------------------
Bitonic Sequence
----------------------------------------
A sequence is called Bitonic if it is first increasing, then decreasing. In other words,
an array arr[0..n-i] is Bitonic if there exists an index i where 0<=i<=n-1 such that

- - - - - - - - - - - - - - - - - - - - - - - - - +
x0 <= x1 ...<= xi  and  xi >= xi+1 .... >= xn-1   |
- - - - - - - - - - - - - - - - - - - - - - - - - +

1. A sequence, sorted in increasing order is considered Bitonic with the decreasing part as empty.
  Similarly, decreasing order sequence is considered Bitonic with the increasing part as empty.
2. A rotation of Bitonic Sequence is also bitonic.

==How to form a Bitonic Sequence from a random input?==

We start by forming 4-element bitonic sequences from consecutive 2-element sequence. Consider
4-element in sequence x0, x1, x2, x3. We sort x0 and x1 in ascending order and x2 and x3 in
descending order. We then concatenate the two pairs to form a 4 element bitonic sequence.
Next, we take two 4 element bitonic sequences, sorting one in ascending order, the other in
descending order (using the Bitonic Sort which we will discuss below), and so on, until we obtain
the bitonic sequence.

Example:
Convert the following sequence to bitonic sequence: 3, 7, 4, 8, 6, 2, 1, 5

Step 1: Consider each 2-consecutive elements as bitonic sequence and apply bitonic sort on each
2- pair elements. In next step, take two 4 element bitonic sequences and so on.

 bitonic sort

 ---- DIAGRAM-GOES-HERE -----

Note: x0 and x1 are sorted in ascending order and x2 and x3 in descending order and so on

Step 2: Two 4 element bitonic sequences : A(3,7,8,4) and B(2,6,5,1) with comparator length as 2

 ---- DIAGRAM-GOES-HERE -----

After this step, we'll get Bitonic sequence of length 8.

 3, 4, 7, 8, 6, 5, 2, 1
Bitonic Sorting

It mainly involves two steps.

1.  Forming a bitonic sequence (discussed above in detail). After this step we reach the fourth
    stage in below diagram, i.e., the array becomes {3, 4, 7, 8, 6, 5, 2, 1}

2.  Creating one sorted sequence from bitonic sequence : After first step, first half is sorted in
    increasing order and second half in decreasing order.
    We compare first element of first half with first element of second half, then second element
    of first half with second element of second and so on. We exchange elements if an element of
    first half is smaller.
    After above compare and exchange steps, we get two bitonic sequences in array. See fifth stage
    in below diagram. In the fifth stage, we have {3, 4, 2, 1, 6, 5, 7, 8}. If we take a closer
    look at the elements, we can notice that there are two bitonic sequences of length n/2 such
    that all elements in first bitnic sequence {3, 4, 2, 1} are smaller than all elements of second
    bitonic sequence {6, 5, 7, 8}.
    We repeat the same process within two bitonic sequences and we get four bitonic sequences of
    length n/4 such that all elements of leftmost bitonic sequence are smaller and all elements of
    rightmost. See sixth stage in below diagram, arrays is {2, 1, 3, 4, 6, 5, 7, 8}.
    If we repeat this process one more time we get 8 bitonic sequences of size n/8 which is 1.
    Since all these bitonic sequence are sorted and every bitonic sequence has one element, we get
    the sorted array.

---------------------------------------------
==Analysis of Bitonic Sort==
---------------------------------------------

To form a sorted sequence of length n from two sorted sequences of length n/2, log(n) comparisons
are required (for example: log(8) = 3 when sequence size. Therefore, The number of comparisons T(n)
of the entire sorting is given by:

T(n) = log(n) + T(n/2)

The solution of this recurrence equation is

T(n) = log(n) + log(n)-1 + log(n)-2 + .... + 1 = log(n) · (log(n)+1) / 2

As, each stage of the sorting network consists of n/2 comparators. Therefore total Theta(n log2n)
comparators. """

from __future__ import print_function


# Python program for Bitonic Sort. Note that this program works only when size of input
# is a power of 2.

def comp_and_swap(a, i, j, dire):
    """
    The parameter dir indicates the sorting direction, ASCENDING or DESCENDING; if (a[i] > a[j])
    agrees with the direction, then a[i] and a[j] are interchanged.
    """
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]


def bitonic_merge(a, low, cnt, dire):
    """
    It recursively sorts a bitonic sequence in ascending order, if dir = 1, and in descending
    order otherwise (means dir=0). The sequence to be sorted starts at index position low,
    the parameter cnt is the number of elements to be sorted.
    """
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            comp_and_swap(a, i, i + k, dire)
        bitonic_merge(a, low, k, dire)
        bitonic_merge(a, low + k, k, dire)


def _bitonic_sort(a, low, cnt, dire):
    """
    This function first produces a bitonic sequence by recursively sorting its two halves in
    opposite sorting orders, and then calls bitonic_merge to make them in the same order
    """
    if cnt > 1:
        k = cnt // 2
        _bitonic_sort(a, low, k, 1)
        _bitonic_sort(a, low + k, k, 0)
        bitonic_merge(a, low, cnt, dire)


def bitonic_sort(a, N, up):
    """
    Caller of bitonicSort for sorting the entire array of length N in ASCENDING order
    """
    _bitonic_sort(a, 0, N, up)


if __name__ == '__main__':
    # Output: Sorted array:  1 2 3 4 5 6 7 8
    a = [3, 7, 4, 8, 6, 2, 1, 5]
    n = len(a)
    up = 1

    bitonic_sort(a, n, up)
    print("Sorted array is: ", end=" ")
    for i in range(n):
        print("%d" % a[i], end=" "),
