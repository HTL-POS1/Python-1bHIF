"""
Marc EDLINGER
1bHIF | 31/03/2022
"""
from math import floor, sqrt


def remove_non_primes(numbers: list):
    list_length: int = len(numbers)
    for to_test in range(2, floor(sqrt(list_length)) + 1, 1):
        for i, n in enumerate(numbers):
            if (i > 1):
                if (n % to_test == 0):
                    numbers[i] = -1


def print_list(numbers: list):
    for n in numbers:
        if (n != -1):
            print(n, end=", ")


l = list(range(10000))
remove_non_primes(l)
print_list(l)
