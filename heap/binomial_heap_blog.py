# http://www.growingwiththeweb.com/data-structures/binomial-heap/overview/


class Node(object):
    def __init__(self, key, degree=0, parent=None, child=None, sibling=None):
        self.key = key
        self.degree = degree
        self.parent = parent
        self.child = child
        self.sibling = sibling

    def compare_to(self, other):
        return self.key.compare_to(other.key)


# ======= IMPLEMENTATAION 1 ========== #
class BinomialHeap1(object):
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None

    def insert(self, key):
        node = Node(key)
        tempHeap = BinomialHeap1(node)
        self.head = self.union(tempHeap)

    def find_minimum(self):
        if self.head is None:
            return None
        else:
            minimum = self.head
            nextt = minimum.sibling

            while nextt is not None:
                if nextt.compare_to(minimum) < 0:
                    minimum = nextt
                nextt = nextt.sibling

            return minimum.key

    def search(self, key):
        """Implemented to test delete/decrease key, runs in O(n) time"""
        nodes = [self.head]
        while len(nodes) != 0:
            curr = nodes[0]
            nodes.pop(0)

            if curr.key == key:
                return curr

            if curr.sibling is not None:
                nodes.append(curr.sibling)

            if curr.child is not None:
                nodes.append(curr.child)

        return None

    def decrease_key(self, node, newKey):
        node.key = newKey
        self.bubble_up(node, False)

    def delete(self, node):
        node = self.bubble_up(node, True)
        if self.head == node:
            self.remove_tree_root(node, None)
        else:
            prev = self.head
            while prev.sibling.compare_to(node) != 0:
                prev = prev.sibling
            self.remove_tree_root(node, prev)

    def bubble_up(self, node, toRoot):
        parent = node.parent
        while parent is not None and (toRoot or node.compareTo(parent) < 0):
            temp = node.key
            node.key = parent.key
            parent.key = temp
            node = parent
            parent = parent.parent

        return node

    def extract_min(self):
        if self.head is None:
            return None

        minimum = self.head
        minPrev = None
        next = minimum.sibling
        nextPrev = minimum

        while next is not None:
            if next.compare_to(minimum) < 0:
                minimum = next
                minPrev = nextPrev
            nextPrev = next
            next = next.sibling

        self.remove_tree_root(minimum, minPrev)
        return minimum.key

    def remove_tree_root(self, root, prev):
        # Remove root from the heap
        if root == self.head:
            self.head = root.sibling
        else:
            prev.sibling = root.sibling

        # Reverse the order of root's children and make a new heap
        new_head = None
        child = root.child
        while child is not None:
            nextt = child.sibling
            child.sibling = new_head
            child.parent = None
            new_head = child
            child = nextt

        newHeap = BinomialHeap(new_head)

        # Union the heaps and set its head as this.head
        self.head = self.union(newHeap)

    def link_tree(self, min_node_tree, other):
        """Merge two binomial trees of the same order"""
        other.parent = min_node_tree
        other.sibling = min_node_tree.child
        min_node_tree.child = other
        min_node_tree.degree += 1

    def union(self, heap):
        """Union two binomial heaps into one and return the head"""
        new_head = self.merge(self, heap)

        self.head = None
        heap.head = None

        if new_head is None:
            return None

        prev = None
        curr = new_head
        nextt = new_head.sibling

        while nextt is not None:
            if curr.degree != nextt.degree or \
                    (nextt.sibling is not None and nextt.sibling.degree == curr.degree):
                prev = curr
                curr = nextt
            else:
                if curr.compareTo(nextt) < 0:
                    curr.sibling = nextt.sibling
                    self.link_tree(curr, nextt)
                else:
                    if prev is None:
                        new_head = nextt
                    else:
                        prev.sibling = nextt

                    self.link_tree(nextt, curr)
                    curr = nextt

            nextt = curr.sibling

        return new_head

    def merge(self, heap1, heap2):
        if heap1.head is None:
            return heap2.head

        elif heap2.head is None:
            return heap1.head

        else:
            head = None
            heap1_next = heap1.head
            heap2_next = heap2.head

            if heap1.head.degree <= heap2.head.degree:
                head = heap1.head
                heap1_next = heap1_next.sibling
            else:
                head = heap2.head
                heap2_next = heap2_next.sibling

            tail = head

            while heap1_next is not None and heap2_next is not None:
                if heap1_next.degree <= heap2_next.degree:
                    tail.sibling = heap1_next
                    heap1_next = heap1_next.sibling
                else:
                    tail.sibling = heap2_next
                    heap2_next = heap2_next.sibling

                tail = tail.sibling

            if heap1_next is not None:
                tail.sibling = heap1_next
            else:
                tail.sibling = heap2_next

            return head

    def printer(self):
        print("Binomial heap:", end=" ")
        if self.head is not None:
            self.print_node(self.head, 0)

    def print_node(self, curr, level):
        while curr is not None:
            sb = ""
            for i in range(level):
                sb += " "
            sb += str(curr.key)
            print(sb)
            if curr.child is not None:
                curr.child.print(level + 1)
            curr = curr.sibling
