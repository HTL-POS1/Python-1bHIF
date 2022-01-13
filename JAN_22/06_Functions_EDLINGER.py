# Funktionen
# 1BHIF | Marc Edlinger | 13.01.2022

def greet():            # funktion def(inieren)
    """
    Was macht die Funktion?
    Sie begrueßt den Anwender
    """
    print("hello from greet")


def hi(msg: str):       # definiert eine funktion namens hi, mit dem parameter msg
    """
    Begrueßt den Anwender mit der nachricht msg
    """
    print("hi " + msg)


def add(a: int, b: int):
    """
    Berechne die Summe zweier Zahlen, und gebe diese aus
    """
    c = a + b
    print(f"{a} + {b} = {c}")


def get_pi() -> float:          # das Ergebnis ist vom typ float
    """
    Liefert den Wert pi
    """
    return 3.14159


def addiere(a: float, b: float) -> float:
    """
    Liefert als Ergebnis einen float
    (a + b)
    """
    return (a + b)

sum = addiere(pi, addiere(7.71, 1.15))
print(f"sum = {sum}")
print(f"pi ist {get_pi()}")

add(7, 2)
add(5, 9)

greet()     # aufrufen
greet()     # noch einmal

t: str = "Walfisch"
hi("Fisch")
hi(t)