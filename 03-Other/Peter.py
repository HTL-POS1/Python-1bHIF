def count(to_check: list, search: str) -> int:
    n: int = 0
    for element in to_check:
        if element == search:
            n += 1
    return n


def get_different_chars(word: str) -> list:
    chars: list = [""] * len(word)
    i: int = 0
    for char in word:
        if count(chars, char) == 0:
            chars[i] = char
        i += 1
    return chars


def get_valid_elements(target: list) -> int:
    n: int = 0
    for e in target:
        if not e == "":
            n += 1
    return n


print(get_different_chars("anna"))
print(get_different_chars("mississippi"))
print(get_different_chars("donnerstag"))
