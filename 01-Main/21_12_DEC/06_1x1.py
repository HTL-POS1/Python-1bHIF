# 1x1 von allen Zahlen von 2 bis zu einer beliebigen
# 1BHIF | Marc Edlinger | 02.12.2021
max = int(input("Bis wie weit willst du das 1x1 berechnen? "))


def calculate_multiplication_row(current_step: int):
    display = ""
    for i in range(1, 11):
        display = display + str(i) + " * " + str(current_step) + " = " + str(current_step * i) + "\n"
    return display

for i in range(1, max + 1):
    print(calculate_multiplication_row(i))
