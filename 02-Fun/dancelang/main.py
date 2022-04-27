"""
Marc EDLINGER
1bHIF | 25/04/2022
"""
import tokenize
from io import BytesIO
from translate import translate

if __name__ == "__main__":
    with tokenize.open("test.py") as f:

        lines = " ".join(f.readlines())

        tokens = tokenize.tokenize(BytesIO(lines.encode('utf-8')).readline)
        translate(tokens)

