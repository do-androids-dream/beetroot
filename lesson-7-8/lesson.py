def test(**kwargs):
    print(kwargs)

test(first="a", second="b", third="c")

def test2(*args):
    print(args)

test2(1, 2, 3)

from _collections import defaultdict

a = defaultdict()

func = lambda x: x
print(func(2))