"""
Send a stream of pitch, yaw, roll values to other devices on a multipeer network.
Uses Pythonista's motion.get_attitude() to get data and @mikaelho's multipeer to send.
Install multipeer on two iOS devices and run this code on one and multipeer.py on the
other.  You should see a stream of attitude data which change as the device is moved.

TODO (cclauss): Upgrade to multipeer streams in latency becomes an issue.

https://forum.omz-software.com/topic/6140/interactive-animation-based-on-orientation-data-of-imu
http://omz-software.com/pythonista/docs/ios/motion.html
https://github.com/mikaelho/multipeer
"""

import motion, multipeer, platform

mc = multipeer.MultipeerConnectivity(display_name=platform.node(), service_type="chat")
motion.start_updates()
try:
    while True:
        mc.send(motion.get_attitude())
finally:
    mc.end_all()
    motion.stop_updates()
