"""
Find the largest multiple of 3 | Set 1 (Using Queue)

Given an array of non-negative integers. Find the largest multiple of 3 that can be formed from
array elements.

For example, if the input array is {8, 1, 9}, the output should be “9 8 1”, and if the input
array is {8, 1, 7, 6, 0}, output should be “8 7 6 0”.

-----------------------------------------------------------------
Method 1 (Brute Force)
-----------------------------------------------------------------

The simple & straight forward approach is to generate all the combinations of the elements and keep
track of the largest number formed which is divisible by 3.

Time Complexity: O(n x 2^n). There will be 2^n combinations of array elements. To compare each
combination with the largest number so far may take O(n) time.
Auxiliary Space: O(n) // to avoid integer overflow, the largest number is assumed to be stored in
the form of array.

-----------------------------------------------------------------
Method 2 (Tricky)
-----------------------------------------------------------------

This problem can be solved efficiently with the help of O(n) extra space. This method is based on
the following facts about numbers which are multiple of 3.

1) A number is multiple of 3 if and only if the sum of digits of number is multiple of 3.
For example, let us consider 8760, it is a multiple of 3 because sum of digits is 8 + 7+ 6+ 0 = 21,
which is a multiple of 3.

2) If a number is multiple of 3, then all permutations of it are also multiple of 3.
For example, since 6078 is a multiple of 3, the numbers 8760, 7608, 7068, ... are also multiples
of 3.

3) We get the same remainder when we divide the number and sum of digits of the number.
For example, if divide number 151 and sum of it digits 7, by 3, we get the same remainder 1.

==What is the idea behind above facts?==
The value of 10%3 and 100%3 is 1. The same is true for all the higher powers of 10, because 3
divides 9, 99, 999, .... etc.
Let us consider a 3 digit number n to prove above facts. Let the first, second and third digits
of n be 'a', 'b' and 'c' respectively. n can be written as

n = 100.a + 10.b + c
Since (10^x)%3 is 1 for any x, the above expression gives the same remainder as following expression

 1.a + 1.b + c
So the remainder obtained by sum of digits and 'n' is same.

Following is a solution based on the above observation.

1. Sort the array in non-decreasing order.

2. Take three queues. One for storing elements which on dividing by 3 gives remainder as 0.The
second queue stores digits which on dividing by 3 gives remainder as 1. The third queue stores
digits which on dividing by 3 gives remainder as 2. Call them as queue0, queue1 and queue2

3. Find the sum of all the digits.

4. Three cases arise:
    4.1 The sum of digits is divisible by 3. Dequeue all the digits from the three queues.
    Sort them in non-increasing order. Output the array.

    4.2 The sum of digits produces remainder 1 when divided by 3.
    Remove one item from queue1. If queue1 is empty, remove two items from queue2. If queue2
    contains less than two items, the number is not possible.

    4.3 The sum of digits produces remainder 2 when divided by 3.
    Remove one item from queue2. If queue2 is empty, remove two items from queue1. If queue1
    contains less than two items, the number is not possible.

5. Finally empty all the queues into an auxiliary array. Sort the auxiliary array in non-increasing
order. Output the auxiliary array.

==The above method can be optimized in following ways.==
1) We can use Heap Sort or Merge Sort to make the time complexity O(nLogn).

2) We can avoid extra space for queues. We know at most two items will be removed from the input
array. So we can keep track of two items in two variables.

3) At the end, instead of sorting the array again in descending order, we can print the ascending
sorted array in reverse order. While printing in reverse order, we can skip the two elements to be
removed.

Time Complexity: O(nLogn), assuming a O(nLogn) algorithm is used for sorting.  """


from functools import cmp_to_key


class MyQueue(object):
    def __init__(self, capacity=10):
        self.front = -1
        self.rear = -1
        self.capacity = capacity
        self.queue = [None for i in range(self.capacity)]

    def is_empty(self):
        return self.front == -1

    def enqueue(self, item):
        self.rear += 1
        self.queue[self.rear] = item
        if self.is_empty():
            self.front += 1

    def dequeue(self):
        item = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1
        return item

    def peek(self):
        """
        Return the top item of the queue
        :return:
        """
        return self.queue[self.front]


def populate_aux(queue0, queue1, queue2, aux):
    """
    :param aux: list
    :param queue0: MyQueue
    :param queue1: MyQueue
    :param queue2: MyQueue
    :return:
    """
    top = 0
    while not queue0.is_empty():
        aux[top] = queue0.dequeue()
        top += 1

    while not queue1.is_empty():
        aux[top] = queue1.dequeue()
        top += 1

    while not queue2.is_empty():
        aux[top] = queue2.dequeue()
        top += 1

    return top


# The main function that finds the largest possible multiple of 3 that can be formed by arr[]
# elements
def find_max_multiple_of_3(arr, size):
    """

    :param arr: list
    :param size: int
    :return:
    """
    # Step 1: sort the arr in non-decreasing order
    arr = sorted(arr, key=cmp_to_key(lambda a, b: a - b))
    summation = 0

    # Create 3 queues to store numbers with remainder 0, 1 and 2 respectively
    queue0, queue1, queue2 = (MyQueue(size) for q in range(3))
    # Step 2 and 3 get the summation of numbers and place them in corresponding queues
    for i in range(size):
        summation += arr[i]
        if (arr[i] % 3) == 0:
            queue0.enqueue(arr[i])

        elif (arr[i] % 3) == 1:
            queue1.enqueue(arr[i])

        elif (arr[i] % 3) == 2:
            queue2.enqueue(arr[i])

    # The summation produces remainder 1
    if (summation % 3) == 1:
        # // either remove one item from queue1
        if not queue1.is_empty():
            queue1.dequeue()

        # // or remove two items from queue2
        else:
            if not queue2.is_empty():
                queue2.dequeue()
            else:
                return 0

            if not queue2.is_empty():
                queue2.dequeue()
            else:
                return 0

    # The summation produces remainder 2
    if (summation % 3) == 2:
        # either remove one item from queue2
        if not queue2.is_empty():
            queue2.dequeue()

        # or remove two items from queue1
        else:
            if not queue1.is_empty():
                queue1.dequeue()
            else:
                return 0

            if not queue1.is_empty():
                queue1.dequeue()
            else:
                return 0

    # Empty all the queues into an auxiliary arr.
    aux = [0] * size
    top = populate_aux(queue0, queue1, queue2, aux)
    aux = sorted(aux, key=cmp_to_key(lambda a, b: b - a))
    print("Multiple of 3", aux[:top])
    return top


if __name__ == "__main__":
    arr = [8, 1, 7, 6, 0]
    size = len(arr)

    result = find_max_multiple_of_3(arr, size)

    print("Not possible" if not result else result)


