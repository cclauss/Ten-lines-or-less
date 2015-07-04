import inspect, platform

for name, value in inspect.getmembers(platform):
    if name[0] != '_' and name != 'libc_ver' and callable(value):
        try:
            name, value = name + '()', str(value())
        except (IndexError, TypeError):
            continue
        if value.strip("( ,')") and not value.startswith('<module'):
            print('{:>23} = {}'.format(name, value))
