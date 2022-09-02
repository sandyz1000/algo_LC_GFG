"""
Print all possible expressions that evaluate to a target
Given a string that contains only digits from 0 to 9, and an integer value, target.
Find out how many expressions are possible which evaluate to target using binary
operator +, – and * in given string of digits.

Input : "123",  Target : 6
Output : {“1+2+3”, “1*2*3”}

Input : “125”, Target : 7
Output : {“1*2+5”, “12-5”}

https://www.geeksforgeeks.org/print-all-possible-expressions-that-evaluate-to-a-target/


This problem can be solved by putting all possible binary operator in mid between to digits and
evaluating them and then check they evaluate to target or not.

While writing the recursive code, we need to keep these variable as argument of recursive method
– result vector, input string, current expression string, target value, position till which input
is processed, current evaluated value and last value in evaluation.

Last value is kept in recursion because of multiplication operation, while doing multiplication we
need last value for correct evaluation.

See below example for better understanding –
---------------------------------------------
Input is 125, suppose we have reached till 1+2 now,
Input = “125”, current expression = “1+2”,
position = 2, current val = 3, last = 2

Now when we go for multiplication, we need last
value for evaluation as follows:

current val = current val - last + last * current val

First we subtract last and then add last * current
val for evaluation, new last is last * current val.
current val = 3 – 2 + 2*5 = 11
last = 2*5 = 10
---------------------------------------------
Another thing to note in below code is, we have ignored all numbers which start from 0 by imposing a
condition as first condition inside the loop so that we will not process number like 03, 05 etc.
"""
from typing import List
# Python program to find all possible expression which evaluate to target

# Utility recursive method to generate all possible expressions


def getExprUtil(res: List[str], curExp: str, input_string: str, target: int, pos: int, curVal: int, last: int):
    # true if whole input is processed with some operators
    if (pos == len(input_string)):
        # if current value is equal to target then only add to final solution
        # if question is : all possible o/p then just push_back without condition
        if (curVal == target):
            res.append(curExp)
        return

    # loop to put operator at all positions
    for i in range(pos, len(input_string)):
        # ignoring case which start with 0 as they are useless for evaluation
        if (i != pos and input_string[pos] == '0'):
            break

        # take part of input from pos to i
        part = input_string[pos: i]

        # take numeric value of part
        cur = int(part)
        # if pos is 0 then just send numeric value for next recurion
        if (pos == 0):
            getExprUtil(res, curExp + part, input_string, target, i + 1, cur, cur)
        # try all given binary operator for evaluation
        else:
            getExprUtil(res, curExp + "+" + part, input_string, target, i + 1, curVal + cur, cur)
            getExprUtil(res, curExp + "-" + part, input_string, target, i + 1, curVal - cur, -cur)
            getExprUtil(res, curExp + "*" + part, input_string, target, i + 1,
                        curVal - last + last * cur, last * cur)

# // Below method returns all possible expression evaluating to target


def getExprs(input_string: str, target: int):
    res = []
    getExprUtil(res, "", input_string, target, 0, 0, 0)
    return res


if __name__ == "__main__":
    input_string = "123"
    target = 6
    res = getExprs(input_string, target)
    print(res)

    input = "125"
    target = 7
    res = getExprs(input_string, target)
    print(res)
