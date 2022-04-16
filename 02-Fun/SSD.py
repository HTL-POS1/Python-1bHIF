"""
Marc EDLINGER
1bHIF | 15/04/2022
Seven segment display
"""
from toolz import partition
from datetime import datetime
from termcolor import colored

SECONDARY_COLOR = ""
MAX_VALUE = 2 ** 7  # 2**7
DISPLAY_REPRESENTATIONS = {
    "0": 0x7E, "1": 0x30, "2": 0x6D,
    "3": 0x79, "4": 0x33, "5": 0x5B,
    "6": 0x5F, "7": 0x70, "8": 0x7F,
    "9": 0x7B
}


class Segment():

    def __init__(self, symbole: str, code: int):
        self.enabled = False
        self.symbole = symbole
        self.code = code

    def __str__(self):
        return self.symbole


digits = []
digit = [
    None, Segment("_", 0), None,
    Segment("|", 5), Segment("_", 6), Segment("|", 1),
    Segment("|", 4), Segment("_", 3), Segment("|", 2)
]


def get_lines() -> list:
    lines = []
    for line in partition(3, digit):
        line_string: str = ""
        for segment in line:
            display: str = " "
            if segment is not None:
                display = colored(str(segment), "red" if segment.enabled else "white")
            line_string += display
        lines.append(line_string)
    return lines


def print_digits(spaces: dict):
    size = len(digit) // 3
    lines = [""] * size
    for i in range(size):
        for count, digit_ in enumerate(digits):
            apply_number(digit_)
            usual_lines = get_lines()

            lines[i] += usual_lines[i] + (" " * (spaces[count + 1] if count + 1 in spaces else 0))
    for line in lines:
        print(line)


def find_segment_by_code(code: int) -> int:
    for index, line in enumerate(digit):
        if line is not None and line.code == code:
            return index


def apply_number(n: int):
    for i in range(6, -1, -1):
        digit[find_segment_by_code(i)].enabled = n & 1 == 1
        n = (n >> 1)


def get_digits(n: int) -> list:
    n_digits = []
    while n != 0:
        n_digits.append(n % 10)
        n //= 10
    n_digits.reverse()
    return n_digits


now = datetime.now()
_ = get_digits(now.hour)
for m in get_digits(now.minute):
    _.append(m)

for s in get_digits(now.second):
    _.append(s)

for digit_ in _:
    digits.append(DISPLAY_REPRESENTATIONS[str(digit_)])
print_digits({2: 2, 4: 2})
