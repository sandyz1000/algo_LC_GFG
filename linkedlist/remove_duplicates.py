"""
Remove duplicates from a sorted linked list

Write a removeDuplicates() function which takes a list sorted in non-decreasing order and deletes
any duplicate nodes from the list. The list should only be traversed once.

For example if the linked list is 11->11->11->21->43->43->60 then removeDuplicates() should convert
the list to 11->21->43->60.

--------------------------------------------------
Remove duplicates from an unsorted linked list
Write a removeDuplicates() function which takes a list and deletes any duplicate nodes from the
list. The list is not sorted.

For example if the linked list is 12->11->12->21->41->43->21 then removeDuplicates() should convert
the list to 12->11->21->41->43.

"""
from __future__ import print_function


class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def push(self, new_data):
        """Function to insert a node at the beginging of the linked list"""
        new_node = Node(new_data)
        new_node.next_node = self.head
        self.head = new_node

    def print_list(self):
        node = self.head
        while node is not None:
            print("%d " % node.data)
            node = node.next_node

    def remove_duplicates_meth1(self):
        """
        METHOD 1 Algorithm:
        Traverse the list from the head (or start) node. While traversing, compare each node with
        its next node. If data of next node is same as current node then delete the next node.
        Before we delete a node, we need to store next pointer of the node

        Time Complexity: O(n) where n is number of nodes in the given linked list.
        The function removes duplicates from a sorted list
        """
        # Pointer to traverse the linked list
        current = self.head
        if current is None:  # do nothing if the list is empty
            return

        # Traverse the list till last node
        while current.next_node is not None:
            # Compare current node with next node
            if current.data == current.next_node.data:
                # Pointer to store the next pointer of a node to be deleted
                next_next = current.next_node.next_node
                del current.next_node
                current.next_node = next_next
            # This is tricky: only advance if no deletion
            else:
                current = current.next_node

    def remove_duplicates_meth2(self):
        """
        Remove duplicates from an unsorted linked list

        METHOD 2 (Using two loops)
        This is the simple way where two loops are used. Outer loop is used to pick the elements
        one by one and inner loop compares the picked element with rest of the elements.

        Time Complexity: O(n^2)

        Function to remove duplicates from a unsorted linked list

        :return:
        """
        ptr1 = self.head

        # Pick elements one by one
        while ptr1 is not None and ptr1.next_node is not None:
            ptr2 = ptr1
            # Compare the picked element with rest of the elements
            while ptr2.next_node is not None:
                # If duplicate then delete it
                if ptr1.data == ptr2.next_node.data:
                    # sequence of steps is important here
                    dup = ptr2.next_node
                    ptr2.next_node = ptr2.next_node.next_node
                    del dup

                else:  # This is tricky
                    ptr2 = ptr2.next_node

            ptr1 = ptr1.next_node

    def remove_duplicates_meth3(self):
        """
        METHOD 3 (Use Hashing)

        We traverse the link list from head to end. For every newly encountered element, we check
        whether it is in the hash table: if yes, we remove it otherwise we put it in the hash table.

        Time Complexity: O(n) on average (assuming that hash table access time is O(1) on average)

        Function to remove duplicates from a unsorted linked list
        :param self:
        :return:
        """
        # Hash to store seen values
        seen = set()
        # Pick elements one by one
        curr, prev = self.head, None
        while curr is not None:
            # If current value is seen before
            if curr.data in seen:
                prev.next_node = curr.next_node
                del curr
            else:
                seen.add(curr.data)
                prev = curr
            curr = prev.next_node

    def remove_duplicates_meth4(self):
        """
        METHOD 4 (Use Sorting)

        In general, Merge Sort is the best suited sorting algorithm for sorting linked lists
        efficiently.

        1) Sort the elements using Merge Sort. We will soon be writing a post about sorting a linked
        list. O(nLogn)

        2) Remove duplicates in linear time using the algorithm for removing duplicates in sorted
        Linked List. O(n)

        Please note that this method doesn't preserve the original order of elements.
        Time Complexity: O(nLogn)
        """
        pass


if __name__ == '__main__':
    print("\n\n----METHOD-1-----\n\n")
    # Let us create a sorted linked list to test the functions Created linked list will be
    # 11->11->11->13->13->20
    llist = LinkedList()

    llist.push(20)
    llist.push(13)
    llist.push(13)
    llist.push(11)
    llist.push(11)
    llist.push(11)
    print("\n Linked list before duplicate removal  ")
    llist.print_list()
    # Remove duplicates from linked list
    llist.remove_duplicates_meth1()
    print("\n Linked list after duplicate removal ")
    llist.print_list()

    # The constructed linked list is: 10->12->11->11->12->11->10
    llist = LinkedList()
    llist.push(10)
    llist.push(12)
    llist.push(11)
    llist.push(11)
    llist.push(12)
    llist.push(11)
    llist.push(10)

    print("Linked list before removing duplicates\n")
    llist.print_list()
    llist.remove_duplicates_meth2()
    print("\nLinked list after removing duplicates ")
    llist.print_list()

    #  The constructed linked list is: 10->12->11->11->12->11->10
    llist = LinkedList()
    llist.push(10)
    llist.push(12)
    llist.push(11)
    llist.push(11)
    llist.push(12)
    llist.push(11)
    llist.push(10)

    print("Linked list before removing duplicates : \n")
    llist.print_list()
    llist.remove_duplicates_meth3()

    print("\nLinked list after removing duplicates : \n")
    llist.print_list()
