from typing import List, Tuple

# We assume that all lists passed to functions are the same length N

# Match
# big
# O
# complexities
# with the code snippets below

# answers
# 1 - log n
# 2 - n^2
# 3 - n
# 4 - n^2
# 5 - 1
# 6 - n


def question1(first_list: List[int], second_list: List[int]) -> List[int]: # O(n)
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


def question2(n: int) -> int: # O(1)
    for _ in range(10):
        n **= 3
    return n


def question3(first_list: List[int], second_list: List[int]) -> List[int]: # O(n^2)
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


def question4(input_list: List[int]) -> int: # O(n)
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


def question5(n: int) -> List[Tuple[int, int]]: # O(n^2)
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


def question6(n: int) -> int: # O(log n)
    while n > 1:
        n /= 2
    return n
