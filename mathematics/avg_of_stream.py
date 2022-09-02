"""Average of a stream of numbers (Difficulty Level: Rookie)

Given a stream of numbers, print average (or mean) of the stream at every point.
For example, let us consider the stream as 10, 20, 30, 40, 50, 60, ....

- - - - - - - - - - - - - - - - - - - -
  Average of 1 numbers is 10.00
  Average of 2 numbers is 15.00
  Average of 3 numbers is 20.00
  Average of 4 numbers is 25.00
  Average of 5 numbers is 30.00
  Average of 6 numbers is 35.00
  ..................
- - - - - - - - - - - - - - - - - - - -

"""
from functools import wraps


def static_vars(**kwargs):
    @wraps
    def method(func):
        for key, value in kwargs.items():
            setattr(func, key, value)
        return func

    return method


def getAvg1(prev_avg, x, n):
    """Returns the new average after including x"""
    return (prev_avg * n + x) / (n + 1)


def streamAvg1(arr, n):
    """
    To print mean of a stream, we need to find out how to find average when a new number is
    being added to the stream. To do this, all we need is count of numbers seen so far in the
    stream, previous average and new number. Let n be the count, prev_avg be the previous average
    and x be the new number being added. The average after including x number can be written as
    (prev_avg*n + x)/(n+1).

    Prints average of a stream of numbers
    """
    avg = 0
    for i in range(n):
        avg = getAvg1(avg, arr[i], i)
        print("Average of %d numbers is %f n" % (i + 1, avg))


# Returns the new average after including x
@static_vars(summation=0, n=0)
def getAvg2(x):
    getAvg2.summation += x
    getAvg2.n += 1
    result = ((float(getAvg2.summation)) / getAvg2.n)
    return result


def streamAvg2(arr, n):
    """
    The above function getAvg() can be optimized using following changes.
    We can avoid the use of prev_avg and number of elements by using static variables
    (Assuming that only this function is called for average of stream).
    Following is the oprimnized version.
    Prints average of a stream of numbers
    """
    avg = 0
    for i in range(n):
        avg = getAvg2(arr[i])
        print("Average of %d numbers is %f n" % (i + 1, avg))


if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50, 60]
    n = len(arr)
    print("\nMethod-1: ")
    streamAvg1(arr, n)

    print("\nMethod-2: ")
    streamAvg2(arr, n)
