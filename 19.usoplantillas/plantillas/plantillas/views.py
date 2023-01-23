
from multiprocessing import context

from django.shortcuts import render


def simple(request):
    return render(request, 'simple.html', {}) 


#solicitud completa pasando parametro dinamico 
def dinamico(request, name):
    categorias = ['code', 'desig', 'marketing']
    context = {'name': name, 'categorias': categorias}
    return render(request, 'dinamico.html', context)