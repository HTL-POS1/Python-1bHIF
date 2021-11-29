# Ausfindung der Ziffern einer Zahl
# 1BHIF | Marc Edlinger | 25.11.2021
target = int(input("Gimme eine Zahl: "))  # number, you want to get the digits
digits = []                               # list with all digits
backup_target = target                    # unmodified target number

while target >= 1:
    digits.append(target % 10)
    target //= 10

print("Ziffern der Zahl", backup_target, "=", digits)
