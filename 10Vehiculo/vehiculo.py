from abc import abstractmethod


class Vehiculo:
    
    def __init__(self, motor, ventanas, ruedas, color):
        self.motor = motor
        self.ventanas = ventanas
        self.ruedas = ruedas
        self.color = color
      

    def set_motor(self):
        self.motor

  
    def set_ruedas(self):
        self.ruedas
    

    def set_cambiarcolor(self):
        self.color = "azul"

    @abstractmethod
    def sonido(self):
        pass

    def __str__(self) -> str:
        return f'{self.motor} {self.ventanas} {self.ruedas} {self.color}'