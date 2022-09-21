class Alumno:
    def __init__(self, name, carrera):
        self.name = name
        self.carrera = carrera
       
    
    def __str__(self):
        return f'{self.name} {self.carrera}'
    
    def id_interno(self):
        id = 45356
        id += 1
    

    def materias(self):
        materias ={
            'programacion': 0,
            'estadistica' : 0,
            'base_de_datos' : 0,
        }