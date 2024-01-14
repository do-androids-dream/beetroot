"""
Task 1

Write a decorator that prints a function with arguments passed to it.

NOTE! It should print the function, not the result of its execution!

For example:

 "add called with 4, 5"
"""
from types import FunctionType


def logger(func: FunctionType):
    def wrapper(*args, **kwargs):
        if not kwargs and args:
            msg = f"{func.__name__} called with {str(args)[1:-1]}"
        elif not args and kwargs:
            msg = f"{func.__name__} called with {str(kwargs.items())[1:-1]}"
        else:
            msg = f"{func.__name__} called with {str(args)[1:-1]} and {str(kwargs.items())[1:-1]}"
        print(msg)
        func(*args, **kwargs)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(2, 3)
square_all(1, 2, 3, 4, 5, 6)

"""
Task 2

Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

"""


def stop_words(words: list):
    def wrapper(func: FunctionType):
        def inner(*args):
            res: str = func(*args)
            for word in words:
                res = res.replace(word, "*")
            print(res)
            return res
        return inner
    return wrapper


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"


"""
Task 3

Write a decorator "arg_rules" that validates arguments passed to the function.

A decorator should take 3 arguments:

max_length: 15

type_: str

contains: [] - list of symbols that an argument should contain

If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.

"""


def arg_rules(type_: type, max_length: int, contains: list):
    def wrapper(func: FunctionType):
        def inner(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    print("wrong type")
                    return False
                if len(arg) > max_length:
                    print("wrong length")
                    return False
                for content in contains:
                    if content not in arg:
                        print("wrong content")
                        return False
            return func(*args)

        return inner
    return wrapper


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('05years') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
