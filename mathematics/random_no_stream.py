"""
Select a random number from stream, with O(1) space
Given a stream of numbers, generate a random number from the stream. You are allowed to use only
O(1) space and the input is in the form of stream, so can't store the previously seen numbers. """
import random


def static_vars(**kwargs):
    def decorate(func):
        for key, value in kwargs.items():
            setattr(func, key, value)
        return func

    return decorate


@static_vars(count=0, res=0)
def select_random(x):
    """
    So how do we generate a random number from the whole stream such that the probability of picking
    any number is 1/n. with O(1) extra space? This problem is a variation of Reservoir Sampling.
    Here the value of k is 1.

    1) Initialize 'count' as 0, 'count' is used to store count of numbers seen so far in stream.
    2) For each number 'x' from stream, do following
        a) Increment 'count' by 1.
        b) If count is 1, set result as x, and return result.
        c) Generate a random number from 0 to 'count-1'. Let the generated random number be i.
        d) If i is equal to 'count – 1', update the result as x.

    ==How does this work==
    We need to prove that every element is picked with 1/n probability where n is the number of
    items seen so far. For every new stream item x, we pick a random number from 0 to ‘count -1’,
    if the picked number is ‘count-1’, we replace the previous result with x.

    To simplify proof, let us first consider the last element, the last element replaces the
    previously stored result with 1/n probability. So probability of getting last element as
    result is 1/n.

    Let us now talk about second last element. When second last element processed first time,
    the probability that it replaced the previous result is 1/(n-1). The probability that
    previous result stays when nth item is considered is (n-1)/n. So probability that the second
    last element is picked in last iteration is [1/(n-1)] * [(n-1)/n] which is 1/n.

    Similarly, we can prove for third last element and others.

    """
    select_random.count += 1
    # If this is the first element from stream, return it
    if select_random.count == 1:
        select_random.res = x
    else:
        i = random.randint(0, select_random.count)
        # Replace the prev random number with new number with 1/count probability
        if i == select_random.count - 1:
            select_random.res = x
    return select_random.res


if __name__ == '__main__':
    stream = [1, 2, 3, 4]
    n = len(stream)
    res = 0
    count = 0
    for i in range(n):
        print("Random number from first %d numbers is %d \n", i + 1,
              select_random(stream[i]), count, res)
