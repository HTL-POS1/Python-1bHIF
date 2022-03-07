from random import seed, randint

seed()


def get_char_index(s: str, c: str) -> list:
    i = 0
    indexes = []
    for char in s:
        if char == c:
            indexes.append(i)
        i += 1
    return indexes

words = ["gott", "jakob", "peter"]

index: int = randint(0, len(words) - 1)
selected_word: str = words[index]
used_chars: str = ""

print(selected_word)
progress: list = ["_"] * len(selected_word)

char: str = input("Buchstabe: ")

char_index = get_char_index(selected_word, char)
print(progress)
if len(char_index) == 0:
    # nicht drinnen
    print("nicht enthalten")
else:
    for i in char_index:
        progress[i] = char

print(progress)