"""
Task 1

The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers
"""
from random import randint

print("\n---Task 1---")

length = 10
random_list = []

while length:
    random_list.append(randint(0, 100))
    length -= 1
print("Random numbers list:", random_list)
print("largest number: ", max(random_list))

print("\nOR\n")

random_list.sort()
print(f"sorted list last element: {random_list[~0]}")

"""
Task 2

Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 15, and make a third list containing the common integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers
"""

print("\n---Task 2---")

length = 10
list_1 = []
list_2 = []

while length:
    list_1.append(randint(0, 15))
    list_2.append(randint(0, 15))
    length -= 1

list_3 = list(set(list_1) & set(list_2))
print(f"list_1 {list_1}\nlist_2 {list_2}")
print(f"3rd list {list_3}")

print("\nOR\n")

list_hardcoding = []
for i in list_1:
    for j in list_2:
        if i == j and i not in list_hardcoding:
            list_hardcoding.append(i)

print("hardcoding list", list_hardcoding)

list_comp = list(set([n for n in list_1 if n in list_2]))
print(list_comp)

print("\nOR\n")

s1 = set(randint(1, 10) for i in range(10))
s2 = set(randint(1, 10) for i in range(10))
print(s1, s2, s1 & s2)

"""
Task 3

Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration

"""

print("\n---Task 3---")

length = 100
list_of_ints = []
filtered_list = []

while length:
    if length % 7 == 0 and length % 5:
        list_of_ints.append(length)
    length -= 1

print(list_of_ints)

print("\nOR\n")

print("list comprehension", [n for n in range(1, 101) if n % 7 == 0 and n % 5])
