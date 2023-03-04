import inspect
import platform

for name, value in inspect.getmembers(platform):
    if name[0] != "_" and callable(value):
        try:
            value = value()
        except (OSError, TypeError):
            continue
        if str(value).strip("(),' "):
            print(f"{name:>21}() = {value}")

print("=" * 40)

# ==== Update...
info = {}
for name, func in inspect.getmembers(platform):
    try:
        if name[0] != "_":
            info[name] = str(func() or "").strip("(),' ")
    except (OSError, TypeError):
        pass
print("\n".join(f"{name:>21}() = {value}" for name, value in info.items() if value))


# import sys
# print(sys.platform, sys.version)

"""
         architecture() = 64bit
              mac_ver() = 13.1', ('', '', ''), 'arm64
              machine() = arm64
                 node() = christians-m1-macbook-pro.home
             platform() = macOS-13.1-arm64-arm-64bit
            processor() = arm
         python_build() = main', 'Dec 23 2022 09:28:24
      python_compiler() = Clang 14.0.0 (clang-1400.0.29.202
python_implementation() = CPython
       python_version() = 3.11.1
 python_version_tuple() = 3', '11', '1
              release() = 22.2.0
               system() = Darwin
                uname() = uname_result(
                              system='Darwin',
                              node='christians-m1-macbook-pro.home',
                              release='22.2.0',
                              version=(
                           'Darwin Kernel Version 22.2.0: Fri Nov 11 02:04:44 PST 2022;'
                           'root:xnu-8792.61.2~4/RELEASE_ARM64_T8103'
                              ),
                              machine='arm64
                          )
              version() = Darwin Kernel Version 22.2.0: Fri Nov 11 02:04:44 PST 2022;
                          root:xnu-8792.61.2~4/RELEASE_ARM64_T8103

ios 3.6.1 (default, Aug 24 2017, 16:20:00)
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)]
"""
