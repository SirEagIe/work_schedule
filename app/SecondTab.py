import tkinter as tk
from app.ViewAllForm import ViewAllForm

class SecondTab(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        tk.LabelFrame.__init__(self, parent, **kwargs)
        self.view_all_form = ViewAllForm(self)
        self.view_all_form.pack(side='top', expand=True)