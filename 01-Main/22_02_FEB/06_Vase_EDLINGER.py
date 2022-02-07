# Formen Zeichnen
# 1BHIF | Marc Edlinger | 03.02.2022
from enum import Enum
count: int = 0                      # wie viele Formen hat der Anwender gezeichnet?
colors: dict = {
    "rot": "\u001b[31m",
    "grün": "\u001b[32m",
    "gelb": "\u001b[33m",
    "blau": "\u001b[34m",
    "lila": "\u001b[35m"
}


class Growing(Enum):
    ASCENDING = "a",
    DESCENDING = "b"


class Binding(Enum):
    LEFT = "l",
    RIGHT = "r"


def ask(message: str, valid_options: list):
    value: str = ""
    while (value == "" or not valid_options.__contains__(value)):
        value = input(message)
    return value


def ask_for_bounded_integer(message: str, min_possible: int, max_possible: int = -1):
    value: int = -1
    while ((value < min_possible) or (max_possible != -1 and value > max_possible)):
        value = int(input(message))
    return value


def draw_triangle(height: int, filled: bool, growing: Growing, binded: Binding):
    if (growing == Growing.ASCENDING):                  # aufsteigend
        if (binded == Binding.RIGHT):                   # rechtsbündig
            if (filled):                                # gefüllt
                for i in range(height):
                    print(" " * (height - i - 1) + "x" * (i + 1), "-", i)
            else:                                       # nicht gefüllt
                print(" " * (height - 1) + "x")
                print(" " * (height - 2) + "xx")
                for i in range(3, height):
                    print(" " * (height - i) + "x" + (i - 2) * " " + "x")
                if (height != 2):
                    print("x" * height)
        else:                                           # linksbündig
            if (filled):
                for i in range(height, 0, -1):
                    print(" " * (height - i) + "x" * i)
            else:
                print(height * "x")
                for i in range(height, 3, -1):
                    print(" " * (height - i) + "x" + " " * (i - 2) + "x")
                print((height - 2) * " " + "xx")
                print((height - 1) * " " + "x")
    else:                                               # absteigend
        if (binded == Binding.RIGHT):                   # rechtsbündig
            if (filled):
                for i in range(height + 1):
                    print("x" * i)
            else:
                print("x")
                print("xx")
                for i in range(3, height):
                    print("x" + " " * (i - 1) + "x")
                print("x" * height)
        else:                                           # linksbündig
            if (filled):
                for i in range(height, 0, -1):
                    print("x" * i)
            else:
                print("x" * height)
                for i in range(height, 2, -1):
                    print("x" + " " * (i - 2) + "x")
                print("xx")
                print("x")


def build_string(i: int, s: str) -> str:
    tmp: str = ""
    for k in range(i):
        tmp += s
    return tmp


def draw_rhombus(height: int, filled: bool):
    pass


def draw_vase(height: int, symbole: str, border: str) -> int:
    """ print a vase on the terminal and returns the area"""
    j: int = 0          # counter
    area: int = 0
    for i in range(height, -1, -2):
        symboles: str = build_string(i, symbole)
        display: str = border + symboles + border + symboles + border
        area += len(display)
        print(build_string(2*j, " ") + display)
        j += 1

    for i in range(height):
        symboles: str = build_string((i + 1), symbole)
        display: str = border + symboles + border + symboles + border
        for k in range(2):
            area += len(display)
            print(build_string(height - i - 1, " ") + display)

    print(build_string(2*height+3, border))
    return area

def start():
    global count
    form: str = ask("Welche Form? (R)aute, (D)reieck, (L)inie, (V)ase (E)nde: ", ["r", "d", "l", "v", "e"])
    if (form == "e"):
        return
    height: int = ask_for_bounded_integer("Wie hoch (mindestens 4)? ", min_possible=4)
    if (form == "r"):
        filled: bool = True if ask("(V)oll oder (L)eer? ", ["l", "v"]) == "v" else False
        draw_rhombus(height, filled)
    elif (form == "v"):
        symbole: str = ask("Mit welchem Zeichen (x oder s)?", ["x", "s"])
        border: str = ask("Mit welchem Rand ($ oder #)?", ["$", "#"])

        primary_color: str = colors[ask("Primärfarbe? " + str(colors.keys()), list(colors.keys()))]
        secondary_color: str = colors[ask("Sekundärfarbe? " + str(colors.keys()), list(colors.keys()))]
        print(f"Flächeninhalt: {draw_vase(height, primary_color + symbole, secondary_color + border)}")
    else:                       # muss d sein
        growing: Growing = Growing.ASCENDING if ask("(A)ufsteigend oder a(B)steigend? ", ["a", "b"]) == "a" else Growing.DESCENDING
        binding: Binding = Binding.RIGHT if ask("(L)inksbündig oder (R)echtsbündig? ", ["l", "r"]) == "r" else Binding.LEFT
        filled: bool = True if ask("(V)oll oder (L)eer? ", ["l", "v"]) == "v" else False
        draw_triangle(height, filled, growing, binding)
    count += 1
    start()


start()
print(f"Bye, du hast {count} Figur(en) gezeichnet.")
