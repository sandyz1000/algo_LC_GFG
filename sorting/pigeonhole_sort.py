"""
Pigeonhole Sort
http://www.geeksforgeeks.org/pigeonhole-sort/

Pigeonhole sorting is a sorting algorithm that is suitable for sorting lists of elements where the
number of elements and the number of possible key values are approximately the same.
It requires O(n + Range) time where n is number of elements in input array and 'Range' is number of
possible values in array.

Working of Algorithm :

1. Find minimum and maximum values in array. Let the minimum and maximum values be 'min' and 'max'
 respectively. Also find range as ' max-min+1 '.
2. Set up an array of initially empty "pigeonholes" the same size as of the range.
3. Visit each element of the array and then put each element in its pigeonhole. An element arr[i]
 is put in hole at index arr[i] – min.
4. Start the loop all over the pigeonhole array in order and put the elements from non- empty holes
 back into the original array.

Comparison with Counting Sort :
It is similar to counting sort, but differs in that it
moves items twice: once to the bucket array and again to the final destination

Pigeonhole sort has limited use as requirements are rarely met. For arrays where range is much
larger than n, bucket sort is a generalization that is more efficient in space and time. """

from __future__ import print_function
from typing import List


# Python program to implement Pigeonhole Sort

def pigeonholeSort(arr, n):
    """Sorts the array using pigeonhole algorithm"""
    # Find minimum and maximum values in arr[]
    minimum = min(arr)
    maximum = max(arr)
    rangediff = maximum - minimum + 1  # Find rangediff

    # our list of pigeonholes
    holes = [0] * rangediff  # type: List[int]

    # Traverse through input array and put every element in its respective hole
    for i in range(n):
        holes[arr[i] - minimum] += 1

    # Put the elements back into the array in order.
    i = 0
    for count in range(rangediff):
        while holes[count] > 0:
            holes[count] -= 1
            arr[i] = count + minimum
            i += 1


if __name__ == '__main__':
    # Output: Sorted order is : 2 3 4 6 7 8 8
    arr = [8, 3, 2, 7, 4, 6, 8]
    n = len(arr)
    pigeonholeSort(arr, n)
    print("Sorted order is : ", arr)
