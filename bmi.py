#BMI Rechner

groesse = float(input("Größe in m (1.67): "))
gewicht = float(input("Gewicht in kg: "))

ergebnis = (gewicht)/(groesse*groesse)

print("Dein BMI beträgt: ", ergebnis)

if ergebnis < 18.50:
    uebersetzung = "Untergewicht"
elif ergebnis < 25.00:
    uebersetzung = "Normalgewicht"
elif ergebnis < 30.00:
    uebersetzung = "Übergewicht"
elif ergebnis < 40.00:
    uebersetzung = "Adipositas"
elif ergebnis >= 40.00:
    uebersetzung = "Adipositas Grad III"

print("Du hast ", uebersetzung)