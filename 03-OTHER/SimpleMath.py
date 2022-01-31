def absolute_value(x: int) -> int:
    return x if (x >= 0) else -x


print(absolute_value(-2))
print(absolute_value(0))
print(absolute_value(56))
print("-"*20)


def sign(x: int) -> str:
    return "-" if (x < 0) else "+"


print(sign(-3))
print(sign(0))
print(sign(6))
print("-"*20)


def negate(x: int) -> int:
    return absolute_value(x) * (-1)


print(negate(-2))
print(negate(0))
print(negate(7))
