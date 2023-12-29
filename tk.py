from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

# root = TK()
root.title("TTK Bootstrap!")
root.iconbitmap('my_icon.ico')
root.geometry("500x350")

# Create a function for the button

# Colors:
# default, primary, secondary, success, info, warning, danger, light, dark

# Create a Label
my_label = tb.Label(root, text="Hello World!", font=("Arial", 28), bootstyle="success, inverse")
my_label.pack(pady=50)

# Create a Button
my_button = tb.Button(root, text="Click Me!", bootstyle="primary, outline")
my_button.pack(pady=20)

root.mainloop()
