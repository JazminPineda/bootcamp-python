from django.conf.urls import url
from catalog  import views
#debe tener exactamente lo mismo que miproyecto 

#Expresión regular cuando una expresión empieza o terminada por nada 
# Dispara la funcion index del moudlo view la cual se llamara index
urlpatterns = [
    url(r'^$', views.index, name='index'),
]