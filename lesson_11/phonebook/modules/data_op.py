import json

DATA_FILE = "data.json"
NO_BOOK_MSG = "\n---You don't have any phone books yet---\n"


def save_changes(phonebook, file_p):
    with open(file_p, "w") as file:
        json.dump(phonebook, file, indent=4)


def load_list_phonebooks():
    try:
        with open(DATA_FILE) as file:
            return json.load(file)
    except FileNotFoundError:
        print(NO_BOOK_MSG)


def save_phonebook_name(file_p):
    try:
        with open(DATA_FILE) as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    with open(DATA_FILE, "w") as file:
        if file_p not in data:
            data.append(file_p)
        else:
            print("\n---phonebook already exists---")
        json.dump(data, file)


def load_phonebook(file_p):
    try:
        with open(file_p) as file:
            phonebook = json.load(file)
    except FileNotFoundError:
        phonebook = []
    return phonebook
