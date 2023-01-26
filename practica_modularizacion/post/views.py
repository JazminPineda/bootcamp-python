from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entrý

# se alcanza la vista sobre la consulta
def queries(request):
    
    # Obtener todos los elementos 
    authors = Author.objects.all()

    # Obtener UN limitE a solo 10 autores

    limites = Author.objects.all()[:10]


    #   Obtener filtros por dondicion
    filtered = Author.objects.filter(email = 'dana71@example.net')


    #  Obtener un único objeto?
    author =  Author.objects.get(id=1)


    ordenes = Author.objects.all().order_by('email')



    # Se Obtiene  el valor cuyo valor de id sea 15 y tampoco se puede colocar < >
    filteres2 = Author.objects.filter(id=15) 
    

    # Obtener todos los elementos cuyo valor de emial  sea <= 15
    # se debe añadir doble barra y especificar las iniciales del operador o modificador de la busque que se desea hacer
    # debe ser en ingles menor igual ltd 
    
    filteres3 = Author.objects.filter(id__lte =3)
    

    # Obtener todos los autores que contienen en su nombre la palabra yes

    contener = Author.objects.filter(name__contains='try')

    # se guardan y se paa a la vista del contexto
    return render(request, 'post/queries.html', {'authors': authors, 'filtered':filtered, 'author':author, 'filtered':filtered, 'limites': limites, 'ordenes':ordenes, 'filteres3':filteres3, 'contener':contener })