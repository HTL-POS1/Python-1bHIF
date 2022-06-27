"""
Marc EDLINGER
1bHIF | 27.06.2022
"""

def get_possibilities(x: int, y: int) -> int:
    if (x == 1 or y == 1):
        return 1

    n = 0
    n += get_possibilities(x - 1, y)
    n += get_possibilities(x, y - 1)

    return n


print(get_possibilities(2, 2))
