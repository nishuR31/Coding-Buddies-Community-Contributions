from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Fasil's Digital Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)
    
label = Label(root, font = ("open_24_display_st", 40), background = "black", foreground = "cyan")
label.pack(anchor = 'center')
time()
mainloop()