"""
POS1
Marc EDLINGER
1bHIF

20.01.2022
"""
def get_positive_number(msg: str):
    """ lässt den benutzer eine positive zahl eingeben """
    return get_number(msg, 1)


def get_number(msg: str, min: int) -> int:
    """
    Fordert den User dazu auf, eine positive Zahl, groesser als min einzugeben
    Als Nachricht wird der Parameter msg angezeigt
    """
    value: int = -1
    while (value < min):
        value = int(input(msg))
    return value


def get_positive_number_incl_zero(msg: str, min_value: int = 0) -> int:
    """
    Fordert den User dazu auf, eine positive Zahl, groesser als min einzugeben
    Als Nachricht wird der Parameter msg angezeigt
    """
    return get_number(msg, min(min_value, 0))


def draw_line(length: int, symbole: str):
    """ Zeichnet eine linie mit der länge length und dem Symbol symbole """
    for i in range(length):
        print(symbole, end="")
    print("\n")


def draw_space_line(length: int, symbole: str):
    print(symbole, end="")
    if (length > 1):
        for i in range(length - 2):
            print(" ", end="")
        print(symbole)


def ask_for_layout() -> str:
    """
    Ask the user for an valid rectangle layout. (q, h)
    :return: the first given valid string
    """
    value: str = ""
    while (value != "q" and value != "h"):
        value = input("(q)uer oder (h)och? ")
    return value


def ask_for_style() -> str:
    """
    Ask the user for an valid fill style. (v, h)
    :return: the first given valid string
    """
    value: str = ""
    while (value != "v" and value != "h"):
        value = input("(v)oll oder (h)ohl? ")
    return value


def draw_rectangle(r_length: int, r_width: int, r_layout: str, r_style: str):
    """ Draw a rectangle with the specified properties. """
    if (r_layout == "h"):
        tmp: int = r_length
        r_length = r_width
        r_width = tmp
    if (r_style == "v"):
        for i in range(r_width):
            draw_line(r_length, "*")
    else:
        draw_line(r_length, "*")
        for i in range(r_width - 2):
            draw_space_line(r_length, "*")
        draw_line(r_length, "*")


length: int = get_positive_number("Länge? ")
width: int = get_positive_number_incl_zero("Breite? ", 0)
if (width == 0):    # dreieck
    pass
else:               # rechteck
    layout: str = ask_for_layout()
    style: str = ask_for_style()
    draw_rectangle(length, width, layout, style)
