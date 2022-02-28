# Listen
# 1bHIF | Marc EDLINGER | 28.02.2022

default_value: int = -1
default_list = [-1 for i in range(10)]


def ask_for_valid_index(list: list) -> int:
    i: int = -1
    while (i < 0 or i > len(list) - 1):
        i = int(input(f"Gib mir einen validen listen-index! Max: {len(list) - 1}! "))
    return i


def ask_for_positive_int() -> int:
    i: int = -1
    while (i < 0):
        i = int(input(f"Gib mir eine positive Zahl! "))
    return i


def different_values(list: list) -> int:
    """ Retrun the amount of different values of an integer list """
    values: list = []
    for i in list:
        if i not in values:
            values.append(i)
    return len(values)


def check_list(list: list) -> bool:
    """ Check if every element in the list is not equal to the default value """
    global default_value

    for i in list:
        if i == default_value:
            return False
    return True


while not check_list(default_list):
    index: int = ask_for_valid_index(default_list)
    value: int = ask_for_positive_int()
    default_list[index] = value
    print(default_list)
