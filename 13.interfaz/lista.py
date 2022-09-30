import sys
import tkinter
from tkinter import ttk


lista_paises= ["arabia", "peru", "colombia", "argentina", "peru", "ecuador", "mexico", "venezuela", "panama",  "peru", "colombia", "argentina"]
lista_paises= map(str.upper, lista_paises)

lista_final  = set(lista_paises)
ordenada = sorted(lista_final)

window = tkinter.Tk()
# label = tkinter.Label(window, text="Elige un pais", bg="blue", fg="white")
window.columnconfigure(0, weight=1)
usar_label = ttk.Label(window, text="Elige un pais")
usar_label.grid(row=1, column=0, sticky=tkinter.W, padx=2, pady=2)

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=4)


#se convierte la lista al formato ttk

lista_items = tkinter.StringVar(value=ordenada)
Listbox = tkinter.Listbox(window, height=10, listvariable=lista_items)
Listbox.grid(row=2, column=0, sticky=tkinter.W)

window.mainloop()

sys.exit(0)