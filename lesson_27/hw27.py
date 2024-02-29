"""Розширити структуру, яку побудували на уроці, можливістю вставки дерева в наявне дерево та видалення піддерева з дерева, що існує."""

from typing import (
    Optional,
    Any,
)


class Category:
    def __init__(self, name: str, parent: Optional["Category"] = None):
        self.name = name
        self._children = []
        self._parent = parent
        if self.parent is not None:
            self._parent._children.append(self)

    def __str__(self):
        return self.name

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent: "Category"):
        self._parent = parent
        parent._children.append(self)

    @property
    def children(self):
        return self._children

    def add_tree(self, other: "Category"):
        other._parent = self
        self._children.append(other)

    def del_subtree(self, sub: "Category"):
        self._children.remove(sub)
        sub._parent = None


def print_tree(category: Category, ident: int = 0):
    print('--' * ident, category, sep="")
    for child in category.children:
        # print(f"  {child}")
        print_tree(child, ident + 1)


def find(category: Category, name: str) -> Optional[Category]:
    print(f"... {category}")
    if category.name == name:
        return category

    for child in category.children:
        value = find(child, name)
        if value is not None:
            return value

    return None


if __name__ == '__main__':
    strings = Category("strings", parent=None)
    beats = Category("beats", parent=None)
    guitars = Category("guitars", parent=strings)
    violins = Category("violins", parent=strings)
    drums = Category("drums", parent=beats)
    acoustics = Category("acoustics", parent=guitars)
    electrics = Category("electrics", parent=guitars)
    alt = Category("alt", parent=violins)
    fenders = Category("fenders", parent=electrics)
    gibsons = Category("gibsons", parent=electrics)

    # print(electrics)
    # print(electrics.parent)
    # print(electrics.parent.parent)
    # print(electrics.parent.parent.parent)
    #
    # print()
    # print_tree(strings, 1)

    # print_tree(strings, 1)
    #
    # print("===")
    # cat = find(strings, "123456")
    # print(cat)
    music_instruments = Category("music instruments", parent=None)
    strings.parent = music_instruments
    print_tree(music_instruments)

    # create separate tree
    synthesizer = Category("synthesizer", parent=beats)
    sampler = Category("sampler", parent=beats)
    tom_tom = Category("tom-tom", parent=drums)
    hi_hat = Category("hi-hat", parent=drums)
    print_tree(beats)

    # insert tree into another tree
    music_instruments.add_tree(beats)
    print_tree(music_instruments)

    # delete subtree
    beats.del_subtree(drums)
    print_tree(music_instruments)



