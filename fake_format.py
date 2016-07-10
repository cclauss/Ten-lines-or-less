#!/usr/bin/env python2
# coding: utf-8

from faker import Faker

def fake_fmt(fmt="{first_name}'s favorite number: {random_int}", fake=None):
    fake = fake or Faker()
    fields = [field.split('}')[0] for field in fmt.split('{')[1:]]
    return fmt.format(**{field: getattr(fake, field)() for field in fields})

print(fake_fmt('\nHello {name}, How is the weather in {city}, {state_abbr}?'))
print(fake_fmt())
print(fake_fmt('My username is {user_name} but my email address is {email}.'))
fake = Faker()
print(fake_fmt('{name} considers a {catch_phrase} in {country}', fake))
