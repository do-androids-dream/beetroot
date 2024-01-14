"""
Task 1

Write a Python program to detect the number of local variables declared in a function.
"""


def some_func(a=0, b=1):
    c = "string"
    return print(c, a + b)


def count_local(func):
    return len(func.__code__.co_varnames)


print(f"{some_func.__name__} local var number:", count_local(some_func))

"""
Task 2

Write a Python program to access a function inside a function (Tips: use function, which returns another function)
"""


def func_1():
    def func_2():
        print("you got func_2")
    return func_2


access_func_2 = func_1()
print(access_func_2.__name__)
access_func_2()

"""

Task 3

Write a function called "choose_func" which takes a list of nums and 2 callback functions. If all nums inside the list are positive, execute the first function on that list and return the result of it. Otherwise, return the result of the second one

"""


def choose_func(nums: list, func1, func2):
    for i in nums:
        if i < 0:
            return func2(nums)
    return func1(nums)


# Assertions

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):

    return [num ** 2 for num in nums]


def remove_negatives(nums):

    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
