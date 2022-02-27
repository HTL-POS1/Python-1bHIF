# Draw a circle
# 1BHIF | Marc Edlinger | 31.01.2022 - 07.02.2022
rad: int = -1            # radius of the circle
symbole: str = ""
selected_colors: list = []
diameter: int = 0
values: list = []       # coordinate system
colors: dict = {
    "rot": "\u001b[31m",
    "grün": "\u001b[32m",
    "gelb": "\u001b[33m",
    "blau": "\u001b[34m",
    "lila": "\u001b[35m",
    "e": ""
}


def ask(message: str, valid_options: list) -> str:
    value: str = input(message)
    while (value == "" or not valid_options.__contains__(value)):
        value = input(message)
    return value


def ask_int(message: str, min: int, max: int) -> int:
    value: int = 0
    while (value == 0 or value < min or value > max):
        value = int(input(message))
    return value


def count(l: list, search: str) -> int:
    """ returns the occurence of a string in a string list """
    count: int = 0
    for s in l:
        if s == search:
            count += 1
    return count

def calculate():
    for x, s in enumerate(values):
        for y, s1 in enumerate(values):
            if ((x - rad)**2 + (y - rad)**2 - rad <= rad**2):
                values[x][y] = symbole

def draw():
    color_index: int = 0
    for line in values:
        spaces: int = count(line, " ")
        line_string: str = ""
        for entry in line:
            if (entry != " "):
                line_string += selected_colors[color_index] + 2 * entry
                if (color_index == len(selected_colors) - 1):
                    color_index = 0
                else:
                    color_index += 1
            else:
                line_string += entry
        print(" " * (spaces // 2) + line_string)

while rad != 0:
    rad = ask_int("Radius? (1-10)", 1, 10)
    color: str = "asd"
    while color != "":
        color = colors[ask("Farbe? (rot, grün, gelb, blau, lila, e=ende)", colors.keys())]
        if (color != ""):
            selected_colors.append(color)
    symbole = ask("Symbol? (x, s, #, $)", ["x", "s", "#", "$"])
    diameter = 2*rad + 1
    values = [[" " for x in range(diameter)] for y in range(diameter)]  # fill the array with space strings
    calculate()
    draw()
