import tkinter as tk
from tkinter import *


window = Tk()
window.title("DEMO")
window.geometry("400x200")
window.maxsize(600, 600)
window.minsize(200, 200)

lbl = Label(window,
            padx="2c",
            bg="lightblue",
            fg="white",
            font=("Arial Bold", 20),
            text="""Hello World!
    This is the
    demonstration of""")
lbl.grid(column=0, row=0)
window.mainloop()
