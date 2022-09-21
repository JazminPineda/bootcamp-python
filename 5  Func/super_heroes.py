from superheroe import Superheroe
from arma import Arma

  
martillo = Arma("Martillo", 36, 4)
hacha = Arma("hacha", 4, 5)
# Se crea un objeto que se agrega en la creación de otro objeto
# esto es compocisión

thor = Superheroe("tHOR", 20, 3, True, martillo)
hulk = Superheroe("Huir", 20, 5, False, hacha)

print("salud hulk", hulk.salud)
thor.atacar(hulk)
print("salud hulk", hulk.salud)
print("resistencia martillo", martillo.resistencia)