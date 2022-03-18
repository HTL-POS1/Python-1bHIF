def einlesen_ug():
    ug = int(input("Gib mir eine Untergrenze: "))
    return ug

def einlesen_og():
    og = int(input("Gib mir eine Obergrenze: "))
    return og

def og_prüfen(og,ug):
    ogrichtig = og
    while ogrichtig > 1000 or ogrichtig < ug:
        ogrichtig = int(input("FEHLER: Gib mir eine Obergrenze! "))
    return ogrichtig

def ug_prüfen(ug,og):
    ugrichtig = ug
    while ugrichtig < 1 or ugrichtig > og:
        ugrichtig = int(input("FEHLER: Gib mir eine Untergrenze! "))
    return ugrichtig

def listcreate(ogrichtig,ugrichtig):
    ug = ugrichtig
    og = ogrichtig
    liste = [0] * 10
    for i in range(len(liste)):
        if i == 0:
            liste[i] = ug
            continue
        liste[i] = liste[i - 1] + ((og-ug) / 9)
    return liste
    

def main():
    ug = einlesen_ug()
    og = einlesen_og()
    ogrichtig = og_prüfen(og,ug)
    ugrichtig = ug_prüfen(ug,og)
    liste = listcreate(ogrichtig,ugrichtig)
    print(liste)

main()