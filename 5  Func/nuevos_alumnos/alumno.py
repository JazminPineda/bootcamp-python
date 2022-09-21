from errno import EAGAIN
from typing import ClassVar
from persona import Persona

class Alumno(Persona):

        
    # def __init__(self, nombre, apellido, dni, fecha_nacimiento, legajo):
    #     super().__init__(nombre, apellido, dni, fecha_nacimiento)
    #     self.legajo = legajo 
    #     self.carrera = None

    def __init__(self, persona :Persona, legajo):
        super().__init__(persona.nombre, persona.apellido, persona.dni, persona.fecha_nacimiento)
        self.legajo = legajo
    
    def establecer_carrera(self, carrera):
        self.carrera = carrera

    #estadisca  def establecer(cls):
    def __str__(self) -> str:
        return super().__str__() + " " + str(self.legajo) + " "+ self.carrera