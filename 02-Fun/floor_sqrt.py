"""
Marc EDLINGER
1bHIF | 13/03/2022
calculate int sqrt of an integer
"""


def sqrt(n: int) -> complex:
    if (n < 0):
        return complex(0, sqrt(n * -1).imag)
    if (n == -1):
        return complex(0, 1)
    if (n == 0 or n == 1):
        return n

    count: int = 0
    while (count < n):
        if (count**2 > n):
            return complex(0, count - 1)
        count += 1
    return -1


while True:
    i: int = int(input("Zahl: "))
    print(i, "|", sqrt(i))
