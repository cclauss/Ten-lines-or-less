# See: https://forum.omz-software.com/topic/2358/appex-safari-content

import appex, inspect  # noqa


def main():
    if appex.is_running_extension():
        for name_func in inspect.getmembers(appex):
            name, func = name_func
            if name.startswith("get_"):  # find all appex.get_xxx() methods
                print(f"{name.partition('_')[2]:<11} : {func()}")


if __name__ == "__main__":
    main()
