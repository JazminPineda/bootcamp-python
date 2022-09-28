from distutils.cmd import Command
import logging
from msilib.schema import CheckBox

import sys
import tkinter
from tkinter import ttk

window = tkinter.Tk()

# def reiniciar(event):
#     print("reiniciado")
    
    # # se coloca la columna y la configuracion para el indice y cuantas columnas
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=4)


selecciona = tkinter.StringVar()
# checkbox = ttk.Checkbutton(window, text="",
r1 = ttk.Radiobutton(window, text='Si', value ='1', variable=selecciona )
r2 = ttk.Radiobutton(window, text='No', value ='2', variable=selecciona )
r3 = ttk.Radiobutton(window, text='Quizas', value ='3', variable=selecciona )


r1.grid(row=1, column=0, pady=2, padx=4)
r2.grid(row=2, column=0, pady=2, padx=4)
r3.grid(row=3, column=0, pady=2, padx=4)


botonReiniciar = tkinter.Button(window, text="Haz click para reiniciar")
botonReiniciar.grid(row=4, column=0, pady=2, padx=4)
# botonReiniciar.pack()
def mi_funcion(event):
    selecciona.set("")
    print("Hola mundo!")
botonReiniciar.bind('<Button-1>',mi_funcion)# asocia accion 
#window.quit()

window.mainloop()

sys.exit(0)

# listas

# lista_paises= ['arabia', 'peru', 'colombia', 'peru','arabia', 'peru', 'colombia', 'peru']
# #se convierte la lista al formato ttk
# lista_items = tkinter.StringVar(value=lista_paises)
# Listbox = tkinter.Listbox(window, height=100, listvariable=lista_items)
# Listbox.grid(row=0, column=0, sticky=tkinter.W)
# window.mainloop()

# sys.exit(0)


# #Boton
# logging_button =ttk.Button(window,text="Login",command=0)
# logging_button.grid(row=3, column=1, sticky=tkinter.W, padx=5, pady=5)







# letras fijas

username_label = ttk.Label(window, text="User Name", font="")
username_label.grid(row=0, column=0, sticky=tkinter.W, padx=5, pady=5)

password_label = ttk.Label(window, text="Password", font="")
password_label.grid(row=1, column=0, sticky=tkinter.W, padx=5, pady=5)


#Ingreso del usuario
username_entry = ttk.Entry(window) #entrada de texto
username_entry.grid(row=0, column=1, sticky=tkinter.E, padx=5, pady=5)

password_entry = ttk.Entry(window, show='*') #entrada de texto
password_entry.grid(row=1, column=1, sticky=tkinter.E, padx=5, pady=5)




