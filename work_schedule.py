import tkinter as tk
from app import MainApplication

root = tk.Tk()
MainApplication(root).pack(side="top", fill="both", expand=True)
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()
