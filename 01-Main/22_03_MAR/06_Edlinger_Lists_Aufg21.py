"""
Marc EDLINGER
1bHIF | 14/03/2022
Listen und Funktionen in Python
"""


def count(numbers: list, n: int) -> int:
    """ liefert die Anzahl, wie oft n in der liste numbers vorkommt"""
    count: int = 0
    for i in numbers:
        if (i == n):
            count += 1
    return count


def copy(source: list, target: list) -> int:
    """ kopiert die Werte aus source nach target und liefert die Anzahl kopierter Werte """
    length: int = min(len(source), len(target))
    for i in range(length):
        target[i] = source[i]
    return length


def compare(first: list, second: list) -> int:
    """ liefert die Anzahl gleicher Werte in beiden Listen """
    same: int = 0
    length: int = min(len(first), len(second))
    for i in range(length):
        if (first[i] == second[i]):
            same += 1
    return same
