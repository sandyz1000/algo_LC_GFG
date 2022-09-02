"""
Remove Invalid Parentheses

An expression will be given which can contain open and close parentheses and optionally some
characters, No other operator will be there in string. We need to remove minimum number of
parentheses to make the input string valid. If more than one valid output are possible removing
same number of parentheses then print all such output.

Examples:
- - - - - - - - - - - - - - - - - - - -
Input  : str = "()())()" -
Output : ()()() (())()
There are two possible solutions
"()()()" and "(())()"

Input  : str = (v)())()
Output : (v)()()  (v())()
- - - - - - - - - - - - - - - - - - - -

As we need to generate all possible output we will backtrack among all states by removing one
opening or closing bracket and check if they are valid, if invalid then add the removed bracket
back and go for next state.
We will use BFS for moving through states, use of BFS will assure removal of minimal number
of brackets because we traverse into states level by level and each level corresponds to one
extra bracket removal.
Other than this BFS involve no recursion so overhead of passing parameters is also saved.

Below code has a method isValidString to check validity of string, it counts open and closed
parenthesis at each index ignoring non-parenthesis character. If at any instant count of close
parenthesis becomes more than open then we return false else we keep update the count variable.

"""
from collections import deque


# Python program to remove invalid parenthesis


def is_valid_string(m_string):
    """method returns true if string contains valid parenthesis"""
    cnt = 0
    for i in range(len(m_string)):
        if m_string[i] == '(':
            cnt += 1
        elif m_string[i] == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0

def remove_invalid_parenthesis(m_string):
    """method to remove invalid parenthesis"""

    is_parenthesis = (lambda c: (c == '(') or (c == ')'))

    if len(m_string) == 0:
        return

    # visit set to ignore already visited string
    visit = set()

    # queue to maintain BFS
    q = deque()
    level = False

    # pushing given string as starting node into queue
    q.append(m_string)
    visit.add(m_string)
    while q:
        m_string = q.popleft()
        if is_valid_string(m_string):
            print(m_string)
            # If answer is found, make level true so that valid string of only that level
            # are processed.
            level = True

        if level:
            continue

        for i in range(len(m_string)):
            if not is_parenthesis(m_string[i]):
                continue

            # Removing parenthesis from str and pushing into queue,if not visited already
            temp = m_string[0:i] + m_string[i + 1:]
            if temp not in visit:
                q.append(temp)
                visit.add(temp)


if __name__ == '__main__':
    # (())()
    # ()()()
    #
    # (v())()
    # (v)()()
    expression = "()())()"
    remove_invalid_parenthesis(expression)

    expression = "(v)())()"
    remove_invalid_parenthesis(expression)
