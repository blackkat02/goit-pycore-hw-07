# from datetime import datetime, timedelta
# import datetime
# from decorators import InputError
# from functools import wraps
from address_book import AddressBook
from functions import show_phone, parse_input, change_phone, show_all_contacts
from functions import add_contacts, add_birthday, birthdays, show_birthday
# from record import Record
# from field import Phone, Name, Field


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(args)
            print(add_contacts(args, book))

        elif command == "change":
            print(change_phone(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all_contacts(args, book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

#  add q 1234567890    add a 2345678900    add-birthday q 10.08.2000    add-birthday a 8.08.2001     birthdays