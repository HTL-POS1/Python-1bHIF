# 06 Edlinger | 1bHIF | 07.03.2022
# 2. Aufgabe mit Listen in python


def getPosition(max: int) -> int:
    """ liest vom Anwender eine gueltige (0 bis max) Position ein und liefert diese """
    pos = int(input("wo willst du die Zahl einfügen (0-" + str(max) + ") "))
    while (pos < 0 or pos > max):
        pos = int(input("von 0 bis " + str(max) + " "))
    return pos


def getValue() -> int:
    """ liest vom Anwender eine positive Zahl ein und liefert diese """
    z = int(input("gib mir eine Zahl, die du einfügen willst "))
    while (z < 0):
        z = int(input("die Zahl muss positiv sein "))
    return z


def readList(liste: list, list_len: int):
    """ liest einen neuen Wert in die Liste liste der Länge list_len ein und liefert diese Liste """
    st = getPosition(list_len-1)    # hol die Position zum Einfügen
    z = getValue()                 # hol den Wert zum Einfügen
    liste[st] = z                   # füg den Wert an der Stelle in die Liste


def countValues(liste: list, list_length: int) -> int:
    """ zählt und liefert in liste der Länge list_length, wie viele Stellen belegt sind """
    c = 0
    for i in range(0, list_length):
        if (liste[i] == -1):
             c += 1
    return list_length - c


list = [-1 for i in range(10)]
length = len(list)
c = 0

while (c != length):
    readList(list, length)            # liest den nächsten Wert in die Liste ein
    c = countValues(list, length)     # zähle die belegten Stellen in der Liste
    print("Es wurden", c, "überschrieben in", list)



