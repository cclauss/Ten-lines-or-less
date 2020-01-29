#!/usr/bin/env python
# coding: utf-8

from faker import Faker


def fake_fmt(fmt="{first_name}'s favorite number: {random_int}", fake=None):
    fake = fake or Faker()
    fields = [fld.split("}")[0].split(":")[0] for fld in fmt.split("{")[1:]]
    return fmt.format(**{field: getattr(fake, field)() for field in fields})


# with no parameters
print(fake_fmt())

# without a fmt but no fake parameter
print(fake_fmt("Hello {name}, How is the weather in {city}, {state_abbr}?"))

print(fake_fmt("My username is {user_name} but my email address is {email}."))

# with both fmt and fake parameters
fake = Faker()
print(fake_fmt("{name} considers a {catch_phrase} in {country}", fake))

# ===== more examples

# a list of ten fake people
fmt = "\t{first_name:10} {last_name:10} {random_int:>7}"
print("\n".join(fake_fmt(fmt) for _ in range(10)))

# a fake form letter
print(
    fake_fmt(
        """
\nDear valued {credit_card_provider} customer,

    On {credit_card_expire} your credit card {credit_card_number} will expire.
Three weeks before that date, we will send a replacement card to your address:

{street_address}
{city}, {state_abbr}  {postalcode_plus4}

    Yours truly,
        {name}
        {credit_card_provider}
"""
    )
)
