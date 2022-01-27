BASE: int = 3
MAX_POSSIBLE_VALUE: int = 100000


def get_positive_number(msg: str, max_value: int) -> int:
    """
    Liefert eine ganze Zahl > 0 und < max_value mit der Nachricht msg
    """
    v: int = -1
    while (v <= 0 or v > max_value):
        v = int(input(msg))
    return v


number: int = get_positive_number("Gib mir eine Zahl: ", MAX_POSSIBLE_VALUE)
exponent: int = 0
while True:                                 # endlosschleife
    if (BASE**exponent > number):
        print(f"Die größtmögliche Potenz mit der basis {BASE} ist {exponent - 1}")
        break                               # schleife abbrechen
    exponent += 1
