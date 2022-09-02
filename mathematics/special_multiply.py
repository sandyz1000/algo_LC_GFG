"""
Multiply two integers without using multiplication, division and bitwise operators, and no loops
By making use of recursion, we can multiply two integers with the given constraints.
"""
# To multiply x and y, recursively add x y times.


def multiply(x, y):
    """function to multiply two numbers x and y"""
    # 0  multiplied with anything gives 0
    if y == 0:
        return 0

    # Add x one by one
    if y > 0:
        return x + multiply(x, y - 1)

    # the case where y is negative
    if y < 0:
        return -multiply(x, -y)


if __name__ == '__main__':
    # Time Complexity: O(y) where y is the second argument to function multiply().
    print("\n %d" % multiply(5, -11))
