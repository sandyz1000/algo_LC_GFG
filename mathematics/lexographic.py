from __future__ import print_function, unicode_literals


def filter_arr(arr):
    index = 0
    while index < len(arr):
        item = arr[index]
        if not validator(item):
            arr.pop(index)
        else:
            index += 1


def validator(item):
    n = len(item)
    for i in range(n-1):
        if ord(item[i+1]) < ord(item[i]):
            return False
    return True


def comparator(input_1, input_2):
    if len(input_1) > len(input_2):
        return 1

    if len(input_1) < len(input_2):
        return -1

    if len(input_1) == len(input_2):
        if sum([ord(i) for i in input_1]) < sum([ord(i) for i in input_2]):
            return -1
        else:
            return 1

if __name__ == "__main__":
    arr = ["abcd", "abde", "abdc", "abc", "ab"]
    filter_arr(arr)
    result = sorted(arr, key=comparator)

    print(result)
