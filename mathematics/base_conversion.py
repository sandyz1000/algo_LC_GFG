"""
Convert from any base to decimal and vice versa

Given a number and its base, convert it to decimal. The base of number can be anything such that
all digits can be represented using 0 to 9 and A to Z. Value of A is 10, value of B is 11 and so
on. Write a function to convert the number to decimal.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Input number is given as string and output is an integer.

Input: str = "1100", base = 2
Output: 12

Input: str = "11A", base = 16
Output: 282

Input: str = "123",  base = 8
Output: 83
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

We can always use below formula to convert from any base to decimal.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"str" is input number as string
"base" is base of input number.

Decimal Equivalent is,
  1*str[len-1] + base*str[len-2] + (base)2*str[len-2] + ...
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""


# Python program to convert a number from any base to decimal

class BaseConversion:
    """
    To return value of a char. For example, 2 is returned for '2'.  10 is
    returned for 'A', 11 for 'B'
    """
    def re_value(self, num):
        """
        To return char for a value. For example '2' is returned for 2. 'A' is
        returned for 10. 'B' for 11

        :type num: int
        :rtype: str
        """
        return chr(num + ord('0')) if (0 <= num <= 9) else chr(num - 10 + ord('A'))

    def strev(self, m_string, index):
        """Utility function to reverse a string"""
        length = index
        i = 0
        while i < length // 2:
            m_string[i], m_string[length - i - 1] = m_string[length - i - 1], m_string[i]
            i += 1

    def from_decimal(self, res, base, inputNum):
        """Function to convert a given decimal number to a base 'base' and"""
        index = 0  # Initialize index of result

        # Convert input number is given base by repeatedly dividing it by base and taking remainder
        while inputNum > 0:
            res[index] = self.re_value(inputNum % base)
            index += 1
            inputNum //= base
        res[index] = '\0'

        # Reverse the result
        self.strev(res, index)
        return "".join(res[:index])

    def value(self, c):
        """
        :type c: str
        :rtype: int
        """
        return ord(c) - ord('0') if ord('0') <= ord(c) <= ord('9') else ord(c) - ord('A') + 10

    def to_decimal(self, m_str, base):
        """Function to convert a number from given base 'b' to decimal"""
        length = len(m_str)
        power = 1  # Initialize power of base
        num = 0  # Initialize result

        # Decimal equivalent is str[len-1]*1 + str[len-1]*base + str[len-1]*(base^2) + ...
        for i in range(length - 1, -1, -1):
            # A digit in input number must be less than number's base
            if self.value(m_str[i]) >= base:
                print("Invalid Number")
                return -1

            num += self.value(m_str[i]) * power
            power = power * base

        return num


if __name__ == '__main__':
    test = BaseConversion()
    m_str = "11A"
    base = 16
    print("Decimal equivalent of %s in base %d is %d\n" %
          (m_str, base, test.to_decimal(m_str, base)))

    # How to do reverse?

    # Let the given input decimal number be "inputNum" and target base be "base". We repeatedly
    # divide inputNum by base and store the remainder. We finally reverse the obtained string.
    # Below is C implementation.

    inputNum = 282
    base = 16
    res = [None] * 100
    print("Equivalent of %d in base %d is  %s\n" % (
        inputNum, base, test.from_decimal(res, base, inputNum)))
