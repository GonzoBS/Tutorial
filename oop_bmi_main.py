#!/usr/bin/python
# OOP BMI Rechner Main

import oop_bmi

beenden = True
benutzer = oop_bmi.Benutzer()
bmirechner = oop_bmi.BMIrechner()
while beenden:
    benutzer.set_daten()
    berechnung = bmirechner.berechnung(benutzer.get_gewicht(), benutzer.get_groesse())
    auswertung = bmirechner.auswertung(berechnung)
    bmirechner.output(berechnung, auswertung)
    abfrage = input("Weitere Berechnung durchführen? (j/n): ")
    if abfrage == "j":
        beenden = True
    else:
        beenden = False
        print("Auf wiedersehen")