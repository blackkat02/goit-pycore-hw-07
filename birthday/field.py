#from bot_address_book_main import AddressBook


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise ValueError("Invalid phone number. Must be 10 digits.")

    @staticmethod
    def validate(value):
        return value.isdigit() and len(value) == 10
