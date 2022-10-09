from email.policy import default
from pickle import TRUE
from random import choices
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse 

# Create your models here.
class Genero(models.Model):
    #campo
    name = models.CharField(max_length=64, help_text="Por el nombre del genero ")
    
    #overrife representación informal del objeto
    def __str__(self):
        return self.name 

class Pelicula(models.Model):
    title = models.CharField(max_length=32)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null = True) 
    summary = models.TextField(max_length=100, help_text="Resumen Pelicula ") 
    año = models.CharField( max_length=4, help_text="Año de producción")
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("video-detalle", args=[str(self.id)])

class PeliculaInstance(models.Model):
    video = models.ForeignKey('Pelicula', on_delete=models.SET_NULL, null=True)
    inprint = models.CharField( max_length= 200)
    alquilado = models.DateField(null=True, blank=True)

    LOAN_STATUS =(
        ("o", "Prestado"),
        ("a", "Disponible"),
        ("r", "Reservado"),
    )
    status = models.CharField(max_length=1, choices= LOAN_STATUS, blank=True, default="m", help_text="Disponibilidad del libro")
    
class Meta:
    ordering =["alquilado"]

def __str__(self):
    return '%s (%s)'% (self.id, self.book.title)


class Director(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField( max_length = 100 )
    data_of_birth = models.DateField(null=True, blank=True)
    data_of_death = models.DateField('Died', null=True, blank = True)

    def get_absoluto_url(self):
        return reverse("Director-detail", args=[str(self.id)])
    
    def __str__(self) -> str:
        return  '%s (%s)'% (self.last_name, self.first_name)
                