class Field:
    def __init__(self, value):
        """
        Initializes a Field object with the given value.
        Args:
            value: The value to store in the field.
        """
        self.value = value

    def __str__(self):
        """
        Returns a string representation of the field value.
        Returns:
            The string representation of the field value.
        """
        return str(self.value)


class Name(Field):
    """Represents a name field."""
    pass


class Phone(Field):
    """Represents a phone number field."""
    def __init__(self, value):
        """
        Initializes a Phone object with the given phone number.
        Args:
            value: The phone number to store in the field.
        Raises:
            ValueError: If the phone number is invalid (not 10 digits).
        """
        if self.validate(value):
            super().__init__(value)
        else:
            raise ValueError("Invalid phone number. Must be 10 digits.")

    @staticmethod
    def validate(value):
        """
        Validates a phone number.
        Args:
            value: The phone number to validate.
        Returns:
            True if the phone number is valid, False otherwise.
        """
        return value.isdigit() and len(value) == 10
