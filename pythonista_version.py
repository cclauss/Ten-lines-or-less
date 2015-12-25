# Output: Pythonista version 1.6 (160037) on iOS 9.2 on an iPad3,4.
#         Pythonista version 1.6 (160037) on iOS 9.2 on an iPad5,4.
# built on https://forum.omz-software.com/topic/2444/determining-pythonista-s-version/3

import os, platform, plistlib, sys

def pythonista_version():
    plist = plistlib.readPlist(os.path.abspath(os.path.join(sys.executable, '..', 'Info.plist')))
    return '{CFBundleShortVersionString} ({CFBundleVersion})'.format(**plist)

fmt = 'Pythonista version {0} on iOS {1} on an {3}.'
print(fmt.format(pythonista_version(), *platform.mac_ver()))
