"""
Marc EDLINGER
1bHIF | 13/03/2022
calculate int sqrt of an integer
"""


def sqrt(n: int) -> int:
    if (n < 0):
        raise ArithmeticError("cannot take square root of negative numbers in R")
    if (n == 0 or n == 1):
        return n

    count: int = 0
    while (count < n):
        if (count**2 > n):
            return count - 1
        count += 1
    return -1


def test(n: int):
    print(n, "|", sqrt(n))


test(0)
test(1)
test(12)
test(16)
test(4)
test(3)
