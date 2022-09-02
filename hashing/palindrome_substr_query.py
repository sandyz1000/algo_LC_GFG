"""
http://www.geeksforgeeks.org/palindrome-substring-queries/

Palindrome Substring Queries
Given a string and several queries on the substrings of the given input string to check whether the
substring is a palindrome or not.

Examples:
Suppose our input string is "abaaabaaaba" and the queries- [0, 10], [5, 8], [2, 5], [5, 9]

We have to tell that the substring having the starting and ending indices as above is a palindrome
or not.

[0, 10] → Substring is "abaaabaaaba" which is a palindrome.
[5, 8] → Substring is "baaa" which is not a palindrome.
[2, 5] → Substring is "aaab" which is not a palindrome.
[5, 9] → Substring is "baaab" which is a palindrome.

Let us assume that there are Q such queries to be answered and N be the length of our input string.
There are the following two ways to answer these queries

-----------------------------------------------------------
Explanation:
-----------------------------------------------------------

Method 1 (Naive)

One by one we go through all the substrings of the queries and check whether the substring under
consideration is a palindrome or not.
Since there are Q queries and each query can take O(N) worse case time to answer, this method
takes O(Q.N) time in the worst case. Although this is an in-place/space-efficient algorithm,
but still there are more efficient method to do this.
"""


# A Python program to answer queries to check whether the substrings are
# palindrome or not efficiently

p = 101
MOD = 1000000007


class Query:
    """
    Structure to represent a query. A query consists of (L,R) and we have to answer
    whether the substring from index-L to R is a palindrome or not
    """

    def __init__(self, L, R):
        self.L = L
        self.R = R


def is_palindrome(mystring, L, R):
    """A function to check if a string str is palindrome in the range L to R"""
    # Keep comparing characters while they are same
    while R > L:
        L += 1
        R -= 1
        if mystring[L] != mystring[R]:
            return False
    return True


def mod_pow(base, exponent):
    """A Function to find pow (base, exponent) % MOD in log (exponent) time"""
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    temp = mod_pow(base, exponent // 2)
    if exponent % 2 == 0:
        return (temp % MOD * temp % MOD) % MOD
    else:
        return (((temp % MOD * temp % MOD) % MOD) * base % MOD) % MOD


def find_mmi(n):
    """A Function to calculate Modulo Multiplicative Inverse of 'n'"""
    return mod_pow(n, MOD - 2)


def compute_prefix_hash(string, n, prefix, power):
    """
    :param string: str
    :param n: int
    :param prefix: list(int)
    :param power: list(int)
    :return:
    """
    prefix[0] = 0
    prefix[1] = ord(string[0])
    for i in range(2, n + 1):
        prefix[i] = (prefix[i - 1] % MOD + (ord(string[i - 1]) % MOD * power[i - 1] % MOD) % MOD) % MOD
    return


def compute_suffix_hash(string, n, suffix, power):
    """
    A Function to calculate the suffix hash Suffix hash is nothing but the prefix
    hash of the reversed string

    :param string: str
    :param n: int
    :param suffix: list(int)
    :param power: list(int)
    :return:
    """
    suffix[0] = 0
    suffix[1] = ord(string[n - 1])

    i, j = n - 2, 2
    while i >= 0 and j <= n:
        suffix[j] = (suffix[j - 1] % MOD + (ord(string[i]) % MOD * power[j - 1] % MOD) % MOD) % MOD
        i -= 1
        j += 1
    return


def query_results(m_string, q, m, n, prefix, suffix, power):
    """
    :param m_string: str
    :param q: list(Query)
    :param m: int
    :param n: int
    :param prefix: list(int)
    :param suffix: list(int)
    :param power: list(int)
    :return:
    """
    for i in range(m):
        L, R = q[i].L, q[i].R

        # Hash Value of Substring [L,R]
        hash_LR = ((prefix[R + 1] - prefix[L] + MOD) % MOD * find_mmi(power[L]) % MOD) % MOD

        # Reverse Hash Value of Substring [L,R]
        reverse_hash_LR = ((suffix[n - L] - suffix[n - R - 1] + MOD) % MOD * find_mmi(
            power[n - R - 1]) % MOD) % MOD

        # If both are equal then the substring is a palindrome
        if hash_LR == reverse_hash_LR:
            if is_palindrome(m_string, L, R):
                print("The Substring [%d %d] is a palindrome\n" % (L, R))
            else:
                print("The Substring [%d %d] is not a palindrome\n" % (L, R))
        else:
            print("The Substring [%d %d] is not a palindrome\n" % (L, R))
    return


def compute_powers(power, n):
    """A Dynamic Programming Based Approach to compute the powers of 101
    """
    power[0] = 1  # 101^0 = 1

    for i in range(1, n + 1):
        power[i] = (power[i - 1] % MOD * p % MOD) % MOD
    return


if __name__ == '__main__':
    # Output:
    # The Substring [0 10] is a palindrome
    # The Substring [5 8] is not a palindrome
    # The Substring [2 5] is not a palindrome
    # The Substring [5 9] is a palindrome

    string = "abaaabaaaba"
    n = len(string)

    # A Table to store the powers of 101
    power = [0 for i in range(n + 1)]

    compute_powers(power, n)
    # Arrays to hold prefix and suffix hash values
    prefix, suffix = [0] * (n + 1), [0] * (n + 1)

    # Compute Prefix Hash and Suffix Hash Arrays
    compute_prefix_hash(string, n, prefix, power)
    compute_suffix_hash(string, n, suffix, power)

    q = [Query(0, 10), Query(5, 8), Query(2, 5), Query(5, 9)]
    m = len(q)

    query_results(string, q, m, n, prefix, suffix, power)
