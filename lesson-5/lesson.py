"""
Гра "Вгадай число"
Компьютер "загадую" число від 1 до 99 і пропонує користувачеві його відгадати з 10 спроб.
Якщо користувач вгадав - програма завершується, вітає з перемогою і виводить "Congratulations! You've won in <N> attempts!" (де N - кількість спроб).
Якщо число не вгадане, а спроби ще залишаються - комп'ютер повідомляє чи загаданге число більше, чи менше введеного.
Якщо число не вгадане за всі десять спроб - комп'ютер виводить "Sorry, the number is <X>. Wanna try again?", де X - число, яке було загадане.
* Якщо користувач вводить невалідне значення - комп'ютер не рахує цієї спроби та виводить "Please, enter a valid number in range [1..99]"
"""
from random import randint

number = randint(1, 99)
tries = 0
win = False

while tries < 10:
    guess = input("Gues the number in range 1-99: ")

    if guess.isdigit():
        guess = int(guess)
        if 0 < guess < 100:
            tries += 1
            if guess == number:
                print(f"Congratulations! You've won in {tries} attempts!")
                win = True
                break
            elif guess != number:
                if guess > number:
                    print("number is smaller")
                elif guess < number:
                    print("number is greater")
    print("Please, enter a valid number in range [1..99]")
if not win:
    print(f"Sorry, the number is {number}. Wanna try again?")