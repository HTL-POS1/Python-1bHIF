"""
Marc EDLINGER
1bHIF | 21/04/2022
Flugbahn einer Drohne
"""
from testing import test_function_float

tList: list[float] = [0.0, 12.3, 7.2, 7.9, 6.3, 9.4, 11.9, 8.7, 14.4, 9.1, 11.3]
hList: list[float] = [0.0, 8.71, 14.92, 12.19, 21.94, 25.97, 34.17, 27.85, 12.76, 5.73, 0.0]

def get_sum(lst: list[float]) -> float:
    """ return the sum of all elements in lst """
    sum: float = 0.0
    for e in lst:
        sum += e
    return sum


def max(lst: list[float]) -> float:
    """ return the max value of lst """
    current_max: float = -1
    for e in lst:
        if e > current_max:
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
