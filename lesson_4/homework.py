"""
Task 1

String manipulation

Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.

Sample String: 'helloworld'

Expected Result : 'held'

Sample String: 'phonebook'

Expected Result : 'mymy'

Sample String: 'x'

Expected Result: Empty String

Tips:

Use built-in function len() on an input string
Use positive indexing to get the first characters of a string and negative indexing to get the last characters
"""


def make_string(input_str):
    if len(input_str) < 2:
        return ""  # Empty string
    return input_str[:2] + input_str[-2:]


print("---Task 1---")
sample = [
    'helloworld',
    'phonebook',
    'x',
    input("enter your string: ")
]

for i in sample:
    print(make_string(i), type(i))


"""
Task 2

The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. 
The program should check that the string contains only numerical characters and is only 10 characters long. Print a suitable message depending on the outcome of the string evaluation.
"""


import re

print("\n---Task 2---", "\nsolution 1")
pattern = r"[0-9]{10}"
print("Successfully validated" if re.fullmatch(pattern, input("please enter your phone number (10 digits): ")) else "Not valid")

print("\n", "solution 2", sep="")
phone_number = input("please enter you phone number (10 digits): ")
if len(phone_number) == 10 and phone_number.isnumeric():
    print("Successfully validated")
else:
    print("Not valid")


"""
Task 3

The math quiz program.

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.
"""

print("\n---Task 3---")
tries = 0
math_expr = "10 - 5"
while True:
    answer = input(f"what is result of {math_expr}? ")
    if answer.isnumeric() and int(answer) == eval(math_expr):
        print("Right!")
        break
    else:
        print("Naaaah! try again\n")
        if tries >= 2 and input('or enter "please let me go" to give up: ') == "please let me go":
            print("Ok, ok, don't cry")
            break
        tries += 1


"""
Task 4

The name check.

Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. 
The program should check if your input is equal to the stored name even if the given name has another case, e.g., if your input is “Anton” and the stored name is “anton”, it should return True.
"""


print("\n---Task 4---")
stored = "volodymyr"
print(stored == input("please enter the name: ").lower())
