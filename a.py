import calendar as cldr
import datetime as dt

now = dt.datetime.today()
calendar = cldr.Calendar(firstweekday=0)
for day in calendar.itermonthdates(2021, 11):
    print(day.day)