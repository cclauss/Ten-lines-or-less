#!/usr/bin/env python3

from contextlib import contextmanager
from datetime import datetime


@contextmanager
def timer(name="timer"):
    start = datetime.now()
    yield
    print(f"Elapsed time ({name}): {datetime.now() - start}")


if __name__ == "__main__":
    # measure the speed of two ways to create a dict
    with timer("dict = {}"):
        for _ in range(10_000_000):
            d: {}  # type: ignore
    with timer("dict = dict()"):  # takes ~50% longer than {}
        for _ in range(10_000_000):
            d = dict()
