from field import Field, Name, Phone
from datetime import datetime
from collections import UserDict


class Birthday(Field):
    """Represents a birthday field and ensures valid date format."""
    def __init__(self, date_of_birth=None):
        self.date_of_birth = date_of_birth

    def get_formatted_date(self, format_code="%Y-%m-%d"):
        """Formats the birthday as a string using the provided format code.
        Args:
            format_code (str, optional): The format code to use. Defaults to "%Y-%m-%d" (YYYY-MM-DD).
        Returns:
            str: The formatted date string.
        """
        if self.date_of_birth is not None:
            try:
                date_obj = datetime.strptime(self.date_of_birth, '%d.%m.%Y')
                return date_obj.strftime(format_code)
            except ValueError:
                print("Invalid date format stored in Birthday object.")
                return None
        else:
            return None


class Record:
    """Represents a record (contact) in the address book."""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_date_of_birth(self, date_of_birth):
        """Adds a birth date, ensuring validity through a Birthday object creation.
        Args:
            date_of_birth (str): The birth date string in DD.MM.YYYY format.

        Returns:
            Birthday: The created Birthday object.
        """
        date_of_birth = Birthday(date_of_birth)
        self.birthday = date_of_birth
        return self.birthday

    def add_phone(self, phone_number):
        """Adds a phone number, presumably validating or formatting it using a Phone class.
        Args:
            phone_number (str): The phone number string.
        """
        phone = Phone(phone_number)
        self.phones.append(phone)

    def __str__(self):
        """Defines the string representation of the record, used when printing.
        Returns:
            str: A formatted string with name, phones, and birthday (if set).
        """
        return (f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, "
                f"birthday: {self.birthday.date_of_birth}")


class AddressBook(UserDict):
    """Provides a dictionary-like interface for managing records in an address book."""
    def add_record(self, record):
        """Adds a Record object to the address book.
        Args:
            record (Record): The Record object to add.
        """
        self.data[record.name.value] = record

    def find(self, name):
        """Finds a record by name.
        Args:
            name (str): The name to search for.
        Returns:
            Record: The record object found, or None if not found.
        """
        return self.data.get(name, None)

    def delete(self, name):
        """Deletes a record from the address book.

        Args:
            name (str): The name of the record to delete.
        """


# Тестування системи управління адресною книгою
if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_date_of_birth("22.02.2000")
    john_record.add_phone("5555755555")
    john_record.add_phone("9955555500")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_date_of_birth("21.11.1999")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)
