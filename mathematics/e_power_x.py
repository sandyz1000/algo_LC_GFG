"""
Returns approximate value of e^x using sum of first n terms of Taylor Series
e^x = 1 + (x/1) (1 + (x/2) (1 + (x/3) (1 + (x/4) (1 + ......))))
"""


def exponential(n, x):
    #  The final result will be considered 1.0
    result = 1.0
    for i in range(n-1, 0, -1):
        result = 1 + (x / i) * result

    return result


if __name__ == "__main__":
    n, x = 10, 1.0
    print("e^x = %f" % exponential(n, x))
