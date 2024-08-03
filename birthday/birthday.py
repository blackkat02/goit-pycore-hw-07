from field import Field, Name, Phone
from datetime import date, datetime, timedelta
from typing import Any, Union, Dict, List


class Birthday(Field):
    """Represents a birthday field and ensures valid date format."""

    def __init__(self, date_of_birth: str):
        formatted_date = self.get_formatted_date(date_of_birth)
        if formatted_date:
            super().__init__(formatted_date)
        else:
            raise ValueError("Invalid date format stored in Birthday object.")

    @staticmethod
    def get_formatted_date(date_of_birth: str) -> Union[date, None]:
        """Formats the birthday as a date object using the provided format code.
        Args:
            date_of_birth (str): The date of birth in DD.MM.YYYY format.
        Returns:
            Union[date, None]: The formatted date object or None if the format is invalid.
        """
        try:
            return datetime.strptime(date_of_birth, '%d.%m.%Y').date()
        except ValueError:
            return None

    @staticmethod
    def get_upcoming_birthdays(birthday_dict: Dict[str, Any]) -> List[Dict[str, str]]:
        """Finds upcoming birthdays within the next 7 days, accounting for weekends.
        Args:
            birthday_dict (Dict[str, Any]): A dictionary with 'name' and 'birthday' keys.
        Returns:
            List[Dict[str, str]]: A list of dictionaries with upcoming birthdays.
        """
        upcoming_list_birthdays = []
        today_date = datetime.today().date()
        birthday = birthday_dict["birthday"]

        if isinstance(birthday, Birthday):
            birthday_date = birthday.value.replace(year=today_date.year)

            if birthday_date < today_date:
                birthday_date = birthday_date.replace(year=today_date.year + 1)

            if birthday_date - today_date <= timedelta(days=7):
                birthday_weekday = int(birthday_date.strftime("%w"))
                number_weekday = [6, 0]
                if birthday_weekday in number_weekday:
                    days = 2 - number_weekday.index(birthday_weekday)
                    birthday_date += timedelta(days=days)

                upcoming_list_birthdays.append(
                    {"name": birthday_dict["name"], "congratulation_date": birthday_date.strftime("%d.%m.%Y")}
                )

        return upcoming_list_birthdays
