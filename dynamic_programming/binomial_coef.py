"""
Dynamic Programming | Set 9 (Binomial Coefficient)

Following are common definition of Binomial Coefficients.
1) A binomial coefficient C(n, k) can be defined as the coefficient of X^k in the expansion of (1 + X)^n.

2) A binomial coefficient C(n, k) also gives the number of ways, disregarding order,
that k objects can be chosen from among n objects; more formally, the number of
k-element subsets (or k-combinations) of an n-element set.

The Problem

Write a function that takes two parameters n and k and returns the value of Binomial
Coefficient C(n, k). For example, your function should return 6 for n = 4 and k = 2,
and it should return 10 for n = 5 and k = 2.

1) Optimal Substructure

The value of C(n, k) can be recursively calculated using following standard formula for
Binomial Coefficients.

   C(n, k) = C(n-1, k-1) + C(n-1, k)
   C(n, 0) = C(n, n) = 1

2) Overlapping Subproblems

It should be noted that the above function computes the same sub problems again and
again. See the following recursion tree for n = 5 an k = 2. The function C(3,
1) is called two times. For large values of n, there will be many common sub problems.

                          ___C(5, 2)___
                    /                      \
           C(4, 1)                           C(4, 2)
            /   \                          /           \
       C(3, 0)   C(3, 1)             C(3, 1)               C(3, 2)
                /    \               /     \               /     \
         C(2, 0)    C(2, 1)      C(2, 0) C(2, 1)          C(2, 1)  C(2, 2)
                   /        \              /   \            /   \
               C(1, 0)  C(1, 1)      C(1, 0)  C(1, 1)   C(1, 0) C(1, 1)

Since same sub problems are called again, this problem has Overlapping Sub problems
property. So the Binomial Coefficient problem has both properties of a dynamic
programming problem. Like other typical Dynamic Programming(DP) problems,
re-computations of same sub problems can be avoided by constructing a temporary array
C[][] in bottom up manner.

Time Complexity: O(n*k)
Auxiliary Space: O(n*k)

     1
    1 1
   1 2 1
  1 3 3 1

Time Complexity: O(n*k)
Auxiliary Space: O(k)

------------------------------
Explanation:
------------------------------

1==========>> n = 0, C(0,0) = 1
1-1========>> n = 1, C(1,0) = 1, C(1,1) = 1
1-2-1======>> n = 2, C(2,0) = 1, C(2,1) = 2, C(2,2) = 1
1-3-3-1====>> n = 3, C(3,0) = 1, C(3,1) = 3, C(3,2) = 3, C(3,3)=1
1-4-6-4-1==>> n = 4, C(4,0) = 1, C(4,1) = 4, C(4,2) = 6, C(4,3)=4, C(4,4)=1
So here every loop on i, builds i'th row of pascal triangle, using (i-1)th row

At any time, every element of array C will have some value (ZERO or more) and in next
iteration, value for those elements comes from previous iteration.

In statement,
C[j] = C[j] + C[j-1]

Right hand side represents the value coming from previous iteration (A row of Pascal's
triangle depends on previous row). Left Hand side represents the value of current
iteration which will be obtained by this statement.

- - - - - - - - - - - - - - - - - - - - - - - -
Let's say we want to calculate C(4, 3),
i.e. n=4, k=3:

All elements of array C of size 4 (k+1) are initialized to ZERO.

i.e. C[0] = C[1] = C[2] = C[3] = C[4] = 0;
Then C[0] is set to 1

For i = 1:
C[1] = C[1] + C[0] = 0 + 1 = 1 ==>> C(1,1) = 1

For i = 2:
C[2] = C[2] + C[1] = 0 + 1 = 1 ==>> C(2,2) = 1
C[1] = C[1] + C[0] = 1 + 1 = 2 ==>> C(2,2) = 2

For i=3:
C[3] = C[3] + C[2] = 0 + 1 = 1 ==>> C(3,3) = 1
C[2] = C[2] + C[1] = 1 + 2 = 3 ==>> C(3,2) = 3
C[1] = C[1] + C[0] = 2 + 1 = 3 ==>> C(3,1) = 3

For i=4:
C[4] = C[4] + C[3] = 0 + 1 = 1 ==>> C(4,4) = 1
C[3] = C[3] + C[2] = 1 + 3 = 4 ==>> C(4,3) = 4
C[2] = C[2] + C[1] = 3 + 3 = 6 ==>> C(4,2) = 6
C[1] = C[1] + C[0] = 3 + 1 = 4 ==>> C(4,1) = 4

C(4,3) = 4 is would be the answer in our example

- - - - - - - - - - - - - - - - - - - - - - - -
"""

import time


def binomial_coeff_rec(n: int, k: int):
    if k == 0 or k == n:
        return 1

    # Recursive Call
    return binomial_coeff_rec(n - 1, k - 1) + binomial_coeff_rec(n - 1, k)


def binomial_coeff(n: int, k: int):
    """
    A Dynamic Programming based Python Program that uses table C[][] to calculate the
    Binomial Coefficient.
    Returns value of Binomial Coefficient C(n, k)
    """
    C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # Calculate value of Binomial Coefficient in bottom up manner
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1
            # Calculate value using previously stored values
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    return C[n][k]


def binomial_coeff_2(n: int, k: int):
    """
    Python program for Optimized Dynamic Programming solution to
    Binomial Coefficient. This one uses the concept of pascal Triangle and less memory
    """
    C = [0 for i in range(k + 1)]  # Declaring an empty _array
    C[0] = 1  # since nC0 is 1

    for i in range(1, n + 1):
        # Compute next row of pascal triangle using the previous row
        j = min(i, k)
        while j > 0:
            C[j] = C[j] + C[j - 1]
            j -= 1

    return C[k]


if __name__ == '__main__':
    n, k = 5, 2
    start_time = time.time()
    result = binomial_coeff_rec(n, k)
    end_time = time.time()
    print("Time: %d -- Value of C[%d][%d] is %d" % (end_time - start_time, n, k, result))

    start_time = time.time()
    result = binomial_coeff(n, k)
    end_time = time.time()
    print("Time: %d -- Value of C[%d][%d] is %d" % (end_time - start_time, n, k, result))

    start_time = time.time()
    result = binomial_coeff_2(n, k)
    end_time = time.time()
    print("Time: %d -- Value of C[%d][%d] is %d" % (end_time - start_time, n, k, result))
