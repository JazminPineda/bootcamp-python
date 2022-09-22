from datetime import datetime, timedelta, time


def hora_actual():
    marca_temporal1 = datetime.now().time() 
    # marca_temporal1.hour, marca_temporal1.minute,
    return ( marca_temporal1)

def calculando_hora(marca_temporal1):
    marca_temporal2 = datetime.now().time().replace(hour=18, minute=00, second=0)
    # print(marca_temporal2,   marca_temporal1)
    
    delta2 = timedelta(hours=marca_temporal2.hour, minutes=marca_temporal2.minute) 
    delta1 = timedelta(hours=marca_temporal1.hour, minutes=marca_temporal1.minute)  
    tiempo = delta2 - delta1 
    respuesta = delta2> delta1 
    if respuesta == "True":
        return f"Ya es salir, vete a casa {tiempo}"
    else:
        return f"Falta para salir {tiempo}"
