from collections import UserDict
from birthday import Birthday
from record import Record
from typing import Any, Union, Dict, List


class AddressBook(UserDict):
    """Provides a dictionary-like interface for managing records in an address book."""

    def add_record(self, record: Record):
        """Adds a Record object to the address book, checking for duplicate names.
        Args:
            record (Record): The Record object to add.
        """
        if record.name.value in self.data:
            print(f"Warning: Duplicate name '{record.name.value}'. Skipping record.")
        else:
            self.data[record.name.value] = record

    def find(self, name: str) -> Union[Record, None]:
        """Finds a record by name.
        Args:
            name (str): The name to search for.
        Returns:
            Record: The record object found, or None if not found.
        """
        return self.data.get(name)

    def delete(self, name: str):
        """Deletes a record from the address book.
        Args:
            name (str): The name of the record to delete.
        """
        if name in self.data:
            if name in self.data:
                del self.data[name]


# Testing the address book system
if __name__ == "__main__":
    # Creating a new address book
    book = AddressBook()

    # Creating a record for John
    john_record = Record("John")
    john_record.add_date_of_birth("11.08.2000")
    john_record.add_phone("5555755555")
    john_record.add_phone("9955555500")

    # Adding John's record to the address book
    book.add_record(john_record)

    # Creating and adding a new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_date_of_birth("03.08.1999")
    book.add_record(jane_record)

    # Printing all records in the book
    for record in book.data.values():
        print(record)

    # Checking upcoming birthdays
    for record in book.data.values():
        upcoming_birthdays = Birthday.get_upcoming_birthdays({"name": record.name.value, "birthday": record.birthday})
        if upcoming_birthdays:
            print(f"Upcoming birthdays: {upcoming_birthdays}")

    jane_find = book.find("Jane")
    print(jane_find)

    jo_record = Record("Jo")
    jo_record.add_date_of_birth("10.08.2000")
    jo_record.add_phone("7755755555")
    jo_record.add_phone("0055555500")
    book.add_record(jo_record)
    jo_find = book.find("Jo")
    print()
    for record in book.data.values():
        print(record)
    print(jo_find)
    book.delete("Jo")
    book.delete("Jane")

    for record in book.data.values():
        print(record)

