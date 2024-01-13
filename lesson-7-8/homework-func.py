"""
Task 1

A simple function.

Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. The function should then print "My favorite movie is named {name}".
"""


def favorite_movie(movie_name: str) -> None:
    """print the name of the movie"""

    print(f"My favorite movie is named {movie_name}")


favorite_movie("Lord Of The Rings")
favorite_movie("Arizona Dream")
favorite_movie(input("Enter the name of your fav movie: "))

"""
Task 2

Creating a dictionary.

Create a function called make_country, which takes in a country’s name and capital as parameters. Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. Make the function print out the values of the dictionary to make sure that it works as intended.
"""

d = {}


def make_country(country_name: str, capital_city: str) -> None:
    """update global dictionary with country as key and capital as value and print it"""

    d[country_name] = capital_city
    print(d)


for i in range(3):
    make_country(input("enter country: "), input("and capital: "))

"""
Task 3

A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be '+', '-' or '*') and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation('+', 7, 7, 2) should return 16
the call make_operation('-', 5, 5, -10, -20) should return 30
the call make_operation('*', 7, 6) should return 42  
"""


def make_operation(operator: str, *args: int) -> int:
    """return the sum or product of all the numbers in the arbitrary parameter"""

    s = operator.join(map(str, args))
    return eval(s)


print(make_operation('+', 7, 7, 2))  # should return 16
print(make_operation('-', 5, 5, -10, -20))  # should return 30
print(make_operation('*', 7, 6))  # should return 42


# Custom solution
def int_to_str(numb: int) -> str:
    """converts int to string"""

    s = ""
    while numb:
        digit = numb % 10
        numb //= 10
        s += chr(digit + 48)
    return s[::-1]


def make_operation_2(operator: str, *args: int) -> int:
    s = [None] * len(args)
    i = 0
    for numb in args:
        s[i] = int_to_str(numb)
        i += 1
    s = operator.join(s)
    return eval(s)


print(make_operation_2('+', 125, 25, 50))  # should return 200