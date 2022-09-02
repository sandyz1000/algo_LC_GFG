# coding=utf-8
# n=range(100) -- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ...]
# delete every second number 1,3,5,7,9,11,13,15,17,19, ....
# delete every third number 1, 3, 7, 9, 13, 15, 19, ....


counter = 2


def is_lucky(n):
    global counter
    position = n
    if counter > n:
        return 1
    if counter % n == 0:
        return 0

    position -= position / counter
    counter += 1
    return is_lucky(position)


if __name__ == "__main__":
    x = 7
    if is_lucky(x):
        print("%d is a lucky no." % x)
    else:
        print("%d is not a lucky no." % x)
