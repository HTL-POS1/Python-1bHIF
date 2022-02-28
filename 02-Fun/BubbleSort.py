def is_sorted(to_check: list) -> bool:
    for i in range(len(to_check) - 1):
        if (to_check[i] > to_check[i + 1]):
            return False
    return True


def sort(to_sort: list) -> list:
    """ Sorts an provided list, and return it back """
    if is_sorted(to_sort):
        return to_sort
    first_element = to_sort[0]
    for i, element in enumerate(to_sort):
        if element < first_element:
            to_sort[0] = to_sort[i]
            to_sort[i] = first_element
    return sort(to_sort)


test_1: list = [5, 7, 2, 8]    # expected output: [2, 4, 7, 8]
print(sort(test_1))
