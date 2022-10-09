from email.policy import default
from pickle import TRUE
from random import choices
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
import uuid
from django.db import models
from django.urls import reverse 



# Create your models here.

# Siempre tiene que heredar de models
class Genre(models.Model):
    #campo
    name = models.CharField(max_length=64, help_text="Por el nombre del genero ")
    
    #overrife representación informal del objeto
    def __str__(self):
        return self.name 
    
class Book(models.Model):
    title = models.CharField(max_length=32)
    #creacion clave foranea con una Referencia se crea una relacion, no solo estan escritos
    #directamente va generar un libro  y ese numero tiene un número 
    # Un campo de una tabla va estar relacionada con otra tabla
    # Y los elmentos se extrae de otra clase
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null = True) 
    # campo texto ilimitada
    summary = models.TextField(max_length=100, help_text="Resumen libro ") 
    isbn = models.CharField('ISBN', max_length=13, help_text="El ISBN es de 13 caracteres")

    # Many tu many fiels genero terror puede tener varios terro modelo genero y pongo la relacion puede tener multiples generos
    genre = models.ManyToManyField(Genre)
    
    # para que cuando se invoquen los libros quiero como referencia su nombre
    def __str__(self):
        return self.title
    
    # url a la inversa 
    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])

class BookInstance(models.Model):

    #se crea un campo id porque quiero algo en concreto
    # Un UUIDF es un numero mas largo genera una cadena de texto
    # generar id de  forma  manera secuencia e integer 
    
    id = models.UUIDField(primary_key= True, default=uuid.uuid4, help_text="ID unico para este libro ")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    inprint = models.CharField( max_length= 200)
    #alquiler  si esta alquilado campo 
    due_back = models.DateField(null=True, blank=True)
    #estados

    LOAN_STATUS =(
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )
    #se crea una variable estatus y se puede asignar a cualquiera de estos estados
    #que se han definido previamente 
    #Diango lo representa en lista 
    status = models.CharField(max_length=1, choices= LOAN_STATUS, blank=True, default="m", help_text="Disponibilidad del libro")
    
class Meta:
    ordering =["due_back"]

def __str__(self):
    return '%s (%s)'% (self.id, self.book.title)

        
class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField( max_length = 100 )
    data_of_birth = models.DateField(null=True, blank=True)
    data_of_death = models.DateField('Died', null=True, blank = True)

    def get_absoluto_url(self):
        return reverse("author-detail", args=[str(self.id)])
    
    def __str__(self) -> str:
        return  '%s (%s)'% (self.last_name, self.first_name)
                