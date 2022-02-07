"""
POS1
Marc EDLINGER
1bHIF

14.01.2022
"""
wrong_inputs: int = 0
calculations: int = 0   # amount of all calculations
area_sum: int = 0
max_length: int = 0
max_width: int = 0

def ask_for_positive_int(msg: str) -> int:
    """
    Ask the user for an positive integer.
    As long as the input value is less than 0, the user has to provide another number.

    :param msg: message for the input dialog
    :return: the first given positive number
    """
    global wrong_inputs

    value: int = -1
    while (value <= 0):
        value = int(input(msg))
        if (value <= 0):
            wrong_inputs += 1
    return value


def ask_for_layout() -> str:
    """
    Ask the user for an valid rectangle layout. (q, h)
    :return: the first given valid string
    """
    global wrong_inputs

    value: str = ""
    while (value != "q" and value != "h"):
        value = input("(q)uer oder (h)och? ")
        if (value != "q" and value != "h"):
            wrong_inputs += 1
    return value


def draw(r_length: int, r_width: int, r_layout: str):
    """
    Draw a rectangle with the specified properties.
    """
    if (r_layout == "h"):
        tmp: int = r_length
        r_length = r_width
        r_width = tmp
    for i in range(r_width):
        s: str = ""
        for j in range(r_length):
            s += "*"
        print(s)


def area(a: int, b: int) -> int:
    """
    Get the area of a rectangle with the side lengths a and b
    """
    return a*b


def ask():
    global max_length, max_width, area_sum, calculations

    length: int = ask_for_positive_int("Länge? ")
    width: int = ask_for_positive_int("Breite? ")
    layout: str = ask_for_layout()

    if (length > max_length):
        max_length = length
    if (width > max_width):
        max_width = width

    draw(length, width, layout)
    reactangle_area: int = area(length, width)
    area_sum += reactangle_area
    calculations += 1
    print("Die Fläche ist " + str(reactangle_area))

    if (input("Noch eine Berechnung (n=Ende)? ") == "n"):
        print("Es gab", calculations, "Berechnungen mit:")
        print("     Gesamtfläche:", area_sum)
        print("     Maximale Länge:", max_length)
        print("     Maximale Breite:", max_width)
        print("     Anzahl der Fehlangaben:", wrong_inputs)
        print("Bye, bye!")
        return
    ask()


ask()
