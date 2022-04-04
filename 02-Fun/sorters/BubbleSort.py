from random import seed, randrange
seed()


def bubble_sort(to_sort: list, predicate) -> list:
    """
    Sorts a provided list recursively, and return it back.
    The predicate parameter has to be an function, which takes two integer-parameters and return that number,
    that should be at the lower index part.

    example: @compare_gt
    """
    had_to_sort: bool = False
    for index, element in enumerate(to_sort):
        if index == len(to_sort) - 1:                            # abbrechen wenn beim letzten Element
            break
        next_element = to_sort[index + 1]                        # musste im aktuellen durchlauf eine Vertrauschung durchgeführt werden?
        if (predicate(element, next_element) == next_element):   # dann tauschen
            to_sort[index] = next_element
            to_sort[index + 1] = element
            if not had_to_sort:
                had_to_sort = True

    if had_to_sort:                     # wenn etwas getauscht werden musste, noch einmal duchlaufen
        return sort(to_sort, predicate)
    return to_sort


def is_reversed_list(list1: list, list2: list) -> bool:
    """
    check if one list is the reversed list of the other object
    """
    if len(list1) != len(list2):
        return False
    for index, element in enumerate(list1):
        if (element != list2[-index]):
            return False
    return True


def generate_int_list(capicity: int) -> list:
    """
    generate and return a list with random elements
    """
    return [randrange(1, 1000) for _ in range(capicity)]


def compare_gt(first: int, second: int) -> int:
    return first if first > second else second


def compare_st(first: int, second: int) -> int:
    return first if first < second else second


if __name__ == "__main__":
    test_1 = generate_int_list(10)

    sorted_st = sort(test_1, compare_gt)
    print(sorted_st)
