import inspect
import platform

for name, value in inspect.getmembers(platform):
    if name[0] != "_" and callable(value):
        try:
            value = value()
        except (IndexError, TypeError):
            continue
        if str(value).strip("(),' "):
            print("{:>21}() = {}".format(name, value))

# ==== Update...
info = {}
for name, func in inspect.getmembers(platform):
    try:
        if name[0] != "_":
            info[name] = str(func() or "").strip("(),' ")
    except (FileNotFoundError, TypeError):
        continue
print("\n".join(f"{name:>21}() = {value}" for name, value in info.items() if value))

# import sys
# print(sys.platform, sys.version)

"""
         architecture() = ('64bit', '')
              mac_ver() = ('11.0.3', ('', '', ''), 'iPad5,4')
              machine() = iPad5,4
                 node() = CCC-iPad
             platform() = Darwin-17.0.0-iPad5,4-64bit
         python_build() = ('default', 'Aug 24 2017 16:20:00')
      python_compiler() = GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)
python_implementation() = CPython
       python_version() = 3.6.1
 python_version_tuple() = ('3', '6', '1')
              release() = 17.0.0
               system() = Darwin
                uname() = uname_result(system='Darwin', node='CCC-iPad',
                                       release='17.0.0',
                                       version='Darwin Kernel Version 17.0.0: '
                                               'Fri Sep  1 14:59:13 PDT 2017; '
                                               'root:xnu-4570.2.5~167/'
                                               'RELEASE_ARM64_T7001',
                                       machine='iPad5,4', processor='')
              version() = ('Darwin Kernel Version 17.0.0: '
                           'Fri Sep  1 14:59:13 PDT 2017; '
                           'root:xnu-4570.2.5~167/RELEASE_ARM64_T7001')

ios 3.6.1 (default, Aug 24 2017, 16:20:00)
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)]
"""
