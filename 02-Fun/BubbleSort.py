def sort(to_sort: list, predicate) -> list:
    """
    Sorts a provided list, and return it back.
    The predicate parameter has to be an function, which takes two integer-parameters and return that number,
    that should be at the lower index part.

    example: @compare_gt
    """
    had_to_sort: bool = False
    for index, element in enumerate(to_sort):
        if index == len(to_sort) - 1:
            break
        next_element = to_sort[index + 1]
        if (predicate(element, next_element) == next_element):          # dann tauschen
            to_sort[index] = next_element
            to_sort[index + 1] = element
            if not had_to_sort:
                had_to_sort = True

    if had_to_sort:
        return sort(to_sort, predicate)
    return to_sort


def compare_gt(first: int, second: int) -> int:
    return first if first > second else second


def compare_st(first: int, second: int) -> int:
    return first if first < second else second


test_1: list = [5, 7, 2, 8]    # expected output: [2, 4, 7, 8]
print(sort(test_1, compare_gt))
print(sort(test_1, compare_st))
