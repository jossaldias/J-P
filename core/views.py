from django.shortcuts import render

# Create your views here.

# HOME


def home(request):
    return render(request, 'core/paginas/home.html')

# PAGINAS


def juegos(request):
    return render(request, 'core/paginas/juegos.html')


def accesorios(request):
    return render(request, 'core/paginas/accesorios.html')
