from tkinter.tix import InputOnly
from wsgiref.validate import validator


lista_paises = []

pais = input("Ingresa un pais ")

while pais != "":
    
    if pais in lista_paises:
       
       pais = input(f"El pais esta en la lista, {lista_paises} ingrese otro pais ")

    if pais not in lista_paises:
       lista_paises.append(pais)       
        
ordenada = sorted(lista_paises)
    
print(f'fin programa {ordenada}')