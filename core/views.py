import requests
from django.shortcuts import render

# Create your views here.

# HOME


def home(request):
    return render(request, 'core/paginas/home.html')

# PAGINAS


def juegos(request):
    response = requests.get(
        'https://api.rawg.io/api/games?key=b40d42ec4f374f75aa29ef424c698357')
    games = response.json()
    print(games)
    return render(request, 'core/paginas/juegos.html', {"juegos": games})


def accesorios(request):
    return render(request, 'core/paginas/accesorios.html')


def contacto(request):
    return render(request, 'core/paginas/contacto.html')


def login(request):
    return render(request, 'core/paginas/login.html')


def loginAdmin(request):
    return render(request, 'core/paginas/loginAdmin.html')


def registro(request):
    return render(request, 'core/paginas/registro.html')


def carritoCompras(request):
    return render(request, 'core/paginas/carritoCompras.html')


def pageTest(request):
    return render(request, 'core/paginas/pageTest.html')
