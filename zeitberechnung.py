#!/usr/bin/python
# Spielereien mit der Zeit

import datetime

datum = datetime.date.today()
dtime = datetime.datetime.now()

print(str(datum.day) + "." + str(datum.month) + "." + str(datum.year))
print(str(dtime.hour) + ":" + str(dtime.minute) + ":" + str(dtime.second))
print(datum)
print(dtime)