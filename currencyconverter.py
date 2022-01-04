import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests

root = Tk()


# Conversion of the parsed value with the API.
def conversionOf(parsed_amount,fromC, toC):
    api_url = r"http://api.exchangeratesapi.io/v1/latest?access_key=c45f716cf519784b160f1ca3b7144073"
    result = requests.get(api_url).json()
    amount = parsed_amount / float(result["rates"][fromC])
    rate = float(result["rates"][toC])
    return amount * rate


# Parsing Value.
def onConvert():
    parsed_amount = float(fromC_parse.get())
    fromC = from_drop.get()
    toC = to_drop.get()

    anstobox = conversionOf(parsed_amount, fromC, toC)
    toC_parse.set(round(anstobox, 3))


# Fn called when "Convert Currency" is pressed in Main Menu.
def onClick():

    # Creates a new Window and closes the root(Main Menu) window.
    convertWindow = Tk()
    convertWindow.geometry("500x400")
    root.destroy()

    # Entry Boxes are initialized here.
    global fromC_parse
    fromC_parse = tkinter.StringVar(convertWindow)
    fromC_txt = Label(convertWindow, text="From Currency :  ", font=("Times New Roman", 16, "bold"))
    fromC_txt.place(relx=0.12, rely=0.2)

    fromC_box = Entry(convertWindow, width=25, textvariable=fromC_parse)
    fromC_box.insert(0, "0.0")
    fromC_box.place(in_=fromC_txt, relx=1, rely=0.15, height=25)

    global toC_parse
    toC_parse = tkinter.StringVar(convertWindow)
    toC_txt = Label(convertWindow, text="To Currency :  ", font=("Times New Roman", 16, "bold"))
    toC_txt.place(relx=0.12, rely=0.35)

    toC_box = Entry(convertWindow, state="readonly", width=25, textvariable=toC_parse)
    toC_box.place(in_=toC_txt, relx=1.19, rely=0.15, height=25)

    # Creates Dropdown boxes for currency selection
    selection = ["INR", "USD", "CAD", "CNY", "DKK", "EUR", "SGD"]
    global from_drop, to_drop
    from_drop = ttk.Combobox(convertWindow, values=selection, width=5, state="readonly")
    to_drop = ttk.Combobox(convertWindow, values=selection, width=5, state="readonly")

    from_drop.current(1)    # Sets Defaults
    to_drop.current(0)

    from_drop.place(in_=fromC_box, relx=1.1)    # Places Dropdown boxes
    to_drop.place(in_=toC_box, relx=1.1)

    # Makes a Calculate button.
    calc = Button(convertWindow, text="Convert!", command=onConvert, padx=10, pady=5, font=("Times New Roman", 16, "bold"))
    calc.place(relx=0.5, rely=0.6, anchor="center")


# Fn called when "Information" is pressed in Main Menu.
def onInfo():
    messagebox.showinfo("Info", message="This is a GUI Application created by Madhav Ram, using Python with Tkinter")


# Fn called when "Exit Application" is pressed in Main Menu.
def onExit():
    ans = messagebox.askyesno("Confirmation", message="Do you really want to EXIT?")
    if ans == TRUE:
        root.destroy()
    else:
        return None


# Defines the window shape and title for the Main Menu window.
root.title("Currency Converter GUI - Main Menu")
root.geometry("400x400")
Title = Label(root, text="Currency Converter", pady=10, font=("Times New Roman", 26, "bold"), anchor="center")
Title.pack()

# Buttons of the Main Menu:
MainMenu = Button(root, text="Convert Currency", command=onClick, padx=5, pady=5, anchor="center", font=("Times New Roman", 16, "bold"), width=15)
MainMenu.place(relx=0.27, rely=0.35)

Info = Button(root, text="Information", command=onInfo, padx=5, pady=5, anchor="center", font=("Times New Roman", 16, "bold"), width=15)
Info.place(relx=0.27, rely=0.5)

Exit = Button(root, text="Exit Application", command=onExit, padx=5, pady=5, anchor="center", font=("Times New Roman", 16, "bold"), width=15)
Exit.place(relx=0.27, rely=0.65)


root.mainloop()
