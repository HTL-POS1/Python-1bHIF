"""
Marc EDLINGER
1bHIF | 08/03/2022

"""
from random import seed, randint
seed()


def init_list(size: int, default: int) -> list:
    """
    Returns a list with "size" elements of "default"
    """
    return [default] * size


def get_random_number(max: int) -> int:
    """ returns a random number between 0 and max """
    return randint(0, max)


def init_random_list(size: int) -> list:
    """ Returns a list with "size" random elemens """
    list = init_list(size, 0)
    for i in range(size):
        list[i] = get_random_number(1000)
    return list


def get_sum(numbers: list) -> int:
    """ returns the sum of all elements in numbers """
    sum: int = 0        # counting sum
    for i in numbers:
        sum += i
    return sum


def get_avg(numbers: list) -> float:
    """ returns the average value of all elements in numbers """
    return (get_sum(numbers) / len(numbers))


def get_max(numbers: list) -> int:
    """ returns the max value of numbers """
    current_max = 0
    for n in numbers:
        if n > current_max:
            current_max = n
    return current_max


def get_first_pos(numbers: list, x: int):
    """ returns the first index, the x value appeares in numbers """
    for i, n in enumerate(numbers):
        if n == x:
            return i
    return -1


def get_last_pos(numbers: list, x: int):
    """ returns the first index, the x value appeares in numbers """
    last_index = -1
    for i, n in enumerate(numbers):
        if n == x:
            last_index = i
    return last_index


list1 = init_list(5, -1)
list2 = init_list(10, 0)
print("L1", list1)
print("L2", list2)

random_list = init_random_list(10)
print("Random", random_list)
print("Sum", get_sum(random_list))
print("Avg", get_avg(random_list))
print("Max", get_max(random_list))
search = int(input("Welchen Wert willst du suchen? "))
print("First", get_first_pos(random_list, search))
print("Last", get_last_pos(random_list, search))
