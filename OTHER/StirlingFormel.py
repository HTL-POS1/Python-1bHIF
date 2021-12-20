# Prove for the stirling formula
# 1BHIF | Marc Edlinger | 18.12.2021
from math import sqrt, pi, e
limit: int = int(input("Wie weit willst du gehen...? "))


def factorial(n: int):
    if (n == 0):
        return 1
    if (n == 1):
        return n
    return factorial(n - 1) * n


def stirling(n: int):
    return sqrt(2 * n * pi) * (n / e)**n


for i in range(1, limit + 1):
    factorial_result: int = factorial(i)
    stirling_result: float = stirling(i)

    drift: float = 0
    if (stirling_result > factorial_result):
        drift = 100 * (factorial_result / stirling_result)
    else:
        drift = 100 * (stirling_result / factorial_result)
    drift = -1 * (drift - 100)
    print(f"{i}. {drift:.10f}%")
