"""
Space and time efficient Binomial Coefficient

Write a function that takes two parameters n and k and returns the value of Binomial Coefficient
C(n, k). For example, your function should return 6 for n = 4 and k = 2, and it should return 10
for n = 5 and k = 2.  """


def binomial_coefficient(n, k):
    """
    We have discussed a O(n*k) time and O(k) extra space algorithm in this post.
    The value of C(n, k) can be calculated in O(k) time and O(1) extra space.

    C(n, k) = n! / (n-k)! * k!
            = [n * (n-1) *....* 1]  / [ ( (n-k) * (n-k-1) *....* 1) *
                                        ( k * (k-1) *....* 1 ) ]
    After simplifying, we get
    C(n, k) = [n * (n-1) *....* (n-k+1)] / [k * (k-1) *....* 1]

    Also, C(n, k) = C(n, n-k)  # we can change r to n-r if r > n-r
    Following implementation uses above formula to calculate C(n, k)

    Time Complexity: O(k)
    Auxiliary Space: O(1)

    """
    res = 1.0
    # Since C(n, k) = C(n, n-k)
    if k > n - k:
        k = n - k

    # Calculate value of
    # [n * (n-1) *---* (n-k + 1)] / [k * (k-1) *----* 1]
    for i in range(k):
        res *= (n - i)
        res /= (i + 1)
        # res /= k - i

    return res


if __name__ == "__main__":
    n, k = 8, 2
    print("Value of C(%d, %d) is %d " % (n, k, binomial_coefficient(n, k)))
