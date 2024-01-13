"""
Task 1
The greeting program.

Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:

     "Good day <name>! <day> is a perfect day to learn some python."
Note that  <name> and <day> are predefined variables in source code.

An additional bonus will be to use different string formatting methods for constructing result string.
"""

print("--Task 1--")

name = "Volodymyr"
day = "Sunday"

print(f"Good day {name}! {day} is a perfect day to learn some python.\n")

name_to_format = "mynameisvolodymyryeah"

print(f"Good day {name_to_format.capitalize()[name_to_format.find("v"):~4]}! {day} is a perfect day to learn some python.\n")
print("Good day {}! {day} is a perfect day to learn some python.\n".format(name, day='Monday')) # Sunday suits more for the rest :)
print("What can really spoil the {}'s morning is {:x} \U0001F923\n".format(day, 50159747054)) # love the joke from article


"""
Task 2
Manipulate strings.

Save your first and last name as separate variables, then use string concatenation to add them together with a white space in between and print a greeting.
"""

print("--Task 2--")

first_name = "Volodymyr"
last_name = "Dukhanin"
full_name = first_name + " " + last_name

print(f"Greetings, {full_name}!\n")

"""
Task3
Using python as a calculator.

Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following: 

Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division
"""

print("--Task 3--")

while True:
    a, b = (input("please enter 1st int number: ")), (input("please enter 2nd int number: "))
    if a.isnumeric() and b.isnumeric():
        break
    print("unsigned INTEGER!!!")

a, b = int(a), int(b)

operation = {
    "Addition": a + b,
    "Subtraction": a - b,
    "Division": "ERROR: Division by zero" if b == 0 else a / b,
    "Multiplication": a * b,
    "Exponent (Power)": a**b,
    "Modulus": "ERROR: Division by zero" if b == 0 else a % b,
    "Floor division": "ERROR: Division by zero" if b == 0 else a // b,
}
print("\n")
for i in operation:
    print(f"{i}: {operation[i]}")
