##############################################
# FUNKTIONEN
##############################################
"""
Reihenfolge einer Dekleration einer Funktion:

def     | Schlüsselwort für den Beginn einer Funktionendekleration
name    | Der Name der Funktion, Englisch, alles kleingeschrieben, Nomen mit Unterstrichen getrennt, Kontext
()      | Klammern, in denen die Parameter geschrieben werden
:       | Nach den Klammern, das Ende der Dekleration
"""

##################################
# Funktionen mit Rückgabewert I.
##################################
"""
get_positive_integer | Name
(text, max_value)    | Klammern mit Parametern

Ein Parameter wird innerhalb einer Funktion gleich wie eine Variable behandelt.
Der Name eines Parameters sollte wie eine Variable benannt werden:
    - Kontextbezogener Name
    - Englisch
    - alles kleingeschrieben
    - Nomen mit unterstrichen getrennt

Zusätzlich kann, aber muss nicht, ein Datentyp für einen Parameter festgelegt werden.
bspw. statt "text", "text: str" um zu zeigen, dass der Parameter nur ein String sein darf.
Die wichtigsten Datentypen:
    - bool (True, False)
    - str (String/Text)
    - int (Ganze Zahlen)
    - float (Kommazahlen)
    - complex (Komplexe Zahlen)
    
Durch das "return"- Statement am Ende der Funktion, kann ein Wert, der bspw. erst innerhalb der Funktion berechnet/einge
lesen etc. wurde, zurückgeben. -> Rückgabewert
"""
def get_positive_integer(text, max_value):
    # Programmablauf der Funktion
    number = -1
    while ((number < 0) or (number > max_value)):
        number = int(input(text))

    return number


"""
Der Aufrug der Funktion, durch den Namen, führt alle Statements aus der oben deklarierten Funktion aus.
Als Parameter wird der Text, und der höchstmögliche Wert übergeben, in der selben Reihenfolge, wie in der dekleration.
Der Rückgabewert, der in der Funktion generiert wird, wird in die neu deklarierte Variable "length" gespeichert.
"""
length = get_positive_integer("Wie lang?", 50)

##################################
# Funktionen mit Rückgabewert II
##################################
"""
Eine Funkion, die die Länge des angeführten Parameters prüft, und entsprechende Werte zurückgibt.
0   | Leer
1-3 | Kurz
4-6 | Mittel
6-9 | Lang
> 9 | Sehr Lang
"""
def check_length(text: str):
    string_length = len(text)   # die len(...) Funktion gibt die Anzahl an Zeichen eines Strings zurück
    if (string_length == 0):  # genau 0
        return "Leer"

    if ((string_length >= 1) and (string_length <= 3)):  # zwischen 1 und 3
        return "Kurz"   # gibt den Wert "Kurz" zurück, die Funktion läuft danach nicht mehr weiter

    if ((string_length >= 4) and (string_length <= 6)):
        return "Mittel"

    if ((string_length >= 6) and (string_length <= 9)):
        return "Lang"

    return "Sehr Lang"  # wenn keines der anderen return Statements erreicht wurde, bedeutet es, dass die Länge größer
                        # als 9 sein muss


print(check_length(""))                             # Leer
print(check_length("Text"))                         # Mittel
print(check_length("Te"))                           # Kurz
print(check_length("Text der Länger ist"))          # Sehr Lang
print(check_length("ABCDE"))                        # Mittel

##################################
# Funktionen kombiniert
##################################
"""
Angenommen, man kombiniert die beiden Funktionen oben. Man will die Länge einer Zahl analysieren, die der Benutzer
eingibt.

Wichtig ist, dass die Funktion get_positive_integer einen Integer zurückgibt, und die Funktion check_length einen String
benötigt. Mit der eingebauten Funktion str(...) kann man den Integer in einen String umwandeln.
"""
def check_input_number_length():
    number = get_positive_integer("Gib mir eine Zahl!", 1000000000)
    # check_length(number) würde einen Fehler geben, da man einen Integer übergibt, obwohl ein String verlangt wird.
    length = check_length(str(number))
    return "Deine Zahl ist: " + length


print(check_input_number_length())

##################################
# Rekursive Funktionen
##################################
"""
Eine rekursive Funktion ist eine Funktion, die sich, bis eine bestimmte Bedingung erfüllt ist, selbst aufruft.
(ähnlich wie eine While-Schleife)

Beispielsweise lässt sich die Fakultät (Produkt aller Zahlen von 1 bis n) gut rekursiv berechnen.
Dabei muss man beachten:
5! = 5*4*3*2*1 = 5*(4!)
4! = 5*4*3*2*1 = 4*(3!)
3! = 3*2*1     = 3*(2!)
2! = 2*1       = 2(1!)
1! = 1

Also gilt:
n! = n * (n - 1)!

Das wird in der unteren Funktion gemacht. Der Anfangswert (number) wird mit der Fakultät, der Fakultät von number - 1
multipliziert. Die Fakultät von number - 1 wird durch (number - 1) * (number - 2)! berechnet usw.
Soweit bis man bei 1 angekommen ist.
"""
def factorial_recursive(number: int):
    if (number == 1):   # End-Bedingung
        return 1        # einen Konstanten Wert zurückgeben (1! = 1); nicht erneut die Funktion aufrufen
    return number * factorial_recursive(number - 1)


print(factorial_recursive(5))   # 120
