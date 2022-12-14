"""
Design a deck of cards
Design the data structures for a generic deck of cards. Explain how you would subclass the data
structures to implement blackjack

Constraints and assumptions
1. Is this a generic deck of cards for games like poker and black jack?
-> Yes, design a generic deck then extend it to black jack

2. Can we assume the deck has 52 cards (2-10, Jack, Queen, King, Ace) and 4 suits?
-> Yes

3. Can we assume inputs are valid or do we have to validate them?
-> Assume they're valid

Solution:
First, we need to recognize that a "generic" deck of cards can mean many things. Generic could
mean a standard deck of cards that can play a poker-like game, or it could even stretch to Uno or
Baseball cards. It is important to ask your interviewer what she means by generic.

"""
from __future__ import print_function
from abc import ABCMeta, abstractmethod
from enum import Enum
import sys


class Suit(Enum):

    HEART = 0
    DIAMOND = 1
    CLUBS = 2
    SPADE = 3


class Card(object):
    __metaclass__ = ABCMeta

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.is_available = True

    @property
    @abstractmethod
    def value(self):
        pass

    @value.setter
    @abstractmethod
    def value(self, other):
        pass


class BlackJackCard(Card):

    def __init__(self, value, suit):
        super(BlackJackCard, self).__init__(value, suit)

    def is_ace(self):
        return True if self._value == 1 else False

    def is_face_card(self):
        """Jack = 11, Queen = 12, King = 13"""
        return True if 10 < self._value <= 13 else False

    @property
    def value(self):
        if self.is_ace() == 1:
            return 1
        elif self.is_face_card():
            return 10
        else:
            return self._value

    @value.setter
    def value(self, new_value):
        if 1 <= new_value <= 13:
            self._value = new_value
        else:
            raise ValueError('Invalid card value: {}'.format(new_value))


class Hand(object):

    def __init__(self, cards):
        self.cards = cards

    def add_card(self, card):
        self.cards.append(card)

    def score(self):
        total_value = 0
        for card in card:
            total_value += card.value
        return total_value


class BlackJackHand(Hand):
    """
    Now, let's say we're building a blackjack game, so we need to know the value of the
    cards. Face cards are 10 and an ace is 11 (most of the time, but that's the job of the Hand
    class, not the following class).

    This is just one way of handling aces. We could, alternatively, create a class of type Ace
    that extends BlackJackCard.
    """
    BLACKJACK = 21

    def __init__(self, cards):
        super(BlackJackHand, self).__init__(cards)

    def score(self):
        min_over = sys.maxsize
        max_under = -sys.maxsize
        for score in self.possible_scores():
            if self.BLACKJACK < score < min_over:
                min_over = score
            elif max_under < score <= self.BLACKJACK:
                max_under = score
        return max_under if max_under != -sys.MAXSIZE else min_over

    def possible_scores(self):
        """Return a list of possible scores, taking Aces into account."""
        pass


class Deck(object):

    def __init__(self, cards):
        self.cards = cards
        self.deal_index = 0

    def remaining_cards(self):
        return len(self.cards) - self.deal_index

    def deal_card(self):
        try:
            card = self.cards[self.deal_index]
            card.is_available = False
            self.deal_index += 1
        except IndexError:
            return None
        return card

    def shuffle(self):  # ...
        pass
