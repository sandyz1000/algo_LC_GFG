# coding=utf-8
"""
Write a function to get the intersection point of two Linked Lists.

http://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/

There are two singly linked lists in a system. By some programming error the end node of one of
the linked list got linked into the second list, forming a inverted Y shaped list. Write a
program to get the point where two linked list merge


    HEAD -> 3 -> 6 -> 9
                      \
                       -> 15 -> 30 -> NULL
                      /
            HEAD -> 10

-----------------------------------------------
Method 1(Simply use two loops)
-----------------------------------------------
Use 2 nested for loops. Outer loop will be for each node of the 1st list and inner loop will be
for 2nd list. In the inner loop, check if any of nodes of 2nd list is same as the current node of
first linked list. Time complexity of this method will be O(mn) where m and n are the number of
nodes in two lists.

-----------------------------------------------
Method 2 (Mark Visited Nodes)
-----------------------------------------------
This solution requires modifications to basic linked list data structure. Have a visited flag
with each node. Traverse the first linked list and keep marking visited nodes. Now traverse
second linked list, If you see a visited node again then there is an intersection point,
return the intersecting node. This solution works in O(m+n) but requires additional information
with each node. A variation of this solution that doesn't require modification to basic data
structure can be implemented using hash. Traverse the first linked list and store the addresses
of visited nodes in a hash. Now traverse the second linked list and if you see an address that
already exists in hash then return the intersecting node.

-----------------------------------------------
Method 3(Using difference of node counts)
-----------------------------------------------
1) Get count of the nodes in first list, let count be c1.
2) Get count of the nodes in second list, let count be c2.
3) Get the difference of counts d = abs(c1 - c2)
4) Now traverse the bigger list from the first node till d nodes so that from here
onwards both the lists have equal no of nodes.
5) Then we can traverse both the lists in parallel till we come across a common node.
(Note that getting a common node is done by comparing the address of the nodes)

-----------------------------------------------
Method 4(Make circle in first list)
-----------------------------------------------
1. Traverse the first linked list(count the elements) and make a circular linked list. (Remember
last node so that we can break the circle later on).

2. Now view the problem as find the loop in the second linked list. So the problem is solved.

3. Since we already know the length of the loop(size of first linked list) we can traverse those
many number of nodes in second list, and then start another pointer from the beginning of second
list. we have to traverse until they are equal, and that is the required intersection point.

4. remove the circle from the linked list.

Time Complexity: O(m+n)
Auxiliary Space: O(1)

Method 5 (Reverse the first list and make equations)
------------------------------------------------------------

1) Let X be the length of the first linked list until intersection point.
   Let Y be the length of the second linked list until the intersection point.
   Let Z be the length of the linked list from intersection point to End of
   the linked list including the intersection node.
   We Have
           X + Z = C1;
           Y + Z = C2;
2) Reverse first linked list.
3) Traverse Second linked list. Let C3 be the length of second list - 1.
     Now we have
        X + Y = C3
     We have 3 linear equations. By solving them, we get
       X = (C1 + C3 - C2)/2;
       Y = (C2 + C3 - C1)/2;
       Z = (C1 + C2 - C3)/2;
      WE GOT THE INTERSECTION POINT.
4)  Reverse first linked list.

Advantage: No Comparison of pointers.
Disadvantage : Modifying linked list(Reversing list).

Time complexity: O(m+n)
Auxiliary Space: O(1)

Method 6 (Traverse both lists and compare addresses of last nodes) This method is only to detect if
there is an intersection point or not. (Thanks to NeoTheSaviour for suggesting this)
---------------------------------------------------------------------------------------------------

1)  Traverse the list 1, store the last node address
2)  Traverse the list 2, store the last node address.
3)  If nodes stored in 1 and 2 are same then they are intersecting.

Time complexity:
Time complexity of this method is O(m+n) and used Auxiliary space is O(1)

----------------------------------------------------------------------
Intersection of two Sorted Linked Lists

Given two lists sorted in increasing order, create and return a new list representing the
intersection of the two lists. The new list should be made with its own memory — the original
lists should not be changed.

Example:
------------------------

Let the first linked list be 1->2->3->4->6 and second linked list be 2->4->6->8, then your
function should create and return a third list as 2->4->6.

"""
# Python program to find intersection of sorted linked list
# Time Complexity: O(m+n)
# Auxiliary Space: O(1)


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Pointer(object):
    def __init__(self, value):
        self.value = value


class IntersectionNodeUtility(object):
    """
    Method 3
    Intersection of two Sorted Linked Lists
    """

    def __init__(self, head1=None, head2=None):
        self.head1 = head1
        self.head2 = head2

    def get_intesection_node(self):
        """function to get the intersection point of two linked lists head1 and head2"""
        head1, head2 = self.head1, self.head2
        c1 = self.get_count(head1)
        c2 = self.get_count(head2)
        d = abs(c1 - c2)
        if c1 > c2:
            return self._get_intesection_node(d, head1, head2)
        else:
            return self._get_intesection_node(d, head2, head1)

    def _get_intesection_node(self, d, head1, head2):
        """
        function to get the intersection point of two linked lists head1 and head2
        where head1 has d more nodes than head2
        """
        current1 = head1
        current2 = head2

        for i in range(d):
            if current1 is None:
                return None
            current1 = current1.next_node

        while current1 is not None and current2 is not None:
            if current1.data == current2.data:
                return current1.data
            current1 = current1.next_node
            current2 = current2.next_node
        return None

    def get_count(self, head):
        current = head
        count = 0
        while current is not None:
            count += 1
            current = current.next_node

        return count


class IntersectionNodeUtility2(object):
    """Method-1 & Method-2"""

    def __init__(self, *args, **kwargs):
        pass
    
    def sorted_intersect_method1(self, a, b):
        """
        Method 1 (Using Dummy Node)
        ---------------------------
        The strategy here uses a temporary dummy node as the start of the result list. The
        pointer tail always points to the last node in the result list, so appending new nodes is
        easy. The dummy node gives tail something to point to initially when the result list is
        empty. This dummy node is efficient, since it is only temporary, and it is allocated in
        the stack. The loop proceeds, removing one node from either 'a' or 'b', and adding it to
        tail. When we are done, the result is in dummy.next.
        This solution uses the temporary dummy to build up the result list
        Time Complexity: O(m+n) where m and n are number of nodes in first and second linked
        lists respectively.
        """
        dummy = Node(None)

        # Once one or the other list runs out -- we're done
        while (a is not None and a.data is not None) and \
                (b is not None and b.data is not None):
            if a.data == b.data:
                ptr = Pointer(dummy.next_node)
                self.push(ptr, a.data)
                dummy = ptr.value
                a = a.next_node
                b = b.next_node
            elif a.data < b.data:  # Advance the smaller list
                a = a.next_node
            else:
                b = b.next_node  # Advanced the larger pointer

        return dummy.next_node
        
    # This solution uses the local reference
    def sorted_intersect_method2(self, a, b):
        """
        Method 2 (Using Local References)
        ---------------------------------
        This solution is structurally very similar to the above, but it avoids using a dummy node
        Instead, it maintains a struct node** pointer, last_ptr, that always points to the last
        pointer of the result list. This solves the same case that the dummy node did - dealing
        with the result list when it is empty. If you are trying to build up a list at its tail,
        either the dummy node or the struct node** "reference" strategy can be used

        Time Complexity: O(m+n) where m and n are number of nodes in first and second linked lists
        respectively.

        :param a:
        :param b:
        :return:
        """
        result = Node(None)
        last_ptr = Pointer(result)

        # Advance comparing the first nodes in both lists. When one or the other list runs
        # out, we're done.
        while (a is not None and a.data is not None) and \
                (b is not None and b.data is not None):
            if a.data == b.data:
                # found a node for the intersection
                self.push(last_ptr, a.data)
                last_ptr.value = last_ptr.value.next_node
                a = a.next_node
                b = b.next_node
            elif a.data < b.data:  # advance the smaller list
                a = a.next_node
            else:
                b = b.next_node
        return result.next_node

    def push(self, node_ref, new_data):
        """Function to insert a node at the beginning of the linked list"""
        new_node = Node(new_data)
        new_node.next_node = node_ref.value
        node_ref.value = new_node

    def print_list(self, node):
        """Function to print nodes in a given linked list"""
        while node is not None:
            print("%d " % node.data)
            node = node.next_node


if __name__ == '__main__':
    # Method-3
    # Create two linked lists
    # 1st 3->6->9->15->30,
    # 2nd 10->15->30
    # 15 is the intersection point
    print("------Method-3-------\n")
    head1 = Node(10)
    head1.next_node = Node(15)
    head1.next_node.next_node = Node(30)

    head2 = Node(3)
    head2.next_node = Node(6)
    head2.next_node.next_node = Node(9)
    head2.next_node.next_node.next_node = Node(15)
    head2.next_node.next_node.next_node.next_node = Node(30)

    utility = IntersectionNodeUtility(head1, head2)
    inter_node = utility.get_intesection_node()
    if inter_node:
        print("\n The node of intersection is %d \n" % inter_node)
    else:
        print("\n No intersection node found")

    # print("\n----- Method 1 & 2-------\n")
    # Method-1 and Method-2
    # TODO: Fix this method
    a = Pointer(Node(None, None))
    b = Pointer(Node(None, None))
    intersect = Node(None, None)
    utility2 = IntersectionNodeUtility2()

    # Let us create the first sorted linked list to test the functions Created linked list will
    # be 1->2->3->4->5->6

    utility2.push(a, 6)
    utility2.push(a, 5)
    utility2.push(a, 4)
    utility2.push(a, 3)
    utility2.push(a, 2)
    utility2.push(a, 1)

    # Let us create the second sorted linked list Created linked list will be 2->4->6->8
    utility2.push(b, 8)
    utility2.push(b, 6)
    utility2.push(b, 4)
    utility2.push(b, 2)

    # Find the intersection two linked lists

    intersect1 = utility2.sorted_intersect_method1(a.value, b.value)
    # print("\n Linked list containing common items of a & b \n ")
    # utility2.print_list(intersect1)

    intersect2 = utility2.sorted_intersect_method2(a.value, b.value)
    print("\n Linked list containing common items of a & b \n ")
    utility2.print_list(intersect2)
