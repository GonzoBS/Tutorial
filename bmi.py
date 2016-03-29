#!/usr/bin/python
# BMI Rechner


def eingabe():
    groesse = float(input("Größe in m (1.67): "))
    gewicht = float(input("Gewicht in kg: "))
    return gewicht,groesse


def berechnung(ge, gr):
    return ge / (gr * gr)


def output(erg, aus):
    print("Dein BMI beträgt:", erg)
    print("Ergebnis gerundet:", round(erg, 2))
    print("Du hast", aus)


def auswertung(erg):
    if erg < 18.50:
        uebersetzung = "Untergewicht"
    elif erg < 25.00:
        uebersetzung = "Normalgewicht"
    elif erg < 30.00:
        uebersetzung = "Übergewicht"
    elif erg < 40.00:
        uebersetzung = "Adipositas"
    elif erg >= 40.00:
        uebersetzung = "Adipositas Grad III"
    else:
        uebersetzung = "Fehler"
    return uebersetzung

beenden = True
einga = []
while beenden:
    einga = eingabe()
    berech = berechnung(einga[0], einga[1])
    auswert = auswertung(berech)
    output(berech, auswert)
    abfrage = input("Weitere Berechnung durchführen? (j/n): ")
    if abfrage == "j":
        beenden = True
    else:
        beenden = False
        print("Auf wiedersehen")
