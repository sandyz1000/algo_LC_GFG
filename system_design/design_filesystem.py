"""
Design data structures and algorithms for in-memory file system

Design data structures and algorithms for in-memory file system

Explain the data structures and algorithms that you would use to design an in-memory file system.
Illustrate with an example in the code logic where possible.

Alternatively, we could have implemented Directory such that it contains separate lists for files
and subdirectories. This makes the nurnberOfFiles () method a bit cleaner, since it doesn't need
to use the instanceof operator, but it does prohibit us from cleanly sorting files and
directories by dates or names.

For data block allocation, we can use bitmask vector and linear search (see "Practical File
System Design") or B+ trees (see Reference or Wikipedia).


"""
from __future__ import print_function
from abc import ABCMeta, abstractmethod
import time


class Entry:
    """Entry is superclass for both File and Directory"""

    __metaclass__ = ABCMeta

    parent = None
    created = 0
    last_updated = 0
    last_accessed = 0
    name = 0

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.created = int(round(time.time() * 1000))
        self.last_updated = int(round(time.time() * 1000))
        self.last_accessed = int(round(time.time() * 1000))

    def delete(self):
        if self.parent is None:
            return False
        return self.parent.delete_entry(self)

    @abstractmethod
    def size(self):
        pass

    def getcreation_time(self):
        """Getters and setters."""
        return self.created

    def get_last_updated_time(self):
        return self.last_updated

    def get_last_accessed_time(self):
        return self.last_accessed

    def change_name(self, n):
        self.name = n

    def get_name(self):
        return self.name


class File(Entry):
    """
    Version -1

    A file system, in its most simplistic version, consists of Files and Directories. Each
    Directory contains a set of Files and Directories. Since Files and Directories share so many
    characteristics, we've implemented them such that they inherit from the same class, Entry.

    A class to represent a File (Inherits from Entry)
    """

    def __init__(self, name, parent, sz):
        super(File, self).__init__(name, parent)
        self.size = sz
        self.content = None

    def size(self):
        return self.size

    def get_contents(self, content):
        return self.content

    def set_contents(self, c):
        self.content = c


class Directory(Entry):
    """A class to represent a Directory (Inherits from Entry)"""

    def __init__(self, name, parent):
        super(Directory, self).__init__(name, parent)
        self.contents = []

    def size(self):
        size = 0
        for en in self.contents:
            size += len(en)
        return size

    def number_of_files(self):
        count = 0
        for en in self.contents:
            if isinstance(en, Directory):
                count += 1 + en.number_of_files()  # Directory counts as a file
            elif isinstance(en, File):
                count += 1
        return count

    def delete_entry(self, entry):
        return self.contents.remove(entry)

    def add_entry(self, entry):
        self.contents.append(entry)

    def get_contents(self):
        return self.contents


if __name__ == '__main__':
    pass
