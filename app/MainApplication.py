import tkinter as tk
from app.TabsList import TabsList
from app.FirstTab import FirstTab
from app.SecondTab import SecondTab

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame .__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.tabs_list = TabsList(self, 'Добавить', 'Общий график работы', 'График работы')
        self.tabs_list.pack(fill='both')
        for i in range(len(self.tabs_list.get_tabs())):
            self.tabs_list.get_tabs()[i].bind('<Button-1>', lambda e, i=i: self.view_tab(i))
        self.tabs = []
        self.tabs.append(FirstTab(self))
        self.tabs.append(SecondTab(self))
        self.tabs[0].pack(fill='both', expand=True)
   
    def view_tab(self, i):
        for j in range(len(self.tabs)):
            if j != i:
                self.tabs[j].pack_forget()
            else:
                self.tabs[j].pack(fill='both', expand=True)