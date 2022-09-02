"""
Program for nth Catalan Number
Catalan numbers are a sequence of natural numbers that occurs in many interesting counting
problems like following.

1) Count the number of expressions containing n pairs of parentheses which are correctly matched.
For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).

2) Count the number of possible Binary Search Trees with n keys (See this)

3) Count the number of full binary trees (A rooted binary tree is full if every vertex has either
two children or no children) with n+1 leaves.

See this for more applications.

The first few Catalan numbers for n = 0, 1, 2, 3, .... are 1, 1, 2, 5, 14, 42, 132, 429, 1430,
4862, .... """


# A recursive function to find nth catalan number
def catalan_rec(n):
    """
    Recursive Solution
    Catalan numbers satisfy the following recursive formula.

    c(0) = 1 and c(n+1) = sum(c(i) * c(n-i)) -> i= 0...n for n >=0
    """
    # Base Case
    if n <= 1:
        return 1

    # Catalan(n) is the sum of catalan(i)*catalan(n-i-1)
    res = 0
    for i in range(n):
        res += catalan_rec(i) * catalan_rec(n - i - 1)

    return res


# Driver Program to test above function
# for i in range(10):
#     print(catalan_rec(i), end=",")
catalan_rec(5)
print("\n")


def catalan_dp(n):
    """
    Dynamic Programming Solution
    We can observe that the above recursive implementation does a lot of repeated work (we can
    the same by drawing recursion tree). Since there are overlapping subproblems, we can use
    dynamic programming for this. Following is a Dynamic programming based implementation in Python.

    A dynamic programming based function to find nth Catalan number

    Time Complexity: Time complexity of above implementation is O(n^2)
    """
    if n == 0 or n == 1:
        return 1

    # Table to store results of subproblems
    catalan = [0 for i in range(n + 1)]

    # Initialize first two values in table
    catalan[0] = 1
    catalan[1] = 1

    # Fill entries in catalan[] using recursive formula
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]

    # Return last entry
    return catalan[n]


# Driver code
for i in range(11):
    print(catalan_dp(i), end=",")
print("\n")


# Returns value of Binomial Coefficient C(n, k)
def binomialCoefficient(n, k):
    """
    Using Binomial Coefficient
    We can also use the below formula to find nth catalan number in O(n) time.

    C(n) =  1/ math.factorial(n+1) * C(2n, n)  for n >= 0

    Time Complexity: Time complexity of above implementation is O(n).

    We can also use below formula to find nth catalan number in O(n) time.
    C(n) =  math.factorial(2n)/ math.factorial(n+1) * math.factorial(n)

    """
    # since C(n, k) = C(n, n - k)
    if k > n - k:
        k = n - k

    # initialize result
    res = 1

    # Calculate value of [n * (n-1) *---* (n-k + 1)] / [k * (k-1) *----* 1]
    for i in range(k):
        res = res * (n - i)
        res = res / (i + 1)
    return res


# A Binomial coefficient based function to find nth catalan number in O(n) time
def catalan(n):
    c = binomialCoefficient(2 * n, n)
    return c / (n + 1)


for i in range(11):
    print(catalan(i), end=",")
print("\n")