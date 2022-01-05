from datetime import date


def calculate_age_from_birthday(birthday):
    """
    Calculate age from birthday
    """
    today = date.today()
    return (
        today.year
        - birthday.year
        - ((today.month, today.day) < (birthday.month, birthday.day))
    )
