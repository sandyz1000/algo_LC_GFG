"""
Turn an image by 90 degree

Given an image, how will you turn it by 90 degrees? A vague question. Minimize the browser and try
your solution before going further.

An image can be treated as 2D matrix which can be stored in a buffer. We are provided with matrix
dimensions and it's base address. How can we turn it?

For example see the below picture,

    * * * ^ * * *
    * * * | * * *
    * * * | * * *
    * * * | * * *

After rotating right, it appears (observe arrow direction)

    * * * *
    * * * *
    * * * *
    -- - - >
    * * * *
    * * * *
    * * * *

Explanation:
----------------------------
The idea is simple. Transform each row of source matrix into required column of final image.
We will use an auxiliary buffer to transform the image.

From the above picture, we can observe that

first row of source ------> last column of destination
second row of source ------> second last column of destination
so ... on
last row of source ------> first column of destination

"""


def rotate(pS, pD, r, c):
    for row in range(r):
        for col in range(c):
            pD[col][r - row - 1] = pS[row][col]


if __name__ == '__main__':
    # Output:
    # 9	    5	1
    # 10	6	2
    # 11	7	3
    # 12	8	4
    image = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12]]
    # setting initial values and memory allocation
    m, n = 3, 4
    pDestination = [[0 for i in range(m)] for j in range(n)]

    # process each buffer
    print("Before rotation", image)
    rotate(image, pDestination, m, n)
    print("After rotation", pDestination)