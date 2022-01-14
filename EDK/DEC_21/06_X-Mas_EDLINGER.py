# Christbaum Zeichnen
# 1BHIF | Marc Edlinger | 13.12.2021
def draw_vertical(tree_height: int):
    print(tree_height * " " + "I")                      # the top of the tree

    # print the leaves of the tree
    for i in range(1, tree_height + 1):
        spaces: str = " " * (tree_height - i)
        placeholders: str = "x" * i + "x" * (i - 1)

        if (i % 2 != 0):                                # every odd number has an i at the front and the end
            placeholders = "i" + placeholders + "i"
        else:
            placeholders = " " + placeholders
        print(spaces + placeholders)

    # print out the log
    log_string: str = ""
    for i in range(tree_height * 2):
        log_string += " "

    log_string = interleave(log_string, "o", 2)                                 # insert the o's at every second char
    log_string = log_string[:tree_height] + "H" + log_string[tree_height + 1:]  # insert the H in the middle
    print(log_string)
    print(log_string.replace("o", " "))


# origin = the original string, you want to interleave
# symbole = the symbole you want to insert
# step = the frequence, you want to insert the given smybole in the origin string
def interleave(origin: str, symbole: str, step: int):
    for i in range(1, len(origin)+1):
        # if i is a divider of step. eg. for step = 3, the valid
        # i values would be 3, 6, 9, 12 ect.
        if (i % step == 0):
            origin = origin[:i-1] + symbole + origin[i:]        # insert the symbole
    return origin


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
            print("Frohe Weihnachten!")
            quit()

    direction: int = -1
    while (direction != 1 and direction != 2):
        direction = int(input("Welche Richtung? (1 = hoch, 2 = quer) "))

    if (direction == 1):
        draw_vertical(height)
    elif (direction == 2):
        draw_horizontal(height)
    start()


start()         # first call of recursive method
