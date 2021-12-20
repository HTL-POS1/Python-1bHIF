# Formen Zeichnen
# 1BHIF | Marc Edlinger | 13.12.2021
def ask(message: str, valid_options: list):
    value: str = ""
    while (value == "" or not valid_options.contains(value)):
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
    pass


def start():
    form: str = ask("Welche Form? (Q)uadrat, (D)reieck, (L)inie, (E)nde: ", list("q", "d", "l", "e"))
    height: int = ask_for_positive_integer("Wie hoch? ")
    filled: bool = ask("Gefüllt? (L)eer, (G)efüllt", list("l", "g"))
    if (form == "q"):
        draw_quadrat(height, filled)


start()