from django.db import models


class Comentario(models.Model):

    name = models.CharField(max_length= 255, null=False)

    # puntuacion
    score =models.IntegerField(default=3)
    comentario = models.TextField(max_length=1000, null=True)
    fecha = models.DateField(null=True)
    signature = models.CharField(max_length=100, default="Firma")

    # para que nos devuelva el formato que se quiere
    def __str__(self):
        return self.name
     