"""
Marc EDLINGER
1bHIF | 23/05/2022

Strings, Chars & ASCII
"""
amounts: list[int] = [0] * 26

def multiply_string(s: str, mult: int) -> str:
    """ returns a string with the sequence s, repeated mult times """
    value: str = ""
    for i in range(mult):
        value += s
    return value


def is_valid_char(s: str) -> bool:
    if len(s) != 1:
        value = False
    else:
        ascii_code: int = ord(s)
        value = ((65 <= ascii_code <= 90) or (97 <= ascii_code <= 122))

    return value


def get_character_position(char: str) -> int:
    """
    return the ASCII code of char, if it is an valid character, otherwise -1
    """
    ascii_code: int = -1

    if is_valid_char(char):
        ascii_code = ord(char)
        amounts[ascii_code - 65] += 1

    return ascii_code


def print_ascii_table(cols: int):
    """
    print out hte ascii chars
    """
    if (cols < 3 or cols > 10):
        print("cols has to be between 3 and 10")
    else:
        start: int = 32
        for code in range(start, 126, 1):
            char: str = chr(code)
            print(code, char, "\t", end="")
            diff = code - start + 1
            if (diff % cols == 0):
                print("")
        print("")


def to_lowe_case(c: str) -> str:
    """
    return the lowercase char of c
    """
    value: str = ""
    if is_valid_char(c):
        code: int = ord(c)
        if (code <= 90):
            value = chr(code + 32)
        else:
            value = c
    else:
        value = chr(0)

    return value


def show_statistics(chars: list[int] = amounts):
    """ print the amount of chars accessed in get_character_position with stars, displaying them """
    for i in range(len(chars)):
        amount: int = chars[i]
        if (amount != 0):
            char = chr(65 + i)
            print(char, multiply_string("*", amount), amount)
