from typing import Sequence, Any

"""
Task 1

Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack.
"""
class Stack:
    def __init__(self):
        self._storage = []

    def read_sequence(self, seq: Sequence):
        if seq:
            for char in seq:
                self._storage.append(char)

    def print_char(self):
        if self._storage:
            print(self._storage.pop())

    def __len__(self):
        return len(self._storage)


my_seq = Stack()

my_seq.read_sequence("abcdefghijklmnopqrstuvwxyz")
for i in range(len(my_seq)):
    my_seq.print_char()


"""
Task 2

Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces, 
and curly brackets are "balanced."
"""

class Balance:
    storage = []
    LEFT = "([{"
    RIGHT = ")]}"
    MAP = {")": "(", "}": "{", "]": "["}

    @classmethod
    def check_balance(cls, seq: Sequence) -> bool:
        if seq:
            for bracket in seq:
                if bracket in cls.LEFT:
                    cls.storage.append(bracket)

                if bracket in cls.RIGHT:
                    try:
                        if cls.MAP[bracket] == cls.storage[-1]:
                            cls.storage.pop()
                            continue
                    except IndexError:
                        return False

            if cls.storage:
                cls.storage.clear()
                return False
            return True


cor_seq = "(2+2) * 2 {{[]}}"
wrong_seq = ")()[]("
wrong_seq2 = "2 * ((2 + 2)]"

print(Balance.check_balance(cor_seq))
print(Balance.check_balance(wrong_seq))
print(Balance.check_balance(wrong_seq2))

"""
Task 3

Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack. 
Any other element must remain on the stack respecting their order. 
Consider the case in which the element is not found - raise ValueError with proper info Message
"""

class Stack:
    def __init__(self):
        self._storage = []

    def read_sequence(self, seq: Sequence):
        if seq:
            for char in seq:
                self._storage.append(char)

    def print_char(self):
        if self._storage:
            print(self._storage.pop())

    def __len__(self):
        return len(self._storage)

    def get_from_stack(self, element: Any):
        try:
            return self._storage[self._storage.index(element)]
        except ValueError:
            raise ValueError("Element not found")


my_seq = Stack()

my_seq.read_sequence("abcdefghijklmnopqrstuvwxyz")
my_seq.get_from_stack("s")
my_seq.get_from_stack("2")
