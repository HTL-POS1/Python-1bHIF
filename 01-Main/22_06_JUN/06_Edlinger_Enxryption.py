"""
Marc EDLINGER
1bHIF | 02/06/2022

String encryption
"""
BIG_Z = 90
SMALL_A = 97
SMALL_Z = 122
BIG_A = 65


def encrypt(s: str, secret: int) -> str:
    encrypted: str = ""
    for c in s:
        code: int = ord(c)
        code += secret
        if code >= SMALL_A:                                     # kleinbuchstabe
            if code > SMALL_Z:                                  # > z
                code = (code - SMALL_Z) + SMALL_A - 1
        else:                                                   # grossbuchstabe
            if code > BIG_Z:                                    # > Z
                code = (code - SMALL_Z) + BIG_A - 1
        encrypted += chr(code)
    return encrypted


def change_mutation_chars(s: str) -> str:
    pass


print(encrypt("Willy", 5))
print(encrypt("ABC", 5))
print(encrypt("Hugo", 5))