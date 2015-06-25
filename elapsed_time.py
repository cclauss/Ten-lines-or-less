#!/usr/bin/env python

import contextlib, datetime

@contextlib.contextmanager
def timer(name='timer'):
    start = datetime.datetime.now()
    yield
    print('Elapsed time ({}): {}'.format(name, datetime.datetime.now() - start)) 

if __name__ == '__main__':
    # measure the speed of two methods of dict creation
    with timer('dict = {}'):
        for _ in xrange(100000):
            d = {}
    with timer('dict = dict()'):  # takes almost twice as long as {}
        for _ in xrange(100000):
            d = dict()
