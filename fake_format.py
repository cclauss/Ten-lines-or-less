#!/usr/bin/env python3
# coding: utf-8

from faker import Faker


def fake_fmt(fmt="{first_name}'s favorite number: {random_int}", fake=None):
    fake = fake or Faker()
    fields = [fld.split('}')[0].split(':')[0] for fld in fmt.split('{')[1:]]
    return fmt.format(**{field: getattr(fake, field)() for field in fields})

print(fake_fmt('\nHello {name}, How is the weather in {city}, {state_abbr}?'))

print(fake_fmt())

print(fake_fmt('My username is {user_name} but my email address is {email}.'))

fake = Faker()
print(fake_fmt('{name} considers a {catch_phrase} in {country}', fake))

fmt = '\t{first_name:10} {last_name:10} {random_int:>7}'
print('\n'.join(fake_fmt(fmt) for _ in range(10)))
