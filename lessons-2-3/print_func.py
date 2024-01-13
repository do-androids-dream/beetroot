print(type(print("\"PY_123\n the best!")))

print((1))

print('02', 12, 2023, sep='-', end=' year')
print('-------------')


print("#" * 9, "\n#\t\t#" * 3, "\n", "#" * 9, sep="", end="\n\n")
print("#\t\t#\n" * 2, "#" * 9, "\n", "#\t\t#\n" * 2, sep="")

string = "string"

print(string[~0])

print(~0)

print(round(1.1))

b = b'foo\xddbar'
print(b[3])
print(b[2:3])
print(hex(50159747054))
print()
print("{:x} {}".format(123, "second"))
print("{:#x} {}".format(123, "second"))
print("{:.2f} {}".format(123, "second"))

SECRET = "333"

class Test():
    def __init__(self):
        pass

user_input = f"{print(globals())}"
# print(Test().__init__.__globals__[SECRET])
#
# print()

# This is our super secret key:
# SECRET = 'this-is-a-secret'
#
# class Test2:
#     def __init__(self):
#         pass
#
# # A malicious user can craft a format string that
# # can read data from the global namespace:
# user_input = '{test.__init__.__globals__[SECRET]}'
# print(user_input.format(test=Test()))
# This allows them to exfiltrate sensitive information,
# like the secret key:
# err = Error()
# print(user_input.format(error=err))

stuff_to_do = 1, 2, 3
print(stuff_to_do)
print(type(stuff_to_do))
print(*stuff_to_do)

