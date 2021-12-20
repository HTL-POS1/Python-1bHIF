# Formen Zeichnen
# 1BHIF | Marc Edlinger | 13.12.2021
from enum import Enum
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


def ask_for_positive_integer(message: str):
    value: int = -1
    while (value <= 0):
        value = int(input(message))
    return value   


def draw_quadrat(height: int, filled: bool):
    full_line: str = "*" * height
    empty_line: str = "*" + (" " * (height - 2)) + "*"
    print(full_line)
    for i in range(height - 2):
        if (filled):
            print(full_line)
        else:
            print(empty_line)
    print(full_line)


def draw_triangle(height: int, filled: bool, growing: Growing, binded: Binding):
    if (growing == Growing.ASCENDING):                  # aufsteigend
        if (binded == Binding.RIGHT):                   # rechtsbündig
            if (filled):                                # gefüllt
                for i in range(height + 1):
                    print(" " * (height - i) + "x" * (i + 1))
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


def start():
    form: str = ask("Welche Form? (Q)uadrat, (D)reieck, (L)inie, (E)nde: ", ["q", "d", "l", "e"])
    height: int = ask_for_positive_integer("Wie hoch? ")
    filled: bool = True if ask("(V)oll oder (L)eer? ", ["l", "v"]) == "v" else False
    if (form == "q"):
        draw_quadrat(height, filled)
    elif (form == "d"):
        growing: Growing = Growing.ASCENDING if ask("(A)ufsteigend oder a(B)steigend? ", ["a", "b"]) == "a" else Growing.DESCENDING
        binding: Binding = Binding.RIGHT if ask("(L)inksbündig oder (R)echtsbündig? ", ["l", "r"]) == "r" else Binding.LEFT
        draw_triangle(height, filled, growing, binding)
    start()


start()
