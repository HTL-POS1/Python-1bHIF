"""
Marc EDLINGER
1bHIF | 21/04/2022
Flugbahn einer Drohne
"""
from testing import test_function_float
from time import sleep

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


def build_empty_string(length: int) -> str:
    s: str = ""
    for i in range(length):
        s += " "
    return s


def let_drone_fly(times: list[float], heights: list[float], radar: int):
    i: int = 0
    while i < len(times) and times[i] != -1:
        current_height: int = round(heights[i])
        current_string: str = build_empty_string(current_height) + "*"

        if current_height < radar:
            additional_zeros: int = radar_height - current_height - 1
            current_string += build_empty_string(additional_zeros) + "\u001b[32m|\033[0m"
        else:
            str_list: list = list(current_string)
            str_list[radar_height] = "\u001b[31m|\033[0m"
            current_string = "".join(str_list)

        sleep(times[i] // 5)

        print(current_string, current_height)
        i += 1


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


def delete(target: list, index: int, default: int) -> int:
    """ remove all search from target and put that much default's at the end of the array """
    count: int = 0
    i = 0
    while index != i:
        i += 1

    for j in range(index, len(target) - 1, 1):
        target[j] = target[j + 1]
    target[len(target) - 1] = default
    count += 1

    if (target[index] != default):
        count += delete(target, index, default)

    return count


def rm_Flugeintrag(hoehen: list[float], zeiten: list[float], n: int) -> int:
    """löscht de n Flugeintrag an der Stelle n in den beiden Listen Flughöhen
    hoehen und Flugzeiten zeiten und liefert die gelöschte Position in beiden
    Listen, oder -1 falls es nicht geklappt hat. Alle Höhen und Zeiten hinter
    dieser Position n werden um eine Stelle nach vor verschoben. An die letzt
     en Stellen kommt jeweils der default value -1.0. """
    result: int = -1
    if 0 < n < len(hoehen):
        result = delete(hoehen, n, -1)
        delete(zeiten, n, -1)
    return result


def get_heigt(time_i: int) -> float:
    """ return the heigt of the drone on a specific time INDEX """
    return hList[time_i]


def printOut(time: list[float], height: list[float]):
    for i in range(len(tList)):
        print(f"{time[i]:5.2f} \t|\t" + ("\033[91m" if height[i] == max(height) else "") + f"{height[i]:5.2f}\033[0m")


test_function_float(max, 34.17, hList)
test_function_float(get_sum, 98.5, tList)
test_function_float(get_sum, 164.23, hList)
let_drone_fly(tList, hList, radar_height)
