def get_jump_count(jumpHeight, declined, heightList=[]):
    noOfJump = 0
    for height in heightList:
        while height > 0:
            height = height - jumpHeight
            if height > 0:
                height += declined
            noOfJump += 1
    return noOfJump


if __name__ == "__main__":
    """
    10, 1, 1, 2, 1
    5, 1, 2, 9, 10
    4, 2, 2, 3, 4
    """
    ip1 = int(input())
    ip2 = int(input())
    ip3_cnt = 0
    ip3_cnt = int(input())
    ip3_i = 0
    ip3 = []
    while ip3_i < ip3_cnt:
        ip3_item = int(input())
        ip3.append(ip3_item)
        ip3_i += 1

    output = get_jump_count(ip1, ip2, ip3)
    print(str(output))