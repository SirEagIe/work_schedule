import tkinter as tk
from app.TabsList import TabsList

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.tabs_list = TabsList(self, 'Главная', 'Не главная', 'Ещё какая-нибудь', 'И ещё какая-нибудь')
        self.tabs_list.pack()
