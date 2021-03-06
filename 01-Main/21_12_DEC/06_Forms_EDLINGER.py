# Formen Zeichnen
# 1BHIF | Marc Edlinger | 13.12.2021
from enum import Enum
count: int = 0                      # wie viele Formen hat der Anwender gezeichnet?


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


def ask_for_color(message: str):
    value: str = ""
    # while (value == "" or not Fore[])


def ask_for_bounded_integer(message: str, min_possible: int, max_possible: int = -1):
    value: int = -1
    while ((value < min_possible) or (max_possible != -1 and value > max_possible)):
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


def draw_line(length: int, growing: Growing):
    if (growing == Growing.DESCENDING):         # absteigend
        for i in range(length):
            print(" " * i + "x")
    else:                                       # aufsteigend
        for i in range(length, 0, -1):
            print(" " * i + "x")


# recursive input fetcher function
def start():
    global count
    form: str = ask("Welche Form? (Q)uadrat, (D)reieck, (L)inie, (E)nde: ", ["q", "d", "l", "e"])
    if (form == "e"):
        return
    height: int = ask_for_bounded_integer("Wie hoch (mindestens 4)? ", min_possible=4)
    if (form == "q"):
        filled: bool = True if ask("(V)oll oder (L)eer? ", ["l", "v"]) == "v" else False
        draw_quadrat(height, filled)
    elif (form == "d"):
        growing: Growing = Growing.ASCENDING if ask("(A)ufsteigend oder a(B)steigend? ", ["a", "b"]) == "a" else Growing.DESCENDING
        binding: Binding = Binding.RIGHT if ask("(L)inksbündig oder (R)echtsbündig? ", ["l", "r"]) == "r" else Binding.LEFT
        filled: bool = True if ask("(V)oll oder (L)eer? ", ["l", "v"]) == "v" else False
        draw_triangle(height, filled, growing, binding)
    else:                               # sonst muss der input immer l sein, anhand der obrigen konditionen
        growing: Growing = Growing.ASCENDING if ask("(A)ufsteigend oder a(B)steigend? ", ["a", "b"]) == "a" else Growing.DESCENDING
        draw_line(height, growing)
    count += 1
    start()


start()
print(f"Bye, du hast {count} Figur(en) gezeichnet.")
