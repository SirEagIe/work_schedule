import tkinter as tk
import calendar as cldr
import datetime as dt

class Calendar(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        tk.LabelFrame.__init__(self, parent, **kwargs)
        self.now = dt.datetime.date(dt.datetime.today())
        self.current_date = self.now
        self.calendar = cldr.Calendar(firstweekday=0)
        self.choosen_days = []
        self.form()

    # TODO: переделать, оптимизировать
    def form(self):
        self.head = tk.Frame(self)
        self.month_and_year = tk.Label(self.head,
            text=self.current_date.strftime('%B')+', '+self.current_date.strftime('%Y'),
            bg='green', width=45)
        self.button_left = tk.Button(self.head, text="<")
        self.button_left.config(command=self.left)
        self.button_right = tk.Button(self.head, text=">")
        self.button_right.config(command=self.right)
        self.button_left.pack(side='left', fill="both", expand=True)
        self.month_and_year.pack(side='left', fill='both')
        self.button_right.pack(side='right', fill="both", expand=True)
        self.head.pack(fill='both')
        self.days = []
        self.weeks = [tk.Frame(self) for i in range(len(self.calendar.monthdatescalendar(self.current_date.year, self.current_date.month)))]
        i = 0
        for day in self.calendar.itermonthdates(self.current_date.year, self.current_date.month):
            self.days.append(tk.Label(self.weeks[i//7], text=day.day, width=7, height=2, bg='white'))
            if day.month == self.current_date.month:
                self.days[i].bind('<Button-1>', lambda e, i=i, day=day: self.choose(self.days[i], day))
            if day.year == self.now.year and day.month == self.now.month and day.day == self.now.day:
                self.days[i].config(bg = 'red')
            if day in self.choosen_days:
                self.days[i].config(bg = 'blue')
            if day.month != self.current_date.month:
                self.days[i].config(bg = 'gray')
            i += 1
        for week in self.weeks:
            week.pack(fill="both", expand=True)
        for day in self.days:
            day.pack(side='left', fill="both", expand=True)
        
    def left(self):
        for day in self.days:
            day.destroy()
        for week in self.weeks:
            week.destroy()
        self.month_and_year.destroy()
        self.button_left.destroy()
        self.button_right.destroy()
        self.head.destroy()
        self.update()
        if self.current_date.month != 1:
            self.current_date = dt.date(self.current_date.year, self.current_date.month - 1, 1)
        else:
            self.current_date = dt.date(self.current_date.year - 1, self.current_date.month + 11, 1)
        self.form()
        
    def right(self):
        for day in self.days:
            day.destroy()
        for week in self.weeks:
            week.destroy()
        self.month_and_year.destroy()
        self.button_left.destroy()
        self.button_right.destroy()
        self.head.destroy()
        self.update()
        if self.current_date.month != 12:
            self.current_date = dt.date(self.current_date.year, self.current_date.month + 1, 1)
        else:
            self.current_date = dt.date(self.current_date.year + 1, 1, 1)
        self.form()
        
    def choose(self, label, day):
        if not day in self.choosen_days:
            label.config(bg='blue')
            self.choosen_days.append(day)
        else:
            label.config(bg='white')
            if day == self.now:
                label.config(bg='red')
            self.choosen_days.remove(day)
    
    def get_choosen(self):
        return self.choosen_days