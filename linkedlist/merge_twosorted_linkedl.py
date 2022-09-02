"""
Merge two sorted linked lists

Write a SortedMerge() function that takes two lists, each of which is sorted in increasing order,
and merges the two together into one list which is in increasing order. SortedMerge() should return
the new list. The new list should be made by splicing together the nodes of the first and the
second lists.

For example if the first linked list a is 5->10->15 and the other linked list b is 2->3->20, then
SortedMerge() should return a pointer to the head node of the merged list 2->3->5->10->15->20.

There are many cases to deal with: either 'a' or 'b' may be empty, during processing either 'a' or
'b' may run out first, and finally there's the problem of starting the result list empty, and
building it up while going through 'a' and 'b'.

"""

from __future__ import print_function


# Python program to merge two sorted linked lists
class Pointer(object):
    def __init__(self, value):
        self.value = value


class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def push(self, new_data):
        new_node = Node(new_data)  # allocate node
        new_node.next_node = self.head  # link the old list off the new node
        self.head = new_node  # move the head to point to the new node


class MergeLinkedList(object):
    def __init__(self):
        # a dummy first node to hang the result on
        self.dummy = Node(None)
        # tail points to the last result node
        self.tail = self.dummy

    def sorted_merge(self, a, b):
        """
        Method 1 (Using Dummy Nodes)

        The strategy here uses a temporary dummy node as the start of the result list. The
        pointer Tail always points to the last node in the result list, so appending new nodes is
        easy.

        The dummy node gives tail something to point to initially when the result list is empty.
        This dummy node is efficient, since it is only temporary, and it is allocated in the
        stack. The loop proceeds, removing one node from either 'a' or 'b', and adding it to
        tail. When we are done, the result is in dummy.next.

        Takes two lists sorted in increasing order, and splices their nodes together to make one
        big sorted list which is returned.
        """

        while True:
            if a is None:
                # if either list runs out, use the other list
                self.tail.next_node = b
                break
            elif b is None:
                self.tail.next_node = a
                break

            if a.data <= b.data:
                a_ptr = Pointer(a)
                self.move_node(a_ptr)
                a = a_ptr.value
            else:
                b_ptr = Pointer(b)
                self.move_node(b_ptr)
                b = b_ptr.value
            self.tail = self.tail.next_node
        return self.dummy.next_node

    def move_node(self, source_ref):
        """
        This function takes the node from the front of the source, and move it
        to the front of the dest.
        It is an error to call this with the source list empty.
        Before calling:
        source == {1, 2, 3}
        dest == {1, 2, 3}

        After calling:
        source == {2, 3}
        dest == {1, 1, 2, 3}
        """
        # the front source node
        new_node = source_ref.value
        assert (new_node is not None)

        source_ref.value = new_node.next_node  # Advance the source pointer
        new_node.next_node = self.tail.next_node  # Link the old dest off the new node
        self.tail.next_node = new_node  # Move dest to point to the new node


class MergeLinkedList2(object):
    def __init__(self):
        self.result = Node(None)
        # point to the last result pointer
        self.tail = self.result

    def sorted_merge(self, a, b):
        """
        Method 2 (Using Local References)

        This solution is structurally very similar to the above, but it avoids using a dummy
        node. Instead, it maintains a struct node** pointer, lastPtrRef, that always points to
        the last pointer of the result list. This solves the same case that the dummy node did -
        dealing with the result list when it is empty. If you are trying to build up a list at
        its tail, either the dummy node or the struct node** "reference" strategy can be used (
        see Section 1 for details).
        """
        while True:
            if a is None:
                self.result = b
                break

            elif b is None:
                self.result = a
                break

            if a.data <= b.data:
                a_ptr = Pointer(a)
                self.move_node(a_ptr)
                a = a_ptr.value
            else:
                b_ptr = Pointer(b)
                self.move_node(b_ptr)
                b = b_ptr.value

            # tricky: advance to point to the next ".next" field
            self.tail = self.tail.next_node
        return self.result

    def move_node(self, source_ref):
        """
        This function takes the node from the front of the source, and move it to the front of
        the dest. It is an error to call this with the source list empty.

        Before calling:
        source == {1, 2, 3}
        dest == {1, 2, 3}

        After calling:
        source == {2, 3}
        dest == {1, 1, 2, 3}
        """
        # the front source node
        new_node = source_ref.value
        assert (new_node is not None)

        source_ref.value = new_node.next_node  # Advance the source pointer
        new_node.next_node = self.tail.next_node  # Link the old dest off the new node
        self.tail.next_node = new_node  # Move dest to point to the new node


def sorted_merge_m3(a, b):
    """
    Method 3 (Using Recursion)
    Merge is one of those nice recursive problems where the recursive solution code is much cleaner
    than the iterative code. You probably wouldn't want to use the recursive version for
    production code however, because it will use stack space which is proportional to the length of
    the lists.
    :param a:
    :param b:
    :return:
    """
    if a is None:  # Base cases
        return b
    elif b is None:
        return a

    # Pick either a or b, and recur
    if a.data <= b.data:
        result = a
        result.next_node = sorted_merge_m3(a.next_node, b)
    else:
        result = b
        result.next_node = sorted_merge_m3(a, b.next_node)

    return result


def print_list(node):
    """Function to print nodes in a given linked list """
    while node is not None:
        print("%d" % node.data, end="->")
        node = node.next_node
    print("\n")


if __name__ == '__main__':
    # Start with the empty list
    # Let us create two sorted linked lists to test the functions Created lists,
    # a: 5->10->15
    # b: 2->3->20
    a = LinkedList()
    a.push(15)
    a.push(10)
    a.push(5)

    b = LinkedList()
    b.push(20)
    b.push(3)
    b.push(2)

    print("Method-2 --- Merged Linked List is: \n")
    test = MergeLinkedList()
    res = test.sorted_merge(a.head, b.head)
    print_list(res)

    a = LinkedList()
    a.push(15)
    a.push(10)
    a.push(5)

    b = LinkedList()
    b.push(20)
    b.push(3)
    b.push(2)

    print("Method-3 (recursion) --- Merged Linked List is: \n")
    res = sorted_merge_m3(a.head, b.head)
    print_list(res)
