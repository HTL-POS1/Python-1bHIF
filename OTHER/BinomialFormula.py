# Binomische Formeln
# 1BHIF | Marc Edlinger | 13.01.2022
from math import factorial

def get_coefficient(exponent: int, step: int) -> int:
    """
    calculate binomial-coefficient (bc)
    :param exponent: the n value of the bc formula
    :param step: the k value of the bc formula
    :return: the coefficient (n over k)
    """
    return factorial(exponent) // (factorial(step) * factorial(exponent - step))


def get_term(exponent: int, first_symbole: str = "a", second_symbole: str = "b") -> str:
    """
    calculate something like (a + b)^c
    :param exponent: the power for the sum
    :param first_symbole: name of the first component of the binomial, default a
    :param second_symbole: name of the second component of the binomial, default b
    :return: the whole term for the binomial
    """
    print(f"{first_symbole}^{exponent}", end=" + ")
    for i in range(1, exponent):
        coefficient: int = get_coefficient(exponent, i)
        value: str = ""
        if (coefficient != 1):
            value = str(coefficient)

        value += first_symbole
        if (exponent - i != 1):
            value += f"^{exponent - 1}*"

        value += second_symbole
        if (i != 1):
            value += f"^{exponent-1}"
        print(value, end=" + ")
    print(f"{second_symbole}^{exponent}")


get_term(2)
get_term(3)
get_term(4)
get_term(5)
get_term(6)