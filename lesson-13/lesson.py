print((1).__class__)

from typing import Any

def my_func():
    pass


def to_upper(s: Any):
    return str(s).upper()

names = (
    "a",
    " b",
    1,
    2,
    3,
    my_func,
)

print([to_upper(name) for name in names])
