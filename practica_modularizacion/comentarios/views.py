from django.shortcuts import render
from django.http import HttpResponse
from .models import Comentario

def test(request):
    return HttpResponse("Funciona correctamente")

def create(request):
    # comment = Comentario(name= "Jaz", score=5, comentario="se puede" ) 
    # comment.save()

    # Otra instruccion distinta
    # comment = Comentario.objects.create(name= "Luc", score=, comentario="vamos")
    return HttpResponse("creacion de modelo")


def delete(request):
    # se tiene que buscar objeto 
    # comment = Comentario.objects.get(id=1)
    # comment.delete()

    # Forma directa
    comment = Comentario.objects.filter(id=2).delete()

    return HttpResponse("Se a borrado tu comentario")