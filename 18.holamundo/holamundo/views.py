from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola Mundo")

def despedida(request):
    return HttpResponse("chao!")

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("Eres MAYOR de edad")
    else:
        return HttpResponse("NO Eres MAYOR de edad")
    