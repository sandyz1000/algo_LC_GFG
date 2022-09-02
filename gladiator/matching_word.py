from __future__ import print_function, absolute_import
from collections import Counter


def appearanceCount(input_1, input_2, input_3, input_4):
    count = 0
    for i in range(input_2 - input_1 + 1):
        count = count + check_match(input_3, input_4[i:i + input_1])
    return count


def check_match(str1, str2):
    f = Counter()
    for i in str1:
        f[i] += 1
    for i in str2:
        if f[i] == 0:
            return 0
        else:
            f[i] -= 1
    return 1


def permute(a, l, r, values=[]):
    if l == r:
        values.append("".join(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r, values)
            a[l], a[i] = a[i], a[l]  # backtrack


def args_counter(source_size, dest_size, source, dest):
    counter = 0
    if dest_size >= source_size:
        a = list(source)
        values = []
        permute(a, 0, source_size - 1, values)
        for i in range(dest_size - source_size + 1):
            if dest[i:i + source_size] in values:
                counter += 1
    return counter


if __name__ == '__main__':
    input1 = 4
    input2 = 7
    input3 = "asda"
    input4 = "asdaawe"
    print(appearanceCount(input1, input2, input3, input4))
    # n = len(input3)
    # a = list(input3)
    # values = []
    # permute(a, 0, n - 1, values)
    # print values
    print(args_counter(input1, input2, input3, input4))
