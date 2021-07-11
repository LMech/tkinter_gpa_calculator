from ttkthemes import ThemedStyle
import tkinter.font as tkFont
import tkinter as tk

import weights as w_ds

keys = w_ds.weights_dict.keys()

def background():

    root = tk.Tk()
    root.title("GPA Calculator")
    root.geometry("540x520")

    def_font = tkFont.nametofont("TkDefaultFont")
    def_font.config(size=12)

    style = ThemedStyle(root)
    style.set_theme("radiance")
    root.iconbitmap('icon.ico')
    return root

root = background()
