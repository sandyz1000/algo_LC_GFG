"""
Function to check if a singly linked list is palindrome

Given a singly linked list of characters, write a function that returns true if the
given list is palindrome, else false.

HEAD-> R -> A -> D -> A -> R -> NULL
"""

# METHOD 1 (Use a Stack)
# A simple solution is to use a stack of list nodes. This mainly involves three steps.
# 1) Traverse the given list from head to tail and push every visited node to stack.

# 2) Traverse the list again. For every visited node, pop a node from stack and compare
# data of popped node with currently visited node.

# 3) If all nodes matched, then return true, else false.
#
# Time Complexity: O(n)
# Auxiliary Space: O(n) if Function Call Stack size is considered, otherwise O(1).
# Program to check if a linked list is palindrome
# Following methods solve this with constant extra space.

from __future__ import print_function


class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedListPalindrome(object):
    """
    METHOD 2 (By reversing the list)
    This method takes O(n) time and O(1) extra space.
    1) Get the middle of the linked list.
    2) Reverse the second half of the linked list.
    3) Check if the first half and second half are identical.

    4) Construct the original linked list by reversing the second half again and
    attaching it back to the first half

    To divide the list in two halves, method 2 of this post is used. When number of
    nodes are even, the first and second half contain exactly half nodes. The
    challenging thing in this method is to handle the case when number of nodes are
    odd. We don't want the middle node as part of any of the lists as we are going to
    compare them for equality. For odd case, we use a separate variable 'midnode'.

    Function to check if given linked list is palindrome or not

    """

    def __init__(self, head=None):
        self.head = head
        self.slow_ptr = None
        self.fast_ptr = None

    def push(self, new_data):
        """Push a node to linked list. Note that this function changes the head"""
        new_node = Node(new_data)
        new_node.next_node = self.head
        self.head = new_node

    def print_list(self):
        """A utility function to print a given linked list"""
        ptr = self.head
        output = []
        while ptr is not None:
            output.append("%s->" % ptr.data)
            ptr = ptr.next_node
        output.append("NULL")
        print("".join(output))

    def is_palindrome(self, head):
        self.slow_ptr = head
        self.fast_ptr = head
        prev_of_slow_ptr = head
        mid_node = None  # To handle odd size list
        res = True  # initialize result

        if head is not None and head.next_node is not None:
            # Get the middle of the list. Move slow_ptr by 1 and fast_ptr by 2, slow_ptr
            # will have the middle node
            while self.fast_ptr is not None and self.fast_ptr.next_node is not None:
                self.fast_ptr = self.fast_ptr.next_node.next_node

                # We need previous of the slow_ptr for linked lists with odd elements
                prev_of_slow_ptr = self.slow_ptr
                self.slow_ptr = self.slow_ptr.next_node

            # fast_ptr would become NULL when there are even elements in list. And not
            # NULL for odd elements. We need to skip the middle node for odd case and
            # store it somewhere so that we can restore the original list
            if self.fast_ptr is not None:
                mid_node = self.slow_ptr
                self.slow_ptr = self.slow_ptr.next_node

            # Now reverse the second half and compare it with first half
            second_half = self.slow_ptr
            prev_of_slow_ptr.next_node = None  # NULL terminate first half
            second_half = self.reverse(second_half)  # Reverse the second half

            res = self.compare_lists(head, second_half)  # compare

            # Construct the original list back
            second_half = self.reverse(second_half)  # Reverse the second half again

            # If there was a mid node (odd size case) which was not part of either first
            # half or second half.
            if mid_node is not None:
                prev_of_slow_ptr.next_node = mid_node
                mid_node.next_node = second_half
            else:
                prev_of_slow_ptr.next_node = second_half

        return res

    def reverse(self, second_half):
        """Function to reverse the linked list  Note that this function may change the
        head"""
        prev = None
        current = second_half
        while current is not None:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node

        return prev

    def compare_lists(self, head1, head2):
        """Function to check if two input lists have same data"""
        temp1 = head1
        temp2 = head2

        while temp1 and temp2:
            if temp1.data == temp2.data:
                temp1 = temp1.next_node
                temp2 = temp2.next_node
            else:
                return 0

        if temp1 is None and temp2 is None:  # Both are empty return
            return 1
        else:  # Will reach here when one is NULL and other is not
            return 0


class IsPalindromeRecursive(object):
    """
    METHOD 3 (Using Recursion)
    Use two pointers left and right. Move right and left using recursion and check for
    following in each recursive call.
    1) Sub-list is palindrome.
    2) Value at current left and right are matching.

    If both above conditions are true then return true.

    The idea is to use function call stack as container. Recursively traverse till the
    end of list. When we return from last NULL, we will be at last node. The last node
    to be compared with first node of list.

    In order to access first node of list, we need list head to be available in the
    last call of recursion. Hence we pass head also to the recursive function. If they
    both match we need to compare (2, n-2) nodes. Again when recursion falls back to (
    n-2)nd node, we need reference to 2nd node from head. We advance the head pointer
    in previous call, to refer to next node in the list.

    However, the trick in identifying double pointer. Passing single pointer is as good as
    pass-by-value, and we will pass the same pointer again and again. We need to pass the
    address of head pointer for reflecting the changes in parent recursive calls.
    """

    def __init__(self, head=None):
        self.head = head
        self.left = None

    def push(self, new_data):
        """Push a node to linked list. Note that this function changes the head"""
        new_node = Node(new_data)
        new_node.next_node = self.head
        self.head = new_node

    def print_list(self):
        """A utility function to print a given linked list"""
        ptr = self.head
        output = []
        while ptr is not None:
            output.append("%s->" % ptr.data)
            ptr = ptr.next_node
        output.append("NULL")
        print("".join(output))

    def is_palindrome_rec_util(self, right):
        """
        Initial parameters to this function are &head and head
        :param left:
        :param right:
        :return:
        """
        self.left = self.head
        if right is None:  # stop recursion when right becomes NULL
            return True

        # If sub-list is not palindrome then no need to check for current left and
        # right, return false
        isp = self.is_palindrome_rec_util(right.next_node)
        if not isp:
            return False

        # Check values at current left and right
        isp1 = right.data == self.left.data

        # Move left to next node
        self.left = self.left.next_node
        return isp1

    def is_palindrome(self, head):
        """
        A wrapper over isPalindromeUtil()
        :param self:
        :return:
        """
        return self.is_palindrome_rec_util(head)


if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedListPalindrome()
    string = "abacaba"
    i = 0

    print("-----------Iterative Method-----------")
    while i < len(string):
        llist.push(string[i])
        llist.print_list()
        print("Is Palindrome" if llist.is_palindrome(llist.head)
              else "Not Palindrome", "\n")
        i += 1

    print("\n-----------Recursive Method-----------\n")
    llist = IsPalindromeRecursive()
    i = 0
    while i < len(string):
        llist.push(string[i])
        llist.print_list()
        print("Is Palindrome" if llist.is_palindrome(llist.head)
              else "Not Palindrome", "\n")
        i +=1
