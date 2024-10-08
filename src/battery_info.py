import collections, objc_util  # noqa

battery_info = collections.namedtuple("battery_info", "level state")
battery_states = "unknown unplugged charging full".split()


def get_battery_info():
    device = objc_util.ObjCClass("UIDevice").currentDevice()
    device.setBatteryMonitoringEnabled_(True)
    try:
        return battery_info(
            int(device.batteryLevel() * 100),
            battery_states[device.batteryState()],
        )
    finally:
        device.setBatteryMonitoringEnabled_(False)


def battery_is_low(threshold=20):
    battery_info = get_battery_info()
    return battery_info.level <= threshold and battery_info.state.startswith("un")


if __name__ == "__main__":
    print(get_battery_info())  # battery_info(level=64, state='unplugged')
    print(battery_is_low(15))  # False
