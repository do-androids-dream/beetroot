"""
Task 2

Extend Phonebook application

Functionality of Phonebook application:

Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program


The first argument to the application should be the name of the phonebook. Application should load JSON data,
if it is present in the folder with application, else raise an error. After the user exits, all data should be
saved to loaded JSON.
"""

from modules.operations import create_phonebook_path, open_phonebook_path, exit_app, create_record, update_record, \
    delete_record, search_func

NO_OP_MSG = "\n---No such operation---\n"


def phonebook_app():
    phonebook_operations = {
        "create": create_phonebook_path,
        "open": open_phonebook_path,
        "exit": exit_app,
    }
    record_operations = {
        "create": create_record,
        "update": update_record,
        "delete": delete_record,
        "search": search_func,
    }

    print("\n<<<---WELCOME to PHONEBOOK APP--->>>\n")
    while True:

        while True:
            print("Phonebook operations:")
            for key in phonebook_operations:
                print("-", key)
            print()

            user_op = input("Enter operation: ")
            if user_op in phonebook_operations:
                file_path = phonebook_operations[user_op]()
                if file_path:
                    file_name = file_path.split(".")[0]
                    print()
                    break
            else:
                print(NO_OP_MSG)
                continue

        while True:
            print(f"Record operations for <{file_name}> phonebook:")
            for key in record_operations:
                print("-", key)
            print("-", "back")
            print()

            user_op = input("Enter operation: ")
            if user_op in record_operations:
                record_operations[user_op](file_path)
            elif user_op == "back":
                break
            else:
                print(NO_OP_MSG)


if __name__ == "__main__":
    phonebook_app()



"""
1. Шаблон тел книги - DONE
2. Функціонал створення запису - DONE
3. Функціонал пошуку - DONE
4. Delete a record - DONE
5. Update a record - DONE
6. Логіка запуску функцій - DONE
7. Валідація даних - DONE
"""
