import tkinter as tk
from app import MainApplication

root = tk.Tk()
MainApplication(root, highlightbackground="blue", highlightthickness=1).pack(side="top", fill="both", expand=True)
root.mainloop()
