"""
Task 1

Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values.
"""
print("---Task-1---")
sentence = input("enter your sentence: ")
d = {}
sentence = sentence.split()
for i in sentence:
    d[i] = d.get(i, 0) + 1
print(d)

"""
Task 2

Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the quantity of this exact item.

The code has to return the dictionary with the sums of the prices by the goods types.
"""

print("---Task-2---")

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = {key: stock[key] * prices[key] for key in stock}
print(total_price)

"""
Task 3

List comprehension exercise

Use a list comprehension to make a list containing tuples (i, j) where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared.
"""

print("---Task-3---")
list_comp = [(i, i ** 2) for i in range(1, 11)]
print(list_comp)

"""
Task 4

Створити лист із днями тижня.
В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,
"""

print("---Task-4---")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
week = {i + 1: days[i] for i in range(7)}
week_rev = {days[i]: i + 1 for i in range(7)}
print(week, week_rev)
