from operaciones import Calculadora, Calculadora2, suma

def main():
    calculadora = Calculadora(5,8)
    sum = calculadora.sumar()
    res = calculadora.restar()
    mult = calculadora.multiplicar()
    div = calculadora.dividir()
    # se accede a los atributos con con cada uno
    print(calculadora.x , "operaciones")
    # Utilizo el metodo str
    print(calculadora)
    
    print(f'La suma es {sum}')
    print(f'La resta es {res}')
    print(f'La multiplicar es {mult}')
    print(f'La dividir es {div}')


    calc2 = Calculadora2()
    z = int(input("ingres numero 1"))
    d = int(input("ingres numero 2"))
    calc2.set_x(z)
    calc2.set_y(d)


    
    print(calc2.suma_x_y())
    calc2.set_x(3)
    calc2.set_y(9)
    print(calc2.suma_x_y())
    
    print(suma(5,9))
   
if __name__ == "__main__":
    main()
