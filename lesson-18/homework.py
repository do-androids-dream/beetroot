"""
Task 1

Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email, passed to the constructor.
The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.

Email validations:

Valid email address format

Email address
"""

import re


class Email:
    pattern = (r'^(\"[^@]{1,62}\"@[a-zA-Z\d]+\.[a-zA-Z]{2,}$)'
               r'|'
               r"^[!#$%&'*+/=?^_`{|}~a-zA-Z\d]+([\.-]\w+)*(?<![\.-])@[a-zA-Z\d]+\.[a-zA-Z]{2,}$")

    def __init__(self, email):
        self.email = email

    @classmethod
    def validate(cls, email):
        """validates email on:
        Local part
        - uppercase and lowercase Latin letters A to Z and a to z
        - digits 0 to 9
        - printable characters !#$%&'*+-/=?^_`{|}~
        - dot ., provided that it is not the first or last character and
            provided also that it does not appear consecutively (e.g., John..Doe@example.com is not allowed)
        - If quoted, it may contain Space, Horizontal Tab (HT), any ASCII graphic except Backslash and Quote and
            a quoted-pair consisting of a Backslash followed by HT, Space or any ASCII graphic;
            it may also be split between lines anywhere that HT or Space appears. In contrast to unquoted local-parts,
            the addresses ".John.Doe"@example.com, "John.Doe."@example.com and "John..Doe"@example.com are allowed.
        - The maximum total length of the local-part of an email address is 64 octets
        Domain
        - Uppercase and lowercase Latin letters A to Z and a to z;
        - Digits 0 to 9, provided that top-level domain names are not all-numeric.
            """

        pattern_match = re.fullmatch(cls.pattern, email) is not None
        length_match = len(email.split("@")[0]) <= 64

        return pattern_match and length_match

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if self.validate(value):
            self._email = value
        else:
            raise ValueError(f'{self} -> {value} - Provided email is not valid')


if __name__ == "__main__":
    print('\n---Task 1---\n')
    e = Email("JohnDoe@gmail.com")
    print(e.email)

"""
Task 2

Implement 2 classes, the first one is the Boss and the second one is the Worker.

Worker has a property 'boss', and its value must be an instance of Boss.

You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own workers. 
You should implement a method that allows you to add workers to a Boss. 
You're not allowed to add instances of Boss class to workers list directly via access to attribute, use getters and setters instead!

You can refactor the existing code.

id_ - is just a random unique integer
"""


class Boss:

    def __init__(self, id_: int, name: str, company: str):

        self.id = id_

        self.name = name

        self.company = company

        self._workers = []

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, worker):
        self._workers.append(worker)
        print(f"{worker} -> {worker.name} has been added to {self.name}")


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):

        self.id = id_

        self.name = name

        self.company = company

        self._boss = None

        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value: "Boss"):
        if isinstance(value, Boss):
            if self.boss:
                del self.boss

            self._boss = value
            value.workers = self

    @boss.deleter
    def boss(self):
        print(f"{self} -> {self.name} has left {self.boss.name}")
        self.boss.workers.remove(self)


if __name__ == "__main__":
    print('\n---Task 2---\n')
    b = Boss(1, "Big Boss", "Corp")
    print(b.workers)
    w1 = Worker(1, "Usual Guy", "Corp", b)
    w2 = Worker(2, "Unusual Guy", "Corp", b)
    print(b.workers)
    print(w1.boss.name)
    b2 = Boss(2, "Good Boss", "Corp")
    w2.boss = b2
    print(f"{b.name} - {b.workers}")
    print(f"{b2.name} - {b2.workers}")

"""
Task 3

Write a class TypeDecorators which has several methods for converting results of functions to a specified type (if it's possible):

methods:

to_int

to_str

to_bool

to_float

 

Don't forget to use @wraps

"""


class TypeDecorators:

    @staticmethod
    def to_type(func, type_):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return type_(result)
            except ValueError:
                raise ValueError(f"convert of {type(result)} to {type_} is not supported")

        return wrapper

    to_int = lambda func: TypeDecorators.to_type(func, type_=int)
    to_str = lambda func: TypeDecorators.to_type(func, type_=str)
    to_bool = lambda func: TypeDecorators.to_type(func, type_=bool)
    to_float = lambda func: TypeDecorators.to_type(func, type_=float)

    # @staticmethod
    # def to_str(func):
    #     def wrapper(*args, **kwargs):
    #         result = func(*args, **kwargs)
    #         try:
    #             return str(result)
    #         except ValueError:
    #             raise ValueError(f"convert of {type(result)} to str is not supported")
    #
    #     return wrapper
    #
    # @staticmethod
    # def to_bool(func):
    #     def wrapper(*args, **kwargs):
    #         result = func(*args, **kwargs)
    #         try:
    #             return bool(result)
    #         except ValueError:
    #             raise ValueError(f"convert of {type(result)} to bool is not supported")
    #
    #     return wrapper
    #
    # @staticmethod
    # def to_float(func):
    #     def wrapper(*args, **kwargs):
    #         result = func(*args, **kwargs)
    #         try:
    #             return float(result)
    #         except ValueError:
    #             raise ValueError(f"convert of {type(result)} to float is not supported")
    #
    #     return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):

    return string


@TypeDecorators.to_bool
def do_something(string: str):

    return string

 
assert do_nothing('25') == 25
print(do_nothing('25'))

assert do_something('True') is True
print(do_something('True'))

