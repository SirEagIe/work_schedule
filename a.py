import calendar as cldr
import datetime as dt

c = cldr.Calendar(firstweekday=0)
print(len(c.monthdatescalendar(2021, 11)))