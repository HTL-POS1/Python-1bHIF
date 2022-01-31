# Draw a circle
# 1BHIF | Marc Edlinger | 31.01.2022
size: int = 15
rad: int = 6
values: list = [["" for x in range(size)] for y in range(size)]  # fill the array with space strings

for y in range(size):  # put valid y,x values in the map
    for x in range(size):
        if ((x - rad) ** 2 + (y - rad) ** 2 <= rad ** 2 - 1):
            values[y][x] = "*"

for line in values:
    print(" ".join(line))
