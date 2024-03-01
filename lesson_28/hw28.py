"""
Task 1

A bubble sort can be modified to "bubble" in both directions. The first pass moves "up" the list and the second pass moves "down."
This alternating pattern continues until no more passes are necessary. Implement this variation and describe under what circumstances it might be appropriate.
"""
from typing import Sequence


def bubble_sort(seq: Sequence):
    for i in range(1, len(seq) // 2):
        ind = 0

        while ind < len(seq) - i:
            if seq[ind] > seq[ind + 1]:
                seq[ind], seq[ind + 1] = seq[ind + 1], seq[ind]
            ind += 1

        while ind > i - 1:
            if seq[ind] < seq[ind - 1]:
                seq[ind], seq[ind - 1] = seq[ind - 1], seq[ind]
            ind -= 1


lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(lst)
print(lst)

"""
Task 2

Implement the mergeSort function without using the slice operator.
"""


def custom_slice(seq: Sequence, start: int = 0, stop: int = None, step: int = 1):
    if stop is None:
        stop = len(seq)

    res = []
    while start < stop and start < len(seq):
        res.append(seq[start])
        start += step

    return res


def merge_sort(seq: Sequence):
    if len(seq) == 1:
        return seq
    left = custom_slice(seq, start=0, stop=len(seq) // 2)
    right = custom_slice(seq, start=len(seq) // 2)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left: Sequence, right: Sequence) -> list:
    res = []
    left = list(left)
    right = list(right)

    while len(left) != 0 and len(right) != 0:
        if left[0] > right[0]:
            res.append(right[0])
            right.remove(right[0])
        else:
            res.append(left[0])
            left.remove(left[0])

    if len(left) == 0:
        res += right
    else:
        res += left

    return res


lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(merge_sort(lst))

string = "fedcba"
print(merge_sort(string))
