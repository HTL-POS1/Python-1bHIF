# Ausfindung der Ziffern einer Zahl
# 1BHIF | Marc Edlinger | 25.11.2021
target = int(input("Gimme eine Zahl: "))  # number, you want to get the digits
digits = 0     # amount of all digits

while target != 0:
    digits += 1
    target //= 10

print(digits)
