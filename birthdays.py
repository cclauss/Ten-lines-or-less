"""Prints a list of birthdays in your address book (in days from now).

NOTE: This script requires access to your contacts in order to work.
"""

import contacts, datetime  # noqa


def days_until_next(date):
    now = datetime.datetime.now()
    inc = int(datetime.datetime(now.year, date.month, date.day) < now)
    return (datetime.datetime(now.year + inc, date.month, date.day) - now).days


text = "\n".join(
    "* {p.first_name} in {days} days".format(**x)
    for x in sorted(
        (
            {"p": p, "days": days_until_next(p.birthday)}
            for p in contacts.get_all_people()
            if p.birthday
        ),
        key=lambda x: x["days"],
    )
)

print(
    f"Upcoming Birthdays:\n{'=' * 19}\n{text}"
    if text
    else "You don't have any birthdays in your address book.",
)
