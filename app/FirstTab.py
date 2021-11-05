import tkinter as tk
from app.Calendar import Calendar

class FirstTab(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        tk.LabelFrame.__init__(self, parent, **kwargs)
        self.calendar = Calendar(self)
        self.calendar.pack()