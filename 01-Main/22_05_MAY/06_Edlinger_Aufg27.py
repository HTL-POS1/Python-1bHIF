"""
Marc EDLINGER
1bHIF | 01/05/2022
Insert element into list
"""
from testing import test_list_function

def insert(lst: list[float], value: float, default: float = 0.0) -> int:
    """ fuegt value an der naechsten freien Stelle in lst ein und liefert entweder den Index, wo eingefuegt wurde,
        oder -1 falls es keine freie Stelle mehr gab.
        Die naechste freie Stelle ist jene, wo der erste default Wert vorkommt. """
    state: int = -1
    index: int = 0
    while state == -1 and index < len(lst):
        if (lst[index] == default):
            lst[index] = value
            state = index

        index += 1
    return state


test1: list[int] = [1, 6, 0, 8, 9, 2, 10, 0]
test_list_function(insert, test1, [1, 6, 7, 8, 9, 2, 10, 0], 2, 7)
test_list_function(insert, test1, [1, 6, 7, 8, 9, 2, 10, 5], 7, 5)
test_list_function(insert, test1, test1, -1, 5)
test_list_function(insert, [], [], -1, 4)
