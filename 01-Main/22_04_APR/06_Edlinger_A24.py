"""
Marc EDLINGER
1bHIF | 07/04/2022
Insert element into array
"""
from testing import test_list_function


def insert(lst: list, index: int, element: int) -> int:
    """ replace the element on index with the element and fall back the other elements """
    if (index < 0 or index >= len(lst)):
        return -1

    for i in range(len(lst) - 1, index, -1):
        lst[i] = lst[i - 1]

    lst[index] = element
    return index


def insert2(lst: list, index: int, element: int) -> int:
    """ replace the element on index with the element and fall back the other elements """
    erg = -1
    if (0 < index < len(lst)):
        for i in range(len(lst) - 1, index, -1):
            lst[i] = lst[i - 1]

        lst[index] = element
        erg = index
    return erg


print("--- TESTING insert ---")
test_list_function(insert, [1, 2, 3, 4, 5], [1, 2, 7, 3, 4], 2, 2, 7)
test_list_function(insert, [1, 2, 3, 4, 5], [8, 1, 2, 3, 4], 0, 0, 8)
test_list_function(insert, [1, 2, 3, 4, 5], [1, 2, 3, 4, 9], 4, 4, 9)
test_list_function(insert, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], -1, 2133, 7)
test_list_function(insert, [], [], -1, 2, 7)
print("All tests completed")
