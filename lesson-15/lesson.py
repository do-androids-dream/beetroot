x = 20

# def func():
#     def inner():
#         def inner_in():
#             nonlocal x
#             x += 1


# print(int)
#
# d = {item: item+1 for item in (i for i in range(10))}
# print(d)
#
#
# import unittest
#
# class Test(unittest.TestCase):
#
#     def setUp(self):
#         self.a = 5
#         self.b = 2
#
#     def test_addition(self):
#         result = self.a + self.b
#         expected = 7
#         self.assertEqual(result, expected)
#
# if __name__ == "__main__":
#     unittest.main()



# class Python:
#     population = 1
#     victims = 0
#     def __init__(self):
#         self.length_ft = 3
#         self.__venomous = False
#
# version_2 = Python()
#
# version_2._Python__venomous = not version_2._Python__venomous
# print(version_2._Python__venomous)
#
# print(not version_2._Python__venomous)

#
# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(B):
#     pass
#
# print(issubclass(C, C))
# print(issubclass(C, A))
#
# c = C()
# print(isinstance(c, C))
# print(isinstance(c, A))


# class I:
#     def __init__(self):
#         self.s = 'abc'
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.i == len(self.s):
#             raise StopIteration
#         v = self.s[self.i]
#         self.i += 1
#         return v
#
#
# for x in I():
#     print(x, end='')


class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.args = (msg,)


try:
    raise Ex('ex')
except Ex as e:
    print(e)
except Exception as e:
    print(e)
