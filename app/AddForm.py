import tkinter as tk
from tkinter import messagebox
import re
import sqlite3 as sql
from app.Calendar import Calendar

class AddForm(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        self.calendar = Calendar(self)
        self.calendar.pack()
        self.fields_frame = tk.Frame(self)
        self.name_label = tk.Label(self.fields_frame, text="ФИО")
        self.time_label_1 = tk.Label(self.fields_frame, text="Время работы с (HH:MM)")
        self.time_label_2 = tk.Label(self.fields_frame, text="до (HH:MM)")
        self.name_entry = tk.Entry(self.fields_frame)
        self.time_entry_1 = tk.Entry(self.fields_frame)
        self.time_entry_2 = tk.Entry(self.fields_frame)
        self.apply_btn = tk.Button(self.fields_frame, text='Добавить', command=self.add)
        self.name_label.grid(row=0, column=0)
        self.time_label_1.grid(row=1, column=0)
        self.time_label_2.grid(row=2, column=0)
        self.name_entry.grid(row=0, column=1)
        self.time_entry_1.grid(row=1, column=1)
        self.time_entry_2.grid(row=2, column=1)
        self.apply_btn.grid(row=3, column=0, columnspan=2)
        self.fields_frame.pack()

    def add(self):
        message_error = ''
        dates = []
        if not self.calendar.get_choosen():
            message_error += 'Дата не выбрана\n'
        else:
            dates = self.calendar.get_choosen()
        name = ''
        if self.validate_name(self.name_entry.get()):
            name = self.name_entry.get()
        else:
            message_error += 'Имя не введено\n'
        time1, time2 = '', ''
        if self.validate_time(self.time_entry_1.get()) and self.validate_time(self.time_entry_2.get()):
            time1 = self.time_entry_1.get()
            time2 = self.time_entry_2.get()
        else:
            message_error += 'Время введено неверно\n'
        if message_error:
            tk.messagebox.showerror(title='Error', message=message_error)
        else:
            connection = sql.connect('test.db')
            with connection:
                cursor = connection.cursor()
                for date in dates:
                    cursor.execute(f"INSERT INTO `test` VALUES ('{name}', '{date}', '{time1}', '{time2}')")
                connection.commit()
        
    def validate_name(self, name):
        if name:
            return True
        else:
            return False
    
    def validate_time(self, time):
        tpl = '^[0-2][0-9]:[0-5][0-9]$'
        if re.match(tpl, time):
            return True
        else:
            return False
        