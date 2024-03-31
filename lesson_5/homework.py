"""
Task 1

The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user via a print statement.
"""
import random
from random import randint, shuffle

print("\n---Task 1---")

while True:
    number = randint(1, 10)

    while True:
        guess = input("\nguess the number in range 1-10: ")
        if guess.isdigit() and 0 < int(guess) < 11:
            guess = int(guess)
            if guess == number:
                print(f"Congratulations! You've won!!!")
                break
            elif guess != number:

                if guess > number:
                    print("number is smaller")
                elif guess < number:
                    print("number is greater")
                stop_play = input("enter 'n' to give up or skip: ")
                if stop_play:
                    print(f"\nSorry, the number is {number}.")
                    break
                continue
        else:
            print("Please, enter a valid number in range [1..99]")

    again = input("Wanna try again? (y/n): ")
    if again == 'n':
        break
"""
Task 2

The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”   
"""
print("\n---Task 2---")

print(f"Hello {input('enter your name: ')}, on your next birthday you’ll be {int(input('enter your age: ')) + 1} years")

"""
Task 3

Words combination

Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.

For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters 

'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
Tips: Use random module to get random char from string)
"""
print("\n---Task 3---")

some_string = list(input("enter your string: "))

for i in range(5):
    random_string = some_string[:]
    shuffle(random_string)
    print("".join(random_string))
print("original string: ", "".join(some_string))  # check if original list wasn't changed
