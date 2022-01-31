# 2. PLF
# 1BHIF | Marc Edlinger | 23.12.2021
invalid_inputs: int = 0                     # amonut of invalid inputs
times_drew: int = 0                         # amount of drew things
max_height: int = 0                         # max given height
height: int = -1                             # current height

# method to ask the user for a valid string, contained in the valid_options list
def ask_for_string(message: str, valid_options: list):
    global invalid_inputs
    value: str = ""
    while (value == "" or not valid_options.__contains__(value)):
        value = input(message)
        invalid_inputs += 1
    invalid_inputs -= 1
    return value

# method to ask the user for a valid input between two numbers, the bypassed variable is for
# some values that are not in the given bindings, but valid tho
def ask_bounded_integer(message: str, max: int, min: int, bypassed: list):
    global invalid_inputs
    value: int = None
    while ((value is None) or (value > max) or (value < min) and not (bypassed.__contains__(value))):
        value = int(input(message))
        invalid_inputs += 1
    invalid_inputs -= 1
    return value

while (height != 0):
    height = ask_bounded_integer("Wie hoch und breit (4 bis 9, 0 = Ende) ? ", 9, 4, [0])
    if (height == 0):               # exit
        break

    if (height > max_height):
        max_height = height
    symbole: str = ask_for_string("Mit welchem Zeichen (x oder o)? ", ["x", "o"])

    # -------------------------------
    # UPPER PART
    # -------------------------------
    for i in range(height):
        symboles = ""
        for j in range(i + 1):
            symboles += symbole
        spaces_amount: int = 2*height - 2*(i + 1)
        spaces: str = ""
        for k in range(spaces_amount):
            spaces += " "
        print(symboles + spaces + symboles)

    # -------------------------------
    # LOWER PART
    # -------------------------------
    for i in range(height - 1, -1, -1):
        symboles = ""
        for j in range(i + 1):
            symboles += symbole
        spaces_amount: int = 2*height - 2*(i + 1)
        spaces: str = ""
        for k in range(spaces_amount):
            spaces += " "
        print(symboles + spaces + symboles)
    times_drew += 1


print(f"Du hast {times_drew}x gezeichnet, bei {invalid_inputs} ungültigen Eingaben und {max_height} als maximale Höhe, bye")
