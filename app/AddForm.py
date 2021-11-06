import tkinter as tk
from app.Calendar import Calendar

class AddForm(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        self.calendar = Calendar(self)
        self.calendar.pack()
        self.fields_frame = tk.Frame(self)
        self.name_label = tk.Label(self.fields_frame, text="ФИО")
        self.time_label_1 = tk.Label(self.fields_frame, text="Время работы с")
        self.time_label_2 = tk.Label(self.fields_frame, text="до")
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
        print(self.name_entry.get())
        print(self.time_entry_1.get())
        print(self.time_entry_2.get())
        print(self.calendar.get_choosen())
        
    def validate(self, a):
        return True
    