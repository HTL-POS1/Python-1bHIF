# Koordinatensystem
# 1BHIF | Marc Edlinger | 11.01.2022
X_AXIS_SYMBOLE: str = "-"
ZERO_POINT_SYMBOLE: str = "+"
Y_AXIS_SYMBOLE: str = "|"
X_FACTOR: int = 2

x_size: int = int(input("Wie groß x-Achse? "))
y_size: int = int(input("Wie groß y-Achse? "))
x_size = x_size if x_size >= 0 else x_size * -1
y_size = y_size if y_size >= 0 else y_size * -1
marked_points = {}

print(f"Generating coord-sys. sizes {x_size} | {y_size}")
def draw():
    """
    Positive Y
    """
    for y in range(y_size):
        point = check_point(y)
        if (point is not None):
            x = point[0]
            if (x < 0):
                spaces = X_FACTOR * (x_size + (x*X_FACTOR))
                print(spaces * " " + marked_points[point] + (spaces * (x_size - spaces + 1) * " "))
                pass
            elif (x > 0):
                pass
            else:
                pass
        else:
            print(" " * x_size * X_FACTOR + Y_AXIS_SYMBOLE)

    print(X_FACTOR * x_size * X_AXIS_SYMBOLE + ZERO_POINT_SYMBOLE + X_FACTOR * x_size * X_AXIS_SYMBOLE)

    """
    Negative Y 
    """
    for y in range(y_size):
        print(" " * x_size * X_FACTOR + Y_AXIS_SYMBOLE)

def mark_point(x: int, y: int, symbole: str = "x"):
    if (x < (x_size * -1) or x > x_size):
        print("Invalid coords, x-axis!")
    if (y < (y_size * -1) or y > y_size):
        print("Invalid coords, y-axis!")
    marked_points[(x, y)] = symbole

def check_point(y: int):
    for point in marked_points.keys():
        if (point[1] == y):
            return point
    return None


mark_point(-2, 3)
draw()
