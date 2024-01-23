"""
Task 1

Create your own implementation of a built-in function enumerate, named 'with_index', which takes two parameters:
'iterable' and 'start', default is 0. Tips: see the documentation for the enumerate function
"""
from typing import Iterable, Tuple, Generator


def with_index(iterable: Iterable, start: int = 0) -> Generator:
    iterator = iter(iterable)
    while True:
        try:
            yield start, next(iterator)
            start += 1
        except StopIteration:
            break


"""
Task 2

Create your own implementation of a built-in function range, named in_range(), which takes three parameters: 
'start', 'end', and optional step. Tips: See the documentation for 'range' function
"""


def in_range(start: int, end: int = None, step=1) -> Generator:
    if end is None:
        start, end = 0, start
    if step == 0:
        raise ValueError("step parameter can't be 0")
    if step > 0:
        while start < end:
            yield start
            start += step
    else:
        while start > end:
            yield start
            start += step


"""
Task 3

Create your own implementation of an iterable, which could be used inside for-in loop. 
Also, add logic for retrieving elements using square brackets syntax.
"""


class Sentence:
    def __init__(self, string: str):
        self.string = string.split()
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.string):
            element = self.string[self.index]
            self.index += 1
            return element
        else:
            raise StopIteration


sentence = Sentence("What we gonna do next?")

