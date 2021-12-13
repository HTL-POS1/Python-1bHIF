# Christbaum Zeichnen
# 1BHIF | Marc Edlinger | 13.12.2021
def draw_vertical(tree_height: int):
    print(tree_height * " " + "I")

    # print the leaves of the tree
    for i in range(1, tree_height + 1):
        spaces: str = " " * (tree_height - i)
        placeholders: str = "x" * i + "x" * (i - 1)

        if (i % 2 != 0):                                # every odd number has an i at the front and the end
            placeholders = "i" + placeholders + "i"
        else:
            placeholders = " " + placeholders
        print(spaces + placeholders)

    # build the left part of first line of the log, with spheres
    log_string: str = " "
    switch: bool = True
    for i in range(tree_height - 1):
        if (switch is True):
            log_string += "o"
            switch = False
            continue
        log_string += " "
        switch = True
    log_string += "H"
    if (tree_height % 2 != 0):                          # if the height is odd, you have to add a space
        log_string += " "

    # build the right part of first line of the log, with spheres
    switch = True
    for i in range(tree_height - 1):
        if (switch is True):
            log_string += "o"
            switch = False
            continue
        log_string += " "
        switch = True
    print(log_string)
    print(" " * (tree_height) + "H")


def draw_horizontal(tree_height: int):
    spaces: str = "  "
    for i in range(1, tree_height + 1):                     # print the upper part
        if (i == tree_height):                              # in the middle, print the log
            print("mm" + "x" * i)
        else:
            print(spaces + "x" * i)

    for i in range(tree_height - 1, 0, -1):                 # print the lower part
        print(spaces + "x" * i)


def start():                                                # recursive method to get the user inputs
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
        draw_horizontal(height)
    start()


start()
