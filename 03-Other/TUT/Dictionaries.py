my_dict: dict = {}                                              # initialisierung leeres dictionary, datentyp: dict
product_prices: dict = {"Kaffee": 20, "Cola": 10, "Fanta": 5}   # initialisierung dictionary, mit Werten

print(product_prices["Kaffee"])                                 # gibt den Wert für "Kaffee" (20) aus
print(product_prices["Fanta"])                                  # gibt den Wert für "Fanta" (5) aus

product_prices["Cola"] = 20                                     # setzt den Wert für Cola auf 20
print(product_prices["Cola"])                                   # gibt den neuen Wert aus (20)

def contains_sprite():
    if (product_prices.__contains__("Sprite")):  # überprüft, ob ein Key mit dem Namen Sprite im dict ist
        print("Ja", product_prices["Sprite"])
    else:
        print("Nein")


contains_sprite()
product_prices["Sprite"] = 100                                 # fügt den Key "Sprite" mit dem Wert 100 hinzu
contains_sprite()

"""
Farben
"""
colors: dict = {
    "rot": "\u001b[31m",
    "grün": "\u001b[32m",
    "lila": "\u001b[35m"
}
color: str = ""
while not colors.__contains__(color):
    color = input("Welche Farbe? ")

color_code: str = colors[color]
print(color_code + "Du hast die Farbe:", color, "Ausgewählt!")
