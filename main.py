import tkinter as tk
from tkinter import ttk
import requests


def money_conv(m, from_curr, to_curr):
    api_url = r"http://api.exchangeratesapi.io/v1/latest?access_key=c45f716cf519784b160f1ca3b7144073"
    result = requests.get(api_url).json()
    #print(result)
    new_m = m / (float(result["rates"][from_curr]))
    rate = float(result["rates"][to_curr])
    return new_m * rate


def convert():
    m = int(from_curr_txt.get())
    from_curr = from_drop.get()
    to_curr = to_drop.get()

    conv_m = money_conv(m, from_curr, to_curr)
    to_curr_txt.set(round(conv_m, 3))


top = tk.Tk()
top.geometry("800x800")
top.title("Currency Convertor")
title = tk.Label(top, text="Currency Convertor")
title.config(font=("Times New Roman", 20, 'bold'))

from_curr_txt = tk.StringVar()
from_curr_label = tk.Label(top, text='From Currency: ', font=('Times New Roman', 15))
from_curr_entry = tk.Entry(top, textvariable=from_curr_txt, font=('Times New Roman', 15, 'normal'))

to_curr_txt = tk.StringVar()
to_curr_label = tk.Label(top, text='To Currency: ', font=('Times New Roman', 15))
to_curr_entry = tk.Entry(top, state='readonly', textvariable=to_curr_txt, font=('Times New Roman', 15, 'normal'))

title.place(relx=0.5, rely=0.1, anchor='center')

from_curr_label.place(relx=0.4, rely=0.2, anchor='center')
from_curr_entry.place(in_=from_curr_label, relx=1.1)

to_curr_label.place(relx=0.4, rely=0.35, anchor='center')
to_curr_entry.place(in_=to_curr_label, relx=1.1)


conv_opt = ["INR", "USD", "CAD", "CNY", "DKK", "EUR", "SGD"]
from_drop = ttk.Combobox(top, values=conv_opt, width=5, state="readonly")
to_drop = ttk.Combobox(top, values=conv_opt, width=5, state="readonly")

from_drop.current(1)
to_drop.current(0)

from_drop.place(in_=from_curr_entry, relx=1.1)
to_drop.place(in_=to_curr_entry, relx=1.1)

conv_but = tk.Button(top, text='Convert', command=convert, font=('Times New Roman', 16))
conv_but.place(relx=0.5, rely=0.5, anchor='center')

top.mainloop()
