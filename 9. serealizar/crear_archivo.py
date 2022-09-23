import os 

class Archivo():
    def __init__(self, name_archivo, modo):
        self.name_archivo = name_archivo
        self.modo = modo
    
    def creando(self):
        ruta = ''
        archivo  = open(self.name_archivo, "a+")
    
    
    def __str__(self):
        return "Arhivo creado" % (self. name_archivo)

        