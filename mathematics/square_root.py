"""
Find the square root of the no
Babylonian method for square root

Example:

n = 4 # n itself is used for initial approximation
Initialize x = 4, y = 1
Next Approximation x = (x + y)/2 (= 2.500000), y = n/x  (=1.600000)
Next Approximation x = 2.050000, y = 1.951220
Next Approximation x = 2.000610, y = 1.999390
Next Approximation x = 2.000000, y = 2.000000
Terminate as (x - y) > e now.  """


def squareRoot(n):
    """
    Method-1
    Algorithm:
    This method can be derived from (but predates) Newton–Raphson method.
    1 Start with an arbitrary positive start value x (the closer to the root, the better).
    2 Initialize y = 1.
    3. Do following until desired approximation is achieved.
        a) Get the next approximation for root using average of x and y
        b) Set y = n/x

    Returns the square root of n. Note that the function
    :param n: float
    :return:
    """
    # We are using n itself as initial approximation This can definitely be improved
    x = float(n)
    y = float(1)
    e = 0.000001  # e decides the accuracy level
    while x - y > e:
        x = (x + y) / 2
        y = n / x
    return x


def squareRoot2(n):
    """
    If we are sure that n is a perfect square, then we can use following method.
    The method can go in infinite loop for non-perfect-square numbers.
    For example, for 3 the below while loop will never terminate.

    Returns the square root of n. Note that the function will not work for numbers
    which are not perfect squares"""
    x = n
    y = 1
    while x > y:
        x = (x + y) / 2
        y = n / x
    return x


def squareRoot3(n):
    x = n
    y = 1
    e = 0.000001  # e decides the accuracy level
    while x - y > e:
        x = (x + y) / 2
        y = n / x
        print(x, y)
    return x


if __name__ == '__main__':
    # For n is not perfect square
    print("\nMethod-1", squareRoot(50))

    # For n is perfect square
    print("\nMethod-2", squareRoot3(49))
    print("\nMethod-3", squareRoot3(49))
