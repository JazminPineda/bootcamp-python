from pprint import pprint

def numeros_impares(inicial, final):
    contador = 1
    lista_impar = []
    lista_par = []

    for numero in range(inicial, final):
        if numero % 2 == 1:
            lista_impar.append(numero)
            pass
            
        else:
            lista_par.append(numero)
    pprint(f"Valores impares {lista_impar}")
inic = int(input("Ingresa un numero inicial "))
final = int(input("Ingresa un numero final mayor "))
numeros_impares(inic, final)
