import json
import random

max_tries = 6

# Sample JSON object
json_data = '{"words": ["apple"]}'

# Parse JSON data
data = json.loads(json_data)
try_number = 0
message = "Please, try again"

if 'words' in data and data['words']:
    random_word = random.choice(data['words'])

    while try_number < max_tries:

        # print("Random Word:", random_word)

        string_length = len(random_word)
        char_index = 0
        iteration = random_word
        user_input = ''

        while len(user_input) != string_length or user_input.isascii() == False:
            user_input = input(f"Enter You word (the word length is {string_length}, only the ascii is allowed).")

        try_result = ''

        while char_index < string_length:

            index = iteration.find(user_input[char_index]);

            if index == char_index:
                try_result = try_result + '!'
                iteration = iteration[:index] + '-' + iteration[index + 1:]
            elif index > -1:
                try_result = try_result + '?'
                iteration = iteration[:index] + '-' + iteration[index + 1:]
            else:
                try_result = try_result + '.'
                iteration = iteration[:char_index] + '-' + iteration[char_index + 1:]
            char_index = char_index + 1

        try_number = try_number + 1
        print(try_result)

        if (user_input == random_word):
            message = f"You are the winnner! The Number of the try: {try_number}"
            break;

print(message)