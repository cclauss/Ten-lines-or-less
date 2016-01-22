# Output: Pythonista version 1.6 (160037) on iOS 9.2 on an iPad3,4.
#         Pythonista version 2.0.1 (201000) on iOS 9.2.1 on an iPad5,4 with a screen size of 1024 x 768.
# built on https://forum.omz-software.com/topic/2444/determining-pythonista-s-version/3

import os, platform, plistlib, sys, ui

def pythonista_version():
    plist = plistlib.readPlist(os.path.abspath(os.path.join(sys.executable, '..', 'Info.plist')))
    return '{CFBundleShortVersionString} ({CFBundleVersion})'.format(**plist)

ios_ver, _, machine_model = platform.mac_ver()
fmt = 'Pythonista version {} on iOS {} on an {} with a screen size of {:.0f} x {:.0f}.'
print(fmt.format(pythonista_version(), ios_ver, machine_model, *ui.get_screen_size()))
