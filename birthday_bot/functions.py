from decorators import InputError
from address_book import AddressBook
from record import Record
#from datetime import date, datetime, timedelta
from birthday import Birthday


@InputError.input_error
def add_contacts(args, book: AddressBook):
    """Adds a new contact or updates an existing one, handling missing phone.
    Args:
        args (list): A list of arguments containing name, phone (optional), and
                     any additional arguments (ignored).
        book (AddressBook): The address book object to manage contacts.
    Returns:
        str: A message indicating whether the contact was added or updated.
    """
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record_phone(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@InputError.input_error
def change_phone(args, book: AddressBook):
    """Changes the phone number for a contact, handling missing contact.
    Args:
        args (list): A list of arguments containing name, old_phone, new_phone,
                     and any additional arguments (ignored).
        book (AddressBook): The address book object to manage contacts.

    Returns:
        str: A message indicating whether the phone number was updated or if
             the contact was not found.
    """
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Phone number updated."
    else:
        return "Contact not found."

@InputError.input_error
def show_phone(args, book: AddressBook):
    """Shows the phone number(s) for a contact, handling missing contact.
    Args:
        args (list): A list of arguments containing name, an old phone, a new phone
         and any additional arguments (ignored).
        book (AddressBook): The address book object to manage contacts.
    Returns:
        str: A string containing the contact's name and phone number(s) separated
             by commas, or a message if the contact is not found.
    """
    name, *_ = args
    record = book.find(name)
    if record:
        return f"{name}: {', '.join(record.phones)}"
    else:
        return "Contact not found."


@InputError.input_error
def show_all_contacts(args, book: AddressBook):
    """Shows all contacts and their information from the address book.
    Args:
        args (list): A list of arguments (ignored).
        book (AddressBook): The address book object to manage contacts.
    Returns:
        str: A string listing all contacts and their information, one per line.
    """
    contacts = []
    for name, record in book.data.items():
        name = ', '.join(book)
        contacts.append(f"{name}: {record}")
    return "\n".join(contacts)



@InputError.input_error
def add_birthday(args, book: AddressBook):
    """Adds a birthday for a contact, handling missing contact.
    Args:
        args (list): A list of arguments containing name, birthday (str in format
                DD.MM.YYYY), and any additional arguments (ignored).
                book (AddressBook): The address book object to manage contacts.
    Returns:
        str: A message indicating whether the birthday was added or if the contact was not found.
    """
    name, birthday, *_ = args
    record = book.find(name)
    if record:
        record.add_date_of_birth(birthday)
        return "Birthday added."
    else:
        return "Contact not found."


@InputError.input_error
def show_birthday(args, book: AddressBook):
    """Shows the birthday for a contact, handling missing contact or missing birthday.
    Args:
        args (list): A list of arguments containing name and any additional arguments (ignored).
        book (AddressBook): The address book object to manage contacts.
    Returns:
        str: A string containing the contact's name and birthday (formatted DD.MM.YYYY)
             if available, or a message if the contact is not found or doesn't have a birthday.
    """
    name, *_ = args
    record = book.find(name)
    if record:
        if isinstance(record.birthday, Birthday):
            record.birthday = record.birthday.value.strftime("%d.%m.%Y")
            return f"{name}'s birthday is on {record.birthday}."
        else:
            return "Birthday not set."
    else:
        return "Contact not found."


@InputError.input_error
def parse_input(user_input):
    return user_input.split()


@InputError.input_error
def birthdays(args, book):
    return book.get_upcoming_birthdays
