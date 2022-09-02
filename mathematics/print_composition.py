MAX_POINT = 3
ARR_SIZE = 100

arr = [0] * ARR_SIZE


def get_composition(num, i):
    if num == 0:
        print_arr(i)

    elif num > 0:
        for k in range(1, MAX_POINT + 1):
            arr[i] = k
            get_composition(num - k, i + 1)


def print_arr(arr_size):
    for i in range(arr_size):
        print("%d " % arr[i])


if __name__ == "__main__":
    n = 5
    get_composition(n, 0)
