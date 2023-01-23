from django.shortcuts import render


def index(request):
    return render(request, "index.html", {})

def porfolio(request):
    return render(request, "porfolio.html", {})

def fotos(request):
    return render(request, "fotos.html", {})