class Persona():
    
    def __init__(self, nombre, apellido, dni, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} {self.dni}'

    
    # def calcula_edad(self):
    #     edad = today - fecha_nacimiento
    #     return edad 