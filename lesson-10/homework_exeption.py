"""
Task 1

Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except state­ment to catch the error. What happens if you change oops to raise KeyError instead of IndexError?
"""

def oops():
    raise IndexError("Oops!")
    # raise KeyError("Oops!")


def call_oops():
    try:
        oops()
    except IndexError as e:
        print(e, "You did it again!")


call_oops()


"""
Task 2

Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the value of squared a divided by b, 
construct a try-except block which raises an exception if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).    
"""


def squared_divided(a, b):
    try:
        return (float(a) / float(b)) ** 2
    except ValueError as e:
        print(e, ": Not a number!")
    except ZeroDivisionError as e:
        print(e, ": Do not ever divide by ZERO!")
    except Exception:
        print("What are you doin'..?")
    finally:
        print("That's all :)")


result = squared_divided(input("number 1: "), input("number2: "))
print(result)
