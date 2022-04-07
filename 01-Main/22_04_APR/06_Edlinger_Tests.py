"""
Marc EDLINGER
1bHIF | 07/04/2022
"""
from testing import test_list_function

def remove(lst: list, value: int, empty: int)  ->  int:
    """ Entfernt alle value aus der Liste lst und fuellt die freien Stellen am
    Ende mit empty auf und liefert die Anzahl enfernter values. Beispiel:
    loesche alle 5 in [1,5,3,5,7] und ersetze freien Stellen am Ende durch 0
    ergibt            [1,3,7,0,0] und liefert 2 als Ergebnis
    bei einem Aufruf von remove(liste, 5, 0)"""
    rm = 0                                  # Anzahl der entfernten values
    last = len(lst) - 1                     # Letzte Position = Laenge der Liste - 1
    i = 0                                   # Index
    while (i <= last):
        while (i <= last and lst[i] != value):  # solange nicht am Ende und value nicht gefunden
            i += 1                              # erhoehe den Idnex
        if (i <= last):              # Index kleiner oder gleich letzter Position (Listenende nicht überschritten)
            rm += 1                    # value gefunden ;-)
        for q in range(i,last):   # vorschieben aller Elemente ab dem gefundenen Wert
                lst[q] = lst[q+1]
        lst[last] = empty         # an die letze Stelle kommt der default-Wert
    return rm


test_list_function(remove, [1, 2, 2, 3, 4, 2], [1, 3, 4, 0, 0, 0], 3, 2, 0)
test_list_function(remove, [2, 1, 5, 3, 4, 8], [1, 5, 3, 4, 8, 0], 1, 2, 0)
test_list_function(remove, [5, 1, 5, 3, 4, 2], [5, 1, 5, 3, 4, 0], 1, 2, 0)
test_list_function(remove, [], [], 0, 2, 0)
test_list_function(remove, [2, 2, 2, 2, 2], [0, 0, 0, 0, 0], 5, 2, 0)

