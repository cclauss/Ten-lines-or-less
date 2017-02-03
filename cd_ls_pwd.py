#!/usr/bin/env python

# Simulate the unix commands cd, ls, and pwd for non-Unix, non-iPython
# platforms (e.g. Pythonista for iOS)
# Recommended usage: $ python
#                  >>> import cd_ls_pwd     # import the three functions
#                  >>> cd = cd_ls_pwd.cd    # send up a top-level alias
#                  >>> ls = cd_ls_pwd.ls    # send up a top-level alias
#                  >>> pwd = cd_ls_pwd.pwd  # send up a top-level alias
# See '__main__' below for runtime usage examples

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
