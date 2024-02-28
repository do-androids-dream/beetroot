"""
Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.

Прочитати про Fibonacci search та імплементуйте його за допомогою Python. Визначте складність алгоритму та
порівняйте його з бінарним пошуком
"""
import sys
from typing import Sequence, Any, Hashable, Optional, NamedTuple


def bin_search_rec(seq: Sequence, item: Any) -> bool:
    """Expected seq to be sorted and same type elements"""

    middle = len(seq) // 2

    if seq[middle] == item:
        return True
    elif len(seq) == 1 and seq[0] != item:
        return False

    if item > seq[middle]:
        right = seq[middle:]
        return bin_search_rec(right, item)
    else:
        left = seq[:middle]
        return bin_search_rec(left, item)


if __name__ == '__main__':

    s = [1, 2, 3, 4, 5]
    print(bin_search_rec(s, 1))
    print(bin_search_rec(s, 5))
    print(bin_search_rec(s, 3))
    print(bin_search_rec(s, 10))

    s2 = ["apple", "book", "capital", "day", "eggplant"]
    print(bin_search_rec(s2, "apple"))
    print(bin_search_rec(s2, "eggplant"))
    print(bin_search_rec(s2, "egg"))

    """
    Реалізувати in (__contains__) та len (__len__) методи для HashTable
    """


class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:
    """
    Custom hashtable realization.
    Possible Error due to hash collisions
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pairs = [None] * capacity

    def __len__(self) -> int:
        return len(self.pairs)

    def __setitem__(self, key: Hashable, value: Any):
        self.pairs[self._index(key)] = Pair(key, value)

    def __getitem__(self, key: Hashable) -> Any:
        value = self.pairs[self._index(key)]
        if value is None:
            raise KeyError(key)
        return value.value

    def __contains__(self, key: Hashable) -> bool:
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def get(self, key: Hashable, default: Optional[Any] = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key: Hashable):
        if key in self:
            self.pairs[self._index(key)] = None
        else:
            raise KeyError()

    def _index(self, key: Hashable) -> int:
        return hash(key) % len(self)


if __name__ == '__main__':

    print(sys.hash_info.algorithm)

