# coding=utf-8
"""
The Turing machine (TM) serves two needs in theoretical computer science:

Formal Definition of a Turing machine

A deterministic Turing machine can be defined as a 7-tuple

M = (Q, Σ, Γ, δ, b, q0, qf)
with
    Q is a finite, non-empty set of states
    Γ is a finite, non-empty set of the tape alphabet
    Σ is the set of input symbols with Σ ⊂ Γ
    δ is a partially defined function, the transition function:
    δ : (Q \ {qf}) x Γ → Q x Γ x {L,N,R}
    b ∈ &Gamma \ Σ is the blank symbol
    q0 ∈ Q is the initial state
    qf ∈ Q is the set of accepting or final states

------------------------------------------
Implementation:
------------------------------------------

We implement a Turing Machine in Python as a class. We define another class for the read/write
tape of the Turing Machine. The core of the tape inside the class Tape is a dictionary,
which contains the entries of the tape. This way, we can have negative indices. A Python list is
not a convenient data structure, because Python lists are bounded on one side, i.e. bounded by 0.

We define the method __str__(self) for the class Tape. __str__(self) is called by the built-in
str() function. The print function uses also the str function to calculate the "informal" string
representation of an object, in our case the tape of the TM. The method get_tape() of our class
TuringMachine makes use of the str representation returned by __str__.

With the aid of the method __getitem__(), we provide a reading access to the tape via indices.
The definition of the method __setitem__() allows a writing access as well, as we can see e.g. in
the statement
self.__tape[self.__head_position] = y[1]
of our class TuringMachine implementation.

The class TuringMachine:
We define the method __str__(self), which is called by the str() built-in function and by the print
statement to compute the "informal" string representation of an object, in our case the string
representation of a tape.

1. The class of languages defined by a TM, i.e. structured or recursively enumerable languages
2. The class of functions a TM is capable to compute, i.e. the partial recursive functions
"""

from __future__ import print_function


class Tape(object):
    blank_symbol = " "

    def __init__(self,
                 tape_string=""):
        self.tape = dict((enumerate(tape_string)))

    def __str__(self):
        s = ""
        min_used_index = min(self.tape.keys())
        max_used_index = max(self.tape.keys())
        for i in range(min_used_index, max_used_index):
            s += self.tape[i]
        return s

    def __getitem__(self, index):
        if index in self.tape:
            return self.tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.tape[pos] = char


class TuringMachine(object):
    def __init__(self, tape="", blank_symbol=" ", initial_state="", final_states=None,
                 transition_function=None):
        self.tape = Tape(tape)
        self.head_position = 0
        self.blank_symbol = blank_symbol
        self.current_state = initial_state
        if transition_function is None:
            self.transition_function = {}
        else:
            self.transition_function = transition_function

        if final_states is None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)

    def get_tape(self):
        return str(self.tape)

    def step(self):
        char_under_head = self.tape[self.head_position]
        x = (self.current_state, char_under_head)
        if x in self.transition_function:
            y = self.transition_function[x]
            self.tape[self.head_position] = y[1]
            if y[2] == "R":
                self.head_position += 1
            elif y[2] == "L":
                self.head_position -= 1
            self.current_state = y[0]

    def final(self):
        if self.current_state in self.__final_states:
            return True
        else:
            return False


if __name__ == '__main__':
    initial_state = "init",
    accepting_states = ["final"],
    transition_function = {
        ("init", "0"): ("init", "1", "R"),
        ("init", "1"): ("init", "0", "R"),
        ("init", " "): ("final", " ", "N")}
    final_states = {"final"}

    t = TuringMachine("010011 ",
                      initial_state="init",
                      final_states=final_states,
                      transition_function=transition_function)

    print("Input on Tape:\n" + t.get_tape())

    while not t.final():
        t.step()

    print("Result of the Turing machine calculation:")
    print(t.get_tape())
