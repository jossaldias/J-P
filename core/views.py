import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

# HOME


def home(request):
    return render(request, 'base/home.html')

# PAGINAS

def exit(request):
    logout(request)
    return redirect('home')

def juegos(request):
    response = requests.get(
        'https://api.rawg.io/api/games?key=b40d42ec4f374f75aa29ef424c698357')
    games = response.json()
    print(games)
    return render(request, 'paginas/catalogo/juegos.html', {"juegos": games})


def accesorios(request):
    return render(request, 'paginas/catalogo/accesorios.html')


def contacto(request):
    return render(request, 'paginas/informacion/contacto.html')

def registro(request):
    return render(request, 'registration/registro.html')

# @login_required
def carritoCompras(request):
    return render(request, 'paginas/productos/carritoCompras.html')


def agregarProducto(request):
    return render(request, 'paginas/productos/agregarProducto.html')

def accionAventura(request):
    return render(request, 'paginas/categorias/accionAventura.html')

def arcadeSimulacion(request):
    return render(request, 'paginas/categorias/arcadeSimulacion.html')

def deportesMusica(request):
    return render(request, 'paginas/categorias/deportesMusica.html')

def shooterEstrategia(request):
    return render(request, 'paginas/categorias/shooterEstrategia.html')

