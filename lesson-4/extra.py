"""
Кожен другий символ рядка у нижньому регістрі, а всі інші - в верхньому
"""

string = "Beetroot Academy Python course"

# 1st solution
for i in range(len(string)):
    print(string[i].upper() if i % 2 == 0 else string[i], end="")
print()

# 2nd solution
string_to_print = ""

for i in range(len(string[::2])):
    string_to_print += string[::2][i].upper() + string[1::2][i].lower()

print(string_to_print)

# 3rd solution
string_to_print = ""

for i in range(len(string)):
    string_to_print += string[i].upper() if i % 2 == 0 else string[i].lower()

print(string_to_print)

# 4th solution
i = 0
while i < len(string):
    print(string[i].upper(), sep="", end="") if i % 2 == 0 else print(string[i].lower(), sep="", end="")
    i += 1
print()

# interesting but problematic
print("interesting")
for j, k in [i for i in list(zip(string[0::2].upper(), string[1::2].lower()))]:
    print(j+k, end="")
print()

print([string[i].lower() if i % 2 == 0 else string[i].upper() for i in range(len(string))])

print()

string = ('For example, the program obtained the word')

c = string[::2].upper()
string = list(string)
string[::2] = c[:]

formatted_string = "".join(string)

print(formatted_string)

formatted_string = ''.join([string[i].lower() if i % 2 == 1 else string[i].upper() for i in range(len(string))])
print(formatted_string)