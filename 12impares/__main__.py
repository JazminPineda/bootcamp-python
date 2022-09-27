from impares import es_impar
from sumatoria import sumar_lambda
def main():
    
    lista_impare =[3,45,78,45,658,45,12,45,84,52,1,2,3,4,5,6,7]
    resultado = es_impar(lista_impare)
    sumando_impares = sumar_lambda(resultado)
    print(f'Lista de números impares es: {resultado }')
    print(f'la sumatoria de los números impares es: {sumando_impares}')

if __name__ == "__main__":
    main()