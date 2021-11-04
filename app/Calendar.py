import tkinter as tk
import calendar as cldr
import datetime as dt

class Calendar(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        tk.LabelFrame.__init__(self, parent, **kwargs)
        self.now = dt.datetime.today()
        self.calendar = cldr.Calendar(firstweekday=0)
        self.month_and_year = tk.Label(self, text=self.now.strftime('%B')+', '+self.now.strftime('%Y'), bg='green')
        self.month_and_year.pack(fill='both')
        self.days = []
        self.weeks = []
        for i in range(5):
            self.weeks.append(tk.Frame(self))
        i = 0
        for day in self.calendar.itermonthdates(self.now.year, self.now.month):
            self.days.append(tk.Label(self.weeks[i//7], text=day.day, width=7, height=2, bg='white'))
            if day.month != self.now.month:
                self.days[i].config(bg = 'gray')
            i += 1
        for week in self.weeks:
            week.pack(fill="both", expand=True)
        for day in self.days:
            day.pack(side='left', fill="both", expand=True)