"""
Design a musical jukebox using object-oriented principles

In any object-oriented design question, you first want to start off with asking your interviewer
some questions to clarify design constraints. Is this jukebox playing CD? Records? MP3s? Is it a
simulation on a computer, or is it supposed to represent a physical jukebox? Does it take money,
or is it free? And if it takes money, which currency? And does it deliver change?

Unfortunately, we don't have an interviewer here that we can have this dialogue with.
Instead, we'll make some assumptions. We'll assume that the jukebox is a computer simulation that
closely mirrors physical jukeboxes, and we'll assume that it's free.

Now that we have that out of the way, we'll outline the basic system components.
-> Jukebox
-> CD
-> Song
-> Artist
-> Playlist
-> Display (displays details on the screen)

Now, let’s break this down further and think about the possible actions.
-> Playlist creation (includes add, delete, and shuffle)
-> CD selector
-> Song selector
-> Queuing up a song
-> Get next song from playlist

A user also can be introduced:
-> Adding
-> Deleting
-> Credit information

Each of the main system components translates roughly to an object, and each action translates to
a method. Let's walk through one potential design.

The Jukebox class represents the body of the problem. Many of the interactions between the
components of the system, or between the system and the user, are channeled through here.

"""
from queue import Queue


class Jukebox:
    def __init__(self, cd_player, user, cd_collection, ts):
        self.cd_player = cd_player
        self.user = user
        self.cd_collection = cd_collection
        self.ts = ts

    def getCurrentSong(self):
        return self.ts.getCurrentSong()

    def setUser(self, u):
        self.user = u


class CDPlayer:
    """
    Like a real CD player, the CDPlayer class supports storing just one CD at a time.
    The CDs that are not in play are stored in the jukebox.
    """
    def __init__(self, c=None, p=None):
        self.c = c
        self.p = p

    def play_song(self, s):
        pass


class Playlist:
    """
    The Playlist manages the current and next songs to play. It is essentially a wrapper class for
    a queue and offers some additional methods for convenience.
    """
    def __init__(self, song, queue):
        self.song = song
        self.queue = queue

    def get_next_to_play(self):
        return self.queue[0]

    def queue_up_song(self, s):
        self.queue.put(s)


# The classes for CD, Song, and User are all fairly straightforward. They consist mainly of
# member variables and getters and setters.

class CD:
    """data for id, artist, songs, etc"""
    pass


class Song:
    """data for id, CD (could be null), title, length, etc"""
    pass

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @staticmethod
    def addUser(name, id):
        pass


if __name__ == '__main__':
    pass
