#!/usr/bin/env python

import contextlib, datetime, typing  # noqa


@contextlib.contextmanager
def timer(name="timer"):
    start = datetime.datetime.now()
    yield
    print("Elapsed time ({}): {}".format(name, datetime.datetime.now() - start))


if __name__ == "__main__":
    # measure the speed of two ways to create a dict
    with timer("dict = {}"):
        for _ in range(100000):
            d: typing.Dict = {}
    with timer("dict = dict()"):  # takes almost twice as long as {}
        for _ in range(100000):
            d = dict()
