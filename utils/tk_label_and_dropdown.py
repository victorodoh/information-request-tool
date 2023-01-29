from tkinter import *

def tkinter_label (window, text, x, y):
    tk_label = Label(window, text=text, font=("Times new romans", 12))
    tk_label.place( x=x, y=y)
    
    return tk_label

def tkinter_menu_dropdown(window, val, args, x, y):
    
    tk_drop_down = OptionMenu(window, val, *args)
    tk_drop_down.place(x=x, y=y)
    
    return tk_drop_down