"""
Marc EDLINGER
1bHIF | 14/03/2022
Quick sort implementation in python
"""


def partition(list: list, start: int, to: int) -> int:
    """ returns the middle index of a list """
    i = start - 1                                           # index of smaller element
    last_element = list[to]                             # last_element

    for j in range(start, to):
        if list[j] <= last_element:
            i += 1
            list[i], list[j] = list[j], list[i]         # switch

    list[i + 1], list[to] = list[to], list[i + 1]       # switch
    return (i + 1)


def quick_sort(list: list, start, to):
    """ quickly sort a list recursively """
    if len(list) == 1:
        return list
    if (start < to):
        middle_index = partition(list, start, to)

        # Separately sort elements before
        # partition and after partition
        quick_sort(list, start, middle_index - 1)
        quick_sort(list, middle_index + 1, to)


arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
