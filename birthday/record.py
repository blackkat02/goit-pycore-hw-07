from field import Field, Name, Phone
from birthday import Birthday
from datetime import date, datetime, timedelta
from typing import Any, Union, Dict, List


class Record:
    """Represents a record (contact) in the address book."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_date_of_birth(self, date_of_birth: str) -> Birthday:
        """Adds a date of birth, ensuring validity through a Birthday object creation.
        Args:
            date_of_birth (str): The date of birth, string in DD.MM.YYYY format.
        Returns:
            Birthday: The created Birthday object.
        """
        self.birthday = Birthday(date_of_birth)
        return self.birthday

    def add_phone(self, phone_number: str):
        """Adds a phone number, validating or formatting it using a Phone class.
        Args:
            phone_number (str): The phone number string.
        """
        phone = Phone(phone_number)
        self.phones.append(phone)

    def __str__(self) -> str:
        """Defines the string representation of the record, used when printing.
        Returns:
            str: A formatted string with name, phones, and birthday (if set).
        """
        phones_str = '; '.join(p.value for p in self.phones)
        birthday_str = self.birthday.value.strftime('%d.%m.%Y') if self.birthday else "No birthday"
        return f"Contact name: {self.name.value}, phones: {phones_str}, birthday: {birthday_str}"
