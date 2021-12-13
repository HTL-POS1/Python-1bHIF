# Christbaum Zeichnen
# 1BHIF | Marc Edlinger | 13.12.2021

def draw_vertical(height: int):
    for i in range(1, height + 1):
        print(" " * (height - i) + "x" * i + "x" * (i - 1))
    print(" " * (height - 1) + "H")
    print(" " * (height - 1) + "H")

def draw_horizontal(width: int):
    pass()

height: int = -1
while (height < 4):
    height = int(input("Wie hoch soll der Baum sein? (min. 4, 0 = Ende) "))
    if (height == 0):
        quit()

direction: int = -1
while (direction != 1 and direction != 2):
    direction = int(input("Welche Richtung? (1 = hoch, 2 = quer) "))

if (direction == 1):
    draw_vertical(height)
elif (direction == 2):
    draw_horizontal(heigth)