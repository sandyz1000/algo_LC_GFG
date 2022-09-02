"""
Program for Fibonacci numbers
http://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

The Fibonacci numbers are the numbers in the following integer sequence.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation
- - - - - - - - - - - - - - - - - - - -
Fn = Fn-1 + Fn-2

with seed values

F0 = 0 and F1 = 1.
- - - - - - - - - - - - - - - - - - - -

Write a function int fib(int n) that returns Fn. For example, if n = 0, then fib() should return
0. If n = 1, then it should return 1. For n > 1, it should return Fn-1 + Fn-2

For n = 9
Output:34

Following are different methods to get the nth Fibonacci number.

Method 1 ( Use recursion )
---------------------------------------
A simple method that is a direct recursive implementation mathematical recurrence relation given
above.

Time Complexity: T(n) = T(n-1) + T(n-2) which is exponential.
We can observe that this implementation does a lot of repeated work (see the following
recursion tree). So this is a bad implementation for nth Fibonacci number.

                         fib(5)
                     /
               fib(4)                fib(3)
             /                      /
         fib(3)      fib(2)         fib(2)    fib(1)
        /             /           /
  fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
  /
fib(1) fib(0)

Extra Space: O(n) if we consider the function call stack size, otherwise O(1).

Method 2 ( Use Dynamic Programming )
---------------------------------------
We can avoid the repeated work done is the method 1 by storing the Fibonacci numbers calculated
so far.

Time Complexity: O(n)
Extra Space: O(n)

Method 3 ( Space Optimized Method 2 )
---------------------------------------
We can optimize the space used in method 2 by storing the previous two numbers only because that
is all we need to get the next Fibonacci number in series.

Time Complexity: O(n)
Extra Space: O(1)

"""
from __future__ import print_function


def fib(n, lookup):
    """
    Python program for Memoized version of nth Fibonacci number
    Function to calculate nth Fibonacci number
    :param n:
    :param lookup:
    :return:
    """
    if n == 0 or n == 1:  # Base case
        lookup[n] = n

    # If the value is not calculated previously then calculate it
    if lookup[n] is None:
        lookup[n] = fib(n - 1, lookup) + fib(n - 2, lookup)

    # return the value corresponding to that value of n
    return lookup[n]


# Function for nth fibonacci number - Dynamic Programing
# Taking 1st two fibonacci numbers as 0 and 1

fib_array = [0, 1]


def fibonacci_m2(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(fib_array):
        return fib_array[n - 1]
    else:
        temp_fib = fibonacci_m2(n - 1) + fibonacci_m2(n - 2)
        fib_array.append(temp_fib)
        return temp_fib


def fibonacci_m3(n):
    """
    Function for nth fibonacci number - Space Optimisation
    Taking 1st two fibonacci numbers as 0 and 1
    """
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


if __name__ == "__main__":
    n = 34
    # Declaration of lookup table
    # Handles till n = 100
    lookup = [None] * 101
    print("Fibonacci Number is ", fib(n, lookup))

    print(fibonacci_m2(9))

    print(fibonacci_m3(9))
