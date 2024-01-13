import random


def retry(function):
    def inner(a, b):
        while True:
            try:
                print("let's try...")
                return function(a, b)
            except ZeroDivisionError:
                continue
    return inner


@retry
def broken_division_calculator(a, b):
    if random.random() < 0.85:
        b = 0

    return a / b


# broken_division_calculator = retry(broken_division_calculator)

result = broken_division_calculator(1, 2)
print(result)


# def broken_division_calculator(a, b):
#     if random.random() < 0.85:
#         b = 0
#
#     return a / b
#
#
# def inner(a, b):
#     while True:
#         try:
#             print("let's try...")
#             return broken_division_calculator(a, b)
#         except ZeroDivisionError:
#             continue
#
#
# print(inner(1, 2))
