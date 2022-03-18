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


def get_average_summand(list: list, start: int, end: int) -> float:
    return float((end - start) / (len(list) - 1))


def get_list(length: int, start: int, end: int) -> list:
    numbers: list = [0] * length
    summand = get_average_summand(numbers, start, end)
    for i in range(len(numbers)):
        last_element: float = start - summand if i == 0 else numbers[i - 1]
        numbers[i] = last_element + summand
    return numbers


def get_display(list: list) -> str:
    s: str = ""
    for e in list:
        s += f"{e:.2f} "
    return s


print(get_display(get_list(10, 4, 67)))
