# Force the user to provide an positive integer
def ask_for_positive_int(text: str):
    input_number = -1
    while (input_number < 0):
        input_number = int(input(text))
    return input_number


# Force the user to provide a number between to other numbers
def ask_for_bounded_int(text: str, max: int, min: int):
    input_number = int(input(text))
    while ((input_number < min) or (input_number > max)):
        input_number = int(input(text))
    return input_number
