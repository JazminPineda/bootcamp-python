from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    ## estatico
    path('saludo/', views.saludo, name="saludo"),
    path("despedida/", views.despedida, name="despedida"),
    ## dinamico dos parametros
    path("adulto/<int:edad>/", views.adulto, name="adulto")
]
