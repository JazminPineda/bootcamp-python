from vehiculo import Vehiculo

# Es buena practica colocar los parametros clase padre y luego colocar los que creo
class Auto(Vehiculo):
    def __init__(self, motor, ventanas, ruedas, color, marca, carroceria, cilindraje ):
        super().__init__(motor, ventanas, ruedas, color)
        self.marca = marca
        self.carroceria = carroceria
        self.cilindraje = cilindraje
        # self.precio = precio

    def sonido(self):
        return "run runnnn"

    def __str__(self) -> str:
        return super().__str__() + f' {self.marca}  "Cilindra" {self.cilindraje}'
  

class AudiVenta(Auto):
    def __init__(self, motor,ventanas, color,carroceria, cilindraje, precio):
        self.precio = precio
        super().__init__(motor, ventanas, 4, color, "Audi", carroceria, cilindraje)

    def __str__(self) -> str:
        return super().__str__() + f" Precio de venta: {self.precio}"

class AudiA5Full(AudiVenta):
    def __init__(self, color, precio):
        super().__init__("MotorV8", 5,color,'carroceria', '8000 cilindrada', precio)


class AudiStock(Auto):
    def __init__(self, motor, ventanas, ruedas, color, marca, carroceria, cilindraje, costo):
        self.costo = costo
        super().__init__(motor, ventanas, ruedas, color, marca, carroceria, cilindraje)

    def __str__(self) -> str:
        return super().__str__()+ f' Costo: {self.costo}'