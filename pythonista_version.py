# Output: Pythonista version 1.6 (160037) on iOS 9.2 on an iPad3,4.
# built on https://forum.omz-software.com/topic/2444/determining-pythonista-s-version/3

def pythonista_version():
    import os, sys, plistlib
    plist = plistlib.readPlist(os.path.abspath(os.path.join(sys.executable, '../Info.plist')))
    return '{CFBundleShortVersionString} ({CFBundleVersion})'.format(**plist)

mac_ver = platform.mac_ver()
fmt = 'Pythonista version {} on iOS {} on an {}.'
print(fmt.format(pythonista_version(), mac_ver[0], mac_ver[2]))
