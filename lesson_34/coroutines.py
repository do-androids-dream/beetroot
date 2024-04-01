# def sample():
#     print("start")
#     yield
#     x = yield
#     print("X", x)
#
#
# g = sample()
# print(g)
# print("***********")
# # print(next(g))
# print(g.send(None))
# print("***********")
# print(g.send(5))
# print(g.send(10))


# def sub():
#     while True:
#         try:
#             a = yield
#             print(f".........{a}")
#         except StopIteration:
#             break
#     return a
#
#
# def delegator(gen):
#     # while True:
#     #     try:
#     #         a = yield
#     #         gen.send(a)
#     #     except StopIteration as e:
#     #         gen.throw(StopIteration)
#     res = yield from gen
#     print(f"RESULT: {res}")
#
#
# s = sub()
# d = delegator(s)
#
# print(next(d))
# print("***************")
# d.send(None)
# print("***************")
# d.send(5)
# print("***************")
# d.send(10)
# print("***************")
# d.throw(StopIteration)


