#!/usr/bin/env python

# Simulate the unix commands cd, ls, and pwd for non-Unix platforms (Pythonista for iOS)
# Recommendation: paste the import plus 3 functions into the Python interactive prompt

import os

def cd(in_dir=os.path.expanduser('~')):
    os.chdir(in_dir)
    print(os.path.abspath(os.curdir))

def ls(in_dir=os.curdir):
    print('\n'.join(os.listdir(in_dir)))

def pwd():
    print(os.path.abspath(os.curdir))

if __name__ == '__main__':
    pwd()
    ls()
    cd()
    pwd()
    ls()
    cd('Python')
    pwd()
    ls()
    cd('/')
    pwd()
    ls()
