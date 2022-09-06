import calendar

def añobisiesto(año):
    #Es multiplo de 4?
    not año % 4 and (año % 100 or not año % 400)
    
    return False


año = int(input("Escribe un año para comprobar si es bisiesto "))

if año % 4 != 0: #no divisible entre cuatro
    print("No es bisiesto ")
elif año % 4 == 0 and año % 100 != 0 or año % 400 !=0: #divisiblen en 4 y no entre 100 o 400
    print("Es bisiesto ")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: #divisiblen en 4 y 10 y no entre 400
    print("No es bisiesto ")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisiblen en 4 y 10 y no entre 400
    print("Es bisiesto ")

respuesta = añobisiesto(año)
respuesta_metodo = calendar.isleap(año)


print(f"El año {año} es bisiesto? {respuesta_metodo}" )


if año == True:
    print("Es bisiesto")
else:
    print("No es bisiesto")