from math import sqrt
from random import randint

GRID: list = [
    [0, 1, 5, 7, 3, 0, 8, 0, 2],
    [6, 0, 0, 0, 0, 1, 0, 0, 0],
    [4, 8, 7, 5, 0, 2, 0, 0, 0],
    [3, 0, 9, 6, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 7, 0, 6, 0, 5],
    [0, 4, 0, 0, 2, 8, 7, 0, 9],
    [0, 0, 1, 0, 0, 3, 2, 0, 0],
    [0, 0, 0, 2, 0, 9, 0, 0, 1],
    [0, 9, 0, 0, 5, 0, 0, 0, 0],
]


def solve():
    for row, row_entry in enumerate(GRID):
        for column, entry in enumerate(row_entry):          # iteration through all elements
            if (entry == 0):                                # if the current field is not set yet
                for i in range(1, 10):                      # all digits
                    if (valid_placement(i, row, column)):   # try if the current digit is a valid digit for the field
                        GRID[row][column] = i               # update field
                        if (solve()):                       # try if the board is solvable with the number, filled in
                            return True                     # is solved
                        else:
                            GRID[row][column] = 0           # set value back to 0 and try with another digit
                return False                                # board is unsolvable
    return True


def get_grid_display() -> str:
    value: str = ""
    for i, row in enumerate(GRID):
        for j, column in enumerate(row):
            value += str(column) + " "
            if ((j + 1) % SQUARE_SIZE == 0):
                if (j + 1 == GRID_SIZE):
                    if not ((i + 1) % SQUARE_SIZE == 0):
                        value += "\n"
                else:
                    value += "| "
        if ((i + 1) % SQUARE_SIZE == 0):
            if not ((i + 1) == GRID_SIZE):
                value += "\n" + ("-" * ((2 * (GRID_SIZE - 1) + 3 * (SQUARE_SIZE - 1))) + "\n")
    return value


def is_in_row(n: int, row: int) -> bool:
    for i in GRID[row]:         # every element of param row
        if (i == n):
            return True
    return False


def is_in_column(n: int, column: int) -> bool:
    for row in GRID:            # every row
        if (row[column] == n):  # check always the row in the given column
            return True
    return False


def is_in_box(n: int, row: int, column: int):
    row_pos: int = row - row % SQUARE_SIZE                          # upper left corner row of the square of the element
    column_pos: int = column - column % SQUARE_SIZE                 # upper left corner col of the square of the element
    for r in range(row_pos, row_pos + SQUARE_SIZE):                 # for every row in the square
        for c in range(column_pos, column_pos + SQUARE_SIZE):       # for every col in the square
            if (GRID[r][c] == n):                                   # if the elements is the element searching for
                return True
    return False


def valid_placement(n: int, row: int, column: int):
    return (not is_in_box(n, row, column) and not is_in_column(n, column) and not is_in_row(n, row))


def grid_to_file():
    sudoko_id: int = randint(1000, 9999)
    file = open(f"sudoko_results/sudoko_result{sudoko_id}.txt", "w")
    file.write(get_grid_display())
    file.close()
    pass


current_row: int = 0

GRID_SIZE: int = len(GRID)
SQUARE_SIZE: int = round(sqrt(GRID_SIZE))
while current_row != GRID_SIZE:
    input_string: str = input(f"Input für Reihe {current_row + 1}")
    if (len(input_string) == 0):
        break
    if (len(input_string) != GRID_SIZE):
        print("Ungültige Länge")
        continue
    for index, char in enumerate(input_string):
        number: int = int(char)
        GRID[current_row][index] = number
    print("\n"*10)
    print(get_grid_display())
    current_row += 1

print("\nUnsolved:")
print(get_grid_display())
solve()
print("\nSolved: \n\n")
print(get_grid_display())
grid_to_file()
