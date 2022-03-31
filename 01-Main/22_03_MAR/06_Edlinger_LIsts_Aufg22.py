"""
Marc EDLINGER
1bHIF | 17/03/2022
delete elements from array
"""


def delete(target: list, search: int, default: int) -> int:
    """ remove all search from target and put that much default's at the end of the array """
    count: int = 0
    for index, element in enumerate(target):
        if (element == search):
            for j in range(index, len(target) - 1, 1):
                target[j] = target[j + 1]
            target[len(target) - 1] = default
            count += 1

    if (search in target):
        count += delete(target, search, default)

    return count


list1: list = [5, 2, 4, 2, 6, 0]
print(delete(list1, 2, -1), list1)                                        # 2 [5, 4, 6, 0, -1, -1]


list2: list = [2, 3, 8, 2, 2, 2, 2, 4, 2, 6, 0]                           # 6 [3, 8, 4, 6, 0, -1, -1, -1, -1, -1, -1]
print(delete(list2, 2, -1), list2)


list3: list = [2, 3, 8, 2, 2, 2, 2, 4, 2, 6, 0]
print(delete(list3, 7, -1), list3)                                        # 0 [2, 3, 8, 2, 2, 2, 2, 4, 2, 6, 0]



list3: list = []
print(delete(list3, 2, -1), list3)                                        # 0 []

