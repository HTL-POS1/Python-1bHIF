"""
Marc EDLINGER
1bHIF | 02/06/2022

String encryption
"""
CAPITAL_ABC = range(65, 91)
LOWER_ABC = range(97, 123)
ABC_LEN = len(CAPITAL_ABC)
REPLACEMENTS = {
    "ö": [ord("ö") - ord("o"), ord("ö") - ord("e")],
    "ä": [ord("ä") - ord("a"), ord("ä") - ord("e")],
    "ü": [ord("ü") - ord("u"), ord("ü") - ord("e")],
    "ß": [ord("ß") - ord("s"), ord("ß") - ord("z")]
}

def encrypt(s: str, secret: int) -> str:
    encrypted: str = ""

    for c in s:
        code: int = ord(c)
        if CAPITAL_ABC[0] <= code and CAPITAL_ABC[ABC_LEN - 1] >= code:
            encrypted_char = chr(CAPITAL_ABC[get_new_index(CAPITAL_ABC, code, secret)])
        else:
            encrypted_char = chr(LOWER_ABC[get_new_index(LOWER_ABC, code, secret)])

        encrypted += encrypted_char

    return encrypted


def decrypt(s: str, secret: int) -> str:
    return encrypt(s, -secret)


def get_new_index(abc: list[int], origin: int, secret: int):
    i: int = abc.index(origin) + secret
    list_len = len(abc)
    if i < 0:
        i = list_len + i
    elif i >= list_len:
        i %= list_len

    return i


def change_mutation_chars(s: str) -> str:
    value: str = ""
    for c in s:
        if c in REPLACEMENTS.keys():
            diffs: list[int] = REPLACEMENTS[c]
            for diff in diffs:
                value += chr(ord(c) - diff)
        else:
            value += c
    return value

print(encrypt("Willy", 5))
print(encrypt("ABC", 5))
print(encrypt("Hugo", 5))
print(change_mutation_chars("Hällöß"))