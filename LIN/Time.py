"""
POS1
Marc EDLINGER
1bHIF

14.01.2022
"""
def validate(x: int, max_value: int) -> bool:
    f"""
    :param x: the number you want to validate 
    :param max_value: the max possible value for {x}
    :return: wheater the value is valid or not
    """
    if (x > max_value):
        return False
    return True


def get_delta_seconds(hours: int, mins: int, secs: int) -> int:
    f"""
    :return the time from {hours}:{mins}:{secs} since 00:00:00 in seconds
    """
    if not (validate(hours, 23) or not validate(mins, 60) or not validate(secs, 60)):
        return -1   # exception value
    return (hours * 3600) + (mins * 60) + secs


print(get_delta_seconds(15, 20, 0))
print(get_delta_seconds(23, 78, 5))
print(get_delta_seconds(8, 2, 21))
