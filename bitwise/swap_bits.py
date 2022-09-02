def swap_bits(x, p1, p2, n):
    # Move all bits of first set to rightmost side
    set_1 = (x >> p1) & ((1 << n) - 1)

    # Move all bits of second set to rightmost side
    set_2 = (x >> p2) & ((1 << n) - 1)

    # XOR the two sets
    xor = (set_1 ^ set_2)

    # Put the xor bits back to their original positions
    xor = (xor << p1) | (xor << p2)

    # XOR the 'xor' with the original number so that the two sets are swapped
    result = x ^ xor
    return result


if __name__ == "__main__":
    res = swap_bits(28, 0, 3, 2)
    print("\nResult = %d " % res)
