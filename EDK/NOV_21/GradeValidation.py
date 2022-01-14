# Notenvalidierung, 1BHIF, Marc Edlinger, 22.11.2021
max_possible, min_possible = 5, 1   # obere/untere Grenze für die Notenvalidierung
current_input = 0                   # derzeit eingegebene note
wrong_input_amount = 0              # anzahl aller fehlerhaften Eingaben


def ask_for_grade():
    return int(input("Gib mir eine note Zwischen 1 und 5: "))


def is_valid(value: int):
    if (value < 0):     # Eine Negative Zahl, kann die untere bedingung niemals erfüllen!
        return False
    return min_possible <= value <= max_possible

current_input = ask_for_grade()
while not (is_valid(current_input)):
    current_input = ask_for_grade()
    wrong_input_amount += 1

print("Du hast", wrong_input_amount, "Versuche gebraucht...")
