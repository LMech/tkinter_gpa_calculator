import tkinter.ttk as ttk

import background as bg
import weights as w_ds
import operations


def widget_maker(label_text, row_n, column_n, value):
    width_p = 20

    label = ttk.Label(bg.root, text=label_text)
    label.grid(row=row_n, column=column_n, padx=1, pady=4)

    textbox = ttk.Entry(bg.root, width=width_p)
    textbox.grid(row=row_n, column=column_n+1)
    textbox.insert("0", value)
    return textbox


def foreground():

    hours = ttk.Label(bg.root, text='Total passed hours')
    hours.grid(row=1, column=1, padx=2, pady=2)
    cerdit = ttk.Label(bg.root, text='Cerdit')
    cerdit.grid(row=1, column=4, padx=2, pady=2)
    g_textboxes = []
    w_textboxes = []
    for num, key in zip(range(2, len(bg.keys)+2), bg.keys):
        g_textbox = widget_maker(key+' hours', num, 0, 0)
        w_textbox = widget_maker(
            key+' credit', num, 3, w_ds.weights_dict[key])
        g_textboxes.append(g_textbox)
        w_textboxes.append(w_textbox)

    btn_calc = ttk.Button(bg.root, text="Calculate",
                          command=lambda: operations.calc(g_textboxes))
    btn_calc.grid(row=15, column=0)
    btn_res = ttk.Button(bg.root, text="Reset",
                         command=lambda: operations.reset(g_textboxes))
    btn_res.grid(row=16, column=0)
    btn_res = ttk.Button(bg.root, text="Update",
                         command=lambda: operations.update(w_textboxes))
    btn_res.grid(row=16, column=3)
    bg.root.mainloop()
