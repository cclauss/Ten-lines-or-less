#!/usr/bin/env python3

from contextlib import contextmanager
from datetime import datetime
from time import perf_counter


@contextmanager
def timer(name="timer"):
    start = datetime.now()
    yield
    print(f"Elapsed time ({name}): {datetime.now() - start}")


@contextmanager
def elapsed_time(name="elapsed_time"):
    """Two ways to use elapsed_time():
    1. As a decorator to time the execution of an entire function:
        @elapsed_time("my_slow_function")
        def my_slow_function(n=10_000_000):
            pass
    2. As a context manager to time the execution of a block of code inside a function:
        with elapsed_time("my_slow_block_of_code"):
            pass
    .
    """
    start = perf_counter()
    yield
    print(f"Elapsed time ({name}): {perf_counter() - start:0.8} seconds")


if __name__ == "__main__":
    # measure the speed of two ways to create a dict
    with timer("dict = {}"):
        for _ in range(10_000_000):
            d: {}  # type: ignore
    with timer("dict = dict()"):  # takes ~50% longer than {}
        for _ in range(10_000_000):
            d = {}
