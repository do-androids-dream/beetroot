def gen():
    x = 0
    while x < 5:
        x += 1
        yield x


g = gen()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


