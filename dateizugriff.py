#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Dateizugriff
"""

import os.path
import time
import shutil

p = 'bmi.txt'
kopie =  'bmi_kopie.txt'

if os.path.exists(p):
    print("Existiert")
    datei = open("bmi.txt")
    zeile = datei.readline()
    print(zeile)
    datei.close()

    if os.path.isfile(p):
        print("Ist eine Datei")
        print("Größe:", os.path.getsize(p))
        print("Änderungsdatum:", time.ctime(os.path.getmtime(p)))
    else:
        print("Ist keine Datei")

    if os.path.exists(kopie):
        print("Kopie existiert")
    else:
        print("Kopie existiert nicht")
        shutil.move(p, kopie)
else:
    print("Existiert nicht")
    datei = open("bmi.txt","w")
    datei.write("Test")
    datei.close()

