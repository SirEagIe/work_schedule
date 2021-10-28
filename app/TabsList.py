import tkinter as tk

class TabsList(tk.Frame):
    def __init__(self, parent, *args):
        self.tabs = []
        self.num_of_tabs = len(args)
        for i in range(0, self.num_of_tabs):
            self.tabs.append(tk.Label(parent, text=args[i], width=30, height=10, bg="lightgreen"))
    
    def pack(self):
        for i in range(0, self.num_of_tabs):
            self.tabs[i].pack(side="left", fill="both", expand=True)
