"""
Комп'ютер загадує слово зі списку words.json і пропонує користувачеві відгатати його за шість спроб.
:mouse_trap: Користувач вводе слово, а комп'ютер "відповідає" на нього таким чином (паттерном):
- яккщо літера не зістрічається в загаданому слові, на її місці комп'ютер ставить крапку (.);
- якщо літера зустрічається, але на іншому місці - знак питання (?);
- якщо литера є і знаходиться на правильній позиції - знак оклику (!).
:page_facing_up: Приклад. Загадане слово - "Agent". Користувач вводить "Angel", відповідь комп'ютера повинна бути:
!???.   # перша літера - вірно; 2, 3, 4 - є такі, але на інших позиціях; 5 літера в слові відсутня
:bulb:Якщо користувач не відгадав слово за 6 спроб - програма завершується і коп'ютер виводить загадане слово.
:exclamation: Зверніть увагу, що літери в словах можуть повторюватись:
Якщо користувач вводить "focus", то для загаданого "Class" потрібно вивести ..?.! - остання літера вірна, а передостанньої в слові немає!
:pushpin:
-------------------- Додатково --------------------
1. Зробити гру регістронезалежною (не важливо, маленькі чи великі літери вводяться).
2. Зробити валідацію того, що вводить користувач: лише 5 літер латінецею (якщо користувач ввів щось невірне - ця спроба не рахується і комп'ютер лише пропонує ввести ще раз).
3. Ввести в гру підрахунок балів - на свій розсуд. Врахуйте, чи вгадана літера, чи на правильному місці, з якої спроби, тощо.
"""
import json
import random

INPUT_ERROR_MESSAGE = "only five latin characters allowed"

with open("words.json") as js:
    words = json.load(js)

guessed_word = list(random.choice(words))
# guessed_word = list("hello")
# user_input = "llolo"
tries = 5
user_input = []


def isvalid_input(user_input):
    return all([
        user_input.isalpha(),
        user_input.isascii(),
        len(user_input) == 5
    ])


while tries and user_input != guessed_word:
    user_input = input("guess the word of 5 chars: ").lower()
    if not isvalid_input(user_input):
        print(INPUT_ERROR_MESSAGE)
        continue

    tries -= 1
    guessed_l = guessed_word[:]
    response = ["."] * 5

    for i in range(len(guessed_word)):
        if guessed_l[i] == user_input[i]:
            response[i] = "!"
            guessed_l[i] = None

    for i in range(len(user_input)):
        if user_input[i] in guessed_l:
            response[i] = "?"
            index_of_guessed = guessed_l.index(user_input[i])
            guessed_l[index_of_guessed] = None

    print("".join(response))
    print(f"you have {tries} tries left")

if user_input != guessed_word:
    print(f"Sorry, the word was '{"".join(guessed_word)}'")
else:
    print("congrats! you won!")





"""
1. Загадування слова - DONE
2. Логіка перевірки вводу користувача відносно загаданого слова:
-- перевірка наявності букв в слові в правильному індексі - DONE
-- перевірка наявності букв в слові взагалі (за виключенням попередніх) - DONE
-- виведення результату/відповіді - DONE
3. Цикл спроб - DONE
"""
