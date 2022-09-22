from difflib import restore
import math
import numpy as np

class Calculadora():
    # cuando quiero inicializar los atributos con parametros

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    # Cuando quiero que se devuelva en string 
    def __str__(self) -> str:
        return f'Operacion: {self.x} + {self.y}'   

    def sumar(self):
        return self.x + self.y 

    def sumari(self):
        return sum(self.x , self.y) 
  
    def restar(self):
        return self.x - self.y 
    
    def multiplicar(self):
        return self.x * self.y 

    def dividir(self):
        return self.x / self.y 

# cuando inicializo sin parametros pero los defino internamente y 
# los puedo cambiar
class Calculadora2():
    x = 0
    y = 0

    def set_x(self, x):
        self.x = int(x)

    def set_y(self, y):
        self.y = int(y)

    def suma_x_y(self):
        return self.x + self.y


def suma(x, y):
    return x + y

def calculadoraSuper():

    lista_numeros = []

    def add_number(self, number):
        lista_numeros.append(number)