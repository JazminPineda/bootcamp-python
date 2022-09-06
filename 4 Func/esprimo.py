from ast import Return
import math
import numpy as np 
import seaborn as sns
import pandas as pd

def esprimo(num):
    #Partimos de una lista de números que van de  2  hasta un determinado número
    for i in range(2 , int(num/2)):
        #Eliminamos de la lista los múltiplos de  2.
        if num % i == 0:
             resultado = "número compuesto"
           
        else:
            resultado = "número primo"

    return resultado

def cuadrado(num):
    for i in range(2, int(math.sqrt(num)+1)): #sqrt cuadrado luego se convierte en numero entero  
        if (num % i) == 0:
            return False
    return True


num1 = int(input("Ingresa un número "))


#O(n) and O(√n) Visually
# def visually():
#     n = 20
#     x = np.arange(n)
#     y1 = np.sqrt(x)
#     y2 = x
#     df = pd.DataFrame({"O(√n)":y1,"O(n)":y2})
#     sns.set_theme()
#     sns.lineplot(data = df)

# print(esprimo(num1), f"El número es primo? {cuadrado(num1)}", )
# print(visually())
