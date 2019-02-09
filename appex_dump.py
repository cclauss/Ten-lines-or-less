# coding: utf-8

# See: https://forum.omz-software.com/topic/2358/appex-safari-content

import appex, inspect  # noqa

this_is_an_undefined_name

def main():
    if appex.is_running_extension():
        for name_func in inspect.getmembers(appex):
            name, func = name_func
            if name.startswith('get_'):  # find all appex.get_xxx() methods
                print('{:<11} : {}'.format(name.partition('_')[2], func()))


if __name__ == '__main__':
    main()
