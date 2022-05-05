"""
Marc EDLINGER
1bHIF | 21/04/2022
Flugbahn einer Drohne
"""
from testing import test_function_float

tList: list[float] = [0.0, 12.3, 7.2, 7.9, 6.3, 9.4, 11.9, 8.7, 14.4, 9.1, 11.3]
hList: list[float] = [0.0, 8.71, 14.92, 12.19, 21.94, 25.97, 34.17, 27.85, 12.76, 5.73, 0.0]
radar_height: int = 10
to_high: list[float] = [0.0] * 11


def insert(lst: list[float], value: float, default: float = 0.0) -> int:
    """ fuegt value an der naechsten freien Stelle in lst ein und liefert entweder den Index, wo eingefuegt wurde,
        oder -1 falls es keine freie Stelle mehr gab.
        Die naechste freie Stelle ist jene, wo der erste default Wert vorkommt. """
    index_inserted: int = -1
    index: int = 0
    while (index_inserted == -1 and index < len(lst)):
        if (lst[index] == default):
            lst[index] = value
            index_inserted = index

        index += 1

    return index_inserted


def get_sum(lst: list[float]) -> float:
    """ return the sum of all elements in lst """
    sum: float = 0.0
    for e in lst:
        sum += e
    return sum


def minimale_hoehe(lst: list[float]) -> float:
    return min(lst)


def count_below_radar(lst: list[float], radar: float) -> int:
    return check_radar(lst, to_high, lambda n: n < radar)


def add_Flugeintrag(hoehen: list[float], h: float, zeiten: list[float], z: float) -> int:
    i = insert(hoehen, h)
    if i != -1:
        zeiten[i] = z
    return i


def check_radar(heights: list[float], found: list[float], matcher) -> int:
    """ checks every element of heights, and put it into found, if it is matches the matcher
        returns the amount of elements, bigger than max_height
        matcher has to be a function, with parameters (n) where n the checking element
        return type has to be a boolean
    """
    count: int = 0
    for index, element in enumerate(heights):
        if (matcher(element)):
            found[index] = element
            count += 1
    return count


def max(lst: list[float]) -> float:
    """ return the max value of lst """
    current_max: float = -1
    for e in lst:
        if e > current_max:
            current_max = e
    return current_max


def min(lst: list[float]) -> float:
    """ return the min value of lst """
    current_max: float = None
    for e in lst:
        if current_max is None or e < current_max:
            current_max = e
    return current_max


def get_heigt(time_i: int) -> float:
    """ return the heigt of the drone on a specific time INDEX """
    return hList[time_i]


def printOut(time: list[float], height: list[float]):
    for i in range(len(tList)):
        print(f"{time[i]:5.2f} \t|\t" + ("\033[91m" if height[i] == max(height) else "") + f"{height[i]:5.2f}\033[0m")


test_function_float(max, 34.17, hList)
test_function_float(get_sum, 98.5, tList)
test_function_float(get_sum, 164.23, hList)
