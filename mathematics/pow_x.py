"""
Efficient program to calculate e^x
The value of Exponential Function e^x can be expressed using following Taylor Series.
- - - - - - - - - - - - - - - - - - - - - -
e^x = 1 + x/1! + x^2/2! + x^3/3! + ......
- - - - - - - - - - - - - - - - - - - - - -

How to efficiently calculate the sum of above series?
The series can be re-written as
- - - - - - - - - - - - - - - - - - - - - - - - - -
e^x = 1 + (x/1) (1 + (x/2) (1 + (x/3) (........) ) )
- - - - - - - - - - - - - - - - - - - - - - - - - -

Let the sum needs to be calculated for n terms, we can calculate sum using following loop.
- - - - - - - - - - - - - - - - - - - - - - - - - -
for (i = n - 1, sum = 1; i > 0; --i )
    sum = 1 + x * sum / i;
- - - - - - - - - - - - - - - - - - - - - - - - - -

"""


class GFG:
    # Function returns approximate value of e^x using sum of first n terms of Taylor Series
    @staticmethod
    def exponential(n, x):
        # initialize sum of series
        summation = 1
        for i in range(n - 1, 0, -1):
            summation = 1 + x * summation / i

        return summation


if __name__ == '__main__':
    test = GFG()
    n, x = 10, 1
    print("e^x = %f " % test.exponential(n, x))
