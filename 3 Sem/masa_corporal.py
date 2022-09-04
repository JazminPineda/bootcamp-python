import math 

peso = int(input("Ingresa tu peso "))
altura = float(input("Ingresa tu altura "))
masaCorporal = peso/(math.pow(altura, 2)) 
masaCorporal = round(masaCorporal, 2)
print(f"Tu indice de masa corporal es: {masaCorporal}")