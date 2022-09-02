# coding=utf-8
"""
Dynamic Programming | Set 22 (Box Stacking Problem)

You are given a set of n types of rectangular 3-D boxes, where the i^th box has height h(i),
width w(i) and depth d(i) (all real numbers). You want to create a stack of boxes which is as
tall as possible, but you can only stack a box on top of another box if the dimensions of the 2-D
base of the lower box are each strictly larger than those of the 2-D base of the higher box. Of
course, you can rotate a box so that any side functions as its base. It is also allowable to use
multiple instances of the same type of box

REFER DIAGRAM
http://www.geeksforgeeks.org/dynamic-programming-set-21-box-stacking-problem/


MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkdc;cldOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xoc;::c:::;cokKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMXd:;:lllllllllllc:;:xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMM0:,:::coddddddoc:::,cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMM0clxdlcccllcccccodxllKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMM0ldOOOOkxc;cdxkOOOOo:xNWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWKkc;d000000dcx0000000d,;ldkKWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMM0:'',:ox0KXXklkXXXKOxoc:c:,':0MMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWXo;cc:;,,:ox0kokKOxolc:::::cc;oXWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWKkoc',oxxdocc;,::;colccccccodxxo,'cokKWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWXOdl::cc;;dkkkkkkdoc::cccclodkkkkkkd;;cc::ldOXWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMWKkoc::cllll;;xOOOOOOOOOkl;;lkOOOOOOOOOx;;llllc::ldkKWMMMMMMMMMMMMM
MMMMMMMMMMMM0c,;clooooool;:k0000000000xccx0000000000k:;loooololc;,c0MMMMMMMMMMMM
MMMMMMMMMMMWx,;;;:clooooo:;d0KKKKKKKKKxccxKKKKKKKKK0d;:ooooolc:;;;,xWMMMMMMMMMMM
MMMMMMMMMMMMx:oolc:::clodocclox0XXXXXXkllkXXXXXX0xolccodolc:::cloo:xMMMMMMMMMMMM
MMMMMMMMMMMWx:oddddolc::clodolclox0XNNOooONNX0xolclodolc::cloddddo:xMMMMMMMMMMMM
MMMMMMMMMMMMx:dxdxddxxdolc:ccoddollodOkookOdolloddocc:clodxxddxdxd:xMMMMMMMMMMMM
MMMMMMMMMMMMxcdxxxxxxxxxxxdoccccodxdolc::clodxdoccccodxxxxxxxxxxxdcxMMMMMMMMMMMM
MMMMMMMMMMMWxcxkkxkkkkkkkkkxxxdlcccldxxxxxxdlcccldxxxkkkkkkkkkkkkxcxWMMMMMMMMMMM
MMMMMMMMMMMWxcxkkkkkkkkkkkkkkkkkkxolccllllccloxkkkkkkkkkkkkkkkkkkxcxWMMMMMMMMMMM
MMMMMMMMMMWKlckOOOOOOOOOOOOOOOOOOkkOkxc,,cxkOkkOOOOOOOOOOOOOOOOOOkclKWMMMMMMMMMM
MMMMMMMN0xoc':kOOOOOOOOOOOOOOOOOOOOOOOd::dOOOOOOOOOOOOOOOOOOOOOOOk:'cox0NMMMMMMM
MMMWXOdl::cl;cO000000000000000000000O0dccd0O000000000000000000000kc;cc::ldOXWMMM
N0koc:clllll;cO00000000000000000000000xccx00000000000000000000000Oc;lllllc:cokKN
;,:clooolool;cO00K00KKKKKKKKKKKKKK0K0KxccxK0KKKKKKKKKKKKKKK000K00Oc;loooooolc;,;
':;;:clooooo::x0KKKKKKKKKKKKKKKKKKKKKKkllkKKKKKKKKKKKKKKKKKKKKKK0x::ooooolc:;;:'
;ool::::cloolcclox0KXXKKXXXXXXXKXXXXXXkllkXXXXXXKXXXXXXXKKXXK0xolccloolc:;::loo;
;odddooc::::lodolccodOKXXXXXXXXXXXXXXXkllkXXXXXXXXXXXXXXXKOdocclodol::::coooddo;
;dddddddddlc:::coddoccldkKXNNXNNNNNXXNOllONXXNNNNNXNNXKkdlccoddoc:::clddddddddd;
;ddddddddddddolc::cldddlclox0XNNNNNNNNOooONNNNNNNNX0xolcldddlc::clodddddddddddd;
;dxxxddddddxddxxdocc:cloddolloxOXNWNWWOooOWWNWNXOxolloddolc:ccodxxdddddddddxxxd;
:xxxxxxxxxxxxxxxxxxxdlccccodxdolodkKNW0oo0WNKkdolodxdoccccldxxxxxxxxxxxxxxxxxxx:
:xxxxxxxxxxxxxxxxxxxxxxxolcccldxxolodkdccdkdoloxxdlcccloxxxxxxxxxxxxxxxxxxxxxxx:
:xkkkkkkxxxxxxxxxkkkkxxkkkxdocccldxxdoc::codxxdlcccodxkkkxkkkkkkxxxxxxxxkkkkkkx:
:kkkkkkkkkkkkkkkkkkkkkkkkkkkkkxdlccloxkkkkxolccldxkkkkkkkkkkkkkkkkkkkkkkkkkkkkk:
:kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxolllccllloxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkc
ckkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkkOkdccdkOkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkc
cOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOdccdOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOc
cOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOdccdOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOc
cO00000000000000000000000000000O0O0000dccd0000O0O00000000000000000000000000000Oc
l0000000000000000000000000000000000000dccd0000000000000000000000000000000000000l
l0000000000000000000000000000000000000dccd0000000000000000000000000000000000000l
l0K0KKKKKKKKKKKKKKKKKKKKKKKKKKKK0KK0KKdccdKK0KKKKKKKKKKKKKKKKKKKKKKK0KKKKKKK0K0l
lKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKdccdKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKl
oxk0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKdccdKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0kxo
N0kxxxOKXXKKXXXXXXXXXXXXXXXXXXXXXXXXXXdccdXKXXXXXXXXXXXXXXXXXXXXXXXXKKXXKOxxxk0N
MMMWXOkxxOKXXXXXXXXXXXXXXXXXXXXXXXXXXXdccdXXXXXXXXXXXXXXXXXXXXXXXXXXXKOxxkOXWMMM
MMMMMMMN0kxxk0XXXXXXXXXXXXXXXXXXXXXXXXdccdXXXXXXXXXXXXXXXXXXXXXXXX0kxxk0NMMMMMMM
MMMMMMMMMMWXOkxxOKNNNNNNNXXNNNNNXNNXXNdccdNXXNNXNNNNNXXNNNNNNNKOxxkOXWMMMMMMMMMM
MMMMMMMMMMMMMWN0kkkOKNNNNNNNNNNNNNNNNNOooONNNNNNNNNNNNNNNNNKOkkk0NWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWKOkkk0XNNNNNNNNNNNNNOooONNNNNNNNNNNNNX0kkkOKWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWN0kkkOXNWWWWWWWWWOooOWWWWWWWWWNXOkkk0NWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWKOkkkKNWWWWWW0oo0WWWWWWNKkkkOKWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWX0kkk0XWWW0oo0WWWX0kkk0XWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKOkkOKOddOKOkkOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0kdlldk0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

---------------------------------------------
Explanation:
---------------------------------------------

The Box Stacking problem is a variation of LIS problem. We need to build a maximum height stack.

Following are the key points to note in the problem statement:
1) A box can be placed on top of another box only if both width and depth (Area=width*depth) of
the upper placed box are smaller than width and depth of the lower box respectively.

2) We can rotate boxes. For example, if there is a box with dimensions {1x2x3} where 1 is height,
2×3 is base, then there can be three possibilities, {1x2x3}, {2x1x3} and {3x1x2}.

3) We can use multiple instances of boxes. What it means is, we can have two different rotations of
a box as part of our maximum height stack.

Following is the solution based on DP solution of LIS problem.

1) Generate all 3 rotations of all boxes. The size of rotation array becomes 3 times the size of
original array. For simplicity, we consider depth as always smaller than or equal to width.

2) Sort the above generated 3n boxes in decreasing order of base area.

3) After sorting the boxes, the problem is same as LIS with following optimal substructure property.
MSH(i) = Maximum possible Stack Height with box i at top of stack
MSH(i) = { Max ( MSH(j) ) + height(i) } where j < i and width(j) > width(i) and depth(j) > depth(i).
If there is no such j then MSH(i) = height(i)

4) To get overall maximum height, we return max(MSH(i)) where 0 < i < n

"""
# Dynamic Programming implementation of Box Stacking problem
from dataclasses import dataclass
from typing import List
from functools import cmp_to_key


@dataclass(init=True, frozen=True)
class Box(object):
    """
    Representation of a box
    Time Complexity: O(n^2)
    Auxiliary Space: O(n)

    for simplicity of solution, always keep w <= d
    h --> height, w --> width, d --> depth
    """
    h: int
    w: int
    d: int


def max_stack_height(arr: List[Box], n: int):
    """
    Returns the height of the tallest stack that can be formed with give type of boxes
    Create an arr of all rotations of given boxes
    For example, for a box {1, 2, 3}, we consider three instances{{1, 2, 3}, {2, 1, 3}, {3, 1, 2}}
    """
    rot = [None for i in range((3 * n))]
    index = 0
    for i in range(n):
        rot[index] = arr[i]
        index += 1

        # First rotation of box
        rot[index] = Box(arr[i].w, min(arr[i].h, arr[i].d), max(arr[i].h, arr[i].d))
        index += 1

        # Second rotation of bo
        rot[index] = Box(arr[i].d, min(arr[i].h, arr[i].w), max(arr[i].h, arr[i].w))
        index += 1

    # Now the number of boxes is 3n
    n = 3 * n

    # Sort the arr 'rot[]' in decreasing order, using library function for quick sort
    rot.sort(key=cmp_to_key(lambda a, b: (b.d * b.w) - (a.d * a.w)))

    # Uncomment following two lines to print all rotations
    for i in range(n):
        print("%d x %d x %d" % (rot[i].h, rot[i].w, rot[i].d))

    # Initialize msh values for all indexes
    # msh[i] --> Maximum possible Stack Height with box i on top
    msh = [rot[i].h for i in range(n)]

    # Compute optimized msh values in bottom up manner
    for i in range(1, n):
        for j in range(i):
            if rot[i].w < rot[j].w and rot[i].d < rot[j].d and msh[i] < msh[j] + rot[i].h:
                msh[i] = msh[j] + rot[i].h

    # Pick maximum of all msh values
    return max(msh)


def max_stack_height_rec(arr: List[Box], n: int):
    """
    Returns the height of the tallest stack that can be formed with give type of boxes
    Create an arr of all rotations of given boxes
    For example, for a box {1, 2, 3}, we consider three instances{{1, 2, 3}, {2, 1, 3}, {3, 1, 2}}
    """
    def _lis(arr, n):
        max_until_now = arr[n - 1].h
        for i in range(1, n):
            res = _lis(arr, i)
            if arr[i - 1].d > arr[n - 1].d and arr[i - 1].w > arr[n - 1].w and \
                    res + arr[i - 1].h > max_until_now:
                max_until_now = res + arr[i - 1].h

        # Compare max_ending_here with overall maximum. And update the overall maximum if needed
        maximum = max(_lis.maximum, max_until_now)
        return maximum

    _lis.maximum = 0

    # rot = [None for i in range((3 * n))]
    rot = [None] * (3 * n)
    index = 0
    for i in range(n):
        rot[index] = arr[i]
        index += 1

        # First rotation of box
        rot[index] = Box(arr[i].w, min(arr[i].h, arr[i].d), max(arr[i].h, arr[i].d))
        index += 1

        # Second rotation of bo
        rot[index] = Box(arr[i].d, min(arr[i].h, arr[i].w), max(arr[i].h, arr[i].w))
        index += 1

    # Now the number of boxes is 3n
    n = 3 * n

    # Sort the arr 'rot[]' in decreasing order, using library function for quick sort
    rot.sort(key=cmp_to_key(lambda a, b: (b.d * b.w) - (a.d * a.w)))

    # Uncomment following two lines to print all rotations
    for i in range(n):
        print("%d x %d x %d" % (rot[i].h, rot[i].w, rot[i].d))

    return _lis(rot, len(rot))


if __name__ == '__main__':
    # Output: The maximum possible height of stack is 60
    arr = [Box(4, 6, 7), Box(1, 2, 3), Box(4, 5, 6), Box(10, 12, 32)]
    # print("The maximum possible height of stack is %d" % max_stack_height(arr, len(arr)))
    print("The maximum possible height of stack is %d" % max_stack_height_rec(arr, len(arr)))
