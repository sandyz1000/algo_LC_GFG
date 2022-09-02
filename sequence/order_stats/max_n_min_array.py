"""
Maximum and minimum of an array using minimum number of comparisons """


class Pair(object):
    def __init__(self, minimum=0, maximum=0):
        self.maximum = maximum
        self.minimum = minimum


def get_min_max_linear(arr, n):
    """
    METHOD 1 (Simple Linear Search)
    Initialize values of min and max as minimum and maximum of the first two elements respectively.
    Starting from 3rd, compare each element with max and min, and change max and min accordingly
    (i.e., if the element is smaller than min then change min, else if the element is greater than
    max then change max, else ignore the element)

    Time Complexity: O(n)

    In this method, total number of comparisons is 1 + 2(n-2) in worst case and 1 + n - 2 in best
    case. In the above implementation, worst case occurs when elements are sorted in descending
    order and best case occurs when elements are sorted in ascending order.
    """
    minmax = Pair()

    # If there is only one element then return it as min and max both
    if n == 1:
        minmax.maximum = arr[0]
        minmax.minimum = arr[0]
        return minmax

    # If there are more than one elements, then initialize min and max
    if arr[0] > arr[1]:
        minmax.maximum = arr[0]
        minmax.minimum = arr[1]
    else:
        minmax.maximum = arr[1]
        minmax.minimum = arr[0]

    for i in range(2, n):
        if arr[i] > minmax.maximum:
            minmax.maximum = arr[i]
        elif arr[i] < minmax.minimum:
            minmax.minimum = arr[i]

    return minmax


def getMinMaxTournament(arr, low, high):
    """
    METHOD 2 (Tournament Method)
    Divide the array into two parts and compare the maximums and minimums of the the two parts to
    get the maximum and the minimum of the the whole array.

    Time Complexity: O(n)
    Total number of comparisons: let number of comparisons be T(n). T(n) can be written as follows:

    Algorithmic Paradigm: Divide and Conquer
    - - - - - - - - - - - - - - - - - - - - - - - - - - -
      T(n) = T(floor(n/2)) + T(ceil(n/2)) + 2
      T(2) = 1
      T(1) = 0
    - - - - - - - - - - - - - - - - - - - - - - - - - - -

    If n is a power of 2, then we can write T(n) as:
    - - - - - - - - - - - - - - - - - - - - - - - - - - -
       T(n) = 2T(n/2) + 2
    - - - - - - - - - - - - - - - - - - - - - - - - - - -

    After solving above recursion, we get
    - - - - - - - - - - - - - - - - - - - - - - - - - - -
      T(n)  = 3/2n -2
    - - - - - - - - - - - - - - - - - - - - - - - - - - -

    Thus, the approach does 3/2n -2 comparisons if n is a power of 2. And it does more than 3/2n
    -2 comparisons if n is not a power of 2.

    :param arr: list(int)
    :param low: int
    :param high: int
    :return:
    """
    minmax, mml, mmr = Pair(), Pair(), Pair()

    if low == high:  # If there is only on element
        minmax.maximum = arr[low]
        minmax.minimum = arr[low]
        return minmax

    if high == low + 1:  # If there are two elements
        if arr[low] > arr[high]:
            minmax.maximum = arr[low]
            minmax.minimum = arr[high]
        else:
            minmax.maximum = arr[high]
            minmax.minimum = arr[low]

        return minmax

    mid = (low + high) // 2  # If there are more than 2 elements
    mml = getMinMaxTournament(arr, low, mid)
    mmr = getMinMaxTournament(arr, mid + 1, high)

    if mml.minimum < mmr.minimum:  # compare minimums of two parts
        minmax.minimum = mml.minimum
    else:
        minmax.minimum = mmr.minimum

    # compare maximums of two parts
    if mml.maximum > mmr.maximum:
        minmax.maximum = mml.maximum
    else:
        minmax.maximum = mmr.maximum

    return minmax


if __name__ == '__main__':
    print("\nGet min-max linear")
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = len(arr)
    minmax = get_min_max_linear(arr, arr_size)
    print("Minimum element is %d" % minmax.minimum)
    print("Maximum element is %d" % minmax.maximum)

    print("\nGet min-max tournament")
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = len(arr)
    minmax = get_min_max_linear(arr, arr_size)
    print("Minimum element is %d" % minmax.minimum)
    print("Maximum element is %d" % minmax.maximum)
