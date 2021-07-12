import tkinter.ttk as ttk
from tkinter import messagebox

import weights as w_ds
import background as bg


gpa_label = ttk.Label(bg.root, text="GPA")
gpa_label.grid(row=15, column=1)
total_label = ttk.Label(bg.root, text="Total hours")
total_label.grid(row=15, column=3)

def calc(textboxes, total_h=0, total_w=0):
    for textbox, key in zip(textboxes, bg.keys):
        char = textbox.get()
        if (not char.isdigit()):
            messagebox.showerror('Invalid data type', 'Please, use digits')
            break
        number_h = int(char)
        
        total_h += number_h
        total_w += number_h * w_ds.weights_dict[key]


    if (total_w <= 0):
        messagebox.showerror('Invalid values', 'Please, use valid values')
        
    gpa = total_w/total_h
    total_p = total_h - int(textboxes[-1].get())
    gpa_label.configure(text=round(gpa, 2))
    total_label.configure(text=(total_p))
    
def reset(textboxes):
    for textbox in textboxes:
        textbox.delete(0, "end")
        textbox.insert(0, "0")
    gpa_label.configure(text="GPA")
    total_label.configure(text="Total passed hours")
    
def update(textboxes):
    for key, textbox in zip(bg.keys, textboxes):
        char = textbox.get()
        if (not char.replace('.', '', 1).isdigit()):
            messagebox.showerror('Invalid data type', 'Please, use digits')
        w_ds.weights_dict[key]=float(textbox.get())
