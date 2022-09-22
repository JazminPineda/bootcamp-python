from cgitb import reset
import math

def sumar(lista):
    resultado = 0
    for numer  in range(0, len(lista)):
        resultado += lista[numer]
    return resultado
    
 