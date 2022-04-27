import builtins
from tokenize import TokenInfo

keymapping: dict[str, str] = {
    "def": "A",
    "int": "B",
    "return": "C",
    "+": "D",
    ":": "E",
    "True": "F",
    "False": "G",
    "complex": "H",
    "==": "I",
    "and": "J",
    "or": "K",
    "<": "L",
    "while": "M",
    "for": "N",
    "if": "O",
    "*": "P",
    "**": "Q",
    "-": "R",
    "=": "S",
    ".": "."
}

exclusions: list[str] = [
    '"""', "#"
]

raw_exclusions: list[str] = [
    "utf-8", "{", "}", "[", "]", "", "->", ","
]

parentheses: list[str] = [
    "{", "}", "[", "]", "(", ")"
]


def is_valid(string: str) -> bool:
    result: bool = True
    if string in raw_exclusions:
        result = False
    else:
        for ex in exclusions:
            if (ex in string):
                result = False
                break

    return result


def translate(tokens: list[TokenInfo]):
    was_last_newline: bool = True

    for token in tokens:
        token_string: str = token.string
        if is_valid(token_string):
            if not token_string.strip():
                if not was_last_newline:
                    print()

                was_last_newline = True
            else:
                val: str = token_string
                if token_string in keymapping:
                    val = keymapping[token_string]
                else:
                    if token_string not in parentheses and not token_string.isnumeric():
                        if getattr(builtins, token_string, None) is None:
                            if token_string not in vars(builtins):
                                val = "!<<-- " + val + " -->>!"

                print(val, end=" ")

                if was_last_newline:
                    was_last_newline = False
