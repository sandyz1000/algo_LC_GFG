"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5,
6, 8, 9, 10, 12, 15, ... shows the first 11 ugly numbers. By convention, 1 is included.

Given a number n, the task is to find n'th Ugly number.
Input  : n = 7
Output : 8

Input  : n = 10
Output : 12

Input  : n = 15
Output : 24

Input  : n = 150
Output : 5832

Algorithm:

To check if a number is ugly, divide the number by greatest divisible powers of 2, 3 and 5,
if the number becomes 1 then it is an ugly number otherwise not.

For example, let us see how to check for 300 is ugly or not. Greatest divisible power of 2 is 4,
after dividing 300 by 4 we get 75. Greatest divisible power of 3 is 3, after dividing 75 by 3 we
get 25. Greatest divisible power of 5 is 25, after dividing 25 by 25 we get 1.
Since we get 1 finally, 300 is ugly number.

"""


class FindUglyNo(object):
    def max_divide(self, a, b):
        """
        This function divides a by greatest divisible power of b
        :param a: int
        :param b: int
        :return:
        """
        while a % b == 0:
            a = a / b
        return a

    def is_ugly(self, no):
        """
        Function to check if a number is ugly or not
        :param no:
        :return:
        """
        no = self.max_divide(no, 2)
        no = self.max_divide(no, 3)
        no = self.max_divide(no, 5)

        return 1 if no == 1 else 0

    def get_nth_ugly_no(self, n):
        """
        Function to get the nth ugly number
        :param n:
        :return:
        """
        i = 1
        count = 1  # ugly number count
        # Check for all integers until ugly count becomes n
        while n > count:
            i += 1
            if self.is_ugly(i):
                count += 1

        return i


def get_nth_ugly_no_dp(n):
    """
    Time Complexity: O(n)
    Auxiliary Space: O(n)
    :param n:
    :return:
    """
    ugly = [0] * n  # To store ugly numbers

    # 1 is the first ugly number
    ugly[0] = 1

    # i2, i3, i5 will indicate indices for 2,3,5 respectively
    i2 = i3 = i5 = 0

    # set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    # start loop to find value from ugly[1] to ugly[n]
    for l in range(1, n):
        # choose the min value of all available multiples
        ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        # increment the value of index accordingly
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2

        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3

        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5

    # return ugly[n] value
    return ugly[-1]


if __name__ == '__main__':
    print("150th ugly no. is %d " % FindUglyNo().get_nth_ugly_no(150))
    print("150th ugly no. is %d " % get_nth_ugly_no_dp(150))
