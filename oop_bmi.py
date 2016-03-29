#!/usr/bin/python
# OOP BMI Rechner

class Benutzer:
    """Die Klasse Benutzer fordert zur Einageb der Groesse und des Gewichtes auf. Mit diesen Daten
    wird dann der BMI errechnet.
    Mit der Methode 'set_daten' können die Variablen Groesse und Gewicht gesetzt werden.
    Mit den getter Methoden kann man sich die Daten dann hohlen und weiterverarbeiten."""
    def __init__(self):
        pass

    def __setter(self):
        self.__groesse = float(input("Größe in m (1.67): "))
        self.__gewicht = float(input("Gewicht in kg: "))

    def get_groesse(self):
        return self.__groesse

    def get_gewicht(self):
        return self.__gewicht

    def set_daten(self):
        self.__groesse = float(input("Größe in m (1.67): "))
        self.__gewicht = float(input("Gewicht in kg: "))


class BMIrechner:
    def berechnung(self, gewicht, groesse):
        return gewicht / (groesse * groesse)

    def output(self, erg, aus):
        print("Dein BMI beträgt:", erg)
        print("Ergebnis gerundet:", round(erg, 2))
        print("Du hast", aus)

    def auswertung(self, erg):
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