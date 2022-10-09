from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre
def index(request):
    # Del modlo Book obtiene los datos q son objetos cuentas todos
    # Se conecta a la base de datos y se obtiene la información 
    num_books = Book.objects.all().count()
    # numero instancias
    num_instances = BookInstance.objects.all().count()
    # status__exact un ampo estado sea exactamente
    disponibles = BookInstance.objects.filter(status__exact='a').count()
    num_authores = Author.objects.all().count()
    # se tiene que devolver un render, luego le decimos q fichero,
    #  la plantilla que muestra el contenido 
    # luego como estan estos datos q son dicc se define con context
  
    # Se prepara el contexto va tener disponbile la variable
    # Esto quiere decir que cuando dispare la funcion index, cuando la ruta
    # se llama la funcion index dentro de views, la cual va obtener cierta informaición
    # esa informac la muestra en el fichero index.html, ademas tiene unos datos lo cuales 
    # los puede utilizar a la hora de mostrarse en pantalla 
    return render(
        request,
        "index.html", 
        contex = {
            "num_books": num_books,
            "num_authores": num_authores,
            "disponibles": disponibles,
            "num_instances": num_instances,
        }
        )
