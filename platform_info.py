import inspect, platform

for name, value in inspect.getmembers(platform):
    if name[0] != '_' and callable(value):
        try:
            value = str(value())
        except (IndexError, TypeError):
            continue
        if value.strip("( ,')"):
            print('{:>23}() = {}'.format(name, value))

#import sys
#print(sys.platform, sys.version)
