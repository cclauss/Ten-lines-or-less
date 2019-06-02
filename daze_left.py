#!/usr/bin/env python3

# Inspired by https://pythonclock.org

from datetime import date, timedelta

print((date(2020, 1, 1) - date.today()).days, "days until Python 2 end of life.")


def daze_left(days=500):
    d = date(2020, 1, 1) - timedelta(days=days)
    return f"On {d} there will be {days} days until Python 2 end of life."


for days in (200, 150, 100, 50):
    print(daze_left(days=days))

"""
627 days until Python 2 end of life.
On 2018-05-11 there will be 600 days until Python 2 end of life.
On 2018-08-19 there will be 500 days until Python 2 end of life.
On 2018-11-27 there will be 400 days until Python 2 end of life.
On 2019-03-07 there will be 300 days until Python 2 end of life.
On 2019-04-26 there will be 250 days until Python 2 end of life.
On 2019-06-15 there will be 200 days until Python 2 end of life.
On 2019-09-23 there will be 100 days until Python 2 end of life.
"""
