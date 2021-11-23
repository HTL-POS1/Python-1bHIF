# Erstes Programm, 1BHIF, Edlinger Marc, 22.11.2021
print("Hello Python world")

i = 0               # legt eine Variable namens i mit dem Wert 0 an
                    # damit ist es automatisch vom typ int(eger) = ganze Zahl
pi = 3.14           # Variable pi vom typ float = gleitkommazahl
msg = "Hello World" # Variable msg vom typ string = Text

print(i, pi, msg)                           # Ausgabe der Werte
i = int(input("Gib Note: "))                # input liefert immer einen String, mit int(...) kann man
                                            # diesen in einen integer umwandeln
print("Eingabe:", i, "vom Typ", type(i))    #type(...) gibt den typen einer Variable zurück