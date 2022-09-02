class Link(object):
    def __init__(self, id, data, next_node=None, prev_node=None):
        self.id = id
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class SortedList(object):
    """Implementation of sorted list where element are arrange in sorted order"""

    def __init__(self):
        self.first = None

    def __del__(self):
        current = self.first
        while current is not None:
            temp = current
            current = current.next_node
            del temp

    def is_empty(self):
        return self.first is None

    def insert(self, id, data):
        new_link = Link(id, data)
        previous = None
        current = self.first

        while current is not None and id > current.id:
            previous = current
            current = current.next_node

        # Check if the inserted element is the first element
        if previous is None:
            self.first = new_link
        else:
            previous.pNext = new_link

        new_link.pNext = current

    def remove(self, id):
        current = self.first
        previous = None

        while current is not None and current.get_id() != id:
            previous = current
            current = current.next_node

        pTemp = current
        # If id found and it is the first element
        if previous is None and current.get_id() == id:
            self.first = current.next_node
        else:
            previous.pNext = current.next_node

        del pTemp
        return True

    def remove_first(self):
        pTemp = self.first
        self.first = pTemp.next_node
        del pTemp

    def display_list(self):
        current = self.first
        while current is not None:
            print(current)
            current = current.next_node


if __name__ == '__main__':
    pass
