from .data_op import load_phonebook, save_changes, save_phonebook_name, load_list_phonebooks, DATA_FILE

RECORD_TEMPLATE = (
    "first name",
    "last name",
    "telephone number",
    "city",
    "state"
)
STR_FIELDS = (
    "first name",
    "last name",
    "city",
    "state"
)
EMPTY_BOOK_MSG = "\n---phonebook is empty---\n"
NEXT_OP = "next"
SELECT_OP = "select"
EXT = ".json"


def validate_record(record_key, record_val, file_p):
    phonebook = load_phonebook(file_p)

    if record_key in STR_FIELDS:
        if not record_val.isalpha() or len(record_val) < 1:
            print(f"\n---{record_key} should include A-Z/a-z letter only---\n")
            return False
    if record_key == RECORD_TEMPLATE[2]:
        if not record_val[1:].isnumeric() or len(record_val) != 13:
            print(f"\n---{record_key} should include 12 digits only---\n")
            return False
        for ex_record in phonebook:
            if ex_record[record_key] == record_val:
                print(f"\n---{record_key} {record_val} already exists---\n")
                return False
    return True


def create_record(file_p):
    record = {}
    for field in RECORD_TEMPLATE:
        while True:
            record[field] = input(f"Please enter {field}: ").capitalize()
            if field == RECORD_TEMPLATE[2]:
                if record[field][0] != "+":
                    record[field] = "+" + record[field]
            if validate_record(field, record[field], file_p):
                break
    save_new_record(record, file_p)
    return record


def save_new_record(record, file_p):
    phonebook = load_phonebook(file_p)
    phonebook.append(record)
    save_changes(phonebook, file_p)
    print_record(record)
    print("---has been saved successfully---\n")


def print_record(record: dict):
    print("\n---record---")
    for key, val in record.items():
        print(f"{key}: {val}")


def delete_record(file_p):
    phonebook = load_phonebook(file_p)
    if not phonebook:
        return print(EMPTY_BOOK_MSG)
    index = search_func(file_p)
    if index is None:
        return
    del_rec = phonebook.pop(index)
    save_changes(phonebook, file_p)
    print_record(del_rec)
    print(f"---has been deleted---\n")


def update_record(file_p):
    phonebook = load_phonebook(file_p)
    if not phonebook:
        return print(EMPTY_BOOK_MSG)

    index = search_func(file_p)
    if index is None:
        return
    print("\navailable fields:")
    for key in phonebook[index]:
        print("-", key)
    while True:
        key = input("Please choose which field you want to update: ")
        value = input("Please enter new value for selected field: ")
        if validate_record(key, value, file_p):
            break
    phonebook[index][key] = value
    save_changes(phonebook, file_p)
    print_record(phonebook[index])
    print(f"---has been updated---\n")


def search(phonebook, key_val, index):
    key, val = key_val
    if key == "first name & last name":
        f_name, l_name = val.split(" ")
        f_name = f_name.capitalize()
        l_name = l_name.capitalize()
        while index < len(phonebook):
            if phonebook[index]["first name"] == f_name and \
                    phonebook[index]["last name"] == l_name:
                return index
            index += 1

    while index < len(phonebook):
        if phonebook[index][key] == val:
            return index
        index += 1


def search_input(phonebook):
    print("\nSearch keys:")
    print("- first name & last name")
    for key in phonebook[0]:
        print("-", key)
    print()
    while True:
        search_key = input("Please enter key for search: ")
        if search_key in phonebook[0] or search_key == "first name & last name":
            break
        else:
            print("\n---wrong search key---\n")
    while True:
        search_val = input(f"Please enter value for {search_key} search: ").capitalize()
        if search_key == RECORD_TEMPLATE[2]:
            if search_val[0] != "+":
                search_val = "+" + search_val
            if len(search_val) != 13:
                print(f"---{search_key} should include 12 digits only---")
                continue
        break
    return search_key, search_val


def search_func(file_p):
    operations = (
        NEXT_OP,
        SELECT_OP,
    )
    phonebook = load_phonebook(file_p)
    if not phonebook:
        return print(EMPTY_BOOK_MSG)

    search_inputs = search_input(phonebook)
    start_ind = 0
    index_list = []

    while start_ind < len(phonebook):
        index = search(phonebook, search_inputs, start_ind)
        if index is None:
            break
        index_list.append(index)
        start_ind = index + 1

    if index_list:
        count = 0
        for index in index_list:
            count += 1
            result = phonebook[index]
            print_record(result)
            print()

            print("Search result operations:")
            for key in operations:
                print("-", key)
            print()

            while True:
                user_op = input("Enter operation: ")
                if user_op in operations:
                    break
                else:
                    print("---No such operation---\n")
            if user_op == NEXT_OP and count == len(index_list):
                print("\n---end of search result---\n")
            elif user_op == NEXT_OP:
                continue
            elif user_op == SELECT_OP:
                break

        return index
    else:
        print("\n---Not found---\n")


def create_phonebook_path():
    while True:
        file_p = input("Please name your phonebook: ") + EXT
        if file_p != DATA_FILE:

            save_phonebook_name(file_p)
            return file_p
        print("---Please choose another name---\n")


def open_phonebook_path():
    phonebook_list = load_list_phonebooks()
    while phonebook_list:
        print("\navailable phonebooks:")
        for i in phonebook_list:
            name = i[:-5]
            print("-", name)
        print()
        file_p = input("please enter the name of phonebook: ") + EXT
        if file_p in phonebook_list:
            print()
            return file_p
        print("\n---Opps, can't find such name---")


def exit_app():
    exit()
