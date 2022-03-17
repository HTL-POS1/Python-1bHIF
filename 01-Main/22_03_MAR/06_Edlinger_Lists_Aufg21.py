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


if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [1, 4, 5]
    list3 = [0, 4, 5]
    list4 = [1, 2, 3, 4]
    list5 = [0, 0, 0, 0]
    list6 = []

    print(count(list1, 2), count(list5, 0), count(list6, 3))  # -> 1 4 0
    copy(list1, list5)
    copy(list2, list6)
    print(list5, list6)  # -> [1, 2, 3, 0] []
    print(compare(list1, list2), compare(list2, list4), compare(list4, list5))  # -> 1 1 3
