# Summe, 1BHIF, Edlinger Marc, 22.11.2021
x = 0   # Bis wie weit der benutzer die Summe berechnen möchte.


def ask_for_number():
    return int(input("Bis wie weit willst du die Summe berechnen? "))


def sum(max_number: list):
    sum = 0
    for i in max_number:
        sum += i
    return sum

x = ask_for_number()
while (x < 0):              # So lange eingeben lassen, bis eine positive Zahl herauskommt.
    x = ask_for_number()

print("Die Summe bis", x, "ist", sum(range(1, x + 1)))
