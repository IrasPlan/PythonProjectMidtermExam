def days_since_birthday(birthday):
    """
    Calculates the number of days that have passed since the birth date,
    excluding the birth year and the current year.

    :param birthday: A string in the format "DD-MM-YYYY"
    :return: Number of days passed (excluding birth year and current year)
    """


    birth_year = int(birthday[-4:])


    current_year = 2025


    full_years_passed = (current_year - birth_year - 1)


    total_days = full_years_passed * 365

    return total_days



birthday_str = "11-10-2005"
days_passed = days_since_birthday(birthday_str)
days_passed
print(days_passed)