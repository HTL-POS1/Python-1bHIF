# Draw a circle
# 1BHIF | Marc Edlinger | 31.01.2022
from math import floor
rad: int = 4            # radius of the circle
diameter: int = 2*rad + 1
values: list = [["" for x in range(diameter)] for y in range(diameter)]  # fill the array with space strings

for x, s in enumerate(values):
    for y, s1 in enumerate(values):
        if ((x - rad)**2 + y**2 <= rad**2):
            values[x][y] = "x"

for line in values:
    line_spaces = " " 
    for entry in line:
        print(rad*entry, end="")
    print("")
