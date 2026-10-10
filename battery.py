BATTERY_CAPACITY_WH = 100  # battery size in watt-hours


def runtime_hours(battery_percent, power_draw_w):
    """How many hours the robot can run on its remaining battery."""
    energy_left_wh = BATTERY_CAPACITY_WH * battery_percent / 100
    return energy_left_wh / power_draw_w


if __name__ == "__main__":
    percent = float(input("Battery %: "))
    power = float(input("Power draw (W): "))
    print(f"Runtime: {runtime_hours(percent, power):.1f} hours")