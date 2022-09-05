import math

def areaTriangulo(b= 4, h = 3 ):
    return b * h / 2

def areaTriang_equilatero(a, b, c=15 ):
    p = (a * b * c )
    s = math.pi *4
    return round(p/ s ,2)

def area_angulo_agudo( a,  angulo = 89,):
    h = a * math.sin(angulo)
    s = (a * h * math.sin(angulo))/2
    return round(s, 5) 

def circulo():
    return lambda radio : math.pi * radio**2

        
area_triangulo = areaTriangulo(4,3)
triang_rectangulo = areaTriang_equilatero(4, 6)
triang_Equilatero = area_angulo_agudo(5)
radio_cir = circulo() #puntero de funcion 
radio_lambda = lambda radio : math.pi * radio **2

print(f"El área de un triangulo es {area_triangulo}, \n \
        El área de un triangulo Rectángulo es {triang_rectangulo}, \n \
        El área de un triangulo Equilátero es {triang_Equilatero}, \n \
        El área de un circulo  es {radio_cir.__call__(5)}" )
print(f"Soy radio lambda aqui hablando {radio_lambda(5)}")

