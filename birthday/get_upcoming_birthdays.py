from datetime import datetime, timedelta
from birthday import Birthday


def get_upcoming_birthdays(users_dict: list[dict]) -> list[dict]:
    """
    Identify colleagues' birthdays within the next 7 days (including today) and adjust greetings for weekend dates.
    Args:
        users_dict (list of dicts): A list of dictionaries where each dictionary contains 'name' (user's name) and
        'birthday' (birthday in YYYY.MM.DD format) keys.
    Returns:
        list of dicts: A list of dictionaries containing 'name' and 'congratulation_date' keys for colleagues with
        upcoming birthdays.
    """
    upcoming_list_birthdays = []
    today_date = datetime.today().date()
    today_year_int = datetime.today().year
    today_year_str = today_date.strftime("%Y")

    for i in range(0, len(users_dict)):
        birthday_value = users_dict[i]["birthday"]
        birthday_date = datetime.strptime(birthday_value, "%Y.%m.%d").date()
        birthday_year_str = birthday_date.strftime("%Y")
        birthday_this_year_str = birthday_value.replace(birthday_year_str, today_year_str)
        birthday_this_year_date = datetime.strptime(birthday_this_year_str, "%Y.%m.%d").date()

        if birthday_this_year_date < today_date:
            birthday_this_year_str = birthday_value.replace(birthday_year_str, str(today_year_int + 1))
            birthday_this_year_date = datetime.strptime(birthday_this_year_str, "%Y.%m.%d").date()

        elif birthday_this_year_date - today_date <= timedelta(days=7):
            birthday_weekday = int(birthday_this_year_date.strftime("%w"))
            number_weekday = [6, 0]
            if birthday_weekday in number_weekday:
                days = 2 - number_weekday.index(birthday_weekday)
                birthday_this_year_date += timedelta(days=days)

            current_birth_upcoming_str = birthday_this_year_date.strftime("%Y.%m.%d")
            upcoming_list_birthdays.append(
                {"name": users_dict[i]["name"], "congratulation_date": current_birth_upcoming_str}
            )

    return upcoming_list_birthdays


# ddd = get_upcoming_birthdays(1999-11-21)
# print(ddd)

users = [
    {"name": "Janeі Smothes", "birthday": "1990.07.13"},
    {"name": "Janeі Smithes", "birthday": "1990.07.09"},
    {"name": "Jane Smithes", "birthday": "1990.07.05"},
    {"name": "Janet Smith", "birthday": "1990.07.06"},
    {"name": "Jihn Doese", "birthday": "1985.07.07"},
    {"name": "Jane Smith", "birthday": "1990.01.26"},
    {"name": "John Doe", "birthday": "1985.01.25"},
    {"name": "Jin Doe", "birthday": "1985.05.31"},
    {"name": "Jo Doe", "birthday": "1985.07.14"},
    {"name": "John Does", "birthday": "1985.12.28"},
    {"name": "Johan Doe", "birthday": "1985.12.31"},
]

upcoming_birthdays = get_upcoming_birthdays(users, )
print("Список привітань на цьому тижні:", upcoming_birthdays)
