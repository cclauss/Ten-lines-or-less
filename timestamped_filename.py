#!/usr/bin/env python

# 'sample.txt' --> 'sample_2016_01_23_18_07_23.txt'
# YYYY_MM_DD_hh_mm_ss order sorts oldest to newest.

import datetime, os

def timestamped_filename(file_name, date_time=None):
    date_time = date_time or datetime.datetime.now()
    root, ext = os.path.splitext(file_name)
    return '{}{:_%Y_%m_%d_%H_%M_%S}{}'.format(root, date-time, ext)

if __name__ == '__main__':
    import time
    print(timestamped_filename('sample.txt'))
    time.sleep(1)
    print(timestamped_filename('sample.txt'))
