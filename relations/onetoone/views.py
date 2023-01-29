from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

def create(request):
    #  creacion de los elementos
    place = Place(name="Lugar 1",  address= "Calle demo")
    place.save()
    
    restaurant = Restaurant(place= place, number_of_employees=8)
    restaurant.save()

    # se puede guardar y devolver el atributo 
    return HttpResponse(restaurant.place.name)
    
