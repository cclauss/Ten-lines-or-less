# Output: Pythonista version 1.6 (160037) on iOS 9.2 on an iPad3,4.
# Pythonista version 2.0.1 (201000) on iOS 9.2.1 on a 64-bit iPad5,4 with a
#    screen size of (1024 x 768) * 2
# Pythonista version 3.0 (300007) running Python 3.5.1 on iOS 9.3.1 on a 64-bit
#    iPad5,4 with a screen size of (1024 x 768) * 2
# Pythonista version 3.0 (300007) running Python 2.7.5 on iOS 9.3.1 on a 64-bit
#    iPad5,4 with a screen size of (1024 x 768) * 2
# Pythonista version 3.1 (301016) running Python 3.5.1 on iOS 10.2.1 on a 64-bit
#    iPad5,4 with a screen size of (1024 x 768) * 2
# Pythonista version 3.4 (340006) running Python 3.10.4 on iOS 16.3 on a 64-bit
#    iPad8,6 with a screen size of (2560 x 1440) * 1  # This is an M1 Mac!!!

#
# built on:
# https://forum.omz-software.com/topic/2444/determining-pythonista-s-version/3

import os, platform, plistlib, scene, sys  # noqa


def pythonista_version_info():  # ('3', '4')
    info_plist = (Path(sys.executable).parent / "Info.plist").read_bytes()
    return tuple(plistlib.loads(info_plist)["CFBundleShortVersionString"].split("."))


def pythonista_version():  # 2.0.1 (201000) or 3.4 (340006)
    with open(
        os.path.abspath(os.path.join(sys.executable, "..", "Info.plist")),
        "rb",
    ) as in_file:
        return "{CFBundleShortVersionString} ({CFBundleVersion})".format(
            **plistlib.load(in_file),
        )


ios_ver, _, machine_model = platform.mac_ver()
bit = platform.architecture()[0].rstrip("bit") + "-bit"
rez = "({:.0f} x {:.0f})".format(*scene.get_screen_size())
fmt = (
    "Pythonista version {} running Python {} on iOS {} on a {} {} with a "
    "screen size of {} * {:.0f}"
)
print(
    fmt.format(
        pythonista_version(),
        platform.python_version(),
        ios_ver,
        bit,
        machine_model,
        rez,
        scene.get_screen_scale(),
    ),
)
