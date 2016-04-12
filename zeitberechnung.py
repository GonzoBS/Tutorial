#!/usr/bin/python
# Spielereien mit der Zeit

import datetime
import time

datum = datetime.date.today()
dtime = datetime.datetime.now()

print(str(datum.day) + "." + str(datum.month) + "." + str(datum.year))
print(str(dtime.hour) + ":" + str(dtime.minute) + ":" + str(dtime.second))
print(datum)
print(dtime)
# Es werden folgende Zeiten unterschieden:
# UTC: Coordinated Universal Time, früher GMT
# DST: Daylight Saving time (Lokalzeit). Zeitzonenzeit, abgeleitet von UTC
# Es ergibt sich für unsere Zeitzone (Berlin) eine Zeitverschiebung von
# 2 Stunden
# Unix-Zeit: Die UTC-Zeit in Sekunden ab dem 1. Januar 1970 in Sekunden
# dargestellt, Schaltsekunden werden nicht mitgezählt.
# (s.a. http://de.wikipedia.org/wiki/Unixzeit#Umrechnung)
# Das Modul time bietet Methoden an, um auf die Systemzeit des Rechners
# geeignet zuzugreifen.
# Die DST: (UTC + 2 Stunden)

print ("**Eine Auswahl von Attributen und Methoden des Moduls time**")
print
print ("time.altzone gibt den Offset der lokalen Zeit DST zur UTC-Zeit an")
print ("in Sekunden. Das sind hier -2Stunden also -7200 Sekunden.")
print
print ("       ",time.altzone)
print

print ("Falls daylight ungleich 0, zeigt uns, dass die Zonenzeit sich")
print ("von der UTC-Zeit unterscheidet  ",time.daylight)
print
print ("Die Methode time gibt uns die Unix-Zeit: ", time.time())
print
print ("gmtime gibt uns eine strukturierte (Liste) Information über die UTC-Zeit:")

print ("               ", time.gmtime())
print
print (" localtime gibt uns die lokale Zeit an in strukturierter Ausgabe,")
print (" Liste: ", time.localtime())
print
print (" Ausgabe von Elementen der List: ")
print ("(yyyy,mm,dd,hh,mm,Wochentag,Jahrestag,...)")
print
print (" Wir haben das Jahr: ", time.localtime()[0])
print (" Es ist der ",time.localtime()[1],". Monat.")
print (" In diesem Monat ist es der ",time.localtime()[2],". Tag.")
print (" Uhrzeit: ",time.localtime()[3],":",time.localtime()[4])
print
print (" Andere Ausgabe der Lokalzeit mit time.asctime(t): ", time.asctime(time.localtime()))
print (" Noch eine Möglichkeit, mit time.ctime(): ", time.ctime(time.time()))

print("===================================")
utc = datetime.datetime.utcnow()
utc2= datetime.datetime.strftime(utc, "%Y-%m-%d %H:%M:%S")
now = datetime.datetime.now()
utc3 = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
print(utc)
print(utc2)
print(utc3)
utc3= datetime.datetime.strftime(utc3, "%Y-%m-%d %H:%M:%S%z")
print(utc3)
diff = now - utc
print(diff)
print(datetime.datetime.strftime(now, "%Y-%m-%d %H:%M:%S.%f"))
print(now.strftime("%Y-%m-%d %H:%M:%S"))

from dateutil.tz import tzlocal
# Get the current date/time with the timezone.
now2 = datetime.datetime.now(tzlocal())
fmt1 = now2.strftime('%Y-%m-%d %H:%M:%S %Z')
fmt2 = now2.strftime('%A, %B %d, %Y %Z')
fmt3 = now2.strftime('%Y-%m-%d %H:%M:%S%z')
# Print it out.
print ('fmt1 = %s' % (fmt1))
print ('fmt2 = %s' % (fmt2))
print ('fmt3 = %s' % (fmt3))