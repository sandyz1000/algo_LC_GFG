"""
Design the data structures for an online book reader system.

Since the problem doesn't describe much about the functionality, let's assume we want to design a
basic online reading system which provides the following functionality:
1. User membership creation and extension.
2. Searching the database of books.
3. Reading a book.
4. Only one active user at a time
5. Only one active book by this user.
To implement these operations we may require many other functions, like get, set, update, and
so on. The objects required would likely include User, Book, and Library.

The class OnlineReaderSystem represents the body of our program. We would implement the class
such that it stores information about all the books, deals with user management, and refreshes
the display, but that would make this class rather hefty. Instead, we've chosen to tear off these
components into Library, UserManager, and Display classes.

The decision to tear off user management, library, and display into their own classes, when this
functionality could have been in the general OnlineReaderSystem class, is an interesting one. On
a very small system, making this decision could make the system overly complex. However,
as the system grows, and more and more functionality gets added to OnlineReaderSystem, breaking
off such components prevents this main class from getting overwhelmingly lengthy

"""
from __future__ import print_function


class OnlineReaderSystem:
    activeBook = None
    activeUser = None

    def __init__(self):
        self.serManager = UserManager()
        self.library = Library()
        self.display = Display()

    def set_active_book(self, book):
        self.activeBook = book
        self.display.display_book(book)

    def set_active_user(self, user):
        self.activeUser = user
        self.display.display_user(user)


class Library:
    """
    We then implement separate classes to handle the user manager, the library, and
    the display components."""
    def __init__(self):
        self.books = {}

    def add_book(self, id, details):
        if id in self.books:
            return None

        book = Book(id, details)
        self.books[id] = book
        return book

    def remove(self, b):
        return self._remove(b.book_id)

    def _remove(self, id):
        if id not in self.books:
            return False

        self.books.pop(id)
        return True

    def find(self, id):
        return self.books[id]


class UserManager:
    def __init__(self):
        self.users = {}

    def addUser(self, id, details, accountType):
        if id in self.users:
            return None

        user = User(id, details, accountType)
        self.users[id] = user
        return user

    def remove(self, u):
        return self._remove(u.user_id)

    def _remove(self, id):
        if id not in self.users:
            return False

        self.users.pop(id)
        return True

    def find(self, id):
        return self.users[id]


class Display:
    def __init__(self):
        self.active_book = None
        self.active_user = None
        self.page_number = 0

    def display_user(self, user):
        self.active_user = user
        self.refreshUsername()

    def display_book(self, book):
        self.page_number = 0
        self.active_book = book
        self.refreshTitle()
        self.refreshDetails()
        self.refreshPage()

    def turn_page_forward(self):
        self.page_number += 1
        self.refreshPage()

    def turn_page_backward(self):
        self.page_number -= 1
        self.refreshPage()

    def refreshUsername(self):
        """updates username display """

    def refreshTitle(self):
        """updates title display"""

    def refreshDetails(self):
        """updates details display"""

    def refreshPage(self):
        """updated page display """


class Book:
    """The classes for User and Book simply hold data and provide little true functionality."""

    def __init__(self, id, det):
        self.book_id = id
        self.details = det


class User:
    def __init__(self, id, details, account_type):
        self.user_id = id
        self.details = details
        self.accountType = account_type

    def renew_membership(self):
        pass

    # Getters and setters */
    def get_details(self):
        return self.details

    def set_details(self, details):
        self.details = details


if __name__ == '__main__':
    pass
