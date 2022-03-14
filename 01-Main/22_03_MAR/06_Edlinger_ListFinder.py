"""
Marc EDLINGER
1bHIF | 14/03/2022

"""


def second_highest_number(list: list) -> int:
    current_biggest: int = None
    second_biggest: int = None

    for n in list:
        if current_biggest is None:
            current_biggest = n
            second_biggest = 0
        elif n > current_biggest:
            second_biggest = current_biggest
            current_biggest = n
        elif second_biggest is not None and (current_biggest > n >= second_biggest):
            second_biggest = n

    return second_biggest


print(second_highest_number([3, 5, 8, 2, 7, 10, 0]))
print(second_highest_number([10, 5, 2, 0, -1, 7, 9]))
print(second_highest_number([7, 8, 3, 1]))
print(second_highest_number([-4, -8, -1, -10, -34, -2]))
print(second_highest_number([1, -2, -5, -6]))
