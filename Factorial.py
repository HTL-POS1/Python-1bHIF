# Fakultät, 1BHIF, Marc Edlinger, 22.11.2021
x = -1  # Zahl von der man die Fakultät berechnen möchte
product = 1  # Produkt, welches bei jedem Schleifendurchlauf aktualisiert wird

while (x < 0):
    x = int(input("Von welcher Zahl möchtest du die Fakultät berechnen? "))

for i in range(1, x + 1):
    product *= i

print(str(x) + "! =", product)
