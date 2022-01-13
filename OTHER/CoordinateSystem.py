# Koordinatensystem
# 1BHIF | Marc Edlinger | 12.01.2022
X_AXIS_SYMBOLE: str = "__"
X_AXIS_SYMBOLE_LENGTH: int = len(X_AXIS_SYMBOLE)
Y_AXIS_SYMBOLE: str = "|"
MARKED_POINT_SYMBOLE: str = "x"

x_size: int = abs(int(input("Wie groß x-Achse? ")))
y_size: int = abs(int(input("Wie groß y-Achse? ")))
points = []

def contains_point(y: int):
    for point in points:
        if (point[1] == y):
            return True
    return False

def get_x_value(y: int):
    for point in points:
        if (point[1] == y):
            return point[0]
    raise Exception

def draw_y_line(line: int):
    print_line = x_size * X_AXIS_SYMBOLE + Y_AXIS_SYMBOLE + x_size * X_AXIS_SYMBOLE
    if (contains_point(line)):
        x: int = get_x_value(line)
        if (x == 0):
            print_line = print_line.replace(Y_AXIS_SYMBOLE, MARKED_POINT_SYMBOLE)
        elif (x < 0):
            spaces: int = (X_AXIS_SYMBOLE_LENGTH * (x_size - abs(x)))
            print_line = print_line[:spaces] + (MARKED_POINT_SYMBOLE * X_AXIS_SYMBOLE_LENGTH) + print_line[
                                                                                                spaces + X_AXIS_SYMBOLE_LENGTH:]
        else:
            spaces: int = (x_size * X_AXIS_SYMBOLE_LENGTH) + 1 + (x - 1) * X_AXIS_SYMBOLE_LENGTH
            print_line = print_line[:spaces] + (MARKED_POINT_SYMBOLE * X_AXIS_SYMBOLE_LENGTH) + print_line[spaces + X_AXIS_SYMBOLE_LENGTH:]

    if (line != 0):
        print_line = print_line.replace(X_AXIS_SYMBOLE, X_AXIS_SYMBOLE_LENGTH*" ")
    print(print_line)


def start():
    y_input = input("Gebe die Y-Koordinate deines Punktes an. (exit=ende): ")
    if (y_input == "exit"):
        for y in range(y_size, -y_size - 1, -1):
            draw_y_line(y)
        quit(1)
    else:
        y_input = int(y_input)
        if (contains_point(y_input)):
            print("invalid point, already a point for this y-value")
            start()
    x_input = int(input("Gebe die X-Koordinate deines Punktes an."))
    points.append((x_input, y_input))

    print(f"registered... {len(points)} points...")
    start()


start()
