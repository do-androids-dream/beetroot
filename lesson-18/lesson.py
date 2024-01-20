
def func(a, b="", c=2, d=True):
    return str(a) + b + str(d)


print(func(3, b="123")[1])


count = 0
for i in range(2):
    for j in range(2):
        if i == j:
            count += 1
    else:
        count += 1

print(count)
