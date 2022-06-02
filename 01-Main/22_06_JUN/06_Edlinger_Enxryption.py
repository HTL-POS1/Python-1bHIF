"""
Marc EDLINGER
1bHIF | 02/06/2022

String encryption
"""
CAPITAL_ABC = range(65, 91)
LOWER_ABC = range(97, 123)
ABC_LEN = len(CAPITAL_ABC)

def encrypt(s: str, secret: int) -> str:
    encrypted: str = ""

    for c in s:
        code: int = ord(c)
        if code in CAPITAL_ABC:
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
    pass


print(encrypt("Willy", 5))
print(encrypt("ABC", 5))
print(encrypt("Hugo", 5))