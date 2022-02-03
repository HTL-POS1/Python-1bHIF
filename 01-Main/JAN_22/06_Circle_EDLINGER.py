# Draw a circle
# 1BHIF | Marc Edlinger | 31.01.2022
rad: int = 4            # radius of the circle
diameter: int = 2*rad
values: list = [["" for x in range(diameter)] for y in range(diameter)]  # fill the array with space strings

for y in range(diameter):  # put valid y,x values in the map
    for x in range(diameter):
        if ((y - rad)**2 + (x - rad)**2 <= rad**2 - 1):
            values[y][x] = "x"

for line in values:
    print(" ".join(line))
