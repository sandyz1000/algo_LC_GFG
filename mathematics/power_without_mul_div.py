"""
Write you own Power without using multiplication(*) and division(/) operators  """


def power(a, b):
    """
    Method 1 (Using Nested Loops)
    We can calculate power by using repeated addition.

    For example to calculate 5^6.
    1) First 5 times add 5, we get 25. (5^2)
    2) Then 5 times add 25, we get 125. (5^3)
    3) Then 5 time add 125, we get 625 (5^4)
    4) Then 5 times add 625, we get 3125 (5^5)
    5) Then 5 times add 3125, we get 15625 (5^6)

    Works only if a >= 0 and b >= 0
    """
    if b == 0:
        return 1
    answer = a
    increment = a

    for i in range(1, b):
        for j in range(a):
            answer += increment
        increment = answer
    return answer


class Power:
    def power(self, a, b):
        """
        Method 2 (Using Recursion)
        Recursively add a to get the multiplication of two numbers. And recursively multiply to
        get a raise to the power b.

        A recursive function to get a^b Works only if a >= 0 and b >= 0
        :param a: int
        :param b: int
        :return: int
        """
        if b:
            return self.multiply(a, power(a, b - 1))
        else:
            return 1

    def multiply(self, x, y):
        """A recursive function to get x*y"""
        if y:
            return x + self.multiply(x, y - 1)
        else:
            return 0


if __name__ == '__main__':
    method2 = Power()
    print("\nMethod-1 ", power(5, 3))
    print("\nMethod-2 %d" % method2.power(5, 3))
