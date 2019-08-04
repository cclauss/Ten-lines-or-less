#!/usr/bin/env python3

from datetime import datetime
from typing import Tuple


def ask_month_day_year(prompt: str = "Enter your birthday") -> Tuple[int, int, int]:
    date = input(f"{prompt} in the format: MM/DD/YYYY ")
    month, day, year = (int(x.strip()) for x in date.split("/"))
    return month, day, year


def day_of_the_week(year, month, day):
    return f"{datetime(year, month, day):%A}"


month, day, year = ask_month_day_year()
print(f"You were born on a {day_of_the_week(year, month, day)}.")
