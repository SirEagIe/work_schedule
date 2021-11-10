import tkinter as tk
import calendar as cldr
import datetime as dt
import sqlite3 as sql
import os, sys

class Calendar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        self.now = dt.datetime.date(dt.datetime.today())
        self.current_date = self.now
        self.calendar = cldr.Calendar(firstweekday=0)
        self.form_head()
        self.form_weeks()
        self.form_days()

    def form_head(self):
        self.head = tk.Frame(self, bg='#3300CC')
        self.month_and_year = tk.Label(self.head,
            text=self.current_date.strftime('%B')+', '+self.current_date.strftime('%Y'),
            bg='#6633FF', width=45, height=2)
        self.button_left = tk.Button(self.head, text='<', borderwidth=0, bg='#6633FF')
        self.button_left.config(command=self.left)
        self.button_right = tk.Button(self.head, text='>', borderwidth=0, bg='#6633FF')
        self.button_right.config(command=self.right)
        self.button_left.pack(side='left', fill='both', padx=1, pady=1, expand=True)  
        self.month_and_year.pack(side='left', fill='both', padx=1, pady=1)
        self.button_right.pack(side='left', fill='both', padx=1, pady=1, expand=True)
        self.name_of_weeks_frame = tk.Frame(self, bg='#3300CC')
        self.name_of_weeks = []
        i = 0
        for name_of_week in ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']:
            self.name_of_weeks.append(tk.Label(self.name_of_weeks_frame, text=name_of_week,
                width=7, height=1, bg='#6666FF'))
            self.name_of_weeks[i].pack(side='left', padx=1, pady=1)
            i += 1
        self.head.pack(fill='both')
        self.name_of_weeks_frame.pack(fill='both')
        
    def form_weeks(self):
        num_of_weeks = len(self.calendar.monthdatescalendar(self.current_date.year, self.current_date.month))
        self.weeks = [tk.Frame(self) for i in range(num_of_weeks)]
        for week in self.weeks:
            week.pack(fill='both', expand=True)
            
    def form_days(self):
        self.days = []
        i = 0
        for day in self.calendar.itermonthdates(self.current_date.year, self.current_date.month):
            self.days.append(tk.Label(self.weeks[i//7], text=day.day,
                width=7, height=2, bg='#CCCCCC'))
            if day.year == self.now.year and day.month == self.now.month and day.day == self.now.day:
                self.days[i].config(borderwidth=2, relief='solid')
            if day.month != self.current_date.month:
                self.days[i].config(bg = '#999999')
            i += 1
        for day in self.days:
            day.pack(side='left', fill='both', expand=True, padx=1, pady=1)
    
    def update_(self):
        self.month_and_year.config(text=self.current_date.strftime('%B')+', '+self.current_date.strftime('%Y'))
        num_of_weeks = len(self.calendar.monthdatescalendar(self.current_date.year, self.current_date.month))
        while len(self.weeks) != num_of_weeks:
            if len(self.weeks) > num_of_weeks:
                self.weeks[-1].pack_forget()
                self.weeks.remove(self.weeks[-1])
            elif len(self.weeks) < num_of_weeks:
                self.weeks.append(tk.Frame(self))
                self.weeks[-1].pack(fill='both', expand=True)
        for day in self.days:
            day.destroy()
        self.form_days()
            
    def left(self):
        self.current_date = self.current_date.replace(day=1) - dt.timedelta(days=1)
        self.update_()
        
    def right(self):
        self.current_date = self.current_date.replace(
            day=cldr.monthrange(self.current_date.year, self.current_date.month)[1]) + dt.timedelta(days=1)
        self.update_()


class AddCalendar(Calendar):
    def __init__(self, parent, *args, **kwargs):
        self.choosen_days = []
        Calendar.__init__(self, parent, *args, **kwargs)
        
    def form_days(self):
        super().form_days()
        i = 0
        for day in self.calendar.itermonthdates(self.current_date.year, self.current_date.month):
            if day.month == self.current_date.month:
                if day in self.choosen_days:
                    self.days[i].config(bg = '#6666FF')
                self.days[i].bind('<Button-1>', lambda e, i=i, day=day: self.choose(self.days[i], day))
            i += 1

    def choose(self, label, day):
        if not day in self.choosen_days:
            label.config(bg='#6666FF')
            self.choosen_days.append(day)
        else:
            label.config(bg='#CCCCCC')
            self.choosen_days.remove(day)
    
    def get_choosen(self):
        return self.choosen_days
        
class ViewAllCalendar(Calendar):
    def __init__(self, parent, *args, **kwargs):
        Calendar.__init__(self, parent, *args, **kwargs)
        
        
    def form_days(self):
        super().form_days()
        i = 0
        for day in self.calendar.itermonthdates(self.current_date.year, self.current_date.month):
            if day.month == self.current_date.month:
                self.days[i].bind('<Button-1>', lambda e, i=i, day=day: self.view_schedule(self.days[i], day))
            i += 1
            
    def view_schedule(self, event, day):
        new_window = tk.Toplevel()
        new_window.focus_force()
        schedule_frame = tk.Frame(new_window)
        date_label = tk.Label(schedule_frame, text=day.strftime('%d %B %Y'))
        date_label.grid(row=0, column=0, padx=5, pady=5, columnspan=4)
        schedule = []
        connection = sql.connect(os.path.abspath(os.path.dirname(sys.argv[0])) + '\\app.db')
        with connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM `work_schedule` WHERE date='{day}'")
            rows = list(cursor.fetchall())
            for row in rows:
                schedule.append([tk.Label(schedule_frame, text=str(row[0])),
                    tk.Label(schedule_frame, text=str(row[2])),
                    tk.Label(schedule_frame, text='-'),
                    tk.Label(schedule_frame, text=str(row[3]))])
            if not schedule:
                tk.Label(schedule_frame, text='Записи отсутствуют').grid(row=1, column=0, padx=5, pady=5, columnspan=4)
            for i in range(len(schedule)):
                schedule[i][0].grid(row=i+1, column=0, padx=5, pady=5)
                schedule[i][1].grid(row=i+1, column=1, padx=5, pady=5)
                schedule[i][2].grid(row=i+1, column=2, padx=5, pady=5)
                schedule[i][3].grid(row=i+1, column=3, padx=5, pady=5)
        schedule_frame.pack(expand=True, padx=10, pady=10)
        x_pos = (new_window.winfo_screenwidth() - new_window.winfo_width())//2
        y_pos = (new_window.winfo_screenheight() - new_window.winfo_height())//2
        new_window.geometry('+' + str(x_pos) + '+' + str(y_pos))
        new_window.update()
        new_window.minsize(new_window.winfo_width(), new_window.winfo_height())
        new_window.bind("<Escape>", lambda event: new_window.destroy())