from msilib.schema import Class


class Carrera():
    def __init__(self, nombre_carrera):
        self.nombre_carrera = nombre_carrera
        self.materias = []
    def __str__(self):
        return self.nombre_carrera
# Aca se definee metodos para componer, es el caso de que puedo 
# agregar o quitar varia materia
    def quitar_materia(self, materia):
        self.materias.pop(materia)
    
    def agregar_materia(self, materia):
        self.materias.append(materia)

    def mostrar_materia(self):
        for materia in self.materias:
            print(materia)
