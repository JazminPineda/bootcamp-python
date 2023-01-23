from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entrý

# se alcanza la vista sobre la consulta
def queries(request):
    return render(request, 'post/queries.html', {})