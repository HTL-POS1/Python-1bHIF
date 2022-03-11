from math import sqrt

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
        for coloumn, entry in enumerate(row_entry):
            if (entry == 0):
                for i in range(1, GRID_SIZE + 1):
                    if (valid_placement(i, row, coloumn)):
                        GRID[row][coloumn] = i
                        if (solve()):
                            return True
                        else:
                            GRID[row][coloumn] = 0
                return False
    return True


def print_grid():
    for i, row in enumerate(GRID):
        for j, coloumn in enumerate(row):
            print(coloumn, end=" ")
            if ((j + 1) % SQUARE_SIZE == 0):
                if (j + 1 == GRID_SIZE):
                    if not ((i + 1) % SQUARE_SIZE == 0):
                        print("")
                else:
                    print("| ", end="")
        if ((i + 1) % SQUARE_SIZE == 0):
            if not ((i + 1) == GRID_SIZE):
                print("\n" + "-" * (2 * (GRID_SIZE - 1) + 3 * (SQUARE_SIZE - 1)))


def is_in_row(n: int, row: int) -> bool:
    for i in GRID[row]:
        if (i == n):
            return True
    return False


def is_in_coloumn(n: int, coloumn: int) -> bool:
    for row in GRID:
        if (row[coloumn] == n):
            return True
    return False


def is_in_box(n: int, row: int, coloumn: int):
    row_position: int = row - row % SQUARE_SIZE
    coloumn_position: int = coloumn - coloumn % SQUARE_SIZE
    for r in range(row_position, row_position + SQUARE_SIZE):
        for c in range(coloumn_position, coloumn_position + SQUARE_SIZE):
            if (GRID[r][c] == n):
                return True
    return False


def valid_placement(n: int, row: int, coloumn: int):
    return (not is_in_box(n, row, coloumn) and not is_in_coloumn(n, coloumn) and not is_in_row(n, row))


current_row: int = 0

GRID_SIZE: int = len(GRID)
SQUARE_SIZE: int = round(sqrt(GRID_SIZE))
while current_row != GRID_SIZE:
    input_string: str = input(f"Input für Reihe {current_row + 1}")
    if (len(input_string) != GRID_SIZE):
        print("Ungültige Länge")
        continue
    for index, char in enumerate(input_string):
        number: int = int(char)
        GRID[current_row][index] = number
    print("\n"*10)
    print_grid()
    current_row += 1

print("\nUnsolved:")
print_grid()
solve()
print("\nSolved: \n\n")
print_grid()
