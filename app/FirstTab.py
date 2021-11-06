import tkinter as tk
from app.AddForm import AddForm

class FirstTab(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        tk.LabelFrame.__init__(self, parent, **kwargs)
        self.add_form = AddForm(self)
        self.add_form.pack(side='top', expand=True)