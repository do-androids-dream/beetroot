# class My:
#     pass
#
#
# a = My()
# b = 25
#
#
# a.attr = b
#
# print(a.attr)


def my_func(a, b):
    print(a, b)


def my_func2(*args):
     print(args)


def my_func3(**kwargs):
    print(kwargs)


my_func(1, 2)
my_func2(1, 2, 3)
my_func3(number_1=1, number_2=2, a="abcd", one=25)
