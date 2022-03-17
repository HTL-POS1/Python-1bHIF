"""
Marc EDLINGER
1bHIF | 17/03/2022
delete elements from array
"""


def delete(target: list, search: int, default: int) -> int:
    """ remove all search from target and put that much default's at the end of the array """
    tmp_list: list = [default] * len(target)
    count: int = 0
    index: int = 0
    for element in target:
        if element != search:
            tmp_list[index] = element
            index += 1
        else:
            count += 1

    for i, e in enumerate(tmp_list):         # copy tmp_list into target
        target[i] = e
    return count


list1: list = [5, 2, 4, 2, 6, 0]
print(delete(list1, 2, -1), list1)                                        # 2 [5, 4, 6, 0, -1, -1]


list2: list = [2, 3, 8, 2, 2, 5, 2, 4, 2, 6, 0]
print(delete(list2, 2, -1), list2)                                        # 5 [3, 8, 5, 4, 6, 0, -1, -1, -1, -1, -1]

