import tkinter as tk
from app.TabsList import TabsList
from app.FirstTab import FirstTab

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame .__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.tabs_list = TabsList(self, 'Добавить', 'Общий график работы', 'График работы')
        self.tabs_list.pack(fill="both")
        self.f_tab = FirstTab(self)
        self.f_tab.pack(fill="both", expand=True)