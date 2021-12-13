# Dreieck Zeichnen
# 1BHIF | Marc Edlinger | 13.12.2021

rows = int(input("Höhe des Dreiecks: "))
for i in range(rows):
    display = "x"
    for j in range(i):
        display += "x"
    
    print(display)