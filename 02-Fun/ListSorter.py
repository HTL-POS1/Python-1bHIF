import random as rndm

rndm.seed()


def is_sorted(to_check: list) -> bool:
    for i in range(len(to_check) - 1):
        if (to_check[i] > to_check[i + 1]):
            return False
    return True


def sort(list: list) -> int:
    tries: int = 0

    while not is_sorted(list):
        i: int = rndm.randrange(len(list))
        j: int = rndm.randrange(len(list))
        tmp: int = list[i]
        list[i] = list[j]
        list[j] = tmp
        tries += 1
        if tries % 5000000 == 0:
            print(f"Zwischenstand {tries:,}")

    print(f"Liste mit {len(list)} Elementen is jetzt sortiert! Gebrauchte Versuche: {tries:,}")
    print(" " * 100)
    return tries


runs: int = 5
for i in range(runs):
    list: list = [3, -557, 2, 8, 1, -7, 9, -7, 89, 8, -45, 47]
    sort(list)