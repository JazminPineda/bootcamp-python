from unicodedata import numeric

#las clases dinamicas tiene como parametro self, se crea instancia
#cada una reserva un espacio de memoria independiente de una instancia a otra instancia 
# solo manipula unicamente las de esa instancia, el resto de instancias no se manipulan  
class Vehiculo:

    def __init__(self):
        self.ruedas = 4
        self.puertas = 2
        self._color = "verde"

    
    @property
    def color(self):  # obtener
        return self._color

    @color.setter  
    def color(self, nombre ):  # establecer
        self._color = nombre   
  

class Coche(Vehiculo):#clase base que se hereda 
    _cilindraje = 1500
    veloz = 1000
    
    @property
    def capacidad(self): 
        return self._cilindraje 
    
    @capacidad.setter
    def capacidad(self, cantidad):
        self._cilindraje = cantidad
       
    def velocidad(self):
        Coche.veloz = 300
      

camioneta = Coche()
camioneta.color = "Amarillo"
color = input("ingrese color: ")
camioneta.color = color 
cilindraje = input("ingrese cilindraje requerido: ")
camioneta.capacidad = cilindraje

print(camioneta.color, "Color")
print(camioneta.ruedas, "Ruedas")
print(camioneta.puertas, "Puertas")
print(camioneta.veloz, "velocidad")
print(camioneta.capacidad, "cilindraje")

#Clase Estatica, NO tiene self comparten el mismo espacio de memoria 
#La clase estática comparte un mismo espacio de memoria, es único y compartido, por eso las variables internamente se van a manipular
class Seguro():
    numero = 50000
    def incremento_anual():
        Seguro.numero*=2




Seguro.incremento_anual() #se incova directamente 
print(Seguro.numero, "año 1")
Seguro.incremento_anual()
print(Seguro.numero, "año 2")
Seguro.incremento_anual()
print(Seguro.numero, "año 3")
coche = Coche()

# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.


