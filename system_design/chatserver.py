# coding=utf-8
"""
Explain how you would design a chat server. In particular, provide details about the various
backend components, classes, and methods. What would be the hardest problems to solve?

Designing a chat server is a huge project, and it is certainly far beyond the scope of what could
be completed in an interview. After all, teams of many people spend months or years creating a
chat server. Part of your job, as a candidate, is to focus on an aspect of the problem that is
reasonably broad, but focused enough that you could accomplish it during an interview. It need
not match real life exactly, but it should be a fair representation of an actual implementation.

For our purposes, we'll focus on the core user management and conversation aspects: adding a
user, creating a conversation, updating one's status, and so on. In the interest of time and
space, we will not go into the networking aspects of the problem, or how the data actually gets
pushed out to the clients.

We will assume that "friending" is mutual; I am only your contact if you are mine. Our chat
system will support both group chat and one-on-one (private) chats. We will not worry about voice
chat, video chat, or file transfer.

==What specific actions does it need to support?
This is also something to discuss with your interviewer, but here are some ideas:
1. Signing online and offline.
2. Add requests (sending, accepting, and rejecting).
3. Updating a status message.
4. Creating private and group chats.
5. Adding new messages to private and group chats.

This is just a partial list. If you have more time, you can add more actions.

==What can we learn about these requirements?
We must have a concept of users, add request status, online status, and messages.

==What are the core components of the system?
The system would likely consist of a database, a set of clients, and a set of servers. We won't
include these parts in our object-oriented design, but we can discuss the overall view of the
system.

The database will be used for more permanent storage, such as the user list or chat archives. A
SQL database is a good bet, or, if we need more scalability, we could potentially use BigTable or
a similar system.

For communication between the client and servers, using XML will work well. Although it’s not the
most compressed format (and you should point this out to your interviewer), it’s nice because
it's easy for both computers and humans to read. Using XML will make your debugging efforts
easier—and that matters a lot.

The server will consist of a set of machines. Data will be divided up across machines, requiring
us to potentially hop from machine to machine. When possible, we will try to replicate some data
across machines to minimize the lookups. One major design constraint here is to prevent having a
single point of failure. For instance, if one machine controlled all the user sign-ins, then we'd
cut off millions of users potentially if a single machine lost network connectivity.

==What are the key objects and methods?

The key objects of the system will be a concept of users, conversations, and status messages.
We've implemented a User-Management class. If we were looking more at the networking aspects of
the problem, or a different component, we might have instead dived into those objects.

"""

from abc import ABCMeta


class Enum:
    pass


class UserService(object):
    def __init__(self):
        self.users_by_id = {}  # key: user id, value: User

    def add_user(self, user_id, name, pass_hash):  # ...
        pass

    def remove_user(self, user_id):  # ...
        pass

    def add_friend_request(self, from_user_id, to_user_id):  # ...
        pass

    def approve_friend_request(self, from_user_id, to_user_id):  # ...
        pass

    def reject_friend_request(self, from_user_id, to_user_id):  # ...
        pass


class User(object):
    def __init__(self, user_id, name, pass_hash):
        self.user_id = user_id
        self.name = name
        self.pass_hash = pass_hash
        self.friends_by_id = {}  # key: friend id, value: User
        self.friend_ids_to_private_chats = {}  # key: friend id, value: private chats
        self.group_chats_by_id = {}  # key: chat id, value: GroupChat
        self.received_friend_requests_by_friend_id = {}  # key: friend id, value: AddRequest
        self.sent_friend_requests_by_friend_id = {}  # key: friend id, value: AddRequest

    def message_user(self, friend_id, message):  # ...
        pass

    def message_group(self, group_id, message):  # ...
        pass

    def send_friend_request(self, friend_id):  # ...
        pass

    def receive_friend_request(self, friend_id):  # ...
        pass

    def approve_friend_request(self, friend_id):  # ...
        pass

    def reject_friend_request(self, friend_id):  # ...
        pass


class Chat(object):
    __metaclass__ = ABCMeta

    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.users = []
        self.messages = []


class PrivateChat(Chat):
    def __init__(self, first_user, second_user):
        super(PrivateChat, self).__init__(0)
        self.users.append(first_user)
        self.users.append(second_user)


class GroupChat(Chat):
    def add_user(self, user):  # ...
        pass

    def remove_user(self, user):  # ...
        pass


class Message(object):
    def __init__(self, message_id, message, timestamp):
        self.message_id = message_id
        self.message = message
        self.timestamp = timestamp


class AddRequest(object):
    def __init__(self, from_user_id, to_user_id, request_status, timestamp):
        self.from_user_id = from_user_id
        self.to_user_id = to_user_id
        self.request_status = request_status
        self.timestamp = timestamp


class RequestStatus(Enum):
    UNREAD = 0
    READ = 1
    ACCEPTED = 2
    REJECTED = 3
